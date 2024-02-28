# Daily Knowledge

## Day 1

### Environment Variable

- `set -a && source .env && set +a` this is to load environment variables defined in .env into the current shell environment
  - `set -a`: This option enables automatic exporting of all variables in the shell environment.
  - `source .env`: This command sources (executes) the contents of the file `.env` in the current shell environment. This typically contains variable assignments or exports.
  - `set +a`: This option disables automatic exporting of variables.

### Concurrency and `async` / `await`

- Modern versions of Python have support for **"asynchronous code"** using something called **"coroutines"**, with `async` and `await` syntax.

#### Concurrency vs Parallelism

- This idea of **asynchronous** code described above is also sometimes called "concurrency". It is different from "parallelism".
- "Concurrency" is better than "parallelism" on specific scenarios that involve a lot of waiting.
