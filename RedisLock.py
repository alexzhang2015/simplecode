# https://heapdump.cn/article/5509526

# 一个最基本的分布式锁需要满足：

# 互斥 ：任意一个时刻，锁只能被一个线程持有；
# 高可用 ：锁服务是高可用的。并且，即使客户端的释放锁的代码逻辑出现问题，锁最终一定还是会被释放，不会影响其他线程对共享资源的访问。
# 可重入：一个节点获取了锁之后，还可以再次获取锁。
# 通常情况下，我们一般会选择基于 Redis 或者 ZooKeeper 实现分布式锁，Redis 用的要更多一点，我这里也以 Redis 为例介绍分布式锁的实现。

import redis
import time

class RedisLock:
    def __init__(self, redis_client, lock_key, expire_time=10, acquire_timeout=5):
        self.redis_client = redis_client
        self.lock_key = lock_key
        self.expire_time = expire_time
        self.acquire_timeout = acquire_timeout

    def acquire(self):
        start_time = time.time()
        while time.time() - start_time < self.acquire_timeout:
            if self.redis_client.set(self.lock_key, "locked", ex=self.expire_time, nx=True):
                return True
            time.sleep(0.1)
        return False

    def release(self):
        self.redis_client.delete(self.lock_key)

# 创建Redis连接
redis_client = redis.Redis(host='localhost', port=6379)

# 创建分布式锁实例
lock = RedisLock(redis_client, "my_lock")

# 获取锁
if lock.acquire():
    try:
        # 执行需要加锁的代码
        print("Got the lock!")
    finally:
        # 释放锁
        lock.release()
else:
    print("Failed to acquire the lock.")
