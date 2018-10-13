import constants
from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import user_com
from datetime import time
import random
flag = False
time_you = False
money = False
money_1 = False
const = False
const_1 = False
start_one = False
flag_e = False
time_you_e = False
const_e = False
const_1_e = False
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
updater = Updater(token=constants.token)
dispatcher = updater.dispatcher
job_queue = updater.job_queue



def start (bot, update):
    if update.message.chat.id == constants.admin or update.message.chat.id == constants.admin2:
        bottons = [['Закинуть деньги', 'Прибавить деньги игроку']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.chat.id, 'Здравствуйте, админ', reply_markup=user_markup)
    else:
        global flag, time_you, money, money_1, const, const_1, start_one, const_e, const_1_e
        flag = time_you = money = money_1 = const = const_1 = const_e = const_1_e = False
        start_one = True
        bottons = [['Русский🇷🇺', 'English🇺🇸']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.chat.id, 'Здравствуйте, выберите язык:', reply_markup=user_markup)

def answer_start(bot, update):
    global flag, time_you, money, money_1, const, const_1, start_one, const_e, const_1_e, flag_e, time_you_e
    if update.message.text == '💰Пополнить баланс':
        bottons = [['Bitcoin- btc', 'Etherium - eth'],['Yаndex Money'], ['Назад']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.chat.id, ' Выберите метод пополнения⬇️')
        bot.send_message(update.message.chat.id, 'Любой из методов пополнения будет автоматичекси конвертирован в BTC.',
                         reply_markup=user_markup)
        bot.send_message(constants.admin,
                         str(update.message.chat.id) + ' это id человека, который нажал "Пополнить баланс"')
        bot.send_message(constants.admin2,
                         str(update.message.chat.id) + ' это id человека, который нажал "Пополнить баланс"')
    elif update.message.text == 'Yаndex Money':
        bottons = [['Оплатил', 'Отмена']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id,
                         constants.ya_text + '\n' + str(random.choice(constants.yandex_pay)), reply_markup=user_markup)
    elif update.message.text == 'Yandex Mоney':
        bottons = [['Paid for', 'Cancel']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id,
                         constants.ya_text_e + '\n' + str(random.choice(constants.yandex_pay)),
                         reply_markup=user_markup)
    elif flag_e == True:
        bot.send_message(constants.admin, 'Вопрос: ' + update.message.text)
        bot.send_message(constants.admin, 'Вопрос: ' + update.message.text)
        flag_e = False
        bot.send_message(update.message.chat.id, 'Thank you')
        update.message.text = 'Cancel'
        answer_start(bot, update)
    elif update.message.text== 'Ask a Question':
        flag_e = True
        bot.send_message(update.message.chat.id, 'Write your question, our moderator will answer it soon!')
    elif update.message.text == 'Referrals':
        info = user_com.info(update.message.chat.id)
        bot.send_message(update.message.chat.id, 'For each given referral that replenishes the balance, you will receive 0.0005 BTC \n This is your referral link: http://t.me/Btc_winbot?start= '+ str (info [3]) +'. \n Your referrals:' + str(info[5]))
    elif update.message.text == '💰Add balance':
        bottons = [['Вitcoin- btс', 'Еthеrium - еth'],['Yandex Mоney'], ['Back']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.chat.id, ' Select replenishment method⬇️')
        bot.send_message(update.message.chat.id, 'Any of the replenishment methods will be automatically converted to BTC.',
                         reply_markup=user_markup)
        bot.send_message(constants.admin,
                         str(update.message.chat.id) + ' это id человека, который нажал "Пополнить баланс"')
        bot.send_message(constants.admin2,
                         str(update.message.chat.id) + ' это id человека, который нажал "Пополнить баланс"')
    elif update.message.text == 'English🇺🇸':
        if start_one == True:
            start_one = False
            link_name = str(update.message.text)[7:]
            hello = user_com.registration(update.message.chat.id, update.message.chat.first_name,
                                          str(update.message.chat.id),
                                          link_name)
            bottons = [['💰Add balance', '🤝Bets'],
                       ['💸Withdraw funds', '💼My balance'],
                       ['🔥Additionally']]
            user_markup = ReplyKeyboardMarkup(bottons)
            bot.send_message(chat_id=update.message.chat_id, text = 'Hi, let\'s get it started', reply_markup=user_markup)
    elif update.message.text == 'FАQ':
        bot.send_message(update.message.chat.id, constants.FAQ_2)
    elif update.message.text == 'Bitcоin- btс' or update.message.text == 'Еtherium - еth' or update.message.text == 'Yаndex Mоney':
        const_e = True
        bot.send_message(update.message.chat.id, 'Enter your wallet number: ')
    elif const_e == True:
        bot.send_message(update.message.chat.id, 'Enter the amount you want to withdraw. (The minimum amount is 0.002 btc or 0.05 eth)')
        const_e = False
        const_1_e =True
    elif const_1_e == True:
        const_1_e = False
        try:
            float(update.message.text)
            bot.send_message(update.message.chat.id, 'There is not enough money on the account. Enter the amount again.')
        except:
            bot.send_message(update.message.chat.id, 'Something went wrong, try again')
        update.message.text = 'Back'
        answer_start(bot, update)
    elif update.message.text == 'Cancel': #Изменить приветствие
        flag = False
        time_you = False
        money = False
        money_1 = False
        bottons = [['💰Add balance', '🤝Bets'],
                   ['💸Withdraw funds', '💼My balance'],
                   ['🔥Additionally']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(chat_id=update.message.chat_id, text = random.choice(constants.hey_text_e), reply_markup=user_markup)
    elif update.message.text == 'Higher📈':
        try:
            money = float(user_com.parse(constants.valume))
            user_com.more_less(update.message.from_user.id, 'more', money, constants.valume)
        except:
            pass
        bottons = [['1 hour', '2 hours', '4 hours'], ['6 hours', '12 hours', '24 hours'], ['Back']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id, 'Select the time you need:', reply_markup=user_markup)
    elif update.message.text == 'Lower📉':
        try:
            money = float(user_com.parse(constants.valume))
            user_com.more_less(update.message.from_user.id, 'less', money, constants.valume)
        except:
            pass
        bottons = [['1 hour', '2 hours', '4 hours'], ['6 hours', '12 hours', '24 hours'], ['Back']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id, 'Select the time you need:', reply_markup=user_markup)
    elif update.message.text == '1 hour':
        time_you_e = True
        user_com.set_alarm(1, update.message.from_user.id)
        bottons = [['Cancel']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id, 'How much do you bet?', reply_markup=user_markup)
    elif update.message.text == '2 hours':
        time_you_e = True
        user_com.set_alarm(2, update.message.from_user.id)
        bottons = [['Cancel']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id, 'How much do you bet?', reply_markup=user_markup)
    elif update.message.text == '4 hours':
        time_you_e = True
        user_com.set_alarm(4, update.message.from_user.id)
        bottons = [['Cancel']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id, 'How much do you bet?', reply_markup=user_markup)
    elif update.message.text == '6 hours':
        time_you_e = True
        user_com.set_alarm(6, update.message.from_user.id)
        bottons = [['Cancel']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id, 'How much do you bet?', reply_markup=user_markup)
    elif update.message.text == '12 hours':
        time_you_e = True
        user_com.set_alarm(12, update.message.from_user.id)
        bottons = [['Cancel']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id, 'How much do you bet?', reply_markup=user_markup)
    elif update.message.text == '24 hours':
        time_you_e = True
        user_com.set_alarm(23, update.message.from_user.id)
        bottons = [['Cancel']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id, 'How much do you bet?', reply_markup=user_markup)
    elif time_you_e == True:
        try:
            q = float(update.message.text)
            if  q <= user_com.info(update.message.chat.id)[2]:
                user_com.add_plus(update.message.chat.id, -q)
                user_com.pay(update.message.chat.id, q)
                bot.send_message(update.message.chat.id, 'Bet accepted')
                bot.send_message(constants.admin, str(q)+ ' '+ str(update.message.chat.id) )

            else:
                bot.send_message(update.message.chat.id, 'Not enough money')
            time_you_e = False
            update.message.text = 'Cancel'
            answer_start(bot, update)

        except:
            time_you_e = False
            bot.send_message(update.message.chat.id, 'Something went wrong')
            update.message.text = 'Cancel'
            answer_start(bot, update)
    elif update.message.text == 'Вitcoin- btс':
        bottons = [['Paid for', 'Cancel']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id,
                         constants.btc_text_e + '\n' + str(random.choice(constants.btc_list)), reply_markup=user_markup)
    elif update.message.text == 'Paid for':
        bot.send_message(update.message.chat.id, 'Payment is accepted, your transaction is being processed, the funds will be credited to your account automatically after the 1st confirmation of the network.')
        update.message.text = 'Cancel'
        answer_start(bot, update)
    elif update.message.text == 'Back':
        update.message.text = 'Cancel'
        answer_start(bot, update)
    elif update.message.text == 'Еthеrium - еth':
        bottons = [['Paid for', 'Cancel']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id,
                         constants.eth_text_e + '\n' + str(random.choice(constants.eth_list)), reply_markup= user_markup)
    elif  update.message.text == 'BTС/USD':
        money = user_com.parse('BTC')
        constants.valume = 'BTC'
        bottons = [['Higher📈', 'Lower📉'], ['Back']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id, 'You can bet that the rate will be higher or lower. At the moment the course BTC: ' + str(
                                    money) + '$',  reply_markup=user_markup)
    elif  update.message.text == 'BCС/USD':
        money = user_com.parse('BCC')
        constants.valume = 'BCC'
        bottons = [['Higher📈', 'Lower📉'], ['Back']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id, 'You can bet that the rate will be higher or lower. At the moment the course BCC: ' + str(
                                    money) + '$',  reply_markup=user_markup)
    elif update.message.text == 'ETН/USD':
        money = user_com.parse('ETH')
        constants.valume = 'ETH'
        bottons = [['Higher📈', 'Lower📉'], ['Back']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id,
                         'You can bet that the rate will be higher or lower. At the moment the course ETH: ' + str(
                                    money) + '$',  reply_markup=user_markup)
    elif update.message.text == 'XRР/USD':
        money = user_com.parse('XRP')
        constants.valume = 'XRP'
        bottons = [['Higher📈', 'Lower📉'], ['Back']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id,
                         'You can bet that the rate will be higher or lower. At the moment the course XRP: ' + str(
                                    money) + '$',  reply_markup=user_markup)
    elif update.message.text == 'EОS/USD':
        money = user_com.parse('EOS')
        constants.valume = 'EOS'
        bottons = [['Higher📈', 'Lower📉'], ['Back']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id,
                         'You can bet that the rate will be higher or lower. At the moment the course EOS: ' + str(
                                    money) + '$',  reply_markup=user_markup)
    elif update.message.text == 'LTС/USD':
        money = user_com.parse('LTC')
        constants.valume = 'LTC'
        bottons = [['Higher📈', 'Lower📉'], ['Back']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id,
                         'You can bet that the rate will be higher or lower. At the moment the course LTC: ' + str(
                                    money) + '$',  reply_markup=user_markup)
    elif update.message.text == '💸Withdraw funds':
        bottons = [['Bitcоin- btс', 'Еtherium - еth'], ['Yаndex Mоney'], ['Back']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id, 'Select the currency in which you want to withdraw funds.', reply_markup=user_markup)
    elif update.message.text == '🤝Bets':
        bottons = [['BTС/USD', 'ETН/USD'], ['XRР/USD', 'BCС/USD'], ['EОS/USD', 'LTС/USD'], ['Back']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.chat.id, 'Choose the pair you need: ', reply_markup= user_markup)
    elif update.message.text == '🔥Additionally':
        bottons = [['Ask a Question', 'Referrals'], ['FАQ'], ['Back']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id, '🔥Additionally help @btc_supp', reply_markup=user_markup)
    elif update.message.text == '💼My balance':
        bottons = [['💰Add balance', '💸Withdraw funds'], ['Back']]
        user_markup = ReplyKeyboardMarkup(bottons)
        id_ = update.message.chat.id
        s = str(user_com.info(id_)[2])
        bot.send_message(update.message.chat.id, 'Your balance: ' + s + ' ВТС', reply_markup= user_markup)
    elif update.message.text == 'Русский🇷🇺':
        if update.message.chat.id == constants.admin or update.message.chat.id == constants.admin2:
            bottons = [['Закинуть деньги', 'Прибавить деньги игроку']]
            user_markup = ReplyKeyboardMarkup(bottons)
            bot.send_message(update.message.from_user.id,
                             'Доброго времени суток, админ', reply_markup=user_markup)
        elif start_one == True:
            start_one = False
            link_name = str(update.message.text)[7:]
            hello = user_com.registration(update.message.chat.id, update.message.chat.first_name,
                                          str(update.message.chat.id),
                                          link_name)
            bottons = [['💰Пополнить баланс', '🤝Пари'],
                       ['💸Вывести средства', '💼Мой баланс'],
                       ['🔥Дополнительно']]
            user_markup = ReplyKeyboardMarkup(bottons)
            bot.send_message(chat_id=update.message.chat_id, text=constants.hello_text, reply_markup=user_markup)
    elif update.message.text == '💼Мой баланс':
        bottons = [['💰Пополнить баланс', '💸Вывести средства'], ['Назад']]
        user_markup = ReplyKeyboardMarkup(bottons)
        id_ = update.message.chat.id
        s = str(user_com.info(id_)[2])
        bot.send_message(update.message.chat.id, 'Ваш баланс ' + s + ' ВТС', reply_markup=user_markup)
    elif update.message.text == '🔥Дополнительно':
        bottons = [['Задать вопрос', 'Рефералы'], ['FAQ'], ['Назад']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id, '🔥Дополнительно, поддержка @btc_supp', reply_markup=user_markup)
    elif update.message.text == '🤝Пари':
        bottons = [['BTC/USD', 'ETH/USD'], ['XRP/USD', 'BCC/USD'], ['EOS/USD', 'LTC/USD'], ['Назад']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.chat.id, 'Выберете нужную вам пару:', reply_markup= user_markup)
    elif update.message.text == '💸Вывести средства':
        bottons = [['Bitcоin- btc', 'Еtherium - eth'], ['Yаndex Money'], ['Назад']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id, 'Выберите валюту в которой вы хотите вывести средства.', reply_markup=user_markup)
    elif update.message.text == 'Bitcоin- btc' or update.message.text == 'Еtherium - eth' or update.message.text == 'Yаndex Money':
        const = True
        bot.send_message(update.message.chat.id, 'Введите номер кошелька: ')
    elif const == True:
        bot.send_message(update.message.chat.id, 'Введите сумму, которую вы желаете вывести. (Минимальная сумма 0,002 btc или  0.05 eth)')
        const = False
        const_1 =True
    elif const_1 == True:
        const_1 = False
        try:
            float(update.message.text)
            bot.send_message(update.message.chat.id, 'Не хватает денег')
        except:
            bot.send_message(update.message.chat.id, 'Что-то пошло не так, попробуйте еще раз')
        update.message.text = 'Назад'
        answer_start(bot, update)
    elif  update.message.text == 'BCC/USD':
        money = user_com.parse('BCC')
        constants.valume = 'BCC'
        bottons = [['Вверх📈', 'Вниз📉'], ['Назад']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id, 'Вы можете сделать ставку на то, что  курс будет выше или ниже. На данный момент курс BCC: ' + str(
                                    money) + '$',  reply_markup=user_markup)
    elif  update.message.text == 'BTC/USD':
        money = user_com.parse('BTC')
        constants.valume = 'BTC'
        bottons = [['Вверх📈', 'Вниз📉'], ['Назад']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id, 'Вы можете сделать ставку на то, что  курс будет выше или ниже. На данный момент курс BTC: ' + str(
                                    money) + '$',  reply_markup=user_markup)
    elif update.message.text == 'ETH/USD':
        money = user_com.parse('ETH')
        constants.valume = 'ETH'
        bottons = [['Вверх📈', 'Вниз📉'], ['Назад']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id, ' Вы можете сделать ставку на то, что  курс будет выше или ниже. На данный момент курс ETH: ' + str(
                                    money) + '$',  reply_markup=user_markup)
    elif update.message.text == 'XRP/USD':
        money = user_com.parse('XRP')
        constants.valume = 'XRP'
        bottons = [['Вверх📈', 'Вниз📉'], ['Назад']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id, 'Вы можете сделать ставку на то, что  курс будет выше или ниже. На данный момент курс XRP: ' + str(
                                    money) + '$',  reply_markup=user_markup)
    elif update.message.text == 'EOS/USD':
        money = user_com.parse('EOS')
        constants.valume = 'EOS'
        bottons = [['Вверх📈', 'Вниз📉'], ['Назад']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id, 'Вы можете сделать ставку на то, что  курс будет выше или ниже. На данный момент курс EOS: ' + str(
                                    money) + '$',  reply_markup=user_markup)
    elif update.message.text == 'LTC/USD':
        money = user_com.parse('LTC')
        constants.valume = 'LTC'
        bottons = [['Вверх📈', 'Вниз📉'], ['Назад']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id, 'Вы можете сделать ставку на то, что  курс будет выше или ниже. На данный момент курс LTC: ' + str(
                                    money) + '$',  reply_markup=user_markup)
    elif update.message.text == 'Bitcoin- btc':
        bottons = [['Оплатил', 'Отмена']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id,
                         constants.btc_text + '\n' + str(random.choice(constants.btc_list)), reply_markup=user_markup)
    elif update.message.text == 'Etherium - eth':
        bottons = [['Оплатил', 'Отмена']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id, constants.eth_text + '\n' + str(random.choice(constants.eth_list)), reply_markup= user_markup)
    elif update.message.text == '1 Час':
        time_you = True
        user_com.set_alarm(1, update.message.from_user.id)
        bottons = [['Назад']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id, 'Сколько ставите?', reply_markup=user_markup)
    elif update.message.text == '2 Часа':
        time_you = True
        user_com.set_alarm(2, update.message.from_user.id)
        bottons = [['Назад']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id, 'Сколько ставите?', reply_markup=user_markup)
    elif update.message.text == '4 Часа':
        time_you = True
        user_com.set_alarm(4, update.message.from_user.id)
        bottons = [['Назад']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id, 'Сколько ставите?', reply_markup=user_markup)
    elif update.message.text == '6 Часов':
        time_you = True
        user_com.set_alarm(6, update.message.from_user.id)
        bottons = [['Назад']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id, 'Сколько ставите?', reply_markup=user_markup)
    elif update.message.text == '12 Часов':
        time_you = True
        user_com.set_alarm(12, update.message.from_user.id)
        bottons = [['Назад']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id, 'Сколько ставите?', reply_markup=user_markup)
    elif update.message.text == '24 Часа':
        time_you = True
        user_com.set_alarm(23, update.message.from_user.id)
        bottons = [['Назад']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id, 'Сколько ставите?', reply_markup=user_markup)
    elif update.message.text == 'Вверх📈':
        try:
            money = float(user_com.parse(constants.valume))
            user_com.more_less(update.message.from_user.id, 'more', money, constants.valume)
        except:
            pass
        bottons = [['1 Час', '2 Часа', '4 Часа'], ['6 Часов', '12 Часов', '24 Часа'], ['Назад']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id, 'Выберите нужное вам время:', reply_markup=user_markup)
    elif update.message.text == 'Вниз📉':
        try:
            money = float(user_com.parse(constants.valume))
            user_com.more_less(update.message.from_user.id, 'less', money, constants.valume)
        except:
            pass
        bottons = [['1 Час', '2 Часа', '4 Часа'], ['6 Часов', '12 Часов', '24 Часа'], ['Назад']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(update.message.from_user.id, 'Выберите нужное вам время:', reply_markup=user_markup)
    elif update.message.text == 'Назад': #Изменить приветствие
        flag = False
        time_you = False
        money = False
        money_1 = False
        bottons = [['💰Пополнить баланс', '🤝Пари'],
                   ['💸Вывести средства', '💼Мой баланс'],
                   ['🔥Дополнительно']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(chat_id=update.message.chat_id, text = random.choice(constants.hey_text), reply_markup=user_markup)
    elif update.message.text == 'Рефералы':
        info = user_com.info(update.message.chat.id)
        bot.send_message(update.message.chat.id, 'За каждого приведенного реферала, который пополнит баланс, вам начислится 0,0005 BTC \n Это ваша реферальная ссылка: http://t.me/Btc_winbot?start=' + str(info[3]) + ' . \n Ваши рефералы: ' + str(info[5]))
    elif update.message.text== 'Задать вопрос':

        flag = True
        bot.send_message(update.message.chat.id, 'Напишите ваш вопрос, в ближайшее время на него ответит наш модератор!')
    elif flag == True:
        bot.send_message(constants.admin, 'Вопрос: ' + update.message.text)
        bot.send_message(constants.admin, 'Вопрос: ' + update.message.text)
        flag = False
        bot.send_message(update.message.chat.id, 'Спасибо')
        update.message.text = 'Назад'
        answer_start(bot, update)
    elif time_you == True:
        try:
            q = float(update.message.text)
            if  q <= user_com.info(update.message.chat.id)[2]:
                user_com.add_plus(update.message.chat.id, -q)
                user_com.pay(update.message.chat.id, q)
                bot.send_message(update.message.chat.id, 'Ставка принята')
                bot.send_message(constants.admin, str(q)+ ' '+ str(update.message.chat.id) )

            else:
                bot.send_message(update.message.chat.id, 'Не хватает денег')
            time_you = False
            update.message.text = 'Назад'
            answer_start(bot, update)

        except:
            time_you = False
            bot.send_message(update.message.chat.id, 'Что-то пошло не так')
            update.message.text = 'Назад'
            answer_start(bot, update)
    elif update.message.text == 'Закинуть деньги' and (update.message.chat.id == constants.admin or update.message.chat.id == constants.admin2 ):
        bot.send_message(update.message.chat.id, 'Какую сумму вы хотите закинуть? и какой id у пользователя?')
        bot.send_message(update.message.chat.id, 'Сначала вы пишите сколько вы хотите закинуть денег, потом, ID.')
        bot.send_message(update.message.chat.id, 'Например')
        bot.send_message(update.message.chat.id, '286077227 123')
        bot.send_message(update.message.chat.id, 'Теперь у человека id  которого 286077227  на счете 123 BTC')
        bot.send_message(update.message.chat.id, '!!! Главное. Эта Кнопка не прибавляет денег, а изменяет кол-во! То есть у человека было 12 BTC,  а после этой операции станет 123. Например !!!')
        bot.send_message(update.message.chat.id, 'Итак. Какую сумму вы хотите закинуть? и какой id у пользователя?')
        money = True
    elif money == True:
        try:
            text = update.message.text.split()
            user_com.add(text[1], text[0])
            bot.send_message(update.message.chat.id, 'Спасибо, деньги в игре')
            money = False
        except:
            bot.send_message(update.message.chat.id, 'Неверный формат')
            money = False
        update.message.text = 'Назад'
        answer_start(bot, update)
    elif update.message.text == 'Прибавить деньги игроку':
        bot.send_message(update.message.chat.id, 'На сколько вы хотите увеличить счет игрока? и какой id у пользователя?')
        bot.send_message(update.message.chat.id,
                         'Сначала вы пишите id человека, которому вы хотите закинуть денег, потом, через пробел сколько денег.')
        bot.send_message(update.message.chat.id, 'Тут Вы прибавляете некую сумму на чей-то id')
        money_1 = True
    elif money_1 == True:
        try:
            text = update.message.text.split()
            user_com.add_plus(int(text[1]), int(text[0]))
            bot.send_message(update.message.chat.id, 'Спасибо, деньги в игре')


        except:
            bot.send_message(update.message.chat.id, 'Неверный формат')
        update.message.text = 'Назад'
        answer_start(bot, update)
        money_1 = False
    elif update.message.text == 'FAQ':
        bot.send_message(update.message.chat.id, constants.FAQ)
    elif update.message.text == 'Оплатил':
        bot.send_message(update.message.chat.id, 'Оплата принята, ваша транзакция находится в обработке, средства поступят к вам на счёт автоматически после 1-го подтверждения сети.')
        update.message.text = 'Назад'
        answer_start(bot, update)
    elif update.message.text == 'Отмена':
        update.message.text = 'Назад'
        answer_start(bot, update)
    s = user_com.o_clock()
    if s != []:
        for i in s:
            info = user_com.info(i)
            try:
                money_l = user_com.parse(i)
            except:
                break
            if info[8] == 'less':
                if float(str(money_l)) < float(info[7]):
                    user_com.add_plus(info[0], info[6] * 1.8)
                    bot.send_message(info[0], 'Ставка прошла')
                else:
                    bot.send_message(info[0], 'Ставка не прошла')
            else:
                if float(str(money_l)) > float(info[7]):
                    user_com.add_plus(info[0], info[6] * 1.8)
                    bot.send_message(info[0], 'Ставка прошла')
                else:
                    bot.send_message(info[0], 'Ставка не прошла')
            user_com.null(info[0])




def question(bot,update):
    print(update.message.text)


def time_now(bot, arg):
    global flag, time_you, money, money_1,const, const_1
    time_you = flag =  money_1 =  money = const = const_1 = False
    id_ = user_com.all_id()
    write = user_com.parse('All')
    for j in id_:
        try:
            bot.send_message(j[0], constants.kurs % (write[0], write[1], write[2], write[3], write[4], write[6]))
            bottons = [['BTC/USD', 'ETH/USD'], ['XRP/USD', 'BCC/USD'], ['EOS/USD', 'LTC/USD'], ['Назад']]
            user_markup = ReplyKeyboardMarkup(bottons)
            bot.send_message(j[0], 'Выберете нужную вам пару:', reply_markup=user_markup)
        except:
            pass




question_handler = CommandHandler('question', question)
start_handler = CommandHandler('start', start)
answer_handler = MessageHandler(Filters.text, answer_start)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(question_handler)
job_queue.run_daily(time_now, time(22,00))
job_queue.run_daily(time_now, time(18,00))
job_queue.run_daily(time_now, time(21,00))
job_queue.run_daily(time_now, time(20,00))
job_queue.run_daily(time_now, time(16,00))
job_queue.run_daily(time_now, time(14,00))
job_queue.run_daily(time_now, time(12,00))
job_queue.run_daily(time_now, time(10,00))
job_queue.run_daily(time_now, time(8,00))
job_queue.run_daily(time_now, time(6,00))
job_queue.run_daily(time_now, time(4,00))
job_queue.run_daily(time_now, time(2,00))
job_queue.run_daily(time_now, time(0,00))
dispatcher.add_handler(answer_handler)
updater.start_polling(timeout=5, clean=True )
