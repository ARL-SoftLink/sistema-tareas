task=[]
def add_task(task):
        task.append(task)
def list_tasks():    
        for i, task in enumerate(task):
                print(f"{i}: {task}")
def delete_task(index):    
        if 0 <= index < len(task):        
                return task.pop(index)
