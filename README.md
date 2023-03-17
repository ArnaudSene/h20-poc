# H2O Wave POC

## Installation
Official guide: [h20-wave installation](https://wave.h2o.ai/docs/installation)

## Prepare environment

```shell
python3 -m venv .venv
pip install --upgrade pip
pip install -r requirements.txt
```

## Install wave server

*Ex: wave server 0.25.2 for Mac M1*
```shell
curl https://h2o-wave.s3.amazonaws.com/releases/wave-0.25.2-darwin-arm64.tar.gz --output wave-0.25.2-darwin-arm64.tar.gz
tar zxvf wave-0.25.2-darwin-arm64.tar.gz
ln -s wave-0.25.2-darwin-arm64 wave-server

```

## [Optional] Enable HTTP over TLS
Official guide: [Security](https://wave.h2o.ai/docs/security)

*Create TLS cert and key files*

```shell
cd wave-server
mkdir certs

openssl req \
   -newkey rsa:2048 -nodes -keyout domain.key \
   -x509 -days 365 -out domain.crt
```

*Export env variable for TLS*
```shell
export H2O_WAVE_TLS_CERT_FILE="./certs/domain.crt"
export H2O_WAVE_TLS_KEY_FILE="./certs/domain.key"
export H2O_WAVE_ADDRESS="https://127.0.0.1:10101"
```


## Run wave server
```shell
cd wave-server
./waved
```
> None
> If `H2O_WAVE_TLS_CERT_FILE` & `H2O_WAVE_TLS_KEY_FILE` are set, `wave` server will start over TLS.

## Run wave apps
> ! Must be located at root directory `h2o-poc/`
> 
```shell
wave run my_app.apps
```