
def load_nairobi_to_mongodb(host):
    """
    Loads the Nairobi air quality data from a parquet file into MongoDB.

    Parameters:
    -----------
    host : str
        The IP address of the MongoDB server (e.g., '192.77.136.3')
    """
    from pymongo import MongoClient
    import pandas as pd

    port = 27017

    try:
        client = MongoClient(f"mongodb://{host}:{port}", serverSelectionTimeoutMS=3000)
        # Force connection check
        client.server_info()
    except Exception as e:
        print(f"❌ Could not connect to MongoDB at {host}:{port}. Please check your host IP.")
        print(f"   Error: {e}")
        return

    db = client["air-quality"]
    db["nairobi"].drop()

    try:
        df = pd.read_parquet('nairobi.parquet')
    except FileNotFoundError:
        print("❌ Could not find 'nairobi.parquet'. Make sure the file is in the same directory.")
        return

    if df['timestamp'].dtype != 'object':
        df['timestamp'] = df['timestamp'].astype(str)

    db['nairobi'].insert_many(df.to_dict('records'))
    print(f"✅ Nairobi data successfully loaded to MongoDB at {host}:{port}!")
    print(f"   Collection: air-quality.nairobi | Documents inserted: {len(df)}")

    client.close()
