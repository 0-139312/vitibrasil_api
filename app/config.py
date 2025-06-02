import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    FALLBACK_DIR = os.getenv('FALLBACK_DIR', 'data/fallback')