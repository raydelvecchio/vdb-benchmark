from constants import *
import time
import glob
import os
import timeit


def memorize_one_v1(v):
    v.memorize(SHORT_DATA)

def remember_v1(v, text):
    v.remember(text)

def memorize_many_v1(v):
    v.memorize(text=LONG_DATA)


if __name__ == "__main__":
    start_time = time.time()
    
    memorize_one_v1_time = timeit.timeit('memorize_one_v1(v)', 
                        setup='''
from vlite import VLite
from __main__ import memorize_one_v1
v = VLite()
                        ''',
                        number=num_executions) / num_executions
    print("FINISHED MEMORIZE ONE V1")

    remember_one_v1_time = timeit.timeit('remember_v1(v, "hello")', 
                        setup='''
from vlite import VLite
from __main__ import remember_v1
v = VLite()
v.memorize("Hello! My name is Ray. How are you?")
                        ''',
                        number=num_executions) / num_executions
    print("FINISHED REMEMBER ONE V1")

    memorize_many_v1_time = timeit.timeit('memorize_many_v1(v)', 
                        setup='''
from vlite import VLite
from __main__ import memorize_many_v1
v = VLite()
                        ''',
                        number=num_executions) / num_executions
    print("FINISHED MEMORIZE MANY V1")

    remember_many_v1_time = timeit.timeit('remember_v1(v, text)', 
                        setup='''
from vlite import VLite
from __main__ import remember_v1, memorize_many_v1
v = VLite()
memorize_many_v1(v)
text = "civil law"
                        ''',
                        number=num_executions) / num_executions
    print("FINISHED REMEMBER MANY V1")

    print(f"\n\nNumber of executions averaged over: {num_executions}")
    print(f"v1 memorize one: {memorize_one_v1_time}")
    print(f"v1 remember one: {remember_one_v1_time}")
    print(f"v1 memorize many: {memorize_many_v1_time}")
    print(f"v1 remember many: {remember_many_v1_time}")

    files_to_delete = glob.glob('*.npz')
    for f in files_to_delete:
        os.remove(f)

    end_time = time.time()
    print(f"Total time to run: {end_time - start_time} seconds")
