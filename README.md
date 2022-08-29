# run the main.py to test the algorithm
python main.py

### how to install pipenv on global level if you already have pip
pip3 install pipenv   ||   brew install pipenv

## how to install pipenv on global level if you don't already have pip

python3 -m pip install pipenv pip --upgrade

### how to run pipenv
python3 -m pipenv

python3 -m pipenv shell

python main.py

### how to initiate project with pipenv
python3 -m pipenv install --python python3.9  //what ever version you have at a time.

### to use an virtual env
python3 -m pipenv shell

### once you are on the virtual env and want to install things
first, install pipenv in the virtual env by
pip install pipenv 

second, once you have pipenv installed in your venv, install the package you want by
pipenv install numpy //any package you want.
