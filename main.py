import telebot 
from config import token
from logic import Pokemon

bot = telebot.TeleBot(token)

# Словарь для отслеживания использования команды /feed
used_feed = {}

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons:
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

@bot.message_handler(commands=['feed'])
def feed_pokemon(message):
    username = message.from_user.username
    # Проверяем есть ли у пользователя покемон
    if username not in Pokemon.pokemons:
        bot.reply_to(message, "У тебя еще нет покемона. Используй /go чтобы создать.")
        return
    
    # Проверяем, использовал ли пользователь команду /feed ранее
    if used_feed.get(username, False):
        bot.reply_to(message, "Ты уже использовал команду /feed. Больше нельзя.")
        return
    
    # Если не использовал — даем возможность накормить и отмечаем использование
    pokemon = Pokemon.pokemons[username]
    result = pokemon.feed()
    bot.send_message(message.chat.id, result)
    
    # Отмечаем, что команда использована
    used_feed[username] = True

bot.infinity_polling(none_stop=True)

