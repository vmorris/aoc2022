# My solutions for Advent of Code 2022

## Setup

After cloning this repository, create a virtual environment, activate it, and install.

```
$ cd aoc2022
aoc2022 $ python3 -m venv venv
aoc2022 $ . venv/bin/activate
(venv) aoc2022 $ pip install -e .[test]
```

## Create new daily workspace

```
(venv) aoc2022 $ newday 1
```

## Run daily solutions

eg.
```
(venv) aoc2022 $ python aoc2022/day03/solution.py
1082324
1353024
```

## Test Suite
Run individual days with `pytest tests/test_day##.py`

Run the whole test suite with `pytest --cov=aoc2022`
