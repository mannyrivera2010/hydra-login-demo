# hydra-login-demo
This repo is used to test openid flows.  It uses hydra and a custom python identity provider

## python identity provider build
Build Dockerfile for python identity provider
```
(cd openid_provider && docker build -t openid_provider:lastest .)

# Image will be run with docker-compose command no need to run individually 
# docker run --rm --name openid-identity-provider -p 5000:5000 openid_provider:lastest
```

## Commands to run hydra
To run containers 
```
docker-compose -f hydra_quickstart.yml -f hydra_tracing.yml up --build --remove-orphans
```

Create Oauth2 Client
```
sh client_create.sh
```
https://www.ory.sh/docs/hydra/cli/hydra-clients-create

Run Token User Test Website
```
sh client_test.sh
```
https://www.ory.sh/docs/hydra/cli/hydra-token-user


Clean up (https://docs.docker.com/compose/reference/down/)
```
docker-compose -f hydra_quickstart.yml down --volumes --remove-orphans 
docker volume prune
```

```
# And check if it's running:
docker logs ory-hydra-example--hydra
```

## Links
```
# openid-configuration
http://127.0.0.1:4444/.well-known/openid-configuration

# jwks store
http://127.0.0.1:4444/.well-known/jwks.json

# Prometheus
http://localhost:9090/

# Jaeger UI end-to-end distributed tracing
http://localhost:16686/
```

# Reference
* https://github.com/westphahl/hydra-login-consent-python
* https://github.com/ory/hydra
* https://www.jaegertracing.io/
* https://prometheus.io/
* https://www.ory.sh/docs/hydra/advanced#json-web-tokens
* https://docs.docker.com/config/containers/multi-service_container/
* https://github.com/ory/sdk/tree/master/clients/hydra/python
* https://openid.net/developers/specs/

