docker-compose -f hydra_quickstart.yml exec hydra \
  hydra clients get --endpoint http://127.0.0.1:4445/ auth-code-client

