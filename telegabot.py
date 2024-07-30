import requests
from telegram import Update, Bot
from telegram.ext import CommandHandler, Updater, CallbackContext

# Замените на свои данные
TELEGRAM_TOKEN = 'ваш_токен_телеграм_бота'

MOEX_API_TOKEN = 'ваш_токен_московской_биржи'
MOEX_API_URL = 'https://iss.moex.com/iss/engines/stock/markets/shares/boards/tqbr/securities'


def get_stock_quote(stock_symbol):
    endpoint = f'{MOEX_API_URL}/{stock_symbol}.json'
    headers = {
        'Authorization': f'Bearer {MOEX_API_TOKEN}'
    }

    try:
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()

        data = response.json()
        if 'marketdata' in data['marketdata']:
            quotes = data['marketdata']['marketdata']
            return quotes
        else:
            return None

    except requests.exceptions.RequestException as e:
        print(f'Error fetching data: {e}')
        return None


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я финансовый бот. Напиши /quote <ticker> для получения текущей цены акции.')


def quote(update: Update, context: CallbackContext) -> None:
    if len(context.args) == 0:
        update.message.reply_text('Пожалуйста, укажите тикер акции. Например: /quote SBER')
        return

    stock_symbol = context.args[0].upper()
    quotes = get_stock_quote(stock_symbol)

    if quotes:
        response_message = f'Текущая цена акции {stock_symbol}: {quotes["LAST"]}'
    else:
        response_message = f'Извините, данные по акции {stock_symbol} не найдены.'

    update.message.reply_text(response_message)


def main() -> None:
    updater = Updater(TELEGRAM_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("quote", quote))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
