import telebot

# токен бота
bot_token = 'токен вашего бота'
bot = telebot.TeleBot(bot_token)

# функция отправки сообщений
def send_message(chat_id, message_text, num_times):
    for _ in range(num_times):
        bot.send_message(chat_id, message_text)

# айди чатов которым нужно отправить сообщение
chat_ids = ['айди']  # заменить на реальные chat_id людей которым кидаете бомбер (можно несколько)

# отправка сообщения каждому чату (chat_id) из списка n-количество раз
message = "текст сообщения" #сообщение для спама
num_times = кол во сообщений # замените кол во сообщений на, число сообщений которое нужно отправить, например: 200

for chat_id in chat_ids:
    send_message(chat_id, message, num_times)

# Запуск бомбнра
bot.polling()
