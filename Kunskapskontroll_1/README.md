## Navigation


main.py : This file fetches the latest temperature data from three SMHI weather stations using their API, converts the date format and saves the results in a local SQLite database. It uses logging for tracking the process, it includes error handling and avoids saving duplicate entries.


temperatures.db : Is a local SQLite database used to store the data retrieved from the API. It contains a table called temperatures with columns for station name, date and time (in ISO format) and temperature value (Celsius).


app.log : Is a log file that records the programs activity, including information, warnings, errors and debugging details about the data retrieval, processing and database operations.


run.bat : Is the batch file that executes the main.py script together with an automated test function. 


Folder: /util: It contains utility modules used by the main program, such as the date conversion function (date_converter.py) and the logger setup (setup_logger.py). These modules help with formatting dates and configuring logging for the program.
The test_main.py is an automated test file that verifies the correctness of key functions in the main program, such as the date conversion.
