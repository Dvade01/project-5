from pymongo import MongoClient
from acp_times import brevet_insert, brevet_find
import os

client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
tables = client.brevets.tables

def test_brevet_insert():
    """
    Tests inserting a new brevet document into the collection.
    """
    # Define the input values for the brevet
    brevet_dist = 200
    start_time = "2022-03-01T00:00:00+00:00"
    control_pts = [{"distance": 50, "close_time": "2022-03-01T02:00:00+00:00"},
                   {"distance": 100, "close_time": "2022-03-01T05:00:00+00:00"},
                   {"distance": 150, "close_time": "2022-03-01T09:00:00+00:00"},
                   {"distance": 200, "close_time": "2022-03-01T14:00:00+00:00"}]
    # Call the function to insert the brevet into the MongoDB collection
    result = brevet_insert(brevet_dist, start_time, control_pts)
    # Check that the function returns the _id of the inserted document as a string
    assert isinstance(result, str)
    # Check that the number of documents in the collection is now 1
    assert tables.count_documents({}) == 1


def test_brevet_find():
    """
    Tests finding the latest brevet document in the collection.
    """
    # Define the input values for the brevet
    brevet_dist = 200
    start_time = "2022-03-01T00:00:00+00:00"
    control_pts = [{"distance": 50, "close_time": "2022-03-01T02:00:00+00:00"},
                   {"distance": 100, "close_time": "2022-03-01T05:00:00+00:00"},
                   {"distance": 150, "close_time": "2022-03-01T09:00:00+00:00"},
                   {"distance": 200, "close_time": "2022-03-01T14:00:00+00:00"}]
    # Insert the brevet into the MongoDB collection
    brevet_insert(brevet_dist, start_time, control_pts)
    # Call the function to find the latest brevet document in the MongoDB collection
    result = brevet_find()
    # Check that the function returns a tuple
    assert isinstance(result, tuple)
    # Check that the tuple contains the correct number of values
    assert len(result) == 3
    # Check that the values in the tuple match the input values for the brevet
    assert result[0] == brevet_dist
    assert result[1] == start_time
    assert result[2] == control_pts
