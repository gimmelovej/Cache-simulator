class CacheBlock:
    def __init__(self, block_size):
        self.valid = False
        self.tag = None
        self.data = [0] * block_size

class CacheSet:
    def __init__(self, associativity, block_size):
        self.blocks = [CacheBlock(block_size) for _ in range(associativity)]

class Cache:
    def __init__(self, cache_size, block_size, associativity):
        self.cache_size = cache_size
        self.block_size = block_size
        self.associativity = associativity
        self.num_blocks = cache_size // block_size
        self.cache = [CacheSet(associativity, block_size) for _ in range(self.num_blocks // associativity)]

    def read_from_cache(self, address):
        block_number, offset = divmod(address, self.block_size)
        set_index, tag = divmod(block_number, self.num_blocks // self.associativity)

        set_index = set_index % len(self.cache)  # Correção

        cache_set = self.cache[set_index]

        for block in cache_set.blocks:
            if block.valid and block.tag == tag:
                print(f"Leitura do endereço {address}: Hit! Dados: {block.data[offset]}")
                # Atualizar política de substituição (LRU)
                cache_set.blocks.remove(block)
                cache_set.blocks.insert(0, block)
                return

        print(f"Leitura do endereço {address}: Miss!")
        # Simples política de substituição LRU
        evicted_block = cache_set.blocks.pop()
        evicted_block.valid = True
        evicted_block.tag = tag
        # Simulando recarregar os dados da memória principal
        evicted_block.data = [address + i for i in range(self.block_size)]
        cache_set.blocks.insert(0, evicted_block)
        print(f"Dados carregados na cache: {evicted_block.data}")

class MainMemory:
    def __init__(self, size):
        self.size = size
        self.data = [i for i in range(size)]

def main():
    cache_size = 16  # Tamanho da cache em bytes
    block_size = 4   # Tamanho do bloco em bytes
    associativity = 2  # Associatividade da cache

    cache = Cache(cache_size, block_size, associativity)
    main_memory = MainMemory(256)  # Tamanho da memória principal em bytes

    # Endereços de leitura simulados
    addresses_to_read = [0, 4, 8, 12, 16, 20, 24, 28]

    for address in addresses_to_read:
        cache.read_from_cache(address)

if __name__ == "__main__":
    main()
