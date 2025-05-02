# lib/models/task.py

class Task:
    _tasks = []
    _id_counter = 1

    def __init__(self, description):
        self.id = Task._id_counter
        self.description = description
        self.completed = False
        Task._id_counter += 1
        Task._tasks.append(self)

    @classmethod
    def all(cls):
        return cls._tasks

    @classmethod
    def get(cls, task_id):
        return next((task for task in cls._tasks if task.id == task_id), None)

    @classmethod
    def delete(cls, task_id):
        task = cls.get(task_id)
        if task:
            cls._tasks.remove(task)

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "✔" if self.completed else "✗"
        return f"[{self.id}] {self.description} - {status}"
