import os
import pymongo
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_db_connection():
    """
    Create and return MongoDB database connection
    """
    try:
        # Get MongoDB URI from environment variables
        mongodb_uri = os.getenv("MONGODB_URI")
        if not mongodb_uri:
            raise ValueError("MONGODB_URI environment variable not set")

        # Create MongoDB client
        client = pymongo.MongoClient(mongodb_uri)
        
        # Get database
        db = client["CampusConnect"]
        
        # Verify connection
        client.admin.command('ping')
        print("Successfully connected to MongoDB!")
        
        return db

    except Exception as e:
        print(f"Error connecting to database: {e}")
        raise