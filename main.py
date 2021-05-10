#!/usr/bin/env python
# import os
import logging
import dotenv

from telegram.ext import (
    Updater,
    CommandHandler,
    ConversationHandler,
    CallbackQueryHandler,
)
from modulos.comandos.main import (
    FINAL,
    LINGUAGEM,
    TOPICO,
    cancelar,
    escolher_linguagem,
    escolher_topico,
    final,
    iniciar,
)

# procura e carrega as variveis de um arquivo .env
dotenv.load_dotenv(dotenv.find_dotenv())

# Habilitar log
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)



def main() -> None:

    updater = Updater("1794849435:AAHpeZLTC6vVCaWtfb8oxMos9Z3AclBgv6Q")

    # Criando o mensageiro
    dispatcher = updater.dispatcher

    # Criando conversa para adicionar ao mensageiro
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('inicio', iniciar)],
        states={
            TOPICO: [
                CallbackQueryHandler(escolher_topico),
            ],
            LINGUAGEM:[
                CallbackQueryHandler(escolher_linguagem)
            ],
            FINAL:[
                CallbackQueryHandler(final)
            ]
        },
        fallbacks=[CommandHandler('cancelar', cancelar)],
    )


    dispatcher.add_handler(conv_handler)

    # Iniando bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
