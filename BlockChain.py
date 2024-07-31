
import datetime

import hashlib

from colorama import init
init()
from colorama import Fore, Back, Style

class Block:
    blockNo = 0
    data = None 
    next = None
    hash = None
    nonce = 0
    previous_hash = 0x0
    timestamp = datetime.datetime.now()

    def __init__(self, data):
        self.data = data

    def hash(self):
        h = hashlib.sha256()

        h.update(
        str(self.nonce).encode('utf-8') +
        str(self.data).encode('utf-8') +
        str(self.previous_hash).encode('utf-8') +
        str(self.timestamp).encode('utf-8') +
        str(self.blockNo).encode('utf-8')
        )
        return h.hexdigest()


    def __str__(self):

        return "Block Hash: " + str(self.hash()) + "\nPreviousHash: " + str(self.previous_hash) + "\nBlockNo: " + str(self.blockNo) + "\nBlock Data: " + str(self.data) + "\nHashes: " + str(self.nonce) + "\n--------------"

class Blockchain:
    
    #mining difficulty
    diff = 10
    #2^32. This is the maximum number
    #we can store in a 32-bit number
    maxNonce = 2**32
    #target hash, for mining
    target = 2 ** (256-diff)

    #generates the first block in the blockchain
    block = Block("Genesis")
    #sets it as the head of our blockchain
    head = block

    def add(self, block):

        block.previous_hash = self.block.hash()

        block.blockNo = self.block.blockNo + 1

        self.block.next = block
        self.block = self.block.next

    def mine(self, block):
        #from 0 to 2^32 
        for n in range(self.maxNonce):
            #is the value of the given block's hash less than our target value?
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                print("Add Block")
                print(block)
                break
            else:
                block.nonce += 1
