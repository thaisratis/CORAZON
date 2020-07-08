# CORAZON

CORAZON is an abreviation of CORrelations Analyses Zipper ONline, a bioinformatic tool that uses artificial intelligence to cluster genes according to their expression in tissues and also a tool to normalize databases.

CORAZON tool is find at: https://corazon.integrativebioinformatics.me/

This repository is just a backup, to see the CORAZON tool original code and run it locally access: https://gitlab.com/integrativebioinformatics/corazon

All the steps below are also at the gitlab link.

## Requisites

- Git version 2 or above
- Docker version 17.09.1-ce or above (https://docs.docker.com/install/)
- Docker Compose 1.18.0 or above (https://docs.docker.com/compose/install)

## Installation

Clone the repository recursively with:
```
user@host:~# git clone https://gitlab.com/integrativebioinformatics/corazon.git
```
This mode the repositorys the frontend and backend are cloned.

## Pre-execution

Create file `.env` in root directory on repository informing environment variables, example content:

```bash
user@host:~/corazon# vim .env

DBUSER=biodados
DBPASS=sacizeir0
DBNAME=meanshift

```

Define permissions for user `www-data` in directory clustering which will be mounted in "volumes" folder in container. Because the user may not exist on the host host, we use the gid that is standard on any system. Execute:

```bash
user@host:~/corazon/volumes# chown 33:33 -R clustering/

```

## Execution

In the root repository, execute the next command:

```bash
user@host:~/corazon# docker-compose -f docker-compose-local.yml up --build -d
```
The option `-d` execute containers in background.

After these steps, the CORAZON web server tool is ready to be used locally!

Enjoy!
