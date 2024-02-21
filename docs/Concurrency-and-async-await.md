# Concurrency and `async` / `await`

- Modern versions of Python have support for **"asynchronous code"** using something called **"coroutines"**, with `async` and `await` syntax.
- [Link](https://fastapi.tiangolo.com/async/)

## `async` / `await` (asynchronous code)

```python
@app.get('/')
async def read_results():
    # have to wait for get_burgers() to finish
    burgers = await get_burgers(2)
    return burgers
```

- `await` tells Python that it has to wait for `get_burgers(2)` to finish doing its thing 🕙 before storing the results in burgers. With that, Python will know that it can go and do something else 🔀 ⏯ in the meanwhile (like receiving another request).
- For `await` to work, it has to be inside a function that supports this asynchronicity. To do that, you just declare it with `async def`
- "wait for `get_burgers(2)`" normally refers to I/O operations that are relatively "slow" (compared to the speed of the processor and the RAM memory), like waiting for:
  - The data from the client to be sent through the network
  - The data sent by your program to be received by the client through the network
  - The contents of a file in the disk to be read by the system and given to your program
  - The contents your program gave to the system to be written to disk
  - A remote API operation
  - A database operation to finish
  - A database query to return the results

### Coroutines

- **Coroutine** is just the very fancy term for the thing returned by an async def function. Python knows that it is something like a function that it can start and that it will end at some point, but that it might be paused ⏸ internally too, whenever there is an await inside of it.
- But all this functionality of using asynchronous code with async and await is many times summarized as using "coroutines". It is comparable to the main key feature of Go, the "**Goroutines**".

## Concurrency vs Parallelism

- This idea of **asynchronous** code described above is also sometimes called "concurrency". It is different from "parallelism".
- "Concurrency" is better than "parallelism" on specific scenarios that involve a lot of waiting.
