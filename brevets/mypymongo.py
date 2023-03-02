import os
from pymongo import MongoClient

def get_mongo_client():
    """
    Returns a MongoClient object with the MongoDB hostname and port number.

    Returns:
    MongoClient: A MongoClient object with the MongoDB hostname and port number.
    """
    # Create a MongoClient object with the MongoDB hostname and port number
    client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
    # Select the brevets database and the tables collection
    return client.brevets.tables

# Get the tables collection object
tables = get_mongo_client()

def brevet_insert(brevet_dist, start_time, control_pts):
    """
    Inserts the brevet distance, start time, and control points into the MongoDB collection.

    Args:
    brevet_dist (int): The distance of the brevet.
    start_time (str): The start time of the brevet in ISO format.
    control_pts (list): A list of dictionaries containing the control point distance and closing time.

    Returns:
    str: The _id of the newly inserted document as a string.
    """
    # Create a dictionary with the fields to insert into the database
    data = {"brevet": brevet_dist, "start": start_time, "control_pts": control_pts}
    # Insert the data into the tables collection and get the _id of the new document
    result = tables.insert_one(data)
    # Return the _id as a string
    return str(result.inserted_id)

def brevet_find():
    """
    Finds the latest document in the MongoDB collection and extracts the brevet distance, start time, and control points.

    Returns:
    tuple: A tuple containing the brevet distance, start time, and control points extracted from the latest document in the MongoDB collection.
    """
    # Find the latest document in the tables collection, sorted by _id in descending order
    latest_table = tables.find_one(sort=[("_id", -1)])
    # Extract the brevet distance, start time, and control points from the latest document
    return latest_table["brevet"], latest_table["start"], latest_table["control_pts"]
