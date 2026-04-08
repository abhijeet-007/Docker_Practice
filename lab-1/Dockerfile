#FREEC

FROM ubuntu:latest
RUN apt-get update && apt-get install -y nginx
#RUN echo "Welcome to DIM TEam Dec 2025!" > /var/www/html/index.html
COPY  ./index.html /var/www/html/index.html
EXPOSE 80
ENTRYPOINT [ "nginx" ]
CMD ["-g", "daemon off;"]