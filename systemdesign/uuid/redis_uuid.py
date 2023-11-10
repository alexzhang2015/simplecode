import redis
import uuid

class UUIDGenerator(object):
    def __init__(self, redis_host='localhost', redis_port=6379, redis_db=0):
        self.redis = redis.Redis(host=redis_host, port=redis_port, db=redis_db)
    
    def get_uuid(self):
        uuid_id = self.redis.incr('uuid')
        return str(uuid.UUID(int=uuid_id))
        
if __name__ == '__main__':
    generator = UUIDGenerator()
    for i in range(100000):
        print(generator.get_uuid())