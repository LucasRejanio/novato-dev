import random
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Update,
)
from telegram.ext import (
    CallbackContext,
    ConversationHandler,
)
from telegram import ParseMode
from modulos.comandos.main import RESULTADO, TESTE
from modulos.comandos.respostas.teste.perguntas import PERGUNTAS


def primeira_pergunta(update: Update, context: CallbackContext) -> None:
    query = update.callback_query

    query.answer()

    context.chat_data["pontuacao"] = 0
    context.chat_data["erro"] = False
    context.chat_data["proxima_pergunta"] = 2

    # Cria lista com as opções para escolher
    opcoes = [
        [
            InlineKeyboardButton("HTML", callback_data='2'),
        ],
        [
            InlineKeyboardButton("CSS", callback_data='erro'),
        ],
        [
            InlineKeyboardButton("Javascript", callback_data='erro'),
        ],
        [
            InlineKeyboardButton("SQL", callback_data='erro'),
        ],
    ]

    opcoes = random.sample(opcoes, len(opcoes))

    # Monta o teclado com as opçoes
    teclado_com_opcoes = InlineKeyboardMarkup(opcoes)

    query.edit_message_text(
        PERGUNTAS[1]['pergunta'],
        parse_mode=ParseMode.HTML,
        reply_markup=teclado_com_opcoes
    )

    return TESTE

def segunda_pergunta(update: Update, context: CallbackContext) -> None:
    query = update.callback_query

    query.answer()

    if query.data == '2' and context.chat_data["erro"] is False:
        context.chat_data["pontuacao"] += 1

    context.chat_data["erro"] = False
    context.chat_data["proxima_pergunta"] = 3


    # Cria lista com as opções para escolher
    opcoes = [
        [
            InlineKeyboardButton("2, 4, 6", callback_data="3"),
        ],
        [
            InlineKeyboardButton("opa", callback_data="erro"),
        ],
        [
            InlineKeyboardButton("opa", callback_data="erro"),
        ],
        [
            InlineKeyboardButton("opa", callback_data="erro"),
        ],

    ]

    opcoes = random.sample(opcoes, len(opcoes))

    # Monta o teclado com as opçoes
    teclado_com_opcoes = InlineKeyboardMarkup(opcoes)

    query.edit_message_text(
        PERGUNTAS[2]['pergunta'],
        parse_mode=ParseMode.HTML,
        reply_markup=teclado_com_opcoes
    )

    return TESTE


def terceira_pergunta(update: Update, context: CallbackContext) -> None:
    query = update.callback_query

    query.answer()

    if query.data == '3' and context.chat_data["erro"] is False:
        context.chat_data["pontuacao"] += 1

    context.chat_data["erro"] = False
    context.chat_data["proxima_pergunta"] = 3

    # Cria lista com as opções para escolher
    opcoes = [
        [
            InlineKeyboardButton("nomeAluno", callback_data='4'),
        ],
        [
            InlineKeyboardButton("2nota", callback_data='erro'),
        ],
        [
            InlineKeyboardButton("rua&Numero", callback_data='erro'),
        ],
        [
            InlineKeyboardButton("numero casa", callback_data='erro'),
        ],
    ]
    opcoes = random.sample(opcoes, len(opcoes))

    # Monta o teclado com as opçoes
    teclado_com_opcoes = InlineKeyboardMarkup(opcoes)

    query.edit_message_text(
        PERGUNTAS[3]['pergunta'],
        parse_mode=ParseMode.HTML,
        reply_markup=teclado_com_opcoes
    )

    return RESULTADO

def resposta_errada(update: Update, context: CallbackContext) -> None:
    query = update.callback_query

    query.answer()

    context.chat_data["erro"] = True

    pergunta = context.chat_data["proxima_pergunta"] - 1
    resposta_certa = PERGUNTAS[pergunta]['resposta']

    # Cria lista com as opções para escolher
    opcoes = [
        [
            InlineKeyboardButton("Bora pra próxima", callback_data=context.chat_data["proxima_pergunta"]),
        ],
    ]

    # Monta o teclado com as opçoes
    teclado_com_opcoes = InlineKeyboardMarkup(opcoes)


    query.edit_message_text(
        text=f"""
        Puts resposta errada 

        A correta era {resposta_certa}

        """,
        parse_mode=ParseMode.HTML,
        reply_markup=teclado_com_opcoes
    )

    return TESTE


def resultado(update: Update, context: CallbackContext) -> None:
    query = update.callback_query

    query.answer()

    if query.data == '4' and context.chat_data["erro"] is False:
        context.chat_data["pontuacao"] += 1

    query.edit_message_text(
        text=f"""
        Acabou !!!

        Você acertou {context.chat_data["pontuacao"]}

        """,
        parse_mode=ParseMode.HTML,
    )

    return ConversationHandler.END
