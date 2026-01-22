import logging

#configure logging

logging.basicConfig(
    filename = 'Logger_REMARKS.log',
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
    
)

# create logger object you can reuse

logger = logging.getLogger("daily_sales_logger")