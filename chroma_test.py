from constants import *
from chromadb.utils import embedding_functions
from vlite2.utils import chop_and_chunk
import time
import timeit
import pandas as pd
from openpyxl import load_workbook
import xlsxwriter
import os

default_ef = embedding_functions.DefaultEmbeddingFunction()

def memorize_one_cdb(cdb):
    cdb.add(
        documents = [SHORT_DATA],
        embeddings = default_ef([SHORT_DATA]),
        ids = ["id0"],
    )

def remember_cdb(cdb, text):
    results = cdb.query(
        query_texts=[text],
    )

def memorize_many_cdb(cdb):
    long_data_chunked = chop_and_chunk(LONG_DATA, 512)
    cdb.add(
        documents = long_data_chunked,
        embeddings = default_ef(long_data_chunked),
        ids = ["id"+str(i) for i in range(len(long_data_chunked))],
    )


if __name__ == "__main__":
    start_time = time.time()

    memorize_one_cdb_time = timeit.timeit('memorize_one_cdb(collection)', 
                        setup='''
import chromadb
from chromadb.utils import embedding_functions
from __main__ import memorize_one_cdb
client = chromadb.Client()
collection = client.create_collection(name="collection")
                        ''',
                        number=num_executions) / num_executions
    print("FINISHED MEMORIZE ONE CDB")

    remember_one_cdb_time = timeit.timeit('remember_cdb(collection2, "hello")', 
                        setup='''
import chromadb
from chromadb.utils import embedding_functions
from __main__ import remember_cdb
client = chromadb.Client()
collection2 = client.create_collection(name="collection2")
collection2.add(
        documents = ["Hello! My name is Ray. How are you?"],
        ids = ["id1"],
    )
                        ''',
                        number=num_executions) / num_executions
    print("FINISHED REMEMBER ONE CDB")

    memorize_many_cdb_time = timeit.timeit('memorize_many_cdb(collection3)', 
                        setup='''
import chromadb
from chromadb.utils import embedding_functions
from __main__ import memorize_many_cdb
client = chromadb.Client()
collection3 = client.create_collection(name="collection3")
                        ''',
                        number=num_executions) / num_executions
    print("FINISHED MEMORIZE MANY CDB")

    remember_many_cdb_time = timeit.timeit('remember_cdb(collection4, "civil law")', 
                        setup='''
import chromadb
from chromadb.utils import embedding_functions
from __main__ import memorize_many_cdb, remember_cdb
client = chromadb.Client()
collection4 = client.create_collection(name="collection4")
memorize_many_cdb(collection4)
                        ''',
                        number=num_executions) / num_executions
    print("FINISHED REMEMBER MANY CDB")

    print(f"\n\nNumber of executions averaged over: {num_executions}")
    print(f"cdb memorize one: {memorize_one_cdb_time}")
    print(f"cdb remember one: {remember_one_cdb_time}")
    print(f"cdb memorize many: {memorize_many_cdb_time}")
    print(f"cdb remember many: {remember_many_cdb_time}")

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
    df = pd.DataFrame({'Chroma': [memorize_one_cdb_time, remember_one_cdb_time, memorize_many_cdb_time, remember_many_cdb_time]})
    writer.worksheets = {ws.title: ws for ws in workbook.worksheets}
    reader = pd.read_excel('benchmark.xlsx')
    if (first == 1):
        first_df.to_excel(writer, startcol=reader.shape[1], index = False)
    df.to_excel(writer, startcol=reader.shape[1] + first, index = False)
    writer.close()
