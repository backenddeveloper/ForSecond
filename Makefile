devenv:
	docker run -it -v `pwd`:/w -w /w python:3.10 bash -c "make requirements && bash"

requirements:
	pip3 install -r requirements.txt

test: unittest integrationtest

unittest:
	python3 -B -m pytest tests -s -vv

integrationtest:
	python3 -B -m behave tests/forsecond/integration/ -vv -s

build:
	python3 -B -m setup.py bdist_wheel

.PHONY: test
