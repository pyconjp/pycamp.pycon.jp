#!/bin/sh

set -ex

sudo apt update
sudo apt install fonts-noto-cjk
rm -rf ~/.cache/matplotlib

pip install -U pip setuptools
pip install -r requirements.txt
