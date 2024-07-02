import time


def measuring_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f'Execution: {round(execution_time)} second')
    return wrapper

@measuring_time
def create_design(project, pause):
    time.sleep(pause)
    print(project)

create_design('Логотип Васильевский рынок', 3)
create_design('Макет сайта Логомашины', 5)