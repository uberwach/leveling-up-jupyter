FROM jupyter/datascience-notebook


RUN pip install --user --upgrade pip && \
    pip install --user --upgrade notebook jupyterthemes

RUN jt -t chesterish
