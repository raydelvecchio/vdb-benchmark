from constants import *
import time
import glob
import os
import timeit
import pandas as pd
from openpyxl import load_workbook
import xlsxwriter

def memorize_one_v2(v):
    v.ingest(SHORT_DATA)

def remember_v2(v, text):
    v.retrieve(text)

def memorize_many_v2(v):
    v.ingest(text=LONG_DATA)


if __name__ == "__main__":
    start_time = time.time()

    memorize_one_v2_time = timeit.timeit('memorize_one_v2(v)', 
                        setup='''
from vlite2 import VLite2
from __main__ import memorize_one_v2
v = VLite2()
                        ''',
                        number=num_executions) / num_executions
    print("FINISHED MEMORIZE ONE V2")

    remember_one_v2_time = timeit.timeit('remember_v2(v, "hello")', 
                        setup='''
from vlite2 import VLite2
from __main__ import remember_v2
v = VLite2()
v.ingest("Hello! My name is Ray. How are you?")
                        ''',
                        number=num_executions) / num_executions
    print("FINISHED REMEMBER ONE V2")

    memorize_many_v2_time = timeit.timeit('memorize_many_v2(v)', 
                        setup='''
from vlite2 import VLite2
from __main__ import memorize_many_v2
v = VLite2()
                        ''',
                        number=num_executions) / num_executions
    print("FINISHED MEMORIZE MANY V2")

    remember_many_v2_time = timeit.timeit('remember_v2(v, "civil law")', 
                        setup='''
from vlite2 import VLite2
from __main__ import remember_v2, memorize_many_v2
v = VLite2()
memorize_many_v2(v)
                        ''',
                        number=num_executions) / num_executions
    print("FINISHED REMEMBER MANY V2")

    print(f"\n\nNumber of executions averaged over: {num_executions}")
    print(f"v2 memorize one: {memorize_one_v2_time}")
    print(f"v2 remember one: {remember_one_v2_time}")
    print(f"v2 memorize many: {memorize_many_v2_time}")
    print(f"v2 remember many: {remember_many_v2_time}")

    files_to_delete = glob.glob('*.info')
    files_to_delete += glob.glob('*.index')
    for f in files_to_delete:
        os.remove(f)

    end_time = time.time()
    print(f"Total time to run: {end_time - start_time} seconds")

    if not os.path.exists('benchmark.xlsx'):
        workbook = xlsxwriter.Workbook('benchmark.xlsx')
        worksheet = workbook.add_worksheet()
        workbook.close()
        first_df = pd.DataFrame({'': ["Memorize One", "Remember One", "Memorize Many", "Remember Many"]})
        first = 1;
    else:
        first = 0;
    writer = pd.ExcelWriter('benchmark.xlsx', engine='openpyxl', mode = 'a', if_sheet_exists='overlay')
    workbook = load_workbook("benchmark.xlsx")
    writer.workbook = workbook
    df = pd.DataFrame({'VLite2': [memorize_one_v2_time, remember_one_v2_time, memorize_many_v2_time, remember_many_v2_time]})
    writer.worksheets = {ws.title: ws for ws in workbook.worksheets}
    reader = pd.read_excel('benchmark.xlsx')
    if (first == 1):
        first_df.to_excel(writer, startcol=reader.shape[1], index = False)
    df.to_excel(writer, startcol=reader.shape[1] + first, index = False)
    writer.close()
    