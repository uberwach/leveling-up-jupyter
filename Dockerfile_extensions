FROM jupyter/datascience-notebook


RUN pip install --user --upgrade pip && \
    pip install --user --upgrade notebook jupyterthemes

RUN conda install --yes -c conda-forge jupyter_contrib_nbextensions
RUN conda install --yes -c damianavila82 rise
# activate extensions

RUN jupyter nbextension enable codefolding/main
RUN jupyter-nbextension enable rise --py --sys-prefix
