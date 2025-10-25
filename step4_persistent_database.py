"""
Step 4: Saving Your Work (Persistent Database)

What's the difference between in-memory and persistent?
-------------------------------------------------------

IN-MEMORY (Steps 1-3):
- Data stored in RAM (temporary memory)
- Super fast! ⚡
- Problem: Data disappears when program ends
- Like writing on a whiteboard ✏️

PERSISTENT (Step 4):
- Data saved to disk (permanent storage)
- Slightly slower but data survives restarts 💾
- Like saving a document to a file 📄

How does ChromaDB Persistent Storage work?
-------------------------------------------
1. You specify a path: "./chroma_db"
2. ChromaDB creates that folder if it doesn't exist
3. All data is automatically saved to that folder
4. Next time you run the program, the data is still there!

It's like having a filing cabinet stored in a filing room instead
of just keeping papers on a desk! 📁 → 📦
"""

import chromadb
import os

print("="*70)
print("STEP 4: PERSISTENT DATABASE")
print("="*70)

# ============================================================================
# Creating a Persistent Client (Instead of in-memory)
# ============================================================================
print("\n" + "="*70)
print("1️⃣  Creating a Persistent Client")
print("="*70)

# PersistentClient saves data to disk in the specified path
# If the path doesn't exist, ChromaDB will create it automatically
persistent_client = chromadb.PersistentClient(path="./chroma_db")

print("\n✅ Persistent client created!")
print(f"   Storage path: ./chroma_db")
print(f"   Data will be saved automatically to disk")

# ============================================================================
# Creating a Collection with Persistent Storage
# ============================================================================
print("\n" + "="*70)
print("2️⃣  Creating a Collection with Persistent Storage")
print("="*70)

# Now, when we create a collection, it will be saved automatically!
p_collection = persistent_client.get_or_create_collection(name="saved_policies")

print("\n✅ Collection 'saved_policies' created with persistent storage!")
print(f"   Collection name: {p_collection.name}")
print(f"   Collection ID: {p_collection.id}")

# ============================================================================
# Adding Data to Persistent Collection
# ============================================================================
print("\n" + "="*70)
print("3️⃣  Adding Travel Expense Policy (Data will be saved to disk)")
print("="*70)

# Add a new policy - this data will NOW be saved permanently!
p_collection.add(
    ids=["expense_policy_01"],
    documents=[
        "All expense reports must be submitted within 15 days of trip completion. "
        "Reports require manager approval and supporting receipts."
    ],
    metadatas=[
        {"policy_type": "expenses", "days_limit": 15}
    ]
)

print("✅ Added expense policy to persistent collection")
print(f"📊 Total documents in persistent collection: {p_collection.count()}")

# ============================================================================
# Verifying Data Persistence
# ============================================================================
print("\n" + "="*70)
print("4️⃣  Verifying Data Persistence")
print("="*70)

# Query the persistent collection
results = p_collection.query(
    query_texts=["When must expense reports be submitted?"],
    n_results=1
)

print("\n🔍 Query: 'When must expense reports be submitted?'")
print(f"\n📄 Result:")
print(f"   {results['documents'][0][0]}")

# ============================================================================
# Important: Data Survives Program Restarts!
# ============================================================================
print("\n" + "="*70)
print("5️⃣  The Magic: Data Persists Between Program Runs")
print("="*70)

print("""
🎯 What happens next:
   1. This program ends
   2. The data is SAVED in the ./chroma_db folder
   3. When you run this script again, the data is STILL THERE!
   4. The collection remembers everything

This is why persistent storage is so powerful! 
Your data survives even if you restart your computer! 💪
""")

# ============================================================================
# Checking File System
# ============================================================================
print("\n" + "="*70)
print("6️⃣  What's Actually Saved to Disk")
print("="*70)

chroma_db_path = "./chroma_db"
if os.path.exists(chroma_db_path):
    print(f"\n✅ Folder '{chroma_db_path}' exists on disk")
    print(f"\n📂 Contents:")
    
    for root, dirs, files in os.walk(chroma_db_path):
        level = root.replace(chroma_db_path, '').count(os.sep)
        indent = ' ' * 2 * level
        print(f'{indent}📁 {os.path.basename(root)}/')
        subindent = ' ' * 2 * (level + 1)
        
        # Only show first few files to keep output clean
        for file in files[:10]:
            print(f'{subindent}📄 {file}')
        
        if len(files) > 10:
            print(f'{subindent}📄 ... and {len(files) - 10} more files')

# ============================================================================
# Summary
# ============================================================================
print("\n" + "="*70)
print("🎉 STEP 4 COMPLETE: Persistent Storage Mastered!")
print("="*70)
print("""
✅ What we learned:
   • Created a PersistentClient (saves to disk)
   • Data automatically saved to ./chroma_db folder
   • Collections survive program restarts
   • No extra code needed - it just works!

🌟 Key Difference:
   • In-Memory Client: ChromaDB.Client()
   • Persistent Client: chromadb.PersistentClient(path="./chroma_db")

📌 Current Storage Status:
   - Storage Path: ./chroma_db
   - Collection: saved_policies
   - Documents: 1
   - Status: ✅ SAVED TO DISK

➡️  Next: Step 5 will teach us CRUD operations on Collections themselves!
""")
print("="*70)
