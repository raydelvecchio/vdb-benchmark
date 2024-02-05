from constants import *
import time
import glob
import os
import timeit
import pandas as pd
from openpyxl import load_workbook
import xlsxwriter

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

    if not os.path.exists('benchmark.xlsx'):
        workbook = xlsxwriter.Workbook('benchmark.xlsx')
        worksheet = workbook.add_worksheet()
        workbook.close()
        first_df = pd.DataFrame({'': ["Memorize One", "Remember One", "Memorize Many", "Remember Many"]})
        first = 1
    else:
        first = 0
    writer = pd.ExcelWriter('benchmark.xlsx', engine='openpyxl', mode = 'a', if_sheet_exists='overlay')
    workbook = load_workbook("benchmark.xlsx")
    writer.workbook = workbook
    df = pd.DataFrame({'VLite1': [memorize_one_v1_time, remember_one_v1_time, memorize_many_v1_time, remember_many_v1_time]})
    writer.worksheets = {ws.title: ws for ws in workbook.worksheets}
    reader = pd.read_excel('benchmark.xlsx')
    if (first == 1):
        first_df.to_excel(writer, startcol=reader.shape[1], index = False)
    df.to_excel(writer, startcol=reader.shape[1] + first, index = False)
    writer.close()
