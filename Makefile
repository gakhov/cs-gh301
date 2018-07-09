.PHONY: run clean

SHELL = /bin/bash

default: bin/python3

bin/python3:
	virtualenv . -p python3 --no-site-packages
	bin/pip3 install --upgrade pip
	bin/pip3 install wheel
	bin/pip3 install -r requirements.txt

nbextensions:
	bin/jupyter-nbextension install --py hide_code --user
	bin/jupyter-nbextension enable --py hide_code --user
	bin/jupyter-serverextension enable --py hide_code --user


run: nbextensions
	bin/jupyter-notebook


clean:
	rm -Rf var/log
	rm -Rf bin include lib local share etc
	rm -Rf develop-eggs eggs *.egg-info
	rm -Rf src parts build dist
	rm -Rf .installed.cfg pip-selfcheck.json
