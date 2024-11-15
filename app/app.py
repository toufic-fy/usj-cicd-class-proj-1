from flask import Flask, jsonify
from redis import Redis
import os 
import logging

app = Flask(__name__)

log_file_path = os.getenv("LOG_FILE_PATH", "/var/log/counter-app/counter.log")
redis_host = os.getenv("REDIS_HOST", "redis-service")
redis_port = int(os.getenv("REDIS_PORT", 6379))


logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

try:
    redis = Redis(host=redis_host, port=redis_port)
    logging.info("Connected to Redis successfully")
except ConnectionError as e:
    logging.error(f"Redis connection error: {e}")
    redis = None

@app.route('/')
def get_count():
    if redis is None:
        logging.error("Redis is not connected.")
        return jsonify(error="Redis connection error"), 500

    try:
        count = redis.incr('counter')
        logging.info(f"Counter incremented: {count}")
        return jsonify(count=count)
    except Exception as e:
        logging.error(f"Error retrieving count: {e}")
        return jsonify(error="Internal Server Error"), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)