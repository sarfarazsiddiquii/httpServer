messages = [] 
message_id_counter = 1 


def get_all_messages():
    return messages


def add_message(message):
    global message_id_counter
    message['id'] = message_id_counter
    messages.append(message)
    message_id_counter += 1
    return message


def update_message(message_id, updated_message):
    for message in messages:
        if message['id'] == message_id:
            message.update(updated_message)
            return message
    return None


def delete_message(message_id):
    global messages
    messages = [msg for msg in messages if msg['id'] != message_id]
    return messages
