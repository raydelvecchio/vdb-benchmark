# VDB Comparisons
Speed and other comparisons, primarily used to test and verify the speed of [Vlite2](https://github.com/raydelvecchio/vlite-v2). The goal here is to show the speed
of Vlite and Vlite2 compared to other vector databases when spinning up a local project. 

# Authors
Bulk of benchmarks written by [Salvatore Del Vecchio](https://github.com/saldelv). Initiated by [me](https://github.com/raydelvecchio). If you'd like to
continue benchmarking or develop new ones, contact me [here](mailto:ray@cerebralvalley.ai).

# Benchmarks
All benchmarks are based on the [original vlite tests](https://github.com/sdan/vlite/blob/master/tests/bench.py), and are definitely not scientifically rigorous. The
goal here is to simulate what a typical user would do when spinning up a RAG app for local, project, or small production use. 
* Memorize One: time to ingest one constant entry into the database
* Memorize Many: time to ingest many texts from a corpus into the database
* Remember One: given a query, time to retrieve the top result when there is only *one* entry in the database
* Remember Many: given a query, time to retrieve the top results when there is an entire corpus of entries in the database

# Results
All the below results are from 100 averaged iterations on a 16GB M2 Macbook Pro *not* plugged into power. Pinecone and Weaviate running *remotely* as 
they would be when starting a new project. Chunking and chopping is normalized across all tests (same function used for all tests). The same embedding model
(all-MiniLM-L6-v2) used across all tests as well (except chroma, where default embedding function used).
![Memorize One](./results/benchmark_1_Memorize%20One.png)
![Memorize Many](./results/benchmark_3_Memorize%20Many.png)
![Remember One](./results/benchmark_2_Remember%20One.png)
![Remember Many](./results/benchmark_4_Remember%20Many.png)

# Run Instructions
* Can run each file individually, or run all at once with `all_tests.sh`
* Configuration for all the test runs found in `config.py`
* All files output the benchmark results to `benchmark.xlsx`
* `graphs.py` outputs each benchmark for each db into `/results` as an image

# Comparisons
* VLite
* VLite2
* Chroma
* Pinecone
* Weaviate
* Qdrant
