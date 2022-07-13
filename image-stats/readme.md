# Cinema Image Statistics example

**NOTE:** Before you can run examples in this directory, you need to follow the instructions on the main repository `readme`.

To view the databases, type this command in the shell:

```
    cinema view --databases data/sphere.cdb --viewer view
```

This command will bring the database up in a different viewer:

```
    cinema view --databases data/sphere.cdb --viewer explorer
```

The setup steps have created a `scratch/` directory that you can work in without polluting the main directory. To run the example:

```
    cd scratch
    jupyter notebook show_image.ipynb
```

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
