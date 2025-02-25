# app/token_store.py
import logging

access_token_store = None  # Global variable to store the token

def set_access_token(token: str):
    """
    Store the access token in memory.
    """
    global access_token_store
    access_token_store = token
    logging.info("Access token successfully updated.")
    
def get_access_token():
    global access_token_store
    if access_token_store is None:
        logging.error("Access token is not set.")
        return None
    logging.info(f"Retrieved access token: {access_token_store[:10]}...")  # Log partial token
    return access_token_store
