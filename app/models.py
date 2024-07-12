from dataclasses import dataclass


@dataclass
class TestTodo:
    title: str
    description: str
    id: int = None


# @dataclass
# class Todo:
#     title: str
#     description: str
#     created_at: str
#     estimated_end: str
#     completion_duration: int
#     id: int = None
#     priority: str = 'unknown'
#     status: str = 'open'
