FROM nvidia/cuda:10.1-cudnn7-devel-ubuntu18.04

WORKDIR /opt/DEV/chamcong_v2/detection
# timezone
RUN     apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \ 
        tzdata \
        rsyslog \
        ntp \
        bash \
        htop \ 
        atop \
        vim \
        wget \
        rsync \
        mlocate \
        collectd \
        ca-certificates \
        logwatch
# python, pip, package
RUN     apt-get install -y \
        libsm6 \
        libxext6 \
        libxrender-dev \
        python3-dev \
        python3-pip
#        /bin/rm -rf /var/lib/apt/lists/*
RUN     pip3 install --upgrade pip
COPY    requirements.txt /opt/DEV/chamcong_v2/detection
RUN     pip install -r requirements.txt
# fix requirement utf8
ENV LANG C.UTF-8

CMD     ["/usr/bin/python3", "chamcong_detection.py"]
