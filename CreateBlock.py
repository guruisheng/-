from datetime import datetime
from Block import Block

# 创世区块的索引为 0 ，其包含一些任意的数据值，其“前一哈希值”参数也是任意值。
def create_genesis_block():
    """构建创世区块"""
    # Manually(手工) construct a block with
    # index zero and arbitrary(任意的) previous hash
    return Block(0, datetime.now(), "Genesis block", "0")

def create_next_block(last_block):
    """创建下一个区块"""
    this_index = last_block.index + 1
    this_time_stamp = datetime.now()
    this_data = "Hey! I'm block " + str(this_index)
    this_previous_hash = last_block.hash
    return Block(this_index, this_time_stamp, this_data, this_previous_hash)
