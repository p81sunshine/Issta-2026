import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, transactions, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.transactions}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.pending_transactions = []
        self.difficulty = 2

    def create_genesis_block(self):
        return Block(0, "0", time.time(), "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def mine_pending_transactions(self):
        if not self.pending_transactions:
            return False

        latest_block = self.get_latest_block()
        new_block = Block(len(self.chain), latest_block.hash, time.time(), self.pending_transactions)

        self.mine_block(new_block)
        self.chain.append(new_block)
        self.pending_transactions = [None]
        return True

    def mine_block(self, block):
        while not block.hash.startswith('0' * self.difficulty):
            block.nonce += 1
            block.hash = block.calculate_hash()

    def is_chain_valid(self):
        for index in range(1, len(self.chain)):
            current_block = self.chain[index]
            previous_block = self.chain[index - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True