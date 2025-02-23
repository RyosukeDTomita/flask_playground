# Dev Container
FROM debian:bookworm AS devcontainer
WORKDIR /flask

ARG PYTHON_VERSION=3.12.4

# aqua install
RUN <<EOF bash -ex
apt-get update -y
apt-get install -y --no-install-recommends wget ca-certificates
wget -q https://github.com/aquaproj/aqua/releases/download/v2.30.0/aqua_linux_amd64.tar.gz
rm -rf /usr/local/bin/aqua && tar -C /usr/local/bin/ -xzf aqua_linux_amd64.tar.gz
rm aqua_linux_amd64.tar.gz
rm -rf /var/lib/lists
EOF

# install packages and some tools.
# NOTE: rye is installed by aqua.
COPY ./aqua.yaml ./aqua.yaml
RUN aqua install

# build
COPY /pyproject.toml .

RUN <<EOF bash -ex
PATH=$PATH":$(aqua root-dir)/bin"
rye pin ${PYTHON_VERSION}
rye sync
EOF

COPY . .

# TODO: build
CMD ["/flask/.venv/bin/gunicorn", "run:app", "--chdir", "/flask/src", "-b", "0.0.0.0:8000"]
