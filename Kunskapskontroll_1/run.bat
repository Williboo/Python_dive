

@echo off
REM Clear the log file
type nul > app.log 

REM Run test first
pytest util/test_main.py
REM Check if tests passed
IF %ERRORLEVEL% NEQ 0 ( 
    echo Tests failed. Exiting.
    REM Exit with the test error code
    exit /b %ERRORLEVEL%
)

REM If test passed, run the main application
python main.py