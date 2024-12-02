import logging

logging.basicConfig(
    filename="server.log",
    level=logging.INFO, 
    format="%(asctime)s - %(message)s"  
)

def log_request(method, path, query_params):
    """
    Log incoming request details.
    """
    log_message = f"Method: {method}, Path: {path}, Query Params: {query_params}"
    logging.info(log_message)
