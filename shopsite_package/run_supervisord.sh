#!/bin/bash
/usr/local/bin/python shopsite/bin/shopsite_manage makemigrations user shop seller product order image comment buyer
/usr/local/bin/python shopsite/bin/shopsite_manage migrate
/usr/local/bin/supervisord -c conf/supervisord.conf
