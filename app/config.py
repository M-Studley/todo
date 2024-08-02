import os


class Config:
    # SET DATABASE URL FROM ENVIRONMENT VARIABLE
    DATABASE_URL = os.environ.get(
        'DATABASE_URL',
        'postgresql://todo_99fq_user:UFzkR7Uld0Xn2s0JbwVrvTBKcIAHIw1P@dpg-cq8f2juehbks738imep0-a.oregon-postgres'
        '.render.com/todo_99fq'
    )
