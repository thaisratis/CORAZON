# IMAGE USED
FROM php:5.6-apache

MAINTAINER Bruno Correia <brunogomescorreia@gmail.com>

# DOWNLOAD SCRIPT ANACONDA
RUN curl https://repo.continuum.io/archive/Anaconda2-5.2.0-Linux-x86_64.sh --output /opt/Anaconda2-5.2.0-Linux-x86_64.sh

# CONF FILE APACHE VIRTUALHOST
COPY ./files/corazon.conf /etc/apache2/sites-available/000-default.conf

# CODING DEFINE
COPY ./files/charset.conf /etc/apache2/conf-available/

# UPDATE AND INSTALL
RUN apt-get update -y && apt-get install -y bzip2 libxml2-dev python3 python-pip \ 
                       python3-pip libssl-dev libcurl4-openssl-dev \ 
                       libffi-dev apt-transport-https gnupg libapache2-mod-python

# ADD REPO R-PROJECT
RUN echo "deb https://cran.r-project.org/bin/linux/debian/ stretch-cran35/" >> /etc/apt/sources.list

# ADD KEYS
COPY ./files/pubkey /tmp/pubkey

RUN gpg --import /tmp/pubkey


# UPDATE REPOS
RUN apt-get update -y

# INSTALL PACKETS
RUN apt-get install -y r-base-core pandoc --force-yes

# COPY SCRIPT INSTALL R PACKETS
COPY ./files/install.R /tmp/

# EXEC SCRIPT R
RUN Rscript /tmp/install.R

# UPDATE JOBLIB - PROBLEM JOB PARALELL
RUN pip install joblib --upgrade

RUN pip3 install setuptools --upgrade

RUN pip3 install pymysql

RUN pip3 install cryptography

RUN pip3 install passlib

RUN ln -s /usr/bin/python3.5 /usr/local/bin/python3.3

RUN chmod +x /opt/Anaconda2-5.2.0-Linux-x86_64.sh

RUN /opt/Anaconda2-5.2.0-Linux-x86_64.sh -b -p /usr/local/anaconda2

RUN rm /opt/Anaconda2-5.2.0-Linux-x86_64.sh

RUN /usr/local/anaconda2/bin/conda install -y mysql-connector-python

RUN a2enmod cgi
