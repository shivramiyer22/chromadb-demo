"""
Step 5: Managing Your Collections (CRUD on Collections)

What does "Collections" mean here?
----------------------------------
In previous steps, we worked with DATA inside collections.
Now we're managing the COLLECTIONS THEMSELVES!

ANALOGY:
- Previous steps: Organizing papers INSIDE filing drawers
- This step: Managing the filing drawers themselves
           (Create new drawers, rename them, remove them, etc.)

Collection CRUD Operations:
- CREATE: Create a new collection
- READ: List all collections in the database
- UPDATE: Rename or modify a collection
- DELETE: Remove an entire collection (⚠️ careful!)
"""

import chromadb

print("="*70)
print("STEP 5: MANAGING YOUR COLLECTIONS")
print("="*70)

# ============================================================================
# Initialize a Persistent Client
# ============================================================================
print("\n" + "="*70)
print("🔧 Setting up: Creating a Persistent Client")
print("="*70)

client = chromadb.PersistentClient(path="./chroma_db")
print("✅ Persistent client initialized")

# ============================================================================
# CREATE: Creating New Collections
# ============================================================================
print("\n" + "="*70)
print("1️⃣  CREATE: Creating New Collections")
print("="*70)

# Create multiple collections for different purposes
# Each collection is independent - like separate filing drawers!

print("\n📌 Creating Collection 1: 'travel_policies'")
travel_collection = client.get_or_create_collection(name="travel_policies")
print(f"   ✅ Created: {travel_collection.name}")

print("\n📌 Creating Collection 2: 'company_benefits'")
benefits_collection = client.get_or_create_collection(name="company_benefits")
print(f"   ✅ Created: {benefits_collection.name}")

print("\n📌 Creating Collection 3: 'employee_handbook'")
handbook_collection = client.get_or_create_collection(name="employee_handbook")
print(f"   ✅ Created: {handbook_collection.name}")

print("\n✨ Now we have 3 collections in our database!")

# ============================================================================
# READ: Listing All Collections
# ============================================================================
print("\n" + "="*70)
print("2️⃣  READ: Listing All Collections")
print("="*70)

# Get all collections in the database
all_collections = client.list_collections()

print(f"\n📁 Total collections in database: {len(all_collections)}")
print("\n📋 Collection List:")
for i, collection in enumerate(all_collections, 1):
    print(f"   {i}. Name: {collection.name}")
    print(f"      ID: {collection.id}")
    print(f"      Documents: {collection.count()}")
    print()

# ============================================================================
# Adding sample data to demonstrate updating
# ============================================================================
print("\n" + "="*70)
print("📝 Adding sample data to collections (for demonstration)")
print("="*70)

# Add data to travel_policies collection
travel_collection.add(
    ids=["policy_001"],
    documents=["Employees must use economy class for flights under 6 hours."]
)
print("✅ Added document to travel_policies collection")

# Add data to company_benefits collection
benefits_collection.add(
    ids=["benefit_001"],
    documents=["Health insurance covers 80% of medical expenses."]
)
print("✅ Added document to company_benefits collection")

# ============================================================================
# UPDATE: Modifying a Collection (Rename)
# ============================================================================
print("\n" + "="*70)
print("3️⃣  UPDATE: Modifying a Collection")
print("="*70)

print("\n🔄 Original collection name: 'employee_handbook'")

# Get the collection we want to modify
handbook_collection = client.get_collection(name="employee_handbook")

# Modify (rename) the collection
handbook_collection.modify(name="employee_guidelines")

print("✅ Collection renamed to: 'employee_guidelines'")

# Verify the change by listing collections again
print("\n✔️ Verification - Updated collection list:")
updated_collections = client.list_collections()
for collection in updated_collections:
    print(f"   • {collection.name}")

# ============================================================================
# DELETE: Removing a Collection
# ============================================================================
print("\n" + "="*70)
print("4️⃣  DELETE: Removing a Collection")
print("="*70)

print("\n⚠️  WARNING: Deleting a collection removes ALL its data!")
print("           This action CANNOT be undone!")

print("\n🗑️  Deleting collection: 'travel_policies'")
client.delete_collection(name="travel_policies")
print("✅ Collection deleted successfully")

# Verify deletion
print("\n✔️ Verification - Collections after deletion:")
final_collections = client.list_collections()
print(f"   Total collections remaining: {len(final_collections)}\n")
for collection in final_collections:
    print(f"   • {collection.name} ({collection.count()} documents)")

# ============================================================================
# Advanced: Working with specific collections
# ============================================================================
print("\n" + "="*70)
print("5️⃣  ADVANCED: Getting specific collections by name")
print("="*70)

print("\n📌 Retrieving 'company_benefits' collection:")
benefits = client.get_collection(name="company_benefits")
print(f"   Collection: {benefits.name}")
print(f"   ID: {benefits.id}")
print(f"   Document count: {benefits.count()}")

# Query this specific collection
print("\n🔍 Querying the collection:")
results = benefits.query(
    query_texts=["What insurance coverage is available?"],
    n_results=1
)
print(f"   Query: 'What insurance coverage is available?'")
print(f"   Result: {results['documents'][0][0]}")

# ============================================================================
# Summary
# ============================================================================
print("\n" + "="*70)
print("🎉 STEP 5 COMPLETE: Collection Management Mastered!")
print("="*70)
print("""
✅ What we learned:
   • CREATE: client.get_or_create_collection(name="...")
   • READ: client.list_collections()
   • UPDATE: collection.modify(name="...")
   • DELETE: client.delete_collection(name="...")

🌟 Key Differences:
   • Steps 1-3: CRUD on DOCUMENTS (data inside collections)
   • Step 4: Persistent storage (where data lives)
   • Step 5: CRUD on COLLECTIONS (containers themselves)

💡 Important Reminders:
   • Each collection is independent
   • Collections can have different types of data
   • Deleting a collection deletes ALL documents in it
   • Use meaningful collection names for organization

📌 Current Status:
   - Database: Persistent (./chroma_db)
   - Collections: 2 (company_benefits, employee_guidelines)
   - Status: ✅ Collection management working!

➡️  Next: Step 6 will show Advanced Features with OpenAI Embeddings!
""")
print("="*70)
