### Deploy:
```bash
git clone https://github.com/henerborn/max_bot
cd max_bot
mkdir -p assets data
nano .env             # configure environment variables (check out .env.example)
docker compose build  # build images
docker compose up -d  # start containers
```

### Update project
```bash
git pull origin main
docker compose up -d --build
```

### Logs
```bash
docker compose logs -f     
docker compose logs -f <container_name>
```