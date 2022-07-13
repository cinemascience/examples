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
The setup steps have created a `scratch/` directory that you can work in without polluting the main directory. To run the example:

```
    cd scratch
    jupyter notebook show_image.ipynb
```

# Advanced examples

- `show_images_with_cinema_database.ipynb` This example shows how to create and read a cinema database, and iterate over images contained in the database. You can run this from the `scratch` directory like this:

```
    jupyter notebook show_images_with_cinema_database.ipynb
```
