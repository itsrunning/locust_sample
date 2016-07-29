from locust import HttpLocust, TaskSet
from wikipedia import *

class MyTaskSet(TaskSet):
    tasks = {open_main_page, search}

class Test(HttpLocust):
    task_set = MyTaskSet
