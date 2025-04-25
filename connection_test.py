from pymongo import MongoClient
import os
from dotenv import load_dotenv

def test_mongodb_connection():
    # Load environment variables
    load_dotenv()
    
    # Get connection details
    mongodb_uri = os.getenv("MONGODB_URI")
    database_name = os.getenv("DATABASE_NAME")
    collection_name = os.getenv("COLLECTION_NAME")
    
    print("Testing MongoDB Connection...")
    print(f"Database Name: {database_name}")
    print(f"Collection Name: {collection_name}")
    
    try:
        # Attempt connection
        client = MongoClient(mongodb_uri)
        
        # Test connection
        client.admin.command('ping')
        print("✓ MongoDB connection successful!")
        
        # Check database
        db = client[database_name]
        print(f"✓ Connected to database: {database_name}")
        
        # Check collection
        collection = db[collection_name]
        doc_count = collection.count_documents({})
        print(f"✓ Collection '{collection_name}' found")
        print(f"✓ Number of documents in collection: {doc_count}")
        
        # Try to fetch one document
        sample_doc = collection.find_one()
        if sample_doc:
            print("✓ Successfully retrieved a document")
            print("\nSample document structure:")
            print(sample_doc)
        else:
            print("! Collection is empty")
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")
    finally:
        if 'client' in locals():
            client.close()
            print("\nConnection closed")

if __name__ == "__main__":
    test_mongodb_connection()