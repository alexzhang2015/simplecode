import sqlite3
import redis

# 连接到 SQLite 数据库
conn = sqlite3.connect('kv_store.db')
cursor = conn.cursor()

# 连接到 Redis 服务器
redis_client = redis.Redis(host='localhost', port=6379)

# 读取键值对（先从缓存中读取，如果缓存中没有，则从数据库中读取）
def get(key):
    value = redis_client.get(key)
    if value is not None:
        return value.decode('utf-8')
    else:
        cursor.execute('SELECT value FROM kv_store WHERE key=?', (key,))
        result = cursor.fetchone()
        if result:
            value = result[0]
            redis_client.set(key, value)
            return value
        else:
            return None

# 写入键值对（同时更新缓存）
def put(key, value):
    cursor.execute('INSERT OR REPLACE INTO kv_store (key, value) VALUES (?, ?)', (key, value))
    conn.commit()
    redis_client.set(key, value)

# 删除键值对（同时更新缓存）
def delete(key):
    cursor.execute('DELETE FROM kv_store WHERE key=?', (key,))
    conn.commit()
    redis_client.delete(key)

# 关闭数据库连接和 Redis 连接
def close_connections():
    cursor.close()
    conn.close()
    redis_client.close()
