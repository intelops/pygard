import os
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("pygard.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("pygard")

def ensure_cache_dir(cache_dir):
    os.makedirs(cache_dir, exist_ok=True)
    logger.info(f"Cache directory ensured at {cache_dir}")
