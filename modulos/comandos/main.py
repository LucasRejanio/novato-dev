from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Update,
    ReplyKeyboardRemove,
)
from telegram.ext import (
    ConversationHandler,
    CallbackContext,
)
from telegram import ParseMode
from modulos.comandos.respostas.tratamento import filtra_resposta



TOPICO, LINGUAGEM, FINAL = range(3)


def iniciar(update: Update, _: CallbackContext) -> int:
    keyboard = [
        [
            InlineKeyboardButton("Sim", callback_data="Sim"),
            InlineKeyboardButton("Bora", callback_data="Bora"),
            InlineKeyboardButton("Claro", callback_data="Claro"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text("Olá !! Sou o NovatoDev !", reply_markup=reply_markup)

    return TOPICO


def cancelar(update: Update, _: CallbackContext) -> int:
    update.message.reply_text(
        'Tchau! Espero que tenha aprendido muito !!!.', reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


def escolher_topico(update: Update, _: CallbackContext) -> None:
    usuario = update.effective_user

    query = update.callback_query

    query.answer()

    # Cria lista com as opções para escolher
    opcoes = [
        [
            InlineKeyboardButton("Hello World", callback_data='hello_world'),
            InlineKeyboardButton("If/Else", callback_data='if_else'),
        ],
        [
            InlineKeyboardButton("Váriaveis", callback_data='variaveis'),
            InlineKeyboardButton("Operadores Lógicos", callback_data='operadores_logicos')
        ],
    ]

    # Monta o teclado com as opçoes
    teclado_com_opcoes = InlineKeyboardMarkup(opcoes)

    query.edit_message_text(
        fr'''Olá {usuario.name} \!
           _*Escolhe ae*_:
        ''',
        parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=teclado_com_opcoes
    )

    return LINGUAGEM

def escolher_linguagem(update: Update, context: CallbackContext) -> None:
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    query.answer()

    context.user_data["topico"] = query.data.lower()

    opcoes = [
        [
            InlineKeyboardButton("Python", callback_data='python'),
            InlineKeyboardButton("Java", callback_data='java'),
        ],
        [
            InlineKeyboardButton("Javascript", callback_data='javascript')
        ],
    ]

    teclado_com_opcoes = InlineKeyboardMarkup(opcoes)

    query.edit_message_text(
        text=f"Boa !! Você escolheu {query.data}, agora escolhe a linguagem !!",
        reply_markup=teclado_com_opcoes
    )

    return FINAL

def final(update: Update, context: CallbackContext) -> None:
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    query.answer()

    context.user_data["linguagem"] = query.data.lower()

    resposta = filtra_resposta(
        linguagem=context.user_data["linguagem"],
        conteudo=context.user_data["topico"]
    )

    query.edit_message_text(
        text=f"""
           Explicação: 
           {resposta['explicacao']}

           Exemplo:
           {resposta['exemplo']}
        """
    )

    return ConversationHandler.END
