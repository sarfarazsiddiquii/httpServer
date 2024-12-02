def process_headers(headers):
    original_headers = {key: value for key, value in headers.items()}
    
    new_headers = {key.upper(): value.lower() for key, value in original_headers.items()}
    
    print("Header Info:", new_headers)
    
    return new_headers