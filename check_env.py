import os
from src.logging import logging
logging.info(f"MONGODB_URL from Python: {os.getenv("MONGODB_URL")}")
