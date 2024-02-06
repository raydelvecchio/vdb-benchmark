# VDB Comparisons
Speed and other comparisons, primarily used to test and verify the speed of [Vlite2](https://github.com/raydelvecchio/vlite-v2). Example of such a benchmark for the [original VLite](https://github.com/sdan/vlite) can be found [here](https://github.com/sdan/vlite/blob/master/tests/bench.py). 

# Benchmarks
* Memorize One: time to memorize one constant entry into the database
* Memorize Many: time to memorize many texts from a corpus into the database
* Remember One: given a query, time to get the top result when there is only *one* entry in the database
* Remember Many: given a query, time to get the top k (constant) results when there is an entire corpus of entries in the database

# Results
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
NOTE: *Vlite, Vlite2, Chroma, and Qdrant are running locally, Pinecone and Weaviate are running remotely*.
* VLite
* VLite2
* Chroma
* Pinecone
* Weaviate
* Qdrant
