from locust import HttpLocust, TaskSet
from wikipedia import *

class MyTaskSet(TaskSet):
    tasks = {open_main_page: 1, search: 1}

class Test(HttpLocust):
    task_set = MyTaskSet

    # Way to specify the think times between tasks
    # min_wait = 1000
    # max_wait = 5000
