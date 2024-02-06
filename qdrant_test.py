from constants import *
import time
import os
import timeit
from vlite2.utils import chop_and_chunk
from qdrant_client.http.models import PointStruct
from sentence_transformers import SentenceTransformer
import pandas as pd
from openpyxl import load_workbook
import xlsxwriter

def ingest_one_q(q):
    short_data_embeddings = SentenceTransformer(model_name).encode(SHORT_DATA).tolist()
    q.upsert(
        collection_name="test_collection",
        points=[PointStruct(id=0, vector=short_data_embeddings)]
    )

def retrieve_q(q, text):
    vectors = SentenceTransformer(model_name).encode(text).tolist()
    search_result = q.search(
        collection_name="test_collection", query_vector=vectors
    )

def ingest_many_q(q):
    long_data_chunked = chop_and_chunk(LONG_DATA, 512)
    long_data_embeddings = SentenceTransformer(model_name).encode(long_data_chunked).tolist()
    points = [PointStruct(id=i, vector=long_data_embeddings[i]) for i in range(len(long_data_embeddings))]
    q.upsert(
        collection_name="test_collection",
        points=points
    )

if __name__ == "__main__":
    start_time = time.time()
    
    ingest_one_q_time = timeit.timeit('ingest_one_q(qdrant)', 
                        setup='''
from qdrant_client import QdrantClient
from constants import dimension
from qdrant_client.http.models import Distance, VectorParams
from __main__ import ingest_one_q
qdrant = QdrantClient(":memory:")
qdrant.create_collection(
collection_name="test_collection",
vectors_config=VectorParams(size=dimension, distance=Distance.COSINE)
)
                        ''',
                        number=num_executions) / num_executions
    print("FINISHED ingest ONE Q")

    retrieve_one_q_time = timeit.timeit('retrieve_q(qdrant, "hello")', 
                        setup='''
from qdrant_client import QdrantClient
from constants import dimension
from qdrant_client.http.models import Distance, VectorParams
from __main__ import ingest_one_q, retrieve_q
qdrant = QdrantClient(":memory:")
qdrant.create_collection(
collection_name="test_collection",
vectors_config=VectorParams(size=dimension, distance=Distance.COSINE)
)
ingest_one_q(qdrant)
                        ''',
                        number=num_executions) / num_executions
    print("FINISHED retrieve ONE Q")

    ingest_many_q_time = timeit.timeit('ingest_many_q(qdrant)', 
                        setup='''
from qdrant_client import QdrantClient
from constants import dimension
from qdrant_client.http.models import Distance, VectorParams
from __main__ import ingest_many_q
qdrant = QdrantClient(":memory:")
qdrant.create_collection(
collection_name="test_collection",
vectors_config=VectorParams(size=dimension, distance=Distance.COSINE)
)
                        ''',
                        number=num_executions) / num_executions
    print("FINISHED ingest MANY Q")

    retrieve_many_q_time = timeit.timeit('retrieve_q(qdrant, "civil law")', 
                        setup='''
from qdrant_client import QdrantClient
from constants import dimension
from qdrant_client.http.models import Distance, VectorParams
from __main__ import ingest_many_q, retrieve_q
qdrant = QdrantClient(":memory:")
qdrant.create_collection(
collection_name="test_collection",
vectors_config=VectorParams(size=dimension, distance=Distance.COSINE)
)
ingest_many_q(qdrant)
                        ''',
                        number=num_executions) / num_executions
    print("FINISHED retrieve MANY Q")

    print(f"\n\nNumber of executions averaged over: {num_executions}")
    print(f"q ingest one: {ingest_one_q_time}")
    print(f"q retrieve one: {retrieve_one_q_time}")
    print(f"q ingest many: {ingest_many_q_time}")
    print(f"q retrieve many: {retrieve_many_q_time}")

    end_time = time.time()
    print(f"Total time to run: {end_time - start_time} seconds")

    if not os.path.exists('benchmark.xlsx'):
        workbook = xlsxwriter.Workbook('benchmark.xlsx')
        worksheet = workbook.add_worksheet()
        workbook.close()
        first_df = pd.DataFrame({'': ["ingest One", "retrieve One", "ingest Many", "retrieve Many"]})
        first = 1
    else:
        first = 0
    writer = pd.ExcelWriter('benchmark.xlsx', engine='openpyxl', mode = 'a', if_sheet_exists='overlay')
    workbook = load_workbook("benchmark.xlsx")
    writer.workbook = workbook
    df = pd.DataFrame({'Qdrant': [ingest_one_q_time, retrieve_one_q_time, ingest_many_q_time, retrieve_many_q_time]})
    writer.worksheets = {ws.title: ws for ws in workbook.worksheets}
    reader = pd.read_excel('benchmark.xlsx')
    if (first == 1):
        first_df.to_excel(writer, startcol=reader.shape[1], index = False)
    df.to_excel(writer, startcol=reader.shape[1] + first, index = False)
    writer.close()