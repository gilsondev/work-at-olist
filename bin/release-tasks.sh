#!/bin/bash

BASE_DIR=$(pwd)
PROJECT_DIR=work-at-olist
MANAGE=$BASE_DIR/$PROJECT_DIR/manage.py

python $MANAGE migrate
python $MANAGE importcategories wallmart initial_data.csv
