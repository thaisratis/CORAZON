#!/bin/sh
if ps -ef | grep -v grep | grep supergirl.py ; then
        continue
else
        /var/www/html/meanshift_execute & > /dev/null
fi

exit 0
