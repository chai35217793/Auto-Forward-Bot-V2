#!/bin/bash

# Start services for devgagan1
devgagan1() {
    gunicorn app:app &
    python main.py
}

# Start services for devgagan2
devgagan2() {
    cp __init__.py src/devgagan/
    cd src
    python -m devgagan
}

# Uncomment the required service
# devgagan1
# devgagan2
