FROM getfemdoc/getfem:stable
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update
RUN apt-get -y install python3-pip
RUN apt-get -y install mayavi2
RUN apt-get -y install xvfb

# install the notebook package
RUN pip install --no-cache --upgrade pip && \
    pip install --no-cache jupyterlab

# create user with a home directory
ARG NB_USER
ARG NB_UID
ENV USER ${NB_USER}
ENV HOME /home/${NB_USER}

RUN adduser --disabled-password \
    --gecos "Default user" \
    --uid ${NB_UID} \
    ${NB_USER}
WORKDIR ${HOME}
USER root
COPY . ${HOME}
RUN pip install -r requirements.txt
RUN pip install .
RUN chown -R ${NB_USER} ${HOME}
USER ${USER}
