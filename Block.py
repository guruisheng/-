from Crypto.Hash import SHA256
import random

class Block:
    """每个区块的内容：该块的索引、时间戳、数据和前一个区块的哈希值和本块的哈希值"""
    def __init__(self, index, timestamp, data, previous_hash):
        """区块头"""
        self.version = 1.0
        self.index = index
        self.time_stamp = timestamp  # 时间戳。stamp为邮票
        self.data = data  # 区块体
        self.previous_hash = previous_hash
        self.nonce = random.randint(0, 100000000)  # 在挖矿时需要找到的随机数
        self.hash = self.hash_block()

    def hash_block(self):
        hash_value = SHA256.new()
        # 更新hash值，做"+="号。先转化为字符串，再编码（转化为二进制）
        hash_value.update(str(self.version).encode() +
                          str(self.index).encode() +
                          str(self.time_stamp).encode() +
                          str(self.data).encode() +
                          str(self.previous_hash).encode() +
                          str(self.nonce).encode())
        return hash_value.hexdigest()  # 返回16进制可打印的哈希摘要值
