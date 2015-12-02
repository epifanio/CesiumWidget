#!/usr/bin/env bash
mkdir -p /home/main/src/
git clone https://github.com/epifanio/CesiumWidget /home/main/src/CesiumWidget
cd /home/main/src/CesiumWidget
/home/main/anaconda/envs/python3/bin/python setup.py install
/home/main/anaconda/envs/python3/bin/python -m CesiumWidget.install --user
# --symlink --user --force


