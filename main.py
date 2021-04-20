import CreateBlock

# Create the genesis block and add it into blockchain
genesis_block = CreateBlock.create_genesis_block()
blockchain = [genesis_block]
previous_block = genesis_block
print("Version:" + str(genesis_block.version))
print("Genesis block has been added to blockchain.It's index is 0.")
print(f'Hash: {genesis_block.hash}\n')

# How many blocks should we add to the chain
# after the genesis block.
# So the number of block in blockchain is 21 in total,including
# the genesis block.
NUM_OF_BLOCKCHAIN_TO_ADD = 20

# Add blocks to the chain
for i in range(0, NUM_OF_BLOCKCHAIN_TO_ADD):
    block_to_add = CreateBlock.create_next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    # Tell everyone about it!
    print("The " + str(block_to_add.index) + " block has been added to blockchain.")
    print(f'Hash: {block_to_add.hash}\n')
