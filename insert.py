from pymongo import MongoClient
import json

# MongoDB connection
MONGODB_URI = "mongodb+srv://toharivenkat:hari2444@clusterhv.ew0w3qw.mongodb.net/?retryWrites=true&w=majority&appName=Clusterhv"

def insert_students():
    try:
        # Connect to MongoDB
        client = MongoClient(MONGODB_URI)
        db = client.CampusConnect
        collection = db.std_data

        # Drop existing collection to avoid duplicates
        collection.drop()

        # Read JSON file
        with open('admin.CampusConnect.json', 'r') as file:
            data = json.load(file)

        # Extract and transform student data
        students_data = []
        for record in data:
            for student_id, details in record.get('students', {}).items():
                student_doc = {
                    '_id': student_id,  # Using student_id as unique _id
                    **details
                }
                students_data.append(student_doc)

        # Insert data into MongoDB
        if students_data:
            result = collection.insert_many(students_data)
            print(f"Successfully inserted {len(result.inserted_ids)} documents.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    insert_students()
