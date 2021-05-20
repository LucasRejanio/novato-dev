#!/usr/bin/env python
import os
import logging
import dotenv

from telegram.ext import (
    Updater,
    CommandHandler,
    ConversationHandler,
    CallbackQueryHandler,
)
from modulos.comandos.main import ESCOLHA, QUIZ, RESPOSTA, LINGUAGEM, RESULTADO, TESTE
from modulos.comandos.main import (
    ajudar,
    cancelar,
    iniciar,
    iniciar_quiz,
)
from modulos.comandos.aprendizagem import escolher_linguagem, escolher_topico, resposta
from modulos.comandos.teste import primeira_pergunta, resposta_errada, resultado, segunda_pergunta, terceira_pergunta

# procura e carrega as variveis de um arquivo .env
dotenv.load_dotenv(dotenv.find_dotenv())

# Habilitar log
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)



def main() -> None:

    updater = Updater(os.getenv('TELEGRAM_TOKEN'))

    # Criando o mensageiro
    dispatcher = updater.dispatcher

    quiz_conv = ConversationHandler(
        entry_points=[CallbackQueryHandler(primeira_pergunta, pattern='^' + "bora" + '$')],
        states={
            TESTE:[
                CallbackQueryHandler(segunda_pergunta, pattern='^' + "2" + '$'),
                CallbackQueryHandler(terceira_pergunta, pattern='^' + "3" + '$'),
            ],
            RESULTADO:[
                CallbackQueryHandler(resultado),
            ]
        },
        fallbacks=[
            CallbackQueryHandler(resposta_errada, pattern='^' + "erro" + '$'),
        ],
    )

    # Criando conversa para adicionar ao mensageiro
    conversa_handler = ConversationHandler(
        entry_points=[CommandHandler('start', iniciar)],
        states={
            ESCOLHA:[
                CallbackQueryHandler(escolher_topico, pattern='^' + "aprender" + '$'),
                CallbackQueryHandler(iniciar_quiz, pattern='^' + "teste" + '$'),
            ],
            LINGUAGEM:[
                CallbackQueryHandler(escolher_linguagem)
            ],
            RESPOSTA:[
                CallbackQueryHandler(resposta)
            ],
            QUIZ:[
                quiz_conv
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
