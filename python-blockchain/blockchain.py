
class Block:
    """
    Block: a unit of storage.
    Store transactions in a blockchain that supports a cryptocurrency.
    """

    def __init__(self, data) -> None:
        self.data = data

    def __repr__(self) -> str:
        return f'Block - data: {self.data}'


class Blockchain:
    """
    Blockchain: a public ledger of transactions.
    Implemented as a list of blocks - data sets of transactions.
    """

    def __init__(self) -> None:
        self.chain = []

    def add_block(self, data):
        self.chain.append(Block(data))

    def __repr__(self) -> str:
        return f'Blockchain: {self.chain}'


blockchain = Blockchain()
blockchain.add_block('one')
blockchain.add_block('two')

print(blockchain)
