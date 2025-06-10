from fastapi import FastAPI
from pymongo import MongoClient
import os

client = MongoClient(os.getenv("MONGO_URI"))
db = client["movies"]
collection = db["movies"]

app = FastAPI()

@app.get("/report/highest-rated-movies")
def get_highest_rated_movies():
    movies = list(
        collection.find(
            { "vote_average": { "$ne": None } }
        ).sort("vote_average", -1).limit(10)
    )
    for m in movies:
        m["_id"] = str(m["_id"])
    return movies



@app.get("/report/popular-movies-summary")
def popularity_summary():
    pipeline = [
        {"$group": {
            "_id": {"$year": {"$toDate": "$release_date"}},
            "count": {"$sum": 1},
            "avg_popularity": {"$avg": "$popularity"}
        }},
        {"$sort": {"_id": 1}}
    ]
    return list(collection.aggregate(pipeline))

@app.get("/debug/movies")
def debug_movies():
    movies = list(collection.find().limit(5))
    for movie in movies:
        movie["_id"] = str(movie["_id"])
    return movies

