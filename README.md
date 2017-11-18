# Olist Channels

[![Build Status](https://travis-ci.org/gilsondev/work-at-olist.svg?branch=master)](https://travis-ci.org/gilsondev/work-at-olist)
[![Maintainability](https://api.codeclimate.com/v1/badges/93c82ab8324f32f3ba0e/maintainability)](https://codeclimate.com/github/gilsondev/work-at-olist/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/93c82ab8324f32f3ba0e/test_coverage)](https://codeclimate.com/github/gilsondev/work-at-olist/test_coverage)

This project offer the management of channels to help integrations with Sellers.

Olist is a company that offers an integration platform for sellers and
marketplaces allowing them to sell their products across multiple channels.


## Requirements

 - Python >= 3.5
 - Docker and Docker compose
 - PostgreSQL Devel (for psycopg2 dependency)


## Install

 - Clone the repository

 ```shell
$ git clone https://github.com/gilsondev/work-at-olist.git
 ```

 - Prepare the virtualenv and active it

 ```shell
 $ cd work-at-olist
 $ python3 -m venv .venv
 ```

 - Install the dependencies

 ```shell
 $ make setup
 ```

 To local development use this command:

 ```shell
 $ make local_setup
 ```

 - Run the system this command to prepare the local server and postgresql with docker-compose:

 ```shell
 $ make run
 ```