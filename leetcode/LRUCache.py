from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1
        value = self.cache.pop(key)
        # 将访问的键值对移动到最前面
        self.cache[key] = value
        return value

    def put(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) >= self.capacity:
            # 移除最久未使用的键值对
            self.cache.popitem(last=False)
        self.cache[key] = value

# 创建一个LRUCache实例
cache = LRUCache(2)
print (cache.capacity)

# 测试put方法
cache.put(1, "A")
cache.put(2, "B")
cache.put(3, "C")

# 测试get方法
print(cache.get(1))  # 输出: -1，因为1已经被淘汰了
print(cache.get(2))  # 输出: "B"
print(cache.get(3))  # 输出: "C"

# 再次测试put方法
cache.put(4, "D")

# 测试get方法
print(cache.get(2))  # 输出: -1，因为2已经被淘汰了
print(cache.get(3))  # 输出: "C"
print(cache.get(4))  # 输出: "D"