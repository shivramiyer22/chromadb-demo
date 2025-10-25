"""
Step 3: Managing Your Data (CRUD on Data Points)

What is CRUD?
-------------
CRUD stands for the four basic operations you can perform on data:
- CREATE: Add new documents
- READ: Search/query documents
- UPDATE: Modify existing documents
- DELETE: Remove documents

What makes ChromaDB special?
-----------------------------
Regular databases search for EXACT words. ChromaDB understands MEANING!

Example:
- Regular search: "flight" only finds documents with the word "flight"
- ChromaDB: "airplane travel" finds documents about flights, even without that exact word!

This is called "Semantic Search" - searching by meaning, not just keywords.

What are Embeddings?
--------------------
Think of embeddings as "coordinates in meaning space":
- Similar concepts are close together
- Different concepts are far apart
- ChromaDB automatically creates these for you!
"""

import chromadb

# Initialize ChromaDB and create/get collection
client = chromadb.Client()
collection = client.get_or_create_collection(name="travel_policies")

print("="*70)
print("STEP 3: CRUD OPERATIONS ON DATA")
print("="*70)

# ============================================================================
# CREATE: Adding Documents
# ============================================================================
print("\n" + "="*70)
print("1️⃣  CREATE: Adding Travel Policy Documents")
print("="*70)

# We need three things for each document:
# 1. ids: Unique identifier (like a document number)
# 2. documents: The actual text content
# 3. metadatas: Extra information for filtering (optional but useful)

collection.add(
    # Unique IDs for each policy document
    ids=[
        "flight_policy_01",
        "hotel_policy_01",
        "rental_car_policy_01",
        "flight_policy_02"
    ],
    
    # The actual policy text - this is what gets searched
    documents=[
        "For domestic flights, employees must book economy class tickets. Business class is only permitted for international flights over 8 hours.",
        "Employees can book hotels up to a maximum of $250 per night in major cities. A list of preferred hotel partners is available.",
        "A mid-size sedan is the standard for car rentals. Upgrades require manager approval. Always select the company's insurance option.",
        "All flights, regardless of destination, must be booked through the official company travel portal, 'Concur'."
    ],
    
    # Metadata: Extra info to help organize and filter documents
    # Think of it like tags or labels on file folders
    metadatas=[
        {"policy_type": "flights"},
        {"policy_type": "hotels"},
        {"policy_type": "rental_cars"},
        {"policy_type": "flights", "requires_portal": "True"}
    ]
)

print("✅ Added 4 travel policy documents to the collection")
print(f"📊 Total documents in collection: {collection.count()}")

# ============================================================================
# READ: Querying Documents (The Magic Part!)
# ============================================================================
print("\n" + "="*70)
print("2️⃣  READ: Querying Documents with Natural Language")
print("="*70)

# Let's ask a question in natural language!
# Notice: We ask about "international flights" 
# ChromaDB will find relevant documents even if they don't use those exact words
results = collection.query(
    query_texts=["What is the policy for international flights?"],
    n_results=2  # Get the top 2 most relevant results
)

print("\n🔍 Query: 'What is the policy for international flights?'")
print("\n📄 Top Results:")
for i, (doc_id, document, distance) in enumerate(zip(
    results['ids'][0], 
    results['documents'][0], 
    results['distances'][0]
), 1):
    print(f"\n   Result {i}:")
    print(f"   ID: {doc_id}")
    print(f"   Document: {document}")
    print(f"   Distance: {distance:.4f} (lower = more relevant)")

print("\n💡 Notice: ChromaDB found the relevant policy about international flights!")
print("   This is semantic search - it understands MEANING, not just keywords.")

# ============================================================================
# UPDATE: Modifying Documents
# ============================================================================
print("\n" + "="*70)
print("3️⃣  UPDATE: Modifying Existing Documents")
print("="*70)

print("\n📝 Original hotel policy: $250 per night")
print("📝 Let's update it to $300 and add a new train policy...")

# upsert = "update or insert"
# - If the ID exists, it UPDATES the document
# - If the ID doesn't exist, it INSERTS a new document
collection.upsert(
    ids=["hotel_policy_01", "train_policy_01"],
    documents=[
        "Employees can book hotels up to a maximum of $300 per night. See the portal for preferred partners.",
        "Train travel is encouraged for trips under 4 hours. Business class tickets are approved for all train journeys."
    ],
    metadatas=[
        {"policy_type": "hotels", "max_spend": 300},
        {"policy_type": "train", "last_updated": "2025-10-15"}
    ]
)

print("✅ Updated hotel_policy_01 (increased budget to $300)")
print("✅ Added train_policy_01 (new policy)")
print(f"📊 Total documents now: {collection.count()}")

# Let's verify the update worked
verify_results = collection.query(
    query_texts=["What is the hotel budget?"],
    n_results=1
)
print(f"\n🔍 Verification - Hotel budget query result:")
print(f"   {verify_results['documents'][0][0]}")

# ============================================================================
# DELETE: Removing Documents
# ============================================================================
print("\n" + "="*70)
print("4️⃣  DELETE: Removing Documents")
print("="*70)

print(f"\n📊 Documents before deletion: {collection.count()}")

# Let's remove the train policy (maybe it was temporary)
collection.delete(ids=["train_policy_01"])

print("🗑️  Deleted train_policy_01")
print(f"📊 Documents after deletion: {collection.count()}")

# ============================================================================
# Summary
# ============================================================================
print("\n" + "="*70)
print("🎉 STEP 3 COMPLETE: CRUD Operations Mastered!")
print("="*70)
print("\n✅ What we learned:")
print("   • CREATE: Added documents with add()")
print("   • READ: Queried with natural language using query()")
print("   • UPDATE: Modified documents with upsert()")
print("   • DELETE: Removed documents with delete()")
print("\n🌟 Key Takeaway:")
print("   ChromaDB uses SEMANTIC SEARCH - it understands meaning,")
print("   not just exact keywords. This is what makes it powerful!")
print("\n📌 Current Collection Status:")
print(f"   - Name: {collection.name}")
print(f"   - Total Documents: {collection.count()}")
print("\n➡️  Next: Step 4 will teach us how to SAVE this data permanently!")
print("="*70)

