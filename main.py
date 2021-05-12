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
    ESCOLHA,
    RESPOSTA,
    LINGUAGEM,
    ajudar,
    cancelar,
    escolher_linguagem,
    escolher_topico,
    resposta,
    iniciar,
    teste_de_conhecimento,
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
    conversa_handler = ConversationHandler(
        entry_points=[CommandHandler('start', iniciar)],
        states={
            ESCOLHA:[
                CallbackQueryHandler(escolher_topico, pattern='^' + "aprender" + '$'),
                CallbackQueryHandler(teste_de_conhecimento, pattern='^' + "teste" + '$'),
            ],
            LINGUAGEM:[
                CallbackQueryHandler(escolher_linguagem)
            ],
            RESPOSTA:[
                CallbackQueryHandler(resposta)
            ]
        },
        fallbacks=[
            CommandHandler('cancelar', cancelar),
            CommandHandler('voltar', iniciar),
            CommandHandler('help', ajudar),
        ],
    )


    dispatcher.add_handler(conversa_handler)

    # Iniando bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
