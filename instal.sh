#!/bin/bash

yum -y install epel-release
yum install git gcc zlib-devel bzip2-devel readline-devel sqlite-devel openssl-devel

curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash


cat >> ~/.bashrc << 'EOF'
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"

if command -v pyenv 1>/dev/null 2>&1; then
  eval "$(pyenv init -)"
fi
EOF

source ~/.bashrc

pyenv install 2.7.10
pyenv install 3.7.5

#pyenv global <version>

sudo pip install virtualenv

pyenv virtualenv 2.7.10 pyenv1
pyenv virtualenv 3.7.5 pyenv2