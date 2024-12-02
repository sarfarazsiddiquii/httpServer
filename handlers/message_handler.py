from data.messages import get_all_messages, add_message, update_message, delete_message


def handle_get_messages():
    return {
        "status": "success",
        "messages": get_all_messages()
    }


def handle_post_message(data):
    new_message = add_message(data)
    return {
        "status": "success",
        "message": "Message added successfully",
        "data": new_message
    }


def handle_put_message(message_id, data):
    updated_message = update_message(message_id, data)
    if updated_message:
        return {
            "status": "success",
            "message": "Message updated successfully",
            "data": updated_message
        }
    return {
        "status": "error",
        "message": "Message not found"
    }


def handle_delete_message(message_id):
    delete_message(message_id)
    return {
        "status": "success",
        "message": f"Message with ID {message_id} deleted successfully"
    }
