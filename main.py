#!/usr/bin/env python
# pylint: disable=C0116

import logging

from telegram import Update
from telegram.ext import Updater, CommandHandler

from modules.commands.main import start, help_command

# Habilitar log
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def main() -> None:
    # Criando o atualizador com o token do bot
    # arquivo = open("token.txt")
    # token = arquivo.read()
    # arquivo.close()

    updater = Updater("TOKEN")

    # Criamdo o mensageiro
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # Start Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
