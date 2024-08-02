from dataclasses import dataclass


@dataclass
class Todo:
    name: str  # min: 2 max: 30 char
    description: str  # min: 0 max: 750 char
    category: str  # min: 2 max: 20 char
    priority: str  # ENUM ('critical', 'high', 'medium', 'low', 'neutral') default: 'neutral'
    created_at: str  # DATETIME ISO format YYYY-MM-DDThh:mm:ss:sssZ ex: 2024-08-02T18:05:45:888Z default: NOW()
    deadline: str  # DATETIME ISO format YYYY-MM-DDThh:mm:ss:sssZ ex: 2024-08-02T18:05:45:888Z ALLOW NULL
    completed: bool  # True for completed False for NOT completed
    id: int = None  # auto-incremented


class TodoValidator:

