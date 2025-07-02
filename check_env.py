import os

mongo_url = os.getenv("MONGODB_URL")
if not mongo_url:
    print("❌ MONGODB_URL is empty or not set")
else:
    print("✅ MONGODB_URL:", mongo_url)