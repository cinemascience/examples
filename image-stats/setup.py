import setuptools

# read the description file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'doc/description.md'), encoding='utf-8') as f:
    long_description = f.read()
 
setuptools.setup(
    name="image-stats",
    version="1.0",
    author="David H. Rogers",
    author_email="dhr@lanl.gov",
    description="Cinema image statistics example.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/cinemascience/training",
    install_requires=[
        "numpy",
        "scipy",
        "matplotlib",
        "py",
        "Pillow",
        "pytest",
        "opencv-python",
        "cinemasci"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
)
