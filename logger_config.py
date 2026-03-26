from loguru import logger
import os
import sys

os.makedirs("logs", exist_ok=True)

# Remove default console logger
logger.remove()

# Console logging
logger.add(sys.stdout, level="INFO")

# File logging with rotation & retention
logger.add(
    "logs/test_{time}.log",
    rotation="1 MB",
    retention="7 days",
    compression="zip",
    level="DEBUG",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {file}:{line} | {message}"
)

app_logger = logger