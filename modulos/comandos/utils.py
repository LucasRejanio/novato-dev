import random
from typing import Dict
from telegram.callbackquery import CallbackQuery
from telegram.inline.inlinekeyboardbutton import InlineKeyboardButton
from telegram.inline.inlinekeyboardmarkup import InlineKeyboardMarkup
from telegram import ParseMode
from modulos.comandos.respostas.teste.perguntas import PERGUNTAS


def montar_perguntas(query: CallbackQuery, pergunta: int, alternativas: Dict[str, str]) -> None:

    # Cria lista com as opções para escolher
    opcoes = [[InlineKeyboardButton(alternativa, callback_data=valor)] for alternativa, valor in alternativas.items()]

    # Reordena a lista aleatóriamente
    opcoes = random.sample(opcoes, len(opcoes))

    # Monta o teclado com as opçoes
    teclado_com_opcoes = InlineKeyboardMarkup(opcoes)

    query.edit_message_text(
        PERGUNTAS[pergunta]['pergunta'],
        parse_mode=ParseMode.HTML,
        reply_markup=teclado_com_opcoes
    )
