#!/usr/bin/env python
import os
import logging
import dotenv

from telegram.ext import CallbackQueryHandler, CommandHandler, Updater
from modulos.comandos.main import botao, iniciar, ajuda

# procura e carrega as variveis de um arquivo .env
dotenv.load_dotenv(dotenv.find_dotenv())

# Habilitar log
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def main() -> None:

    updater = Updater(os.getenv("TELEGRAM_TOKEN"))

    # Criando o mensageiro
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", iniciar))
    dispatcher.add_handler(CallbackQueryHandler(botao))
    dispatcher.add_handler(CommandHandler("help", ajuda))

    # Iniando bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
