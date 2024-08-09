from datetime import datetime

from dataclasses import dataclass


@dataclass
class Todo:
    name: str  # min: 2 max: 30 char
    description: str  # min: 0 max: 750 char
    category: str  # min: 2 max: 20 char
    priority: str  # ENUM ('critical', 'high', 'medium', 'low', 'neutral') default: 'neutral'
    created_at: datetime  # DATETIME ISO format YYYY-MM-DDThh:mm:ss:sssZ ex: 2024-08-02T18:05:45:888Z default: NOW()
    deadline: datetime  # DATETIME ISO format YYYY-MM-DDThh:mm:ss:sssZ ex: 2024-08-02T18:05:45:888Z ALLOW NULL
    completed: bool  # True for completed False for NOT completed
    id: int = None  # auto-incremented


class TodoValidator:

    @staticmethod
    def check_name(todo: Todo) -> bool:
        if 2 <= len(todo.name) <= 30:
            print('Name: Passed!')
            return True
        print('Name: Failed [incorrect name length]...')
        return False

    @staticmethod
    def check_description(todo: Todo) -> bool:
        if len(todo.description) <= 750:
            print('Description: Passed!')
            return True
        print('Description: Failed [incorrect description length]...')
        return False

    @staticmethod
    def check_category(todo: Todo) -> bool:
        if 2 <= len(todo.category) <= 20:
            print('Category: Passed!')
            return True
        print('Category: Failed [incorrect category length]...')
        return False

    @staticmethod
    def check_priority(todo: Todo) -> bool:
        if todo.priority in ['critical', 'high', 'medium', 'low', 'neutral']:
            print('Priority: Passed!')
            return True
        print('Priority: Failed [priority not in priority list]...')
        return False

    @staticmethod
    def check_deadline(todo: Todo) -> bool:
        if todo.deadline:
            if todo.deadline > todo.created_at:
                print('Deadline: Passed!')
                return True
            print('Deadline: Failed [deadline cannot be less than created_at datetime]...')
            return False
        print('Deadline: Passed! [No deadline specified]')
        return True

    @staticmethod
    def check_completed(todo: Todo) -> bool:
        if isinstance(todo.completed, bool):
            print('Completed: Passed!')
            return True
        print('Completed: Failed [completed must be a boolean]...')
        return False

    def check_all(self, todo: Todo) -> bool:
        checks = [
            self.check_name(todo),
            self.check_description(todo),
            self.check_category(todo),
            self.check_priority(todo),
            self.check_deadline(todo)
        ]
        return all(checks)
