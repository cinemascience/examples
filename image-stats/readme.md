# Cinema Image Statistics example

**NOTE:** Before you can run examples in this directory, you need to follow the instructions on the main repository `readme`.

## Viewing example databases

To view the databases, type this command in the shell:

```
    cinema view --databases data/sphere.cdb --viewer view
```

This command will bring the database up in a different viewer:

```
    cinema view --databases data/sphere.cdb --viewer explorer
```

## Starting a server on example databases

To view the databases, type this command in the shell, which will start a server. You can then view the database at the URL that is printed to the shell:

```
    cinema server --databases data/sphere.cdb
```

## Managing the examples with `make` targets

To manage the python environment and the example, you can clean each of them, using the `make` targets:

```
    make clean-python-env

    OR

    make clean-example
```

Then you can recreate everything using make:

```
    make pythone-env

    OR

    make example

```

## The `scratch` directory
The setup steps have created a `scratch/` directory that you can work in without polluting the main directory. To run the simple example:

```
    cd scratch
    jupyter notebook show_image.ipynb
```

# Examples

- `show_image.ipynb` This is the most basic example, showing how to load an image and run some `opencv` methods. Run it with this command:

```
    jupyter notebook show_image.ipynb
```

- `show_images_with_cinema_database.ipynb` This example shows how to create and read a cinema database, and iterate over images contained in the database. You can run this from the `scratch` directory like this:

```
    jupyter notebook show_images_with_cinema_database.ipynb
```
