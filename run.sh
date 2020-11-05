#!/bin/bash

source venv/bin/activate
export FLASK_APP=src/Watch_it/
export FLASK_ENV=production
flask run
