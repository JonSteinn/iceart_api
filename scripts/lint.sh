#!/bin/bash
python3 -m pylint iceart
python3 -m flake8
python3 -m mypy
python3 -m black iceart
