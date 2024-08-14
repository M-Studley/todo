import os


class Config:
    # SET DATABASE URL FROM ENVIRONMENT VARIABLE
    DATABASE_URL = os.environ.get(
        'DATABASE_URL',
        'postgresql://todo_3m8m_user:CBfySLlcCTMJJddARDWjJw3lWrWFWeak'
        '@dpg-cqu60lbqf0us73a5sc80-a.oregon-postgres.render.com/todo_3m8m'
    )
