import time
class Block:
    """
    Block: a unit of storage.
    Store transactions in a blockchain that supports a cryptocurrency.
    """
    def __init__(self, last_block_hash) -> None:
        self.timestamp = time.time_ns()
        self.last_hash = last_block_hash
        self.hash = f'{self.timestamp}-{self.last_hash}'
        self.data = None

    def __repr__(self) -> str:
        return (
            'Block('
            f'timestamp: {self.timestamp}, '
            f'last_hash: {self.last_hash}, '
            f'hash: {self.hash}, '
            f'Block - data: {self.data})'
        )

    def mine_block(self, data) -> None:
        """
        Mine a block based on the given last_block and data.
        Mining refers to using computational power.
        """
        self.timestamp = time.time_ns()
        self.hash = f'{self.timestamp}-{self.last_hash}'
        self.data = data #needs something computationally intense?


def main():
    block = Block(str(hash('deezNutz57')))
    print(block)


if __name__ == '__main__':
    """
    Executes program iff executed directly from interpreter
    """
    main()
