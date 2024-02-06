from constants import *
from vlite2.utils import chop_and_chunk
from sentence_transformers import SentenceTransformer
import os
import time
import timeit
from dotenv import load_dotenv
import weaviate
import pandas as pd
from openpyxl import load_workbook
import xlsxwriter

def memorize_one_w(client):
    short_data_embeddings = SentenceTransformer('all-MiniLM-L6-v2').encode(SHORT_DATA).tolist()
    with client.batch as batch:
        batch.add_data_object(
            data_object={"test": short_data_embeddings},
            class_name="Question"
        )

def remember_w(client, text):
    text = SentenceTransformer('all-MiniLM-L6-v2').encode(text).tolist()
    response = (
        client.query
        .get("Question", ["test"])
        .with_near_text({"concepts": text})
        .do()
    )

def memorize_many_w(client):
    long_data_chunked = chop_and_chunk(LONG_DATA, 512)
    long_data_embeddings = SentenceTransformer('all-MiniLM-L6-v2').encode(long_data_chunked).tolist()
    with client.batch as batch:
        for i in range(len(long_data_embeddings)):
            batch.add_data_object(
                data_object={"test": long_data_embeddings[i]},
                class_name="Question"
            )

if __name__ == "__main__":
    start_time = time.time()
    
    memorize_one_w_time = timeit.timeit('memorize_one_w(client)', 
                        setup='''
import weaviate
import weaviate.classes as wvc
import os
from dotenv import load_dotenv
from __main__ import memorize_one_w
load_dotenv(dotenv_path='.env', verbose=True)
client = weaviate.Client(
    url = os.getenv('W_URL'),
    auth_client_secret=weaviate.auth.AuthApiKey(api_key=os.getenv('W_API_KEY')),
)
class_obj = {
    "class": "Question",
    "vectorizer": "none",
}
client.schema.delete_class("Question")
client.schema.create_class(class_obj)
                        ''',
                        number=num_executions) / num_executions
    print("FINISHED MEMORIZE ONE W")
    
    remember_one_w_time = timeit.timeit('remember_w(client, "hello")', 
                        setup='''
import weaviate
import weaviate.classes as wvc
import os
from dotenv import load_dotenv
from __main__ import memorize_one_w, remember_w
load_dotenv(dotenv_path='.env', verbose=True)
client = weaviate.Client(
    url = os.getenv('W_URL'),
    auth_client_secret=weaviate.auth.AuthApiKey(api_key=os.getenv('W_API_KEY')),
)
class_obj = {
    "class": "Question",
    "vectorizer": "none",
}
client.schema.delete_class("Question")
client.schema.create_class(class_obj)
memorize_one_w(client)
                        ''',
                        number=num_executions) / num_executions
    print("FINISHED REMEMBER ONE W")

    memorize_many_w_time = timeit.timeit('memorize_many_w(client)', 
                        setup='''
import weaviate
import weaviate.classes as wvc
import os
from dotenv import load_dotenv
from __main__ import memorize_many_w
load_dotenv(dotenv_path='.env', verbose=True)
client = weaviate.Client(
    url = os.getenv('W_URL'),
    auth_client_secret=weaviate.auth.AuthApiKey(api_key=os.getenv('W_API_KEY')),
)
class_obj = {
    "class": "Question",
    "vectorizer": "none",
}
client.schema.delete_class("Question")
client.schema.create_class(class_obj)
                        ''',
                        number=num_executions) / num_executions

    remember_many_w_time = timeit.timeit('remember_w(client, "civil law")', 
                        setup='''
import weaviate
import weaviate.classes as wvc
import os
from dotenv import load_dotenv
from __main__ import memorize_many_w, remember_w
load_dotenv(dotenv_path='.env', verbose=True)
client = weaviate.Client(
    url = os.getenv('W_URL'),
    auth_client_secret=weaviate.auth.AuthApiKey(api_key=os.getenv('W_API_KEY')),
)
class_obj = {
    "class": "Question",
    "vectorizer": "none",
}
client.schema.delete_class("Question")
client.schema.create_class(class_obj)
memorize_many_w(client)
                        ''',
                        number=num_executions) / num_executions
    print("FINISHED REMEMBER MANY W")
    
    print(f"\n\nNumber of executions averaged over: {num_executions}")
    print(f"w memorize one: {memorize_one_w_time}")
    print(f"w remember one: {remember_one_w_time}")
    print(f"w mmemorize many: {memorize_many_w_time}")
    print(f"w remember many: {remember_many_w_time}\n\n")

    load_dotenv(dotenv_path='.env', verbose=True)
    client = weaviate.Client(
    url = os.getenv('W_URL'),
    auth_client_secret=weaviate.auth.AuthApiKey(api_key=os.getenv('W_API_KEY')),
    )
    client.schema.delete_class("Question")
    
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
    df = pd.DataFrame({'Weaviate': [memorize_one_w_time, remember_one_w_time, memorize_many_w_time, remember_many_w_time]})
    writer.worksheets = {ws.title: ws for ws in workbook.worksheets}
    reader = pd.read_excel('benchmark.xlsx')
    if (first == 1):
        first_df.to_excel(writer, startcol=reader.shape[1], index = False)
    df.to_excel(writer, startcol=reader.shape[1] + first, index = False)
    writer.close()