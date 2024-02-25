PYTHON = python3
APP = app
WORKDIR = $(shell pwd)

all: venv install run

venv:
	$(PYTHON) -m venv venv

touch-venv:
	. $(WORKDIR)/venv/bin/activate

install: touch-venv
	pip3 install -r requirements.txt

run:
	$(PYTHON) $(APP)

clean:
	rm -rf venv .venv

