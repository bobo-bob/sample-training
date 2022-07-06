FROM python:3.9
WORKDIR /gridai/project
RUN apt update && apt install ffmpeg libsm6 libxext6 -y
ARG SCM_VERSION=1.0.0
ENV SETUPTOOLS_SCM_PRETEND_VERSION=$SCM_VERSION

COPY . .
COPY conf lestereo/conf
RUN pip install -e .
