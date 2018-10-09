import sqlite3
import datetime
import urllib.request
from bs4 import BeautifulSoup

def null(user_id):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET time_=:time_ , pay_mail=:pay_mail, status=:status, more_less=:more_less  WHERE id=:user_id',
                   {'time_': None, 'pay_mail': None, 'status': None, 'more_less': None, 'user_id': user_id})

    conn.commit()
    cursor.close()
    conn.close()


def registration(user_id, name_, link_, link_name): #Регистрация нового юзера
    flag = False
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id=:id",
                   {'id': user_id})
    write = cursor.fetchone()

    if write == None:
        cursor.execute('INSERT INTO users (id, name, coin, link, link_members) VALUES (?, ?, 0, ?, 0)',(user_id, name_, link_))

        flag = True

    conn.commit()
    cursor.close()
    conn.close()
    if flag == True:
        try:
            invite_plus(int(link_name))
        except:
            pass
        return 'Я смотрю, ты новенький! Добро пожаловать!'
    else:
        return ''

def bot_insert(user_id, name, link): # создание нового юзера
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (id, name, coin, link, link_members) VALUES (user_id, name, 0, link, 0)",
                   {'user_id': user_id, 'name': name, 'link':link })
    conn.commit()
    cursor.close()
    conn.close()

def add(user_id, coin): # заменить ячейку денег на кол-во
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET coin=:coin WHERE id=:user_id',
                   {'coin': coin, 'user_id': user_id})
    conn.commit()
    cursor.close()
    conn.close()

def info(user_id): #все о пользователе
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE id=:user_id',
                   {'user_id': user_id})
    write = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return write

def add_plus(user_id, summ): # прибавляет деньги
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE id=:user_id',
                   {'user_id': user_id})
    write = cursor.fetchone()[2]
    summ += write
    cursor.execute('UPDATE users SET coin=:summ WHERE id=:user_id',
                   {'summ': summ, 'user_id': user_id})
    conn.commit()
    cursor.close()
    conn.close()

def WTII(): # собирает всех пользователей
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    write = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return write

def pay(user_id, money):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET pay_mail=:money WHERE id=:user_id',
                   {'money': money, 'user_id': user_id})
    conn.commit()
    cursor.close()
    conn.close()

def o_clock(): # выводит все id тех, у кого запланированно время
    a = []
    mass = WTII()
    time_now = str(datetime.datetime.today().time())[2:5]
    hour_now = datetime.datetime.today().hour  % 24
    time_now = str(hour_now) + time_now
    for i in mass:
        if i[4] == time_now:
          a.append(i[0])

    return a

def has_no(user_id): # выводит False если денег нет, и наоборот
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE id=:user_id',
                   {'user_id': user_id})
    write = cursor.fetchone()[2]
    conn.commit()
    cursor.close()
    conn.close()

    if write == 0 :
        return False
    else:
        return True

def parse(arg): # парсинг сайта
    if arg == 'BTC':
        url = 'https://coinmarketcap.com/currencies/bitcoin/'
        r = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(r, "html.parser")
        table = soup.find('span', class_ = 'h2 text-semi-bold details-panel-item--price__value').text
        return table
    elif arg == 'ETH':
        url = 'https://coinmarketcap.com/currencies/ethereum/'
        r = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(r, "html.parser")
        table = soup.find('span', class_='h2 text-semi-bold details-panel-item--price__value').text
        return table
    elif arg == 'XRP':
        url = 'https://coinmarketcap.com/currencies/ripple/'
        r = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(r, "html.parser")
        table = soup.find('span', class_='h2 text-semi-bold details-panel-item--price__value').text
        return table
    elif arg == 'BCC':
        url = 'https://coinmarketcap.com/currencies/bitcoin-cash/'
        r = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(r, "html.parser")
        table = soup.find('span', class_='h2 text-semi-bold details-panel-item--price__value').text
        return table
    elif arg == 'EOS':
        url = 'https://coinmarketcap.com/currencies/eos/'
        r = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(r, "html.parser")
        table = soup.find('span', class_='h2 text-semi-bold details-panel-item--price__value').text
        return table
    elif arg == 'LTC':
        url = 'https://coinmarketcap.com/currencies/litecoin/'
        r = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(r, "html.parser")
        table = soup.find('span', class_='h2 text-semi-bold details-panel-item--price__value').text
        return table
    elif arg == 'All':
        url = 'https://coinmarketcap.com/'
        r = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(r, "html.parser")
        table = soup.find_all('td', class_='no-wrap text-right')
        write = []
        for i in table:
            write.append(i.text[2:-2:])
        return  write[:14:2]
    else:
        conn = sqlite3.connect('base.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE id=:user_id',
                       {'user_id': arg})
        write = cursor.fetchone()[9]
        conn.commit()
        cursor.close()
        conn.close()
        parse(write)



def invite_plus(user_id): # Рефералка
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE id=:user_id',
                   {'user_id': user_id})
    write = cursor.fetchone()
    number_ = write[5]
    write = write[2] + 0.0005
    number_+=1
    cursor.execute('UPDATE users SET coin=:summ , link_members=:number_ WHERE id=:user_id',
                   {'summ': write, 'number_':number_ ,'user_id': user_id})
    conn.commit()
    cursor.close()
    conn.close()

def set_alarm(hour, user_id):
    time_now = str(datetime.datetime.today().time())[2:5]
    hour_now = (datetime.datetime.today().hour + hour) % 24
    time = str(hour_now) + time_now

    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET time_=:time_ WHERE id=:user_id',
                   {'time_': time, 'user_id':user_id})
    conn.commit()
    cursor.close()
    conn.close()

def more_less(user_id, moree, money,valume):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET status=:money , more_less=:moree, valume=:valume WHERE id=:user_id',
                   {'money': money, 'moree': moree, 'valume': valume, 'user_id': user_id})
    conn.commit()
    cursor.close()
    conn.close()


def all_id():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()

    cursor.execute('SELECT id, boolsh FROM users ')
    write = cursor.fetchall()

    conn.commit()
    cursor.close()
    conn.close()
    return write

def all_id_false(user_id, arg):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET boolsh=:boolsh WHERE id=:id',
                   {'boolsh': arg , 'id': user_id})

    conn.commit()
    cursor.close()
    conn.close()

def one_id_false(user_id):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()

    cursor.execute('SELECT boolsh FROM users WHERE id=:id', {'id': user_id})
    write = cursor.fetchone()

    conn.commit()
    cursor.close()
    conn.close()
    return write

def minus_minus(user_id):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('SELECT boolsh_num FROM users WHERE id=:id', {'id': user_id})
    arg = int(cursor.fetchone()[0])
    arg -=1
    cursor.execute('UPDATE users SET boolsh_num=:boolsh_num WHERE id=:id',
                   {'boolsh_num': arg, 'id': user_id})

    conn.commit()
    cursor.close()
    conn.close()
    return arg

def plus_plus(user_id):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('SELECT boolsh_num FROM users WHERE id=:id', {'id': user_id})
    arg = int(cursor.fetchone()[0])
    arg += 1
    cursor.execute('UPDATE users SET boolsh_num=:boolsh_num WHERE id=:id',
                   {'boolsh_num': arg, 'id': user_id})

    conn.commit()
    cursor.close()
    conn.close()
    return arg