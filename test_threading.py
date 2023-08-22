import threading
import time 

def worker_function(task_name):
    print(f"Starting the {task_name}")
    time.sleep(2)
    print(f"completed the {task_name}")


thread1 = threading.Thread(target=worker_function, args=("Task 1",))
thread2 = threading.Thread(target=worker_function, args=("Task 2",))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("All threads have finished")