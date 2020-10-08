python -m pip install -r requirements-dev.txt
python setup.py egg_info
python -m pip install -r iceart.egg-info\requires.txt
pre-commit install
