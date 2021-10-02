from datetime import datetime, date, time

from bot_token import TOKEN
from random import choice
import telebot

bot = telebot.TeleBot(TOKEN)

################################################################################

with open('word_rus.txt', encoding='utf') as file:
    words = file.read()
words = words.split('\n')
word = choice(words)
print(word)
game = False
ard = list(word)
ar2 = ['⬜'] * len(word)
if len(word) < 10:
    d = len(word) * 3
else:
    d = 30
uss = []
work = False


################################################################################

@bot.message_handler(commands=['start'])
def start_game(message):
    global work, uss
    uss = []
    print("start")
    bot.send_message(message.chat.id, 'Привет, сыграем в висельницу? Я загадал слово, вводи ПО ОДНОЙ РУССКОЙ БУКВЕ')
    z = " ".join(ar2)
    bot.send_message(message.chat.id, z)
    work = True


@bot.message_handler(commands=['s'])
def stop_game(message):
    global work
    print("stop")
    bot.send_message(message.chat.id, 'Остановка...')
    work = False


@bot.message_handler(commands=['giveup'])
def surrender(message):
    global word, game, ard, ar2, d, work, uss
    print('give up')
    bot.send_message(message.chat.id, word, '')
    uss = []
    word = choice(words)
    print(word)
    game = False
    ard = list(word)
    ar2 = ['⬜'] * len(word)
    if len(word) < 10:
        d = len(word) * 3
    else:
        d = 30
    bot.send_message(message.chat.id, 'Ещё раз? Я уже загадал новое слово, вводи ПО ОДНОЙ РУССКОЙ БУКВЕ')
    z = " ".join(ar2)
    bot.send_message(message.chat.id, z)
    work = True


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    global word, game, ard, ar2, d, work, uss
    if work == True:
        print(f"{datetime.now()}   {message.from_user.username}:   {message.text}")
        global d
        d -= 1
        if d > 0:
            x = message.text.lower()
            if x not in uss:
                uss.append(x)
                if x in ard:
                    for k in range(len(word)):
                        if ard[k] == x:
                            ar2[k] = x
                    z = " ".join(ar2)
                    bot.send_message(message.chat.id, z)
                    if ar2 == ard:
                        bot.send_message(message.chat.id, f'Ответ: {word}    !!! WIN !!!')
                        print('win')
                        uss = []
                        word = choice(words)
                        print(word)
                        ard = list(word)
                        ar2 = ['⬜'] * len(word)
                        if len(word) < 10:
                            d = len(word) * 3
                        else:
                            d = 30
                        bot.send_message(message.chat.id,
                                         'Ещё раз? Я уже загадал новое слово, вводи ПО ОДНОЙ РУССКОЙ БУКВЕ')
                        z = " ".join(ar2)
                        bot.send_message(message.chat.id, z)
                        work = True
                else:
                    bot.send_message(message.chat.id, f'Такой буквы нет, попыток осталось: {d} :(')
        if d == 0:
            bot.send_message(message.chat.id, f'Ответ: {word}')
            bot.send_message(message.chat.id, 'NOOB')
            print('lose')
            uss = []
            word = choice(words)
            print(word)
            ard = list(word)
            ar2 = ['⬜'] * len(word)
            if len(word) < 10:
                d = len(word) * 3
            else:
                d = 30
            bot.send_message(message.chat.id, 'Ещё раз? Я уже загадал новое слово, вводи ПО ОДНОЙ РУССКОЙ БУКВЕ')
            z = " ".join(ar2)
            bot.send_message(message.chat.id, z)
            work = True


if __name__ == '__main__':
    bot.infinity_polling()
