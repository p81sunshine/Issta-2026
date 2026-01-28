from solution import *

import math

from solution import *

import math

from solution import *

import math

from solution import Blockchain, Block

def test_create_genesis_block():
    blockchain = Blockchain()
    assert len(blockchain.chain) == 1
    assert blockchain.chain[0].transactions == "Genesis Block"

def test_add_transaction():
    blockchain = Blockchain()
    blockchain.add_transaction("TX1")
    assert blockchain.pending_transactions == ["TX1"]

def test_mine_block():
    blockchain = Blockchain()
    blockchain.add_transaction("TX1")
    blockchain.mine_pending_transactions()
    assert len(blockchain.chain) == 2
    assert blockchain.pending_transactions == []
    assert blockchain.chain[1].transactions == ["TX1"]
    assert blockchain.chain[1].previous_hash == blockchain.chain[0].hash

def test_chain_validity():
    blockchain = Blockchain()
    blockchain.add_transaction("TX1")
    blockchain.mine_pending_transactions()
    assert blockchain.is_chain_valid() == True

    # Tampering with the chain
    blockchain.chain[1].transactions = "Tampered TX"
    assert blockchain.is_chain_valid() == False