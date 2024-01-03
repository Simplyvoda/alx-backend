# Concepts of Caching Systems

1. **Caching System:** A mechanism used to store frequently accessed or critical data in a high-speed, easily accessible location to improve system performance.

2. **FIFO (First In, First Out):** Removes the oldest data first when the cache is full, operating like a queue.

3. **LIFO (Last In, First Out):** Removes the most recently added data first when the cache is full, operating like a stack.

4. **LRU (Least Recently Used):** Removes the data that hasn’t been accessed for the longest time, prioritizing recent access.

5. **MRU (Most Recently Used):** Removes the data that has been accessed most recently, prioritizing immediate use.

6. **LFU (Least Frequently Used):** Removes the data that has been accessed the fewest times, prioritizing frequently used data.

7. **Purpose of a Caching System:** Enhances system performance by storing frequently accessed data closer to the point of need, reducing access time.

8. **Limits of a Caching System:** Size limitations restrict the amount of data stored; volatile access patterns can impact efficiency. Choosing an inappropriate replacement policy may lead to suboptimal performance.
