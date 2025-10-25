"""
Step 2: Creating Your First "Filing Cabinet" (Collection)

What is a Collection?
---------------------
Think of a collection like a DRAWER in a filing cabinet:
- Each drawer (collection) holds related documents
- You can have multiple drawers for different topics
- In our case, we'll create a drawer specifically for "travel policies"

What happens when we run this code?
------------------------------------
1. We initialize ChromaDB - this creates an in-memory database (like RAM)
2. We create a collection called "travel_policies"
3. The collection is ready to store documents!

Note: This is "in-memory" which means it disappears when the program ends.
We'll learn how to save it permanently in Step 4!
"""

# Import the ChromaDB library
import chromadb

# Initialize the ChromaDB client
# This creates an in-memory database (data exists only while program runs)
# Think of this as opening a filing cabinet
client = chromadb.Client()
print("✅ ChromaDB client initialized successfully!")
print(f"   Client type: {type(client)}")

# Create a new collection or get it if it already exists
# A collection is like a single drawer in your filing cabinet
# dedicated to a specific topic—in our case, company travel policies
collection = client.get_or_create_collection(name="travel_policies")
print("\n✅ Collection 'travel_policies' created successfully!")
print(f"   Collection name: {collection.name}")
print(f"   Collection ID: {collection.id}")

# Check how many documents are in the collection (should be 0 since it's new)
count = collection.count()
print(f"\n📊 Number of documents in collection: {count}")

# List all collections in the database
all_collections = client.list_collections()
print(f"\n📁 Total collections in database: {len(all_collections)}")
for coll in all_collections:
    print(f"   - {coll.name}")

print("\n" + "="*60)
print("🎉 Step 2 Complete! Your first collection is ready!")
print("="*60)
print("\nNext up: We'll add documents to this collection in Step 3!")

