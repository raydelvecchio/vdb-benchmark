# VDB Comparisons
Speed and other comparisons, primarily used to test and verify the speed of [Vlite2](https://github.com/raydelvecchio/vlite-v2). 

# Benchmarks
* Startup Time: time to initialize an instance of the database
* Memorize One: time to memorize one constant entry into the database
* Memorize Many: time to memorize many texts from a corpus into the database
* Remember One: given a query, time to get the top result when there is only *one* entry in the database
* Remember Many: given a query, time to get the top k (constant) results when there is an entire corpus of entries in the database

# Comparisons
* VLite
* VLite2
* Chroma
* Pinecone
* Weaviate
* Qdrant