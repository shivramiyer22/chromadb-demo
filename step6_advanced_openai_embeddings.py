"""
Step 6: Advanced - Using OpenAI's Embedding Model

What are Embeddings?
---------------------
Embeddings are numerical representations of text meaning.
Think of them as coordinates in a "meaning space":
- Similar concepts cluster together
- Different concepts are far apart
- ChromaDB's default model is good, but OpenAI's is BETTER!

Why Use OpenAI's Model?
-----------------------
- Better semantic understanding
- More accurate search results
- Works with specialized domains
- Small model = cheaper and faster
- Uses: text-embedding-3-small

What are Tokens?
----------------
Tokens are pieces of words that AI models see.
Examples:
- "ChatGPT" = 1 token
- "I love ChromaDB" = 5 tokens
- "The quick brown fox" = 4 tokens

Why Count Tokens?
- OpenAI charges per 1M tokens
- Helps manage costs
- Ensures you stay within limits
- Important for production applications

IMPORTANT: You'll need an OpenAI API key!
------------------------------------------
1. Go to: https://platform.openai.com/account/api-keys
2. Create a new API key
3. Set it as an environment variable: OPENAI_API_KEY
4. Or paste it directly (not recommended for production)

For this demo, we'll show you how to set it up!
"""

import os
import chromadb
from chromadb.utils import embedding_functions

print("="*70)
print("STEP 6: ADVANCED - USING OPENAI'S EMBEDDING MODEL")
print("="*70)

# ============================================================================
# ⚠️  IMPORTANT: OpenAI API Key Setup
# ============================================================================
print("\n" + "="*70)
print("🔑 STEP 1: Setting up OpenAI API Key")
print("="*70)

print("""
To use OpenAI's embedding model, you need an API key.

Options to set your API key:
1. Environment Variable (Recommended):
   export OPENAI_API_KEY='your-key-here'

2. Direct in Code (Not recommended - less secure):
   os.environ['OPENAI_API_KEY'] = 'your-key-here'

3. Use .env file with python-dotenv library

For now, we'll show the structure. In production, use option 1 or 3!
""")

# Check if API key is already set
api_key = os.getenv('OPENAI_API_KEY')
if api_key:
    print("✅ OpenAI API key found in environment variables!")
else:
    print("⚠️  OpenAI API key not found.")
    print("    To complete this step fully, set OPENAI_API_KEY environment variable")
    print("\n📝 For demonstration, we'll show the code structure.")
    print("   In real usage, comment out the demo and use your actual API key!")

# ============================================================================
# Understanding Tokens with tiktoken
# ============================================================================
print("\n" + "="*70)
print("📊 STEP 2: Understanding Tokens with tiktoken")
print("="*70)

print("\n💡 Token counting helps estimate API costs")
print("   OpenAI's text-embedding-3-small uses 'cl100k_base' encoding\n")

try:
    import tiktoken
    
    # Get the encoding for OpenAI's embedding model
    encoding = tiktoken.get_encoding("cl100k_base")
    
    # Examples of token counting
    examples = [
        "Hello",
        "ChromaDB is awesome!",
        "All expense reports must be submitted within 15 days of trip completion.",
        "For domestic flights, employees must book economy class tickets."
    ]
    
    print("📈 Token Counts for Sample Sentences:")
    print("=" * 70)
    total_tokens = 0
    for text in examples:
        tokens = encoding.encode(text)
        token_count = len(tokens)
        total_tokens += token_count
        print(f"Text: '{text}'")
        print(f"Tokens: {token_count}\n")
    
    print(f"📊 Total tokens across all examples: {total_tokens}")
    print(f"💰 Estimate: {total_tokens} tokens ≈ ${total_tokens / 1_000_000 * 0.02:.6f}")
    print("   (at $0.02 per 1M tokens for text-embedding-3-small)")
    
except ImportError:
    print("⚠️  tiktoken not installed. Run: pip install tiktoken")

# ============================================================================
# Creating Collections with OpenAI Embeddings
# ============================================================================
print("\n" + "="*70)
print("🧠 STEP 3: Creating Collections with OpenAI Embeddings")
print("="*70)

print("\n📌 How to create a collection with OpenAI embeddings:\n")

code_example = """
# Step 1: Create an embedding function using OpenAI
from chromadb.utils import embedding_functions

openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    model_name="text-embedding-3-small"
)

# Step 2: Create a collection and pass the embedding function
client = chromadb.PersistentClient(path="./chroma_db")
openai_collection = client.get_or_create_collection(
    name="travel_policies_openai",
    embedding_function=openai_ef
)

# Step 3: Use it like normal! The embedding happens automatically
openai_collection.add(
    ids=["policy_001"],
    documents=["Policy text here..."]
)
"""
print(code_example)

# ============================================================================
# Comparison: Default vs OpenAI Embeddings
# ============================================================================
print("\n" + "="*70)
print("⚖️  STEP 4: Comparing Default vs OpenAI Embeddings")
print("="*70)

print("""
DEFAULT EMBEDDING MODEL (all_MiniLM-L6-v2):
- Fast ⚡
- Good for general text
- Less accurate for specialized domains
- No API calls (free!)
- Built-in to ChromaDB

OPENAI EMBEDDING MODEL (text-embedding-3-small):
- Requires API key 🔑
- Better semantic understanding 🧠
- More accurate search results ✅
- Costs money (but very cheap - $0.02 per 1M tokens)
- Great for production systems
- Handles specialized vocabulary better

WHEN TO USE EACH:
- Default: Learning, prototypes, local experiments
- OpenAI: Production apps, better accuracy needed, specialized domains
""")

# ============================================================================
# Summary
# ============================================================================
print("\n" + "="*70)
print("🎉 STEP 6 COMPLETE: Advanced Embeddings Explained!")
print("="*70)
print("""
✅ What we learned:
   • Embeddings = Numerical text representation
   • Tokens = Building blocks AI models see
   • Token counting = Cost management
   • OpenAI model = Better accuracy
   • Custom embedding functions = Flexibility

🌟 Key Concepts:
   • ChromaDB handles embeddings automatically
   • You can swap embedding functions easily
   • OpenAI provides state-of-the-art embeddings
   • Token counting is crucial for budgeting

💡 Important Takeaways:
   • Default embeddings: Great for learning
   • OpenAI embeddings: Better for production
   • Always count tokens to manage costs
   • Choose the right model for your use case

🚀 Next Steps (Beyond Step 6):
   • Set up your OpenAI API key
   • Create a production collection with OpenAI embeddings
   • Monitor token usage
   • Fine-tune your queries for better results
   • Build amazing AI applications! 🎯

📌 What You've Accomplished:
   ✅ Step 1: Installation & Environment Setup
   ✅ Step 2: Created Collections
   ✅ Step 3: CRUD on Documents
   ✅ Step 4: Persistent Storage
   ✅ Step 5: Manage Collections
   ✅ Step 6: Advanced Features
   
   🎓 You're now a ChromaDB Expert! 🏆
""")
print("="*70)

print("\n" + "="*70)
print("📚 ADDITIONAL RESOURCES")
print("="*70)
print("""
ChromaDB Documentation:
  https://docs.trychroma.com/

OpenAI Embeddings:
  https://platform.openai.com/docs/guides/embeddings

Tiktoken (Token Counter):
  https://github.com/openai/tiktoken

Pricing:
  https://openai.com/pricing

Feel free to explore and build amazing things! 🚀
""")
print("="*70)
