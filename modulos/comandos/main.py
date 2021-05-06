from modulos.comandos.respostas.tratamento import filtra_resposta
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Update
)
from telegram.ext import CallbackContext
from telegram import ParseMode


def iniciar(update: Update, _: CallbackContext) -> None:
    usuario = update.effective_user

    # Cria lista com as opções para escolher
    opcoes = [
        [
            InlineKeyboardButton("Python", callback_data='Python'),
            InlineKeyboardButton("Java", callback_data='Java'),
        ],
        [
            InlineKeyboardButton("Javascript", callback_data='Javascript')
        ],
    ]

    # Monta o teclado com as opçoes
    teclado_com_opcoes = InlineKeyboardMarkup(opcoes)

    update.message.reply_text(
        fr'''Olá {usuario.name} \!
           _*Escolhe ae*_:
        ''',
        parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=teclado_com_opcoes
    )

def botao(update: Update, _: CallbackContext) -> None:
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    query.answer()

    resposta = filtra_resposta(linguagem=query.data.lower(), conteudo="if/else")

    query.edit_message_text(
        text=f"{resposta['explicacao']}",
        parse_mode=ParseMode.MARKDOWN_V2
    )


def ajuda(update: Update, _: CallbackContext) -> None:
    update.message.reply_text('Help!')
