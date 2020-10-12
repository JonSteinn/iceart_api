#!/bin/bash
python3 -m pip install -r requirements-dev.txt
python3 setup.py egg_info
python3 -m pip install -r iceart.egg-info/requires.txt
pre-commit install
