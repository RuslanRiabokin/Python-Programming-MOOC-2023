# Write your solution here:
class Task:
    id_counter = 0

    def __init__(self, description, programmer, workload):
        Task.id_counter += 1
        self.id = Task.id_counter
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.finished = False

    def is_finished(self):
        return self.finished

    def mark_finished(self):
        self.finished = True

    def __str__(self):
        status = "FINISHED" if self.finished else "NOT FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}"

class OrderBook:
    def __init__(self):
        self.orders = []

    def add_order(self, description, programmer, workload):
        self.orders.append(Task(description, programmer, workload))

    def all_orders(self):
        return self.orders

    def programmers(self):
        unique_programmers = set(order.programmer for order in self.orders)
        return list(unique_programmers)

    def mark_finished(self, id):
        found = False
        for order in self.orders:
            if order.id == id:
                order.mark_finished()
                found = True
                break
        if not found:
            raise ValueError("No task with the given id")

    def finished_orders(self):
        return [order for order in self.orders if order.is_finished()]

    def unfinished_orders(self):
        return [order for order in self.orders if not order.is_finished()]

    def status_of_programmer(self, programmer):
        finished_tasks = 0
        finished_hours = 0
        unfinished_tasks = 0
        unfinished_hours = 0

        for order in self.orders:
            if order.programmer == programmer:
                if order.is_finished():
                    finished_tasks += 1
                    finished_hours += order.workload
                else:
                    unfinished_tasks += 1
                    unfinished_hours += order.workload

        if finished_tasks == 0 and unfinished_tasks == 0:
            raise ValueError("No tasks found for the given programmer")

        return finished_tasks, unfinished_tasks, finished_hours, unfinished_hours
