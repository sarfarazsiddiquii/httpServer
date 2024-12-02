from database.messages import get_all_messages, add_message, update_message, delete_message

def filter_messages_by_query(query_params):
    all_messages = get_all_messages()
    if query_params:
        return [
            message for message in all_messages
            if all(
                str(message.get(key)) in values
                for key, values in query_params.items()
            )
        ]
    return all_messages

def handle_get_messages(query_params=None):
    all_messages = get_all_messages()
    filtered_messages = filter_messages_by_query(query_params)
    return {"status": "success", "messages": filtered_messages}



def handle_post_message(data):
    new_message = add_message(data)
    return {
        "status": "success",
        "message": "Message added successfully",
        "data": new_message
    }


def handle_put_message(query_params, data):
    messages_to_update = filter_messages_by_query(query_params)
    if not messages_to_update:
        return {"status": "error", "message": "No matching messages found"}

    updated_messages = []
    for message in messages_to_update:
        updated_message = update_message(message["id"], data)
        updated_messages.append(updated_message)

    return {
        "status": "success",
        "message": f"{len(updated_messages)} message(s) updated successfully",
        "data": updated_messages
    }


def handle_delete_message(query_params):

    messages_to_delete = filter_messages_by_query(query_params)
    if not messages_to_delete:
        return {"status": "error", "message": "No matching messages found"}

    for message in messages_to_delete:
        delete_message(message["id"])

    return {
        "status": "success",
        "message": f"{len(messages_to_delete)} message(s) deleted successfully"
    }

