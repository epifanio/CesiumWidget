FROM andrewosh/binder-base

MAINTAINER Massimo Di Stefano <epiesasha@me.com>

USER main

RUN /home/main/anaconda/envs/python3/bin/pip install --upgrade pip

RUN /home/main/anaconda/envs/python3/bin/pip install -U jupyter

ADD . $HOME/notebooks

RUN /home/main/anaconda/envs/python3/bin/pip install czml

ADD install_cesiumwidget.sh /tmp/install_cesiumwidget.sh
RUN /tmp/install_cesiumwidget.sh

COPY Examples /home/main/notebooks/Examples

USER root
RUN chown -R main:main $HOME/notebooks
USER main

# Convert notebooks to the current format
# RUN find $HOME/notebooks -name '*.ipynb' -exec ipython nbconvert --to notebook {} --output {} \;
RUN find $HOME/notebooks -name '*.ipynb' -exec ipython trust {} \;


WORKDIR $HOME/notebooks