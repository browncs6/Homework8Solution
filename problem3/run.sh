#!/usr/bin/env bash

# start mbrot Flask app

export FLASK_APP=mbrot
export FLASK_ENV=development
export FLASK_DEBUG=1
flask run