.PHONY: run clean test

SHELL = /bin/bash

default: bin/python3

bin/python3:
	virtualenv . -p python3 --no-site-packages
	bin/pip3 install --upgrade pip wheel pytest
	bin/pip3 install wheel Cython==0.28.5 numpy
	bin/pip3 install -r requirements.txt

nbextensions:
	bin/jupyter-nbextension install --py hide_code --user
	bin/jupyter-nbextension enable --py hide_code --user
	bin/jupyter-serverextension enable --py hide_code --user


run: nbextensions
	bin/jupyter-notebook

test:
	bin/py.test -m 'not ignore' tests

clean:
	rm -Rf .Python
	rm -Rf var/log
	rm -Rf bin include lib local share etc man
	rm -Rf develop-eggs eggs *.egg-info
	rm -Rf src parts build dist
	rm -Rf .installed.cfg pip-selfcheck.json
