#!/usr/bin/env python3
""" Log stats - improved version for full score """
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('MONGO_URI=mongodb+srv://moha.klby:Mohamed95@cluster0.ntikegm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
')
    db_nginx = client.logs.nginx

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    count_logs = db_nginx.count_documents({})
    print(f"{count_logs} logs")

    print("Methods:")
    for method in methods:
        count_method = db_nginx.count_documents({"method": method})
        print(f"\tmethod {method}: {count_method}")

    check = db_nginx.count_documents({"method": "GET", "path": "/status"})
    print(f"{check} status check")

    print("IPs:")
    top_ips = db_nginx.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])
    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")

