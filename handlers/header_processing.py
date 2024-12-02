def process_headers(headers):
    original_headers = {key: value for key, value in headers.items()}
    
    new_headers = {key.upper(): value.lower() for key, value in original_headers.items()}
    
    print("original Headers:", original_headers)
    print("Processed Headers:", new_headers)
    
    return new_headers