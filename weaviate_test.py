from constants import *
from vlite2.utils import chop_and_chunk
from sentence_transformers import SentenceTransformer
import os
import time
import timeit
import weaviate_test

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
    url = "https://test-i6cwsfxe.weaviate.network",
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
    url = "https://test-i6cwsfxe.weaviate.network",
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
    url = "https://test-i6cwsfxe.weaviate.network",
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
    url = "https://test-i6cwsfxe.weaviate.network",
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

    client = weaviate_test.Client(
    url = "https://test-i6cwsfxe.weaviate.network",
    auth_client_secret=weaviate_test.auth.AuthApiKey(api_key=os.getenv('W_API_KEY')),
    )
    client.schema.delete_class("Question")
    