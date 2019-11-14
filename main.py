class Blockchain(object):
    def __init__(self):
        '''
        Initiates a new blockchain
        '''
        self.chain = []
        self.current_transactions = []


    def new_block(self):
            '''
            Creates a new block and add it to the chain
            '''
            pass

    def new_transaction(self):
        '''
        Creates a new transaction to go into the next mined block
        '''
        pass
    
    @staticmethod
    def hash(block):
        '''
        Hashes a the given block with sha256
        '''
        pass

    @property
    def last_block(self):
        '''
        Returns the last block in the chain
        '''
        pass

