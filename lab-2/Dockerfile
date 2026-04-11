#FREEC

FROM ubuntu:latest
RUN apt-get update && apt-get install -y nginx
EXPOSE 80
ENTRYPOINT [ "nginx" ]
CMD ["-g", "daemon off;"]