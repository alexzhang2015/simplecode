import redis


# 在分布式系统中,要实现多个机器生成不重复的ID,常用的方法有:

# 使用数据库的自动增长字段:每个机器连接到同一个数据库,将ID设置为自动增长的字段,数据库可以保证不同机器获取的ID不重复。
# 分布式ID生成器:使用Twitter的Snowflake算法、美团的Leaf算法等。核心思想是每个机器有各自的ID范围,不会重复。
# UUID:使用全局唯一的UUID,由机器MAC地址、时间戳、随机数等混合生成,可以保证全局不重复。
# Redis原子操作:使用Redis的原子操作 INCR 对一个键进行自增,可以生成全局不重复的ID。
# Zookeeper顺序节点:每个机器在Zookeeper上维护一个顺序节点,Zookeeper提供单调递增的顺序ID。
# 具体选用哪种方法,需要根据实际应用的分布式程度、性能要求等来决定。比如分布式ID生成器方案可扩展性好,但需要维护生成器状态。Redis和Zookeeper适用于中小规模分布式场景。

# 关键是要根据业务需求选择合适的分布式ID生成方案,并在设计上考虑扩展性、性能、容错性等因素,以满足生成全局不重复ID的需求。

# Snowflake算法:
# 使用41位的时间戳(毫秒级),10位的机器id,12位的序列号
# 通过位操作组成64位的ID
# 可以支撑单台机器每毫秒产生4096个ID

# Leaf算法:
# 使用32位的时间戳,32位的机器id,16位的序列号
# 支持更多的机器节点,通过序号实现高吞吐量

# 两者主要区别在于:
# 时间戳粒度不同,Snowflake使用毫秒,Leaf使用秒
# Leaf使用更多位数表示机器id,可支持更多节点
# Leaf序列号位数较少,依赖时间戳避免重复
# Snowflake可以单机每毫秒产生更多ID
# 核心思想都是利用时间戳+机器ID+序列号确保全局唯一,并且可以横向扩展到多台机器。

# 实现上利用位运算进行组合编码,可以获得较短的ID。

class IdGenerator:
    def __init__(self):
        self.r = redis.Redis(host='192.168.194.173', port=6379)

    def get_id(self):
        return self.r.incr('id_generator')

if __name__ == '__main__':
    gen = IdGenerator()
    for i in range(50000):
        print(gen.get_id())