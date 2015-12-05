FROM andrewosh/binder-base

MAINTAINER Massimo Di Stefano <epiesasha@me.com>

USER main

RUN /home/main/anaconda/envs/python3/bin/pip install --upgrade pip
#RUN /home/main/anaconda/envs/python3/bin/pip install -U jupyter
RUN /home/main/anaconda/envs/python3/bin/pip install czml
RUN /home/main/anaconda/envs/python3/bin/pip install geocoder

RUN conda install \
    ipywidgets \
    numpy \
  && pip install \
    czml \
    geocoder
RUN /home/main/anaconda/envs/python3/bin/pip install ipywidgets
#RUN /home/main/anaconda/bin/pip install ipywidgets

USER root

RUN echo "root:root" | chpasswd
RUN echo "main:main" | chpasswd


USER main

RUN git clone https://github.com/epifanio/CesiumWidget --depth=1


WORKDIR CesiumWidget

RUN python setup.py install
RUN /home/main/anaconda/envs/python3/bin/python setup.py install

RUN jupyter nbextension install CesiumWidget --user --quiet

WORKDIR $HOME/Examples
