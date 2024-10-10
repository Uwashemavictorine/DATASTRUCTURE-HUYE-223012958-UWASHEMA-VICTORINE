class ProjectManager:
    def __init__(self):
        self.undo_stack = []   
        self.pending_tasks = [] 
        self.members = []       
    def add_member(self, name, role):
        self.members.append({'name': name, 'role': role})
        print(f"Added member: {name}, Role: {role}")
    def assign_task(self, task, member):
        if member in [m['name'] for m in self.members]:
            self.undo_stack.append((task, member))  
            print(f"Assigned task '{task}' to {member}")
        else:
            print(f"Member {member} does not exist.")
    def undo_assignment(self):
        if self.undo_stack:
            task, member = self.undo_stack.pop()
            print(f"Undid assignment of task '{task}' from {member}")
        else:
            print("No task assignments to undo.")
    def add_task(self, task):
        self.pending_tasks.append(task)
        print(f"Added task: '{task}' to pending tasks.")
    def complete_task(self):
        if self.pending_tasks:
            task = self.pending_tasks.pop(0)  # 
            print(f"Completed task: '{task}'")
        else:
            print("No pending tasks to complete.")
    def show_members(self):
        print("Group Members:")
        for member in self.members:
            print(f"{member['name']} - {member['role']}")
    def show_pending_tasks(self):
        print("Pending Tasks:")
        for task in self.pending_tasks:
            print(f"- {task}")
if __name__ == "__main__":
    pm = ProjectManager()
    pm.add_member("vicky", "Developer")
    pm.add_member("jolly", "Designer")
    pm.add_task("organisation ")
    pm.add_task("planning ")
    pm.assign_task("organisation", "vicky")
    pm.assign_task("planning", "jolly")
    pm.show_members()
    pm.show_pending_tasks()
    pm.undo_assignment()
    pm.complete_task()
    pm.show_pending_tasks()
