from block import Block
class Blockchain:
    """
    Blockchain: a public ledger of transactions.
    Implemented as a list of blocks - data sets of transactions.
    """

    def __init__(self,genesis) -> None:
        self.chain = [Block(genesis)]

    def __repr__(self) -> str:
        return f'Blockchain: {self.chain}'

    def validate_block(self,timestamp):
        """
        Simple case:
            Check if timestamp Greater than timestamp of last block in chain
        Goal:
            Timestamp too easy to manipulate nefariously. Needs something more secure. 
        """
        if self.chain[len(self.chain)-1].timestamp >= timestamp: 
            return True
        else:
            return False

    def add_block(self,data) -> None:
        self.chain.append(Block(self.chain[len(self.chain)-1]).mine_block(data))

def main():
    genesisHash = str(hash('simpleKey01'))
    blockchain = Blockchain(genesisHash)
    blockchain.add_block('one')
    blockchain.add_block('two')

    print(blockchain)
    print(f'blockchain.py __name__: {__name__}')


if __name__ == '__main__':
    """
    Executes program iff executed directly from interpreter
    """
    main()
