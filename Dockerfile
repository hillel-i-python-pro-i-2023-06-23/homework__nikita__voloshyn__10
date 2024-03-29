FROM python:3.11

ENV PYTHONUNBUFFERED=1

ARG WORKDIR=/wd
ARG USER=user

WORKDIR ${WORKDIR}

RUN useradd --system ${USER} && \
    chown --recursive ${USER} ${WORKDIR}

RUN apt update && apt upgrade -y

COPY --chown=${USER} requirements.txt requirements.txt

RUN pip install --upgrade pip && \
    pip install --requirement requirements.txt

COPY --chown=${USER} --chmod=555 ./docker/app/entrypoint.sh /entrypoint.sh
COPY --chown=${USER} --chmod=555 ./docker/app/start.sh /start.sh

COPY --chown=${USER} ./Makefile Makefile
COPY --chown=${USER} ./manage.py manage.py
COPY --chown=${USER} ./homework__voloshyn__10 homework__voloshyn__10
COPY --chown=${USER} ./app app

USER ${USER}

VOLUME ${WORKDIR}/db

EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]

CMD ["/start.sh"]