docker exec hydra \
    hydra clients create \
    --endpoint http://127.0.0.1:4445 \
    --id auth-code-client \
    --secret secret \
    --grant-types authorization_code,refresh_token \
    --response-types code,id_token \
    --scope openid,profile,email,groups,offline \
    --callbacks http://127.0.0.1:5555/callback \
    --callbacks https://localhost:8443/mobirest/auth/oauth/callback