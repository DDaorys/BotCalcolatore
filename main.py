import requests
import random
url = "https://api.telegram.org/bot1406557101:AAEfpvHkwFKUUAVd-t-0mTQry30yC3VvO4s/"

# create function that get chat id
def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id

# create function that get message text
def get_message_text(update):
    message_text = update['message']['text']
    return message_text

# create function that get last update
def last_update(req):
    response = requests.get(req + "getUpdates")
    response = response.json()
    result = response['result']
    total_updates = len(result) - 1
    return result[total_updates]  #get last record message update

# create function that send message to user
def send_message(chat_id, message_text):
    params = {"chat_id": chat_id, "text": message_text}
    response = requests.post(url + "sendMessage", data = params)
    return response

#main function for navigate or replay
def main():
    update_id = last_update(url)["update_id"]
    while True:
        update = last_update(url)
        if update_id == update["update_id"]:
            if get_message_text(update).lower() == "hi" or get_message_text(update).lower() == "hello":
                send_message(get_chat_id(update), "Hello Welcome to our bot. Type 'Play' to roll the dice!")
            elif get_message_text(update).lower() == "play":
                _1 = random.randint(1, 6)
                _2 = random.randint(1, 6)
                _3 = random.randint(1, 6)
                send_message(get_chat_id(update), 'You have ' + str(_1) + ' and ' + str(_2) + ' and ' + str(_3) + '!\n Your is ' + str(_1 + _2 + _3) + '!!!!')
            else:
                send_message(get_chat_id(update), "Sorry Not Understand what you inputted")
            update_id += 1

main()