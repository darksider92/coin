import json
import requests
import os

URL = "https://api.coinmarketcap.com/v1/global/"
tickerURL = "https://api.coinmarketcap.com/v1/ticker/"


class Portfolio:
    def __init__(self, ripple, litecoin, ethereum, bitcoin):
        self.ripple = ripple
        self.litecoin = litecoin
        self.ethereum = ethereum
        self.bitcoin = bitcoin

    def add_coin(self, coin, value):
        if coin == "ethereum":
            self.ethereum += value
        elif coin == "bitcoin":
            self.bitcoin += value
        elif coin == "litecoin":
            self.litecoin += value
        elif coin == "ripple":
            self.ripple += value
        else:
            print("Такой валюты нет!")

    def take_away_coin(self, coin, value):
        if coin == "ethereum":
            self.ethereum -= value
        elif coin == "bitcoin":
            self.bitcoin -= value
        elif coin == "litecoin":
            self.litecoin -= value
        elif coin == "ripple":
            self.ripple -= value
        else:
            print("Такой валюты нет!")


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


def create_dict():
    """
    Создаем экземпляр класса
    """
    my_coins = Portfolio(result["ripple"], result["litecoin"], result["ethereum"], result["bitcoin"])
    print(my_coins)


if __name__ == "__main__":
    if os.path.isfile("E:\\Python\\coin\\db.json"):
        pass
    else:
        my_coin_porfolio()
    with open("db.json", "r", encoding="UTF-8") as f:
        result = json.load(f)
        create_dict()
        for key, value in result.items():
            param = input_coin(key)
            print_price(param, value)
