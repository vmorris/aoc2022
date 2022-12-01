#!/bin/bash

DAY="${1}"
DAYDIR="aoc2022/day${DAY}"

#echo "from .day${1} import *" >> "aoc2022/__init__.py"

mkdir "${DAYDIR}"
touch "${DAYDIR}/input"
cp "newday/solution.py" ${DAYDIR}

touch "tests/testinput.day${1}"
cp "newday/_test_day00.py" "tests/test_day${1}.py"
