import pymysql
import requests

URL = "https://api.coinmarketcap.com/v1/global/"
tickerURL = "https://api.coinmarketcap.com/v1/ticker/"

def create_table ():
    """
    Создается Таблица в  базе данных mysql
    :return:
    """
    conection = pymysql.connect(host='localhost', port=3306, user='root',
                                passwd='root', db='coin')
    cursor = conection.cursor()

    MySQLQuery = ("""CREATE TABLE `coin`.`coins`(
                            `id` INT NOT NULL AUTO_INCREMENT,
                            `name` VARCHAR(128) NOT NULL,
                            `price` FLOAT NOT NULL,
                            `quantity` FLOAT NOT NULL,
                            PRIMARY KEY(`id`))""")

    cursor.execute(MySQLQuery)
    conection.commit()
    conection.close()

# create_table()

def my_coin_porfolio():
    """
    Тут вводится информация по портфелю
    """
    total_coins = {}
    total_coins['ripple'] = float(input("Введите количество монеты Ripple: "))
    total_coins['bitcoin'] = float(input("Введите количество монеты Bitcoin: "))
    total_coins['litecoin'] = float(input("Введите количество монеты Litecoin: "))
    total_coins['ethereum'] = float(input("Введите количество монеты Ethereum: "))
    return  total_coins

def insert_table(total_coins):

    conection = pymysql.connect(host='localhost', port=3306, user='root',
                                passwd='root', db='coin')
    cursor = conection.cursor()
    for key, value in total_coins.items():
        choice = key
        request = requests.get(tickerURL + choice)
        data = request.json()
        for i in data:
            ticker = i['name']
            price = i['price_usd']
            sql = ("""INSERT INTO coins(`name`, `price`, `quantity`) VALUES(%s,%s,%s)""")
            cursor.execute(sql, (ticker, price, value))
            conection.commit()
    conection.close()

def read_bd():
    conection = pymysql.connect(host='localhost', port=3306, user='root',
                                passwd='root', db='coin')
    cursor = conection.cursor()
    sql =("""SELECT * FROM coins """)
    cursor.execute(sql)
    conection.commit()
    result = cursor.fetchall()
    conection.close()
    total_coins = {}
    for i in result:
        total_coins[i[1]]= i[3]
    return total_coins




def update_table(total_coins):
    conection = pymysql.connect(host='localhost', port=3306, user='root',
                                passwd='root', db='coin')
    cursor = conection.cursor()
    for key, value in total_coins.items():
        choice = key
        request = requests.get(tickerURL + choice)
        data = request.json()
        for i in data:
            price = i['price_usd']
            sql = ("""UPDATE coins SET price = %s,quantity = %s  WHERE name = %s """)
            print("Введите новое значение для: ", key)
            new_value = float(input("Ввод: "))
            cursor.execute(sql, (price, new_value, key))
            conection.commit()
    conection.close()

save_read_bd = read_bd()
update_table(save_read_bd)

#param = my_coin_porfolio()
#insert_table(param)