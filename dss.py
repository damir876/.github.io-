import telebot
from telebot import types
bot = telebot.TeleBot('7815451322:AAHTk_va1S6ZzV7bqjBhycEKOOAtogGh0tY')
@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помошник!", reply_markup=markup)

@bot.message_handler(content_types=['text'])

        
def get_text_messages(message):

    if message.text == '👋 Поздороваться' or message.text == 'Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Что такое С++?')
        btn2 = types.KeyboardButton('История C++?')
        btn3 = types.KeyboardButton('Обучение С++')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '❓ Задайте интересующий вас вопрос', reply_markup=markup) #ответ бота


    elif message.text == 'Что такое С++?':
        bot.send_message(message.from_user.id, 'Это компилируемый статически типизированный язык программирования общего назначения. Был разработан Бьярне Страуструпом в начале 1980-х годов как расширение языка C (и даже изначально назывался «Си с классами»)' )

    elif message.text == 'История C++?':
        bot.send_message(message.from_user.id, 'История языка C++ начинается в начале 1980-х годов, когда датский программист Бьёрн Страуструп разработал его как расширение к языку Си. Фактически вначале C++ просто дополнял язык Си некоторыми возможностями объектно-ориентированного программирования.')

    elif message.text == 'Обучение С++':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn4 = types.KeyboardButton('Базовые типы ввода, вывода')
        btn5 = types.KeyboardButton('Циклы')
        btn6 = types.KeyboardButton('Операторы')
        btn7 = types.KeyboardButton('Назад')
        markup.add(btn4, btn5, btn6,btn7)
        bot.send_message(message.from_user.id, "Выбери интересующию тему", reply_markup=markup)
    elif message.text == 'Базовые типы ввода, вывода':
        bot.send_message(message.from_user.id, 'В C++ операции ввода и вывода реализованы с помощью потоков. Поток — это объект, в который программа может вставлять или извлекать символы.\n' + 'Стандартные потоки:\n cin — объект класса istream, соответствующий стандартному вводу. В общем случае он позволяет читать данные с терминала пользователя\n cout — объект класса ostream, соответствующий стандартному выводу. В общем случае он позволяет выводить данные на терминал пользователя\nПример:\nstd::cout<< i << std::endl;')
    elif message.text == 'Циклы':
        bot.send_message(message.from_user.id, 'Циклы в C++ позволяют выполнять одно действие несколько раз подряд. С их помощью можно автоматизировать задачи, парой строк кода выполнять несколько действий и генерировать данные\nПример:\nfor(int i; i<10;i++){std::cout<< i << std::endl;}')
    elif message.text == 'Операторы':
        bot.send_message(message.from_user.id, 'Это союзы, которые позволяют объединять по несколько условий. В Python есть всего три оператора: and (и), or (или) и not (не). И (and). Если условия с двух сторон оператора and истинны, тогда все выражение целиком считается истинным. Пример: if (a > 7 and b<8) std::cout << (a) False Или (or) << std::endl; Выражение ложно, если оба операнда с двух сторон ложные. Если хотя бы одно из них истинное, то и все выражение истинно.')


bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть
