FROM andrewosh/binder-base

MAINTAINER Massimo Di Stefano <epiesasha@me.com>

USER main

RUN /home/main/anaconda/envs/python3/bin/pip install --upgrade pip

RUN /home/main/anaconda/envs/python3/bin/pip install -U jupyter

ADD Examples $HOME/Examples/

RUN /home/main/anaconda/envs/python3/bin/pip install czml

RUN /home/main/anaconda/envs/python3/bin/pip install geocoder

ADD install_cesiumwidget.sh /tmp/install_cesiumwidget.sh
RUN /tmp/install_cesiumwidget.sh

USER root
RUN chown -R main:main $HOME/notebooks
USER main

WORKDIR $HOME/Examples