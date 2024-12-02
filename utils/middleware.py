def validation(headers, path, query_params, method):
    if not path.startswith('/messages'):
        return {"status": "error", "message": "Invalid endeddapoint"}

    if method == 'GET' and 'user' not in query_params:
        return {"status": "error", "message": "Missing required query parameter: user"}

    return None