#!/bin/bash

set -e

python3 vlite1_test.py
python3 vlite2_test.py
python3 chroma_test.py
python3 pinecone_test.py
python3 weaviate_test.py
python3 qdrant_test.py
