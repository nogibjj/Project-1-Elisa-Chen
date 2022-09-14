install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_hello.py

#profile-test-code:
#	python -m pytest -vv --durations=1 --durations-min=1.0

#parallel-test:
#	python -m pytest -n auto --dist loadgroup -vv --cov=mylib testing/ 

format:
	black *.py mainlib/*.py

lint:
	pylint --disable=R,C mainlib

all: install lint test
