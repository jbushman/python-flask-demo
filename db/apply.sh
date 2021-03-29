#!/usr/bin/env bash
cd db || exit
pipenv run yoyo apply --database mysql://root:P@ssw0rd@localhost:3306/flask_recipe ./migrations