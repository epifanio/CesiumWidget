FROM andrewosh/binder-base

MAINTAINER Massimo Di Stefano <epiesasha@me.com>

USER main

RUN /home/main/anaconda/envs/python3/bin/pip install --upgrade pip

RUN /home/main/anaconda/envs/python3/bin/pip install czml
RUN git clone https://github.com/epifanio/CesiumWidget /tmp/CesiumWidget
RUN cd /tmp/CesiumWidget
COPY Examples /home/main/notebooks/Examples

RUN ls /tmp/CesiumWidget/

RUN /home/main/anaconda/envs/python3/bin/python /tmp/CesiumWidget/setup.py install user

ADD . $HOME/notebooks

USER root
RUN chown -R main:main $HOME/notebooks
USER main

# Convert notebooks to the current format
# RUN find $HOME/notebooks -name '*.ipynb' -exec ipython nbconvert --to notebook {} --output {} \;
RUN find $HOME/notebooks -name '*.ipynb' -exec ipython trust {} \;


WORKDIR $HOME/notebooks