import telebot

points = []
bot = telebot.TeleBot('5536281576:AAEOnhtQCf13ym_GeBWKBK4XIrJI7v2bnF8')

@bot.message_handler(commands=['start'])
def start(message):
    """Функция, выполняемая при запуске бота"""
    markup = telebot.types.ReplyKeyboardMarkup()
    test = telebot.types.KeyboardButton('Начать тестирование')
    markup.add(test)
    start_text = 'Добрый день, {username} \n\nЭто бот предназначен для тестирования психологического состояния. Тест анонимный.\n\n'
    start_text += '!ВАЖНО!\nРезультаты и интерпретации, полученные без участия специалистов, не следует воспринимать слишком серьезно. '
    start_text += 'Диагностическую ценность имеют только исследования, проведенные профессиональным психологом.'
    bot.send_message(message.chat.id, start_text.format(username=message.from_user.username), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def message_func(message):
    """Функция, выполняемая при получении текстового сообщения"""
    from questions import number_q
    from statistics import write_log, chart
    from becks_depression_inventory import progress, rating_scale

    def test_keyboard():
        """Функция создания клавиатуры для тестирования"""
        markup = telebot.types.ReplyKeyboardMarkup()
        one = telebot.types.KeyboardButton('1')
        two = telebot.types.KeyboardButton('2')
        three = telebot.types.KeyboardButton('3')
        four = telebot.types.KeyboardButton('4')
        markup.add(one, two, three, four)
        return markup

    global points
    standart_text = 'В течение последних двух недель, включая сегодняшний день\n\n'

    if (message.text == 'Начать тестирование'):
        markup = telebot.types.ReplyKeyboardMarkup()
        description = telebot.types.KeyboardButton('Продолжить')
        markup.add(description)
        description_text = 'Следующий тест представляет собой Шкалу депрессии Бека.\n\n'
        description_text += 'Этот тест оценивает, насколько вы подвержены депрессии.\n'
        description_text += 'Он учитывает распространённые симптомы и жалобы пациентов с этим заболеванием.\n'
        description_text += 'Вам предстоит при ответе на каждый вопрос выбрать из нескольких утверждений наиболее близкое.\n'
        bot.send_message(message.chat.id, description_text, reply_markup=markup)

    elif (message.text == 'Продолжить' or message.text == 'Пройти тест заново'):
        points.clear()
        markup = test_keyboard()
        text_1q = standart_text + number_q(1)
        bot.send_message(message.chat.id, text_1q, reply_markup=markup)

    elif (message.text == '1' or
          message.text == '2' or
          message.text == '3' or
          message.text == '4'):

        points.append(int(message.text) - 1)
        markup = test_keyboard()
        nq = len(points) + 1
        text = standart_text + number_q(nq)
        if nq < 22:
            bot.send_message(message.chat.id, text, reply_markup=markup)
        else:
            markup = telebot.types.ReplyKeyboardMarkup()
            fin_description = telebot.types.KeyboardButton('Завершить тестирование')
            markup.add(fin_description)
            fin_text = 'Вы ответили на все вопросы'
            bot.send_message(message.chat.id, fin_text, reply_markup=markup)

    elif (message.text == 'Завершить тестирование'):
        markup = telebot.types.ReplyKeyboardMarkup()
        run = telebot.types.KeyboardButton('Пройти тест заново')
        info = telebot.types.KeyboardButton('Как бороться с депрессией')
        markup.add(run, info)

        result = 0
        for i in points:
            result += i
        text_d = rating_scale(result)
        progress_str = progress(result)
        result_text = f'Результат теста: \n{progress_str}.\nУ вас наблюдается {text_d}'
        bot.send_message(message.chat.id, result_text, reply_markup=markup)
        write_log(result)

    elif (message.text == 'Как бороться с депрессией'):
        markup = telebot.types.ReplyKeyboardMarkup()
        run = telebot.types.KeyboardButton('Пройти тест заново')
        markup.add(run)
        info_text = 'Как бороться с депрессией: \nhttps://psytests.org/article/chto-eto-takoe-depressiia-i-kak-s-nei-borotsia.html'
        bot.send_message(message.chat.id, info_text, reply_markup=markup)
    elif (message.text == 'stat'):
        chart()
    else:
        bot.send_message(message.chat.id, 'Неизвестная команда')



bot.polling(none_stop=True)