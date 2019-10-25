# Base Image
FROM nginx:latest

WORKDIR /etc/nginx/
ADD ./nginx.conf /etc/nginx/nginx.conf
ADD ./apps/ /etc/nginx/apps/

WORKDIR /opt/shopsite/

ADD ./static/ /opt/shopsite/static/
ADD ./entrypoint.sh .
RUN chmod 766 entrypoint.sh

# ENTRYPOINT ["bash", "entrypoint.sh", "&"]
