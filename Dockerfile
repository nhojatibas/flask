FROM alpine:3.9.6

RUN apk add \
    python3 \
    py3-pip \
    python3-dev \
    mariadb-dev \
    tzdata

COPY ./ /flask

WORKDIR /flask

RUN pip3 install --upgrade pip
RUN pip3 install -r /flask/docker/requirements.txt

RUN cp /usr/share/zoneinfo/Brazil/East /etc/localtime
RUN echo "Brazil/East" >  /etc/timezone

RUN rm -rf /var/cache/apk/*

EXPOSE 5000

CMD [ "./docker/entrypoint.sh" ]
