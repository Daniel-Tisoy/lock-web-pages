#!/bin/bash

function create() {
    cd ~/Documents/projects/automate
    source automation/bin/activate
    source .env
    python3 create.py $1
    deactivate
    cd $FILEPATH$1
    git init
    git remote add origin git@github.com:$USERNAME/$1.git
    touch README.md
    git add .
    git commit -m "Initial commit"
    git push -u origin master
    atom .
}

function lock_pages() {
    cd ~/Documents/projects/block_web_pages
    sudo python3 main.py
    cd ~
}
