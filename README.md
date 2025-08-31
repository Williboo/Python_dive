# Python_dive
This repository serves as a personal portfolio showcasing my projects and code snippets written in Python. Its a collection of my work, ranging from small scripts and exercises to more extensive projects.


Short description of folder: Kunskapskontroll_1

I wrote a Python script that automatically collects the latest temperature data from three different SMHI weather stations (Malmö, Göteborg, and Stockholm) by using their public API. For each station, I fetched the most recent temperature reading, converted the date format to ISO standard, and logged each step of the process for transparency and troubleshooting. 
I then stored the results in a local SQLite database, making sure not to save duplicate entries by using a unique constraint. The program includes error handling to manage issues during data retrieval and storage. It logs any issues that occur, and ensures the database connection is properly closed when finished. There is also a separate automated testing file to verify the correctness of the date conversion function. It is also possible to use Task Scheduler to automate the process by running the batch file.
