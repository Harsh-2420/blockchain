from time import time
import hashlib
import json

class Blockchain(object):
    '''
    A Blockchain Class
    '''
    def __init__(self):
        '''
        Initiates a new blockchain
        '''
        self.chain = []
        self.current_transactions = []

        self.new_block(proof=100, previous_hash=None)

    def new_block(self, proof:int, previous_hash:str) -> dict:
        '''
        Creates a new block and add it to the chain

        :param proof: proof of work 
        :param previous_hash: the hash of the previous block
        :return: New block thats created
        '''
        block = {
            'index' : len[self.chain] + 1,
            'timestamp' : time(),
            'transactions' : self.current_transactions
            'proof' : proof, 
            'previous_hash' = previous_hash
        }

        self.current_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender:str, recipient:str, amount:int) -> int:
        '''
        Creates a new transaction to go into the next mined block

        :param sender: Address of sender
        :param recipient: Address of recipient
        :param amount: Amount
        :return: index of the block that will hold this transaction
        '''
        self.current_transactions.append/
        ({'sender': sender, 
          'recipient': recipient,
          'amount':amount})

        return self.last_block['index'] + 1
    
    @staticmethod
    def hash(block:dict) -> str:
        '''
        Hashes a the given block with sha256
        '''
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        '''
        Returns the last block in the chain
        '''
        return self.chain[-1]

