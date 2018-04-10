import json
import requests
import os

URL = "https://api.coinmarketcap.com/v1/global/"
tickerURL = "https://api.coinmarketcap.com/v1/ticker/"


def my_coin_porfolio():
    """
    Тут вводится информация по портфелю и сохроняется в json файл
    """
    total_coins = {}
    total_coins['ripple'] = float(input("Введите количество монеты Ripple: "))
    total_coins['bitcoin'] = float(input("Введите количество монеты Bitcoin: "))
    total_coins['litecoin'] = float(input("Введите количество монеты Litecoin: "))
    total_coins['ethereum'] = float(input("Введите количество монеты Ethereum: "))
    with open("db.json", "w", encoding="UTF-8")as f:
        json.dump(total_coins, f, indent=2)


# CoinMarketCap

def input_coin(key):
    """
    Выбираем криптовалюту по которой хотим получить информацию
    :return:
    """
    choice = key
    request = requests.get(tickerURL + choice)
    data = request.json()
    return data


def print_price(data, count_coins):
    """
    Функция вывода необходимой информации по монете
    Итоговый вывод по кошельку
    """
    for i in data:
        ticker = i['name']
        price = i['price_usd']
    print(ticker + " cейчас стоит: " + price + "$" + ". У вас в портфеле: " + str(count_coins))
    print("Итого: " + str(float(price) * count_coins) + "$")


def add_coin(coin, number):
    totals = {}
    with open("db.json", "r", encoding="UTF-8") as f:
        date = json.load(f)
        for k, v in date.items():
            if coin == k:
                summ = v + number
                totals[k] = summ
            elif coin != k:
                totals[k] = v

    with open("db.json", "w", encoding="UTF-8") as file:
        json.dump(totals, file)


def take_away(coin, number):
    totals = {}
    with open("db.json", "r", encoding="UTF-8") as f:
        date = json.load(f)
        for k, v in date.items():
            if coin == k:
                summ = v - number
                totals[k] = summ
            elif coin != k:
                totals[k] = v

    with open("db.json", "w", encoding="UTF-8") as file:
        json.dump(totals, file)


if __name__ == "__main__":
    while True:
        print("""
            n - создание базы данных
            d - удаление базы данных
            c - получение информации по криптовалюте
            a - добавление криптовалюты в портфель
            t - отнимаем криптовалюту с портфеля
            q - выход
        """)
        name_inp = input("Введите ключ: ")
        if name_inp == "n":
            if os.path.isfile(os.getcwd() + "db.json"):
                pass
            else:
                my_coin_porfolio()
        if name_inp == "c":
            with open("db.json", "r", encoding="UTF-8") as f:
                result = json.load(f)
                for key, value in result.items():
                    param = input_coin(key)
                    print_price(param, value)
        if name_inp == "a":
            print("ripple", " bitcoin", " litecoin", " ethereum")
            coin_name = input("Введите имя криптовалюты: ").lower()
            coin_value = float((input("Введите число для добавления: ")))
            add_coin(coin_name, coin_value)
        if name_inp == "t":
            print("ripple", " bitcoin", " litecoin", " ethereum")
            coin_name = input("Введите имя криптовалюты: ").lower()
            coin_value = float((input("Введите число для вычитание: ")))
            take_away(coin_name, coin_value)
        if name_inp == "q":
            break
        if name_inp == "d":
            print("Вы точно хотите сбросить базу данных? ")
            print("Yes, No")
            answer = input(": ")
            if answer == "Yes".lower():
                os.remove("db.json")
            elif answer == "No".lower():
                pass
