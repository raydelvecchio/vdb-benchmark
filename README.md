# VDB Comparisons
Vector database speed comparisons primarily used to test and verify the speed of [VLite2](https://github.com/raydelvecchio/vlite-v2). This repo shows speed
comparisons of different vector databases when spinning up a new project.

# Authors
Bulk of benchmarks written by [Salvatore Del Vecchio](https://github.com/saldelv). Initiated by [me](https://github.com/raydelvecchio). If you'd like to
continue benchmarking or develop new ones, contact me [here](mailto:ray@cerebralvalley.ai).

# Methodology
All benchmarks are based on the [original vlite tests](https://github.com/sdan/vlite/blob/master/tests/bench.py), and are definitely not scientifically rigorous. **The
goal here is to simulate what a typical user would do when spinning up a RAG app for local, project, or small production use.** 
Thus, for managed servies running remotely (Pinecone and Weaviate), we use the base free version. 
All the below results are from 100 averaged iterations on a 16GB M2 Macbook Pro plugged into power. 
Chunking and chopping is normalized across all tests (same function used for all tests). The same embedding model
(all-MiniLM-L6-v2) used across all tests as well. 
When retrieving, the top k results is kept constant with k=10.
All tests are designed to be the fastest possible methods for ingestion and retrieval in each given database per the latest documentation for [Weaviate](https://weaviate.io/developers/weaviate/manage-data/import), [Pinecone](https://docs.pinecone.io/docs/upsert-data), [Chroma](https://docs.trychroma.com/usage-guide), and [Qdrant](https://github.com/qdrant/qdrant-client). If these are not the fastest methods a typical user would use to ingest or retrieve from the database, please let me know!

**Tests Conducted:**
* *ingest One*: time to ingest one constant entry into the database
* *ingest Many*: time to ingest many texts from a corpus into the database
* *retrieve One*: given a query, time to retrieve the top result when there is only *one* entry in the database
* *retrieve Many*: given a query, time to retrieve the top results when there is an entire corpus of entries in the database

All entries, short and long, used to retrieve and ingest found in [constants.py](./constants.py). Short entry is used in ingest/retrieve one and consists of
one small snippet of text. Long entry is used in ingest/retrieve many and consists of a corpus of ~2,900 words of legal philosophy text.

# Comparisons
We compare many different vector *databases*. A vector database is a wrapper around a vector index. We are *not* benchmarking vector indexes, as the
average user starting out does not directly inference the index, but rather a pre-built, ready-to-use database.
* [VLite](https://github.com/sdan/vlite) (local)
* [VLite2](https://github.com/raydelvecchio/vlite-v2) (local)
* [Chroma](https://www.trychroma.com/) (local)
* [Pinecone](https://www.pinecone.io/) (managed)
* [Weaviate](https://weaviate.io/) (managed)
* [Qdrant](https://qdrant.tech/) (local)

# Results
![ingest One](./results/benchmark_1_Ingest%20One.png)
![ingest Many](./results/benchmark_3_Ingest%20Many.png)
![retrieve One](./results/benchmark_2_Retrieve%20One.png)
![retrieve Many](./results/benchmark_4_Retrieve%20Many.png)

# Conclusions
* VLite2 is the fastest database for retrieval time by a large margin (2x over VLite)
* For ingestion, VLite is the fastest, since they don't index vectors (rather calling `np.vstack` to store vectors)
* VLite2 is the easiest to use, with two exposed functions for ingestion and retrieval, fastest setup time, and fastest install time
    * Look at the code base for the complexity to use other databases; many steps to set up and inference the db
* Pinecone's GCP starter environment crashed frequently during testing of this (giving error code 500 often)

# Run Instructions / Files
* Can run each file individually, or run all at once with `all_tests.sh`
* Configuration for all the test runs found in `constants.py`
* All files output the benchmark results to `benchmark.xlsx`
* `graphs.py` outputs each benchmark for each db into `/results` as an image
