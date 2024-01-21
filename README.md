### This is a Work In Progress!

## About

This solution involves reading an input file, creating a directed graph from the file, then uses a [Depth First Search](https://en.wikipedia.org/wiki/Depth-first_search) to find the progenitor node with the largest connected family tree; ignoring the recounting of cyclic sub-graphs.

This solution was developed against [Python 3.10](https://hub.docker.com/_/python)

The only dependency required to run it is [Docker](https://docker.com)

## How to:

If you have [GNUMake](https://www.gnu.org/software/make/) installed you can create a working development environment, that mounts the local directory by running
```bash
make devenv
```
Alternatively you can copy the following line out of the Makefile and run it directly
```bash
docker run -it -v `pwd`:/w -w /w python:3.10 bash -c "make requirements && bash"
```

To run the tests associated with the solution you can run (inside docker)
```bash
make test
```

The solution is designed to be run as a Python module
```bash
python3 -m forsecond path/to/input/file
```
But you can also (depending on your PYTHONPATH) import and run the code in a different module
```python3
from forsecond.app import run
```

You can build a Wheel for distribution with
```bash
VERSION='XYZ_1.2.3-rc4' make build
```


# assumptions:

- We can fit the whole file into a datastructure in memory
- The names are alphanumeric
- to avoid casing errors the names preserve their meaning when converted to lowercase

- The file is well formatted, one entry per line
- We can just ignore empty lines
- We can just ignore left and right padding

- Python array functions are "free" from the perspective of time complexity calculations
- The file is read-write lockable and in standard UTF-8 encoding, so no need additional arguments are needed to open()

- E501 is ignored by testing convention
- There is a philosophical question about whether a player can see themselves, this ignores it out of the box

# TODO:
- validate graph
- validate filename
- PYDOC, particularly for `forsecond.app.run`
- Boundary style behavioural testing for application running directives
- Justify time complexity expectations


# Issues:

- directory traversal
- reflection issue in code printing
- leaf node players are included in the graph

# Comments:

- Normally I would just use a validation library for reading the file into CSV, I skipped this to make it easier to show testing
- Normally we would just use a graphing library, but again skipped to show testing
