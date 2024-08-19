#from pinecone import Pinecone, ServerlessSpec

#pc = Pinecone(api_key="a419417e-0e49-48de-ad2f-dabde984c611")

from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec

pc = Pinecone(api_key='a419417e-0e49-48de-ad2f-dabde984c611')

# pc.create_index(
#    name="quickstart",
#    dimension=2, # Replace with your model dimensions
#    metric="cosine", # Replace with your model metric
#    spec=ServerlessSpec(
#        cloud="aws",
#        region="us-east-1"
#    ) 
#)

index_name = "docs-quickstart-index"

if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=2,
        metric="cosine",
        spec=ServerlessSpec(
            cloud='aws', 
            region='us-east-1'
        ) 
    ) 

    index = pc.Index(index_name)

index.upsert(
    vectors=[
        {"id": "vec1", "values": [1.0, 1.5]},
        {"id": "vec2", "values": [2.0, 1.0]},
        {"id": "vec3", "values": [0.1, 3.0]},
    ],
    namespace="ns1"
)

index.upsert(
    vectors=[
        {"id": "vec1", "values": [1.0, -2.5]},
        {"id": "vec2", "values": [3.0, -2.0]},
        {"id": "vec3", "values": [0.5, -1.5]},
    ],
    namespace="ns2"
)

print(index.describe_index_stats())
