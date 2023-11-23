# Cache Simulator in Python

This is a cache simulator in Python that demonstrates the basic concepts of a cache, including replacement policies (LRU) and data manipulation in the cache.

## Project Structure

- **`CacheBlock`**: Class representing an individual block in the cache.
- **`CacheSet`**: Class representing a set in the cache containing multiple blocks.
- **`Cache`**: Class representing the complete cache, containing multiple sets.
- **`MainMemory`**: Class representing the main memory containing the original data.
- **`main`**: Main function that initiates the simulation.

## Functionality

1. **Initialization**:
    - You can adjust cache parameters, such as `cache_size`, `block_size`, and `associativity` in the `main` function.
    - `main_memory` is initialized with sequential data from 0 up to the specified size.

2. **Cache Reading (`read_from_cache`)**:
    - The function simulates reading from a specific address.
    - It calculates the block number, set index, and block tag.
    - Checks if the block is in the cache.
    - If it is, it's a "hit," and the data is read.
    - If it's not, it's a "miss," and the block is replaced using the LRU policy.

3. **Replacement Policy (LRU)**:
    - The most recently used block is moved to the beginning of the list within the set.
    - In the case of a "miss," the least recently used block is removed and replaced.

4. **Simulation of Address Accesses**:
    - The `main` function simulates reading a series of specific addresses by calling `read_from_cache` for each one.

## Execution

Make sure to have Python installed in your environment. Run the code using:

```bash
python filename.py
