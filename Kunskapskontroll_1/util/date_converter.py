
import datetime

# Convert milliseconds since epoch from SMHI API to string format

def iso_date_converter(ms_since_epoch, format="%Y-%b-%d %H:%M"):
    """Convert milliseconds since epoch to a formatted date string."""
    dt_object = datetime.datetime.fromtimestamp(ms_since_epoch / 1000)
    return dt_object.strftime(format)