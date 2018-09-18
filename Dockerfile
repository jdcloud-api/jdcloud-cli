FROM ubuntu

RUN apt-get update
RUN apt-get install -y python-pip
RUN pip install -U jdcloud_cli

RUN echo 'eval "$(register-python-argcomplete jdc)"' >> /root/.bashrc
RUN echo 'export COLUMNS=100' >> /root/.bashrc
