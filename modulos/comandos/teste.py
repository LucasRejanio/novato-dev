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
            InlineKeyboardButton("HTML", callback_data='acerto'),
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
            InlineKeyboardButton("2, 4, 6", callback_data="acerto"),
        ],
        [
            InlineKeyboardButton("1, 3, 5", callback_data="erro"),
        ],
        [
            InlineKeyboardButton("2, 3, 6", callback_data="erro"),
        ],
        [
            InlineKeyboardButton("1, 4, 5", callback_data="erro"),
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
    context.chat_data["proxima_pergunta"] = 4

    # Cria lista com as opções para escolher
    opcoes = [
        [
            InlineKeyboardButton("nomeAluno", callback_data='acerto'),
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

    return TESTE

def quarta_pergunta(update: Update, context: CallbackContext) -> None:
    query = update.callback_query

    query.answer()

    if query.data == '4' and context.chat_data["erro"] is False:
        context.chat_data["pontuacao"] += 1

    context.chat_data["erro"] = False
    context.chat_data["proxima_pergunta"] = 5

    # Cria lista com as opções para escolher
    opcoes = [
        [
            InlineKeyboardButton("+", callback_data='acerto'),
        ],
        [
            InlineKeyboardButton("*", callback_data='erro'),
        ],
        [
            InlineKeyboardButton(">", callback_data='erro'),
        ],
        [
            InlineKeyboardButton(";", callback_data='erro'),
        ],
    ]
    opcoes = random.sample(opcoes, len(opcoes))

    # Monta o teclado com as opçoes
    teclado_com_opcoes = InlineKeyboardMarkup(opcoes)

    query.edit_message_text(
        PERGUNTAS[4]['pergunta'],
        parse_mode=ParseMode.HTML,
        reply_markup=teclado_com_opcoes
    )

    return TESTE


def quinta_pergunta(update: Update, context: CallbackContext) -> None:
    query = update.callback_query

    query.answer()

    if query.data == '5' and context.chat_data["erro"] is False:
        context.chat_data["pontuacao"] += 1

    context.chat_data["erro"] = False
    context.chat_data["proxima_pergunta"] = 6

    # Cria lista com as opções para escolher
    opcoes = [
        [
            InlineKeyboardButton("Inteiro, Booleano, Caractere, Double", callback_data='acerto'),
        ],
        [
            InlineKeyboardButton("Inteiro, Booleano, Tipografia, Double", callback_data='erro'),
        ],
        [
            InlineKeyboardButton("Inteiro, Temporal, Caractere, Double", callback_data='erro'),
        ],
        [
            InlineKeyboardButton("Temporal, Triple, Caractere, Double", callback_data='erro'),
        ],
    ]
    opcoes = random.sample(opcoes, len(opcoes))

    # Monta o teclado com as opçoes
    teclado_com_opcoes = InlineKeyboardMarkup(opcoes)

    query.edit_message_text(
        PERGUNTAS[5]['pergunta'],
        parse_mode=ParseMode.HTML,
        reply_markup=teclado_com_opcoes
    )

    return TESTE


def sexta_pergunta(update: Update, context: CallbackContext) -> None:
    query = update.callback_query

    query.answer()

    if query.data == '6' and context.chat_data["erro"] is False:
        context.chat_data["pontuacao"] += 1

    context.chat_data["erro"] = False
    context.chat_data["proxima_pergunta"] = 7

    # Cria lista com as opções para escolher
    opcoes = [
        [
            InlineKeyboardButton("Calcular o resto de uma divisão inteira", callback_data='0'),
        ],
        [
            InlineKeyboardButton("Realizar cálculos aritméticos de investimentos", callback_data='erro'),
        ],
        [
            InlineKeyboardButton("Calcular porcentagens", callback_data='erro'),
        ],
        [
            InlineKeyboardButton("Retornar o módulo matemático (valor absoluto)", callback_data='erro'),
        ],
    ]
    opcoes = random.sample(opcoes, len(opcoes))

    # Monta o teclado com as opçoes
    teclado_com_opcoes = InlineKeyboardMarkup(opcoes)

    query.edit_message_text(
        PERGUNTAS[6]['pergunta'],
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

    retornar_proxima_ou_resultado = "0" if context.chat_data["proxima_pergunta"] == 7 else context.chat_data["proxima_pergunta"]

    # Cria lista com as opções para escolher
    opcoes = [
        [
            InlineKeyboardButton("Bora pra próxima", callback_data=retornar_proxima_ou_resultado),
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

    return TESTE if context.chat_data["proxima_pergunta"] < 7 else RESULTADO


def resposta_correta(update: Update, context: CallbackContext) -> None:
    query = update.callback_query

    query.answer()

    retornar_proxima_ou_resultado = "0" if context.chat_data["proxima_pergunta"] == 7 else context.chat_data["proxima_pergunta"]

    finalizar_ou_bora = "Finalizar" if context.chat_data["proxima_pergunta"] == 7 else "Bora pra próxima"

    # Cria lista com as opções para escolher
    opcoes = [
        [
            InlineKeyboardButton(finalizar_ou_bora, callback_data=retornar_proxima_ou_resultado),
        ],
    ]

    # Monta o teclado com as opçoes
    teclado_com_opcoes = InlineKeyboardMarkup(opcoes)


    query.edit_message_text(
        text="""
        Boaaa !! Resposta correta !
        """,
        parse_mode=ParseMode.HTML,
        reply_markup=teclado_com_opcoes
    )

    return TESTE if context.chat_data["proxima_pergunta"] < 7 else RESULTADO



def resultado(update: Update, context: CallbackContext) -> None:
    query = update.callback_query

    query.answer()

    if query.data == '0' and context.chat_data["erro"] is False:
        context.chat_data["pontuacao"] += 1

    query.edit_message_text(
        text=f"""
        Acabou !!!

        Você acertou {context.chat_data["pontuacao"]}

        """,
        parse_mode=ParseMode.HTML,
    )

    return ConversationHandler.END
