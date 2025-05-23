import os
import logging
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

env_path = ".env"
if os.path.exists(env_path):
    with open(env_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            if "=" in line:
                key, value = line.strip().split("=", 1)
                os.environ[key] = value

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
TMDB_API_KEY = os.getenv("TMDB_API_KEY")
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

logging.info("TMDB_API_KEY loaded")
