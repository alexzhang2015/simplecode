# https://segmentfault.com/a/1190000015967922

import time

class LeakyBucket:
    def __init__(self, capacity, rate):
        self.capacity = capacity
        self.rate = rate
        self.tokens = 0
        self.last_time = time.time()

    def allow_request(self):
        current_time = time.time()
        elapsed_time = current_time - self.last_time
        self.tokens = min(self.capacity, self.tokens + elapsed_time * self.rate)
        self.last_time = current_time

        if self.tokens >= 1:
            self.tokens -= 1
            return True
        else:
            return False

class TokenBucket:
    def __init__(self, capacity, rate):
        self.capacity = capacity
        self.rate = rate
        self.tokens = capacity
        self.last_time = time.time()

    def allow_request(self):
        current_time = time.time()
        elapsed_time = current_time - self.last_time
        self.tokens = min(self.capacity, self.tokens + elapsed_time * self.rate)
        self.last_time = current_time

        if self.tokens >= 1:
            self.tokens -= 1
            return True
        else:
            return False
        
class RateLimiter:
    def __init__(self, strategy):
        self.strategy = strategy

    def allow_request(self):
        return self.strategy.allow_request()

# 根据配置选择限流器策略
def get_limiter_strategy(config):
    if config == "TokenBucket":
        return TokenBucket(10, 2)
    elif config == "LeakyBucket":
        return LeakyBucket(10, 2)
    else:
        raise ValueError("Invalid limiter configuration")

# 创建一个RateLimiter实例，通过配置选择不同的限流器策略
limiter_config = "TokenBucket"
limiter_strategy = get_limiter_strategy(limiter_config)
limiter = RateLimiter(limiter_strategy)

# 测试限流器
for i in range(15):
    if limiter.allow_request():
        print(f"Request {i+1}: Allowed")
    else:
        print(f"Request {i+1}: Denied")
    time.sleep(0.5)