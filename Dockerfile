ARG PYTHON_VERSION=3.10.2-alpine3.15

### Python base image ###
FROM python:${PYTHON_VERSION} AS recerca-python310-base

### Compile base image ###
RUN set -x \
    && apk add --virtual build-dependencies \
    g++ \
    git \
    openssh \
    libffi-dev \
    zlib-dev \
    jpeg-dev \
    pango-dev \
    cairo-dev \
    postgresql-dev

### Compile external libraries ###
WORKDIR /wheels_ext
COPY requirements/prod.txt requirements/dev.txt  ./

# Only triggered when requeriments.txt/requirements_dev.txt changed.
RUN pip install --upgrade pip \
    && pip wheel -r /wheels_ext/dev.txt

# Service development image
FROM python:${PYTHON_VERSION} AS tr-jan-dev

RUN set -x \
    && apk add \
    g++ \
    git \
    openssh \
    libpq \
    mailcap \
    make \
    texlive-dvi \
    texmf-dist \
    pango-dev \
    cairo-dev \
    zlib-dev \
    jpeg-dev \
    texmf-dist-latexextra

COPY --from=recerca-python310-base /wheels_ext /wheels_ext

# Only triggered when requeriments.txt/requirements_dev.txt changed.
RUN pip install --upgrade pip \
    && pip install -r /wheels_ext/dev.txt -f /wheels_ext \
    && rm -rf /wheels_ext

# Creating app's user/group
RUN addgroup -S appgroup \
    && adduser -S -h /home/appuser appuser appgroup \
    # Some extra initialization
    && mkdir -p /var/log/uwsgi /var/run/uwsgi \
    && chown appuser:appgroup /var/run/uwsgi \
    && mkdir /home/appuser/tr-jan \
    && chown -R appuser:appgroup /home/appuser

WORKDIR /home/appuser/tr-jan

COPY --chown=appuser:appgroup . ./

CMD [ "uwsgi", "--ini", "./build/dev/uwsgi.ini" ]
