# Base Image
FROM python:3.7

# MAINTAINER INFO
MAINTAINER jackson.zhang1@hotmail.com

# Configure the user as root
User root

# Port Expose Configurations
EXPOSE 8000
EXPOSE 8001
# Port Expose for Supervisord
EXPOSE 9001
# Port Expose for Flower Monitor
EXPOSE 5555

# Configure the Proxy for this image.
# Please change it based on your own Host Env.
ENV workdir=/opt/ShopSite/\
	http_proxy=http://web-proxy.am.softwaregrp.net:8080\
	https_proxy=http://web-proxy.am.softwaregrp.net:8080
 
# Configure The Working Dir
WORKDIR $workdir

# Create an virtual Environment for App
# RUN python -m venv venv
# && chmod 777 $workdir/shopsitevenv/bin/activate\
# && $workdir/shopsitevenv/bin/activate
# CMD ['/bin/bash', 'source shopsitevenv/bin/activate']

# Add the Extra File 
ADD requirements.txt ./requirements.txt
ADD supervisord.conf ./conf/supervisord.conf


# Update the PIP Installation
# PIP Install ShopSite Package And Its Requirements
RUN pip install --upgrade pip\
 && pip install -r requirements.txt

WORKDIR $workdir/shopsite/

# Update the ShopSite Package
RUN pip install shopsite
RUN pip install --target=. shopsite

# Data Initialized
# RUN python bin/shopsite_manage makemigrations user shop seller product order image comment buyer
# RUN python bin/shopsite_manage migrate

WORKDIR $workdir

# Add the entrypoint sh and change its ownships
ADD run_supervisord.sh ./run_supervisord.sh
RUN chmod 766 ./run_supervisord.sh 

# Unset the proxy
ENV http_proxy=""\
	https_proxy=""

# Port Opening for the test
EXPOSE 7777

# Test Command
# CMD [ "supervisord", "-c", "conf/supervisord.conf"]
# ENTRYPOINT ["/bin/bash", "./run_supervisord.sh", "&"]