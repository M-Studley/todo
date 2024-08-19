import os


class Config:
    # Set DATABASE URL from environment variable
    DATABASE_URL = os.environ.get('DATABASE_URL')
    if not DATABASE_URL:
        raise ValueError("No DATABASE_URL environment variable set...")
