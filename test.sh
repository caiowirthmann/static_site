#!/bin/bash

#this code tells python to run a unit test
# python3 -m unittest works, but if we want to use arguments for this test, we should use "discover"
# followed by arguments
# -s specifies in which directory the test will be done
python3 -m unittest discover -s src
