import random

class VirtualAssistant:
    def __init__(self):
        self.tasks = []
        self.appointments = []
        self.information = {
            "weather": "The weather is sunny today.",
            "news": "Latest news: AI is transforming industries.",
            "reminder": "Drink water and take breaks while working."
        }

    def add_task(self, task):
        self.tasks.append(task)
        return f"Task '{task}' added."

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            return f"Task '{task}' removed."
        return "Task not found."

    def show_tasks(self):
        return self.tasks if self.tasks else "No tasks available."

    def add_appointment(self, event):
        random_date = f"2025-02-{random.randint(1, 28)}"
        random_time = f"{random.randint(10, 18)}:{random.randint(0, 59):02d}"
        self.appointments.append({"event": event, "date": random_date, "time": random_time})
        return f"Appointment '{event}' scheduled on {random_date} at {random_time}."

    def show_appointments(self):
        return self.appointments if self.appointments else "No appointments scheduled."

    def get_information(self, key):
        return self.information.get(key, "No relevant information found.")

assistant = VirtualAssistant()

print(assistant.add_task("Complete project"))
print(assistant.show_tasks())
print(assistant.remove_task("Complete project"))
print(assistant.show_tasks())

print(assistant.add_appointment("Doctor's Appointment"))
print(assistant.add_appointment("Team Meeting"))
print(assistant.show_appointments())

print(assistant.get_information("weather"))
