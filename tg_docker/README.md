1. sudo su
2. docker network create local_net
3. docker run --rm -d -p 8123:8123 -p 9000:9000 --name ch_db --network local_net yandex/clickhouse-server
4. docker run -d -p 8080:80 --network local_net spoonest/clickhouse-tabix-web-client
5. docker run -d -e APP_TOKEN={token} --name bot --network local_net tg_bot:latest
6. docker logs -f bot
