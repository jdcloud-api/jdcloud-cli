FROM alpine:3.6
RUN apk -v --update add \
        python \
        py-pip \
        groff \
        less \
        mailcap \
	wget \
        jq  \
        openssl \
	ca-certificates \
	py-setuptools \
        && \
    pip install -U jdcloud_cli
RUN update-ca-certificates
RUN wget -q -c  -O kubectl https://storage.googleapis.com/kubernetes-release/release/v1.8.12/bin/linux/amd64/kubectl \
&& chmod +x kubectl \
&& mv kubectl /usr/local/bin
RUN apk -v --purge del py-pip && \
    rm /var/cache/apk/*
    
RUN echo 'eval "$(register-python-argcomplete jdc)"' >> /root/.bashrc
RUN echo 'export COLUMNS=100' >> /root/.bashrc

VOLUME /root/.jdc
WORKDIR /root
ENTRYPOINT ["jdc"]

