FROM jupyter/datascience-notebook

RUN pip install --upgrade notebook jupyterthemes

RUN jt -t chesterish
