import requests
import pandas as pd

# Определите URL для получения данных
url = "https://iss.moex.com/iss/engines/stock/markets/shares/securities.json"


# Функция для получения данных о котировках
def fetch_stock_data():
    # Отправляем GET-запрос на API
    response = requests.get(url)
    response.raise_for_status()  # Проверка на успешность запроса

    # Получаем данные в формате JSON
    data = response.json()

    # Извлекаем интересующие нас данные
    securities = data['securities']['data']
    columns = data['securities']['columns']

    # Создаем DataFrame с данными
    df = pd.DataFrame(securities, columns=columns)
    return df


# Получаем данные и выводим их
stock_data = fetch_stock_data()
print(stock_data.head())
