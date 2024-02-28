# Environment Variable

- The environment variables defined in `.env` file can be loaded before running the uvicorn server `set -a && source .env && set +a`
  - `set -a`: This option enables automatic exporting of all variables in the shell environment.
  - `source .env`: This command sources (executes) the contents of the file `.env` in the current shell environment. This typically contains variable assignments or exports.
  - `set +a`: This option disables automatic exporting of variables.

```bash
set -a && source .env && set +a
uvicorn main:app --host 0.0.0.0 --port 8081

# after this, the fastapi can access the environment variables defined in .env
# os.environ["KEY"]
```
