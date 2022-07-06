## Prepare the environment
Install everything locally

```bash
pip install -e .

```

## Run the job
Locally one can try to run as follows:

```bash
python foobar/__main__.py surname=bob
```
The expected stdout should be:

```
Hello Foo bob!
```

Currently when we try to launch remotely we get an error.
kASimply hit the following command inside the project folder to trigger the remote execution
```bash
make
```
This yields an error. That it can't find the config.
We expected it to be runnable like:
```
make local
```
