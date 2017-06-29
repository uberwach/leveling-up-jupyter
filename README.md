# Leveling up your Jupyter notebook skills

Most of us regularly work with Jupyter notebooks, but fail to see obvious productivity gains involving its usage. Did you know that the web interface works like a modal editor such as vim? Do you know that you can actually profile AND debug code in notebooks? How about setting formulas or use pre-made style settings for visualizations? Let us go through the tricks of the trade together!

In this tutorial I want to give you an overview working with Jupyter notebooks, especially giving you valuable information on what things there are. Additionally, I show you some micro things to improve your productivity. The tutorial closes with a small overview on how Jupyter notebooks are used in practice. To summarize you learn what Jupyter is, how to use it in practice and get an overview on what there is in its evergrowing ecosystem (thanks to the work of the community!).

## Overview

Notebooks are an important tool for data science as they allow for: 

- *collaboration* - as they can be shared as editable text files.

- *presentation* - notebooks are visually presented in an attractive web interface, which we will further improve on, and can also be exported into several reporting formats (html, pdf, slides, ...). 

- *reproducibility* - results can be reproduced by (re-)running the notebook on a different machine. To avoid system related issues, this is often done in docker images (see [1.]).

- *flexibility* - you can write your analysis in several programming languages, and even mix them, or connect to cluster via Spark for instance.

### Jupyter project / Setup

If you have Anaconda then Jupyter should already be installed, if not you can do by installing it via `pip install jupyter`. The command `jupyter --version` gives you the version of Jupyter you are running, this tutorial was tested with version `4.3.0`, a ``jupyter notebook --version` of `5.0.0`.

The config directory of Jupyter can be found under `~/.jupyter` and changed via the environment_variable `JUPYTER_CONFIG_DIR`. If you do not want to touch your installation, you can change to a different anaconda environment:

```
conda create -n levelup_jupyter python=3.5
source activate levelup_jupyter
pip install jupyter
```

_Note: the environment has to be activated in every shell session._

The Jupyter notebook server can be started with the command 

    jupyter notebook --port 8888 --no-browser
    
Running Jupyter notebook servers can be found with `jupyter notebook list`.

It's a good idea to run `pip install --upgrade notebook`


#### Using Docker

By running the docker commands `docker pull jupyter/datascience-notebook` (_DO NOT DO THIS ON CONFERENCE WIFI_) you get a docker image that contains a simple Jupyter installation.

You can run this with the command `docker run -p <local_port>:8888 jupyter/datascience-notebook` and then connect to `localhost:<local_port>` with the token provided.

This repository contains an example ``Dockerfile`` that shows how to customize this Jupyter notebook in your own settings. Advantages are the isolation provided, so you could run on a colleague's PC or on your cluster with the same settings as your laptop.

### The UI

The UI of Jupyter is web-based. In the entry tab you are able to traverse to the working directory to open notebooks, take a look at running notebooks and the cluster.

The notebook view works like a modal editor such as vim. The notebook consists out of a sequence of cells that can be of several types, most often you encounter code cells that contain runnable code and markdown cells that can be typeset into integrated html on-the-fly.

You can go into edit mode by typing <kbd>ENTER</kbd> and leave back to the command mode by pressing <kbd>ESC</kbd>. Colors indicate in which mode you are at. The shortcuts for your system can be listed under `Help > Keyboard Shortcuts`.

Most helpful is <kbd>CMD</kbd> + <kbd>SHIFT</kbd> + <kbd>p</kbd> (<kbd>CTRL</kbd> + <kbd>SHIFT</kbd> + <kbd>p</kbd> in Linux).

[Command Mode]: ./images/command_mode.png

[Edit Mode]: ./images/edit_mode.png

#### Themes

Of course there are also themes. Try `pip install jupyterthemes`. The program `jt` is used to switch themes, try `jt -t chesterish`. Restarting the session if it does not work. Reset with `jt -r`. There are plenty of more options

#### Exporting of notebooks

Under `File > Download as` several options can be found to export the notebook from. For some reason, there are no shortcuts to do this. For `pdf` export, `pandoc` is required.

### Improve Visualization quality by pre-made settings

See the snippets.

### Profiling && Debugging
### Extensions
### Some words regarding the work flow in industrial applications

See the slides.
## Helpful links / Sources

1. [docker-stacks](https://github.com/jupyter/docker-stacks)
2. [Best Practices for Jupyter Notebooks](https://svds.com/jupyter-notebook-best-practices-for-data-science/)
3. [Jupytercon](https://conferences.oreilly.com/jupyter/jup-ny)
4. [IPython and Jupyter in Depth](https://github.com/ipython/ipython-in-depth)
5. [Jupyter docker stacks](https://github.com/jupyter/docker-stacks)
6. [Slides from Jupyter](https://github.com/damianavila/RISE)
7. [Reproducible Data Analysis in Jupyter](https://jakevdp.github.io/blog/2017/03/03/reproducible-data-analysis-in-jupyter/)
8. [Data Science is Software (SciPy 2016 Tutorial)](http://isaacslavitt.com/2016/07/20/data-science-is-software-talk/)
9. [Jupyter Themes](https://github.com/dunovank/jupyter-themes)
10. [28 Jupyter Notebook tips, tricks and shortcuts](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/)
