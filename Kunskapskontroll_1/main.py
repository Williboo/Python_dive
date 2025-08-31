
# pip install requests in terminal

import requests
import json
import datetime
import sqlite3
import logging

# Import custom modules
from util.date_converter import iso_date_converter
from util.setup_logger import setup_logger

# Set up logging
logger = logging.getLogger(__name__)# Create a logger for this module
logger.setLevel(logging.DEBUG) # Set the logging level
logger.addHandler(setup_logger())  # Add the file handler to the logger


database = sqlite3.connect("temperatures.db") # Connect to (or create) the SQLite database
cursor = database.cursor() # Create a cursor object to interact with the database



# SMHI API endpoint for temperature data
stations_api = [ # List of stations with their respective API URLs
    {
        'name': 'station 1,', # Malmö
        'url': 'https://opendata-download-metobs.smhi.se/api/version/latest/parameter/39/station/53300/period/latest-hour/data.json'
    },
    {
        'name': 'station 2', # Göteborg
        'url': 'https://opendata-download-metobs.smhi.se/api/version/latest/parameter/39/station/72420/period/latest-hour/data.json'
    }, 
    {
        'name': 'station 3', # Stockholm
        'url': 'https://opendata-download-metobs.smhi.se/api/version/latest/parameter/39/station/97400/period/latest-hour/data.json'
    }
]


# Log the start of the data retrieval process
logger.debug("-" * 60) # Create a separator line in the log
logger.info("Starting data retrieval from SMHI API.")


def get_temperature_data(api_url): # Function to fetch temperature data from SMHI API

    # try to fetch data from the SMHI API
    try:
        logger.info('Connecting to SMHI API...') # Log the attempt to connect
        response = requests.get(api_url) # Make a GET request to the API
        # Check if the request was successful
        response.raise_for_status() # Raises an error for bad responses

        return response.json() 

    # Handle potential exceptions
    except Exception as e:

        # Write to log file
        logger.error(f"Failed to fetch data from API for {station['name']} ({station['url']}): {e}")
        return None # Return None if there was an error but continue execution


# Create the temperatures table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS temperatures (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        station_name TEXT,
        date_time TEXT,
        temperature REAL,
        UNIQUE(station_name, date_time)
    )""") # Create table with unique constraint on station_name and date_time
database.commit() # Commit the table creation


for station in stations_api: # Loop through each station in the list

    temperature_info = get_temperature_data(station['url']) # Fetch temperature data from the API

    # Extract relevant information with error handling
    try:
        if temperature_info: # Check if data is valid
            station_name = temperature_info['station']['name'] # Extract station name
            date_time_entry = temperature_info['value'][0]['date'] # Extract date-time of the measurement
            temperature_value = temperature_info['value'][0]['value'] # Extract temperature value
        
            iso_date = iso_date_converter(date_time_entry) # Convert date-time to ISO format using the custom function

        else: # If data is None, set all values to "No data"
            station_name = "No data"
            iso_date = "No data"
            temperature_value = "No data"

    except (KeyError, IndexError, TypeError) as e: # Handle missing or malformed data
        logger.warning(f"Missing data from API: {e}")
        station_name = "No data"
        iso_date = "No data"
        temperature_value = "No data"


    # Save the extracted data to the database if valid
    if station_name != "No data" and iso_date != "No data" and temperature_value != "No data": # Only save if all data is valid
        try:
            cursor.execute( 
                "INSERT OR REPLACE INTO temperatures (station_name, date_time, temperature) VALUES (?, ?, ?)", # Use INSERT OR REPLACE to avoid duplicates
                (station_name, iso_date, float(temperature_value)) # Convert temperature to float before saving
            )
            database.commit()
            logger.info(f"Successful, data saved for: {station_name}") # Log success

        except Exception as e:
            logger.error(f"Failed to save data in database: {e}") # Log any database errors

    else:
        logger.info(f"Data not saved for {station['name']} due to missing information.") # Log if data was not saved due to missing info

database.close() # Close the database connection
logger.info("Database connection closed.")
