from constants import *
from pinecone import Pinecone
from vlite2.utils import chop_and_chunk
from sentence_transformers import SentenceTransformer
import time
import timeit
import os
from dotenv import load_dotenv

def memorize_one_pc(index):
    short_data_embeddings = SentenceTransformer('all-MiniLM-L6-v2').encode(SHORT_DATA).tolist()
    index.upsert(vectors=[
        {"id": "id0", "values": short_data_embeddings}
    ])

def remember_pc(index, text):
    text = SentenceTransformer('all-MiniLM-L6-v2').encode(text).tolist()
    query_response = index.query(
        namespace="ns0",
        vector=text,
        top_k=10
    )

def memorize_many_pc(index):
    long_data_chunked = chop_and_chunk(LONG_DATA, 512)
    long_data_embeddings = SentenceTransformer('all-MiniLM-L6-v2').encode(long_data_chunked).tolist()
    for i in range(len(long_data_chunked)):
        index.upsert(vectors=[
            {"id": "id"+str(i), "values": long_data_embeddings[i]}
        ])


if __name__ == "__main__":
    start_time = time.time()

    memorize_one_pc_time = timeit.timeit('memorize_one_pc(index)', 
                        setup='''
from pinecone import Pinecone, PodSpec
import os
from dotenv import load_dotenv
from __main__ import memorize_one_pc
load_dotenv(dotenv_path='.env', verbose=True)
pc = Pinecone(api_key=os.getenv('PC_API_KEY'))
for i in pc.list_indexes():
    if i['name'] == "quickstart":
        pc.delete_index(i['name'])
pc.create_index(name="quickstart", dimension=384, metric="cosine", spec=PodSpec(environment='gcp-starter'))
index = pc.Index("quickstart")
                        ''',
                        number=num_executions) / num_executions
    print("FINISHED MEMORIZE ONE PC")

    remember_one_pc_time = timeit.timeit('remember_pc(index, "hello")', 
                        setup='''
from pinecone import Pinecone, PodSpec
from sentence_transformers import SentenceTransformer
import os
from dotenv import load_dotenv
from __main__ import memorize_one_pc, remember_pc
load_dotenv(dotenv_path='.env', verbose=True)
pc = Pinecone(api_key=os.getenv('PC_API_KEY'))
for i in pc.list_indexes():
    if i['name'] == "quickstart":
        pc.delete_index(i['name'])
pc.create_index(name="quickstart", dimension=384, metric="cosine", spec=PodSpec(environment='gcp-starter'))
index = pc.Index("quickstart")
memorize_one_pc(index)
                        ''',
                        number=num_executions) / num_executions
    print("FINISHED REMEMBER ONE PC")

    memorize_many_pc_time = timeit.timeit('memorize_many_pc(index)', 
                        setup='''
from pinecone import Pinecone, PodSpec
import os
from dotenv import load_dotenv
from __main__ import memorize_many_pc
load_dotenv(dotenv_path='.env', verbose=True)
pc = Pinecone(api_key=os.getenv('PC_API_KEY'))
for i in pc.list_indexes():
    if i['name'] == "quickstart":
        pc.delete_index(i['name'])
pc.create_index(name="quickstart", dimension=384, metric="cosine", spec=PodSpec(environment='gcp-starter'))
index = pc.Index("quickstart")
                        ''',
                        number=num_executions) / num_executions
    print("FINISHED MEMORIZE MANY PC")

    remember_many_pc_time = timeit.timeit('remember_pc(index, "civil law")', 
                        setup='''
from pinecone import Pinecone, PodSpec
from sentence_transformers import SentenceTransformer
import os
from dotenv import load_dotenv
from __main__ import memorize_many_pc, remember_pc
load_dotenv(dotenv_path='.env', verbose=True)
pc = Pinecone(api_key=os.getenv('PC_API_KEY'))
for i in pc.list_indexes():
    if i['name'] == "quickstart":
        pc.delete_index(i['name'])
pc.create_index(name="quickstart", dimension=384, metric="cosine", spec=PodSpec(environment='gcp-starter'))
index = pc.Index("quickstart")
memorize_many_pc(index)
                        ''',
                        number=num_executions) / num_executions
    print("FINISHED REMEMBER MANY PC")

    print(f"\n\nNumber of executions averaged over: {num_executions}")
    print(f"pc memorize one: {memorize_one_pc_time}")
    print(f"pc remember one: {remember_one_pc_time}")
    print(f"pc memorize many: {memorize_many_pc_time}")
    print(f"pc remember many: {remember_many_pc_time}")

    load_dotenv(dotenv_path='.env', verbose=True)
    pc = Pinecone(api_key=os.getenv('PC_API_KEY'))
    for i in pc.list_indexes():
        if i['name'] == "quickstart":
            pc.delete_index(i['name'])
