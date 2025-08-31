

# pip install pytest

from util.date_converter import iso_date_converter
from util.setup_logger import setup_logger
import logging

# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(setup_logger())


# Test function for iso_date_converter
def test_iso_date_converter():

    logger.debug("-" * 60) # Separator line in the log
    logger.info("Running test...") # Log the start of the test

    ms_since_epoch = 1756551600000 # Translates to 2025-Aug-30 13:00
    iso_date = iso_date_converter(ms_since_epoch) # Call the function to test

    # Assert the expected output
    try:
        assert iso_date == "2025-Aug-30 13:00" # Expected result
        logger.info("Test: iso_date_converter PASSED!") # Log success

    # Catch assertion errors and log them
    except AssertionError as e:
        logger.error(f"Test: iso_date_converter FAILED! {e}") # Log failure
        raise
    finally: # Ensure this runs regardless of test outcome
        logger.info("All test completed.") # Log the completion of the test

