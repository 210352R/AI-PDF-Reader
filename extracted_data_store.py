# data_store.py

# Initialize an empty dictionary to store data
data_store = {}


# Function to add data to the data store
def add_data(key, value):
    data_store[key] = value


# Function to get data from the data store
def get_data(key):
    return data_store.get(key)
