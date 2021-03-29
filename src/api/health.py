from flask import jsonify
import logging
import time
from config.server_config import ServerConfig

logger = logging.getLogger('app')

server_config = ServerConfig()
limiter = server_config.get_rate_limiter()


@limiter.limit("1/second")
def status():
    return jsonify({
        "successful": True,
        "status": "active",
        "timestamp": time.time_ns()
    })
