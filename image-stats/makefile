SHELL=/bin/bash
ENVNAME=exenv

all: python-env example

clean-all: clean-python-env clean-example

clean-python-env:
	rm -rf $(ENVNAME)
	rm -rf build
	rm -rf image_stats.egg-info
	rm -rf dist
	rm -rf 'Local State'

python-env:
	@echo "Creating python environment ..."
	python3 -m venv $(ENVNAME)
	. $(ENVNAME)/bin/activate
	python3 -m pip install --upgrade pip
	pip3 install wheel
	pip3 install .

example:
	@echo "Setting up example ..."
	@mkdir scratch
	@cp -rf ../data scratch
	@cp show_image.ipynb scratch	
	@cp show_images_with_cinema_database.ipynb scratch	

clean-example:
	rm -rf data
	rm -rf scratch
