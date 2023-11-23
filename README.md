# Cache Simulator in Python

This is a cache simulator in Python that demonstrates the basic concepts of a cache, including replacement policies (LRU) and data manipulation in the cache.

## Demonstrated Concepts

### Cache Memory

Simulates the memory hierarchy, featuring a cache that temporarily stores data blocks to accelerate access to frequently used data.

### Replacement Policy (LRU)

Implements a simple replacement policy called "Least Recently Used" (LRU). This policy ensures that the least recently used block is replaced in the event of a cache miss.

### Read Operations

Demonstrates how read operations in memory are handled in the cache. When an address is read, the simulator checks whether the corresponding block is in the cache. If it is, it's a "hit"; otherwise, it's a "miss," and replacement occurs.

### Data Reload

Simulates reloading data from main memory to the cache when a "miss" occurs.

## Potential Applications

### Computer Science Education

Can be used as an educational tool to teach memory cache concepts in computer science courses.

### Experimentation and Analysis

Can be expanded to experiment with different cache sizes, replacement policies, and associativities to understand their impact on system performance.

### Benchmarking

Can be adapted to assess the relative performance of different cache configurations in terms of hits, misses, and access time.

### Algorithm Development

Can serve as a foundation for experimenting and testing more advanced cache management algorithms.

This simulator is a learning tool that can be valuable for understanding the importance of memory hierarchy and the strategies used to optimize data access in computer systems.

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
```
# Data Analysis Project Introduction

I sincerely appreciate your time dedicated to reading and following along with this initial data analysis project. This notebook serves as a starting point to explore the vast field of data analysis, providing a practical and structured insight.

This project is just the beginning, a starting point to build skills and understanding in the field of data analysis. I am open to suggestions, ideas, and collaborations that can further enrich this journey. Your feedback is valuable and can contribute to the improvement of this work and future projects.

I invite you to join me on my learning and development journey on LinkedIn (https://www.linkedin.com/in/viniciuscarvs/) and explore the source code of my projects on GitHub (https://github.com/gimmelovej). Your presence and interaction are always welcome.

Thank you again for your interest and support. Together, we can continue exploring the fascinating world of analysis and data science.

Best regards,

Vinícius Carvalho.

