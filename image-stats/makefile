SHELL=/bin/bash
ENVNAME=exenv

clean:
	rm -rf $(ENVNAME)
	rm -rf build
	rm -rf image_stats.egg-info
	rm -rf dist
	rm -rf data

example:
	python3 -m venv $(ENVNAME)
	. $(ENVNAME)/bin/activate
	python3 -m pip install --upgrade pip
	pip3 install wheel
	pip3 install .
	@echo "Setting up example ..."
	@cp -rf ../data .
