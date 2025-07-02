import os

mongo_url = os.getenv("MONGODB_URL")
if mongo_url and mongo_url.startswith("mongodb+srv"):
    print("✅ MongoDB URI is valid and starts with 'mongodb'")
else:
    print("❌ MongoDB URI is missing or invalid")