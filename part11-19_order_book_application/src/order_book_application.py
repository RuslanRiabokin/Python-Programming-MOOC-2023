# Write your solution here
# If you use the classes made in the previous exercise, copy them here
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


def main():
    orders = OrderBook()
    while True:
        print("\ncommands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer\n")

        command = input("command: ")

        if command == "0":
            break

        elif command == "1":
            description = input("description: ")
            try:
                programmer, workload = input("programmer and workload estimate: ").split()
                workload = int(workload)
                orders.add_order(description, programmer, workload)
                print("added!")
            except (ValueError, IndexError):
                print("erroneous input")

        elif command == "2":
            finished_tasks = orders.finished_orders()
            if not finished_tasks:
                print("no finished tasks")
            else:
                for task in finished_tasks:
                    print(task)

        elif command == "3":
            unfinished_tasks = orders.unfinished_orders()
            for task in unfinished_tasks:
                print(task)

        elif command == "4":
            try:
                id = int(input("id: "))
                orders.mark_finished(id)
                print("marked as finished")
            except ValueError:
                print("erroneous input")

        elif command == "5":
            programmers = orders.programmers()
            for programmer in programmers:
                print(programmer)

        elif command == "6":
            programmer = input("programmer: ")
            try:
                status = orders.status_of_programmer(programmer)
                print(f"tasks: finished {status[0]} not finished {status[1]}, hours: done {status[2]} scheduled {status[3]}")
            except ValueError:
                print("erroneous input")

        else:
            print("Invalid command. Please try again.")



main()
