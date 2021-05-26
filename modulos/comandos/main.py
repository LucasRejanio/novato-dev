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

RESULTADO, TESTE, ESCOLHA, LINGUAGEM, RESPOSTA, QUIZ = range(6)


def iniciar(update: Update, _: CallbackContext) -> int:
    usuario = update.effective_user

    keyboard = [
        [
            InlineKeyboardButton("Aprenda mais!", callback_data="aprender"),
        ],
        [
            InlineKeyboardButton(text="Teste seus conhecimentos", callback_data="teste"),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        f"""
Olá {usuario.name}, sou o <b>NovatoDev!</b> 🚀 💻

Aqui irei te ajudar com dúvidas básicas sobre o universo da programação, além de testar seu conhecimento!
Vamos começar?

Para ver meus outros comandos digite <b><u>/help</u></b>
        """,
        reply_markup=reply_markup,
        parse_mode=ParseMode.HTML,
    )

    return ESCOLHA


def cancelar(update: Update, _: CallbackContext) -> int:
    update.message.reply_text(
        'Até mais, espero que tenha aprendido muito! 🖖', reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END

def ajudar(update: Update, _: CallbackContext) -> int:
    update.message.reply_text(
        """
Comandos disponíveis:

<b><u>/cancelar</u>  → </b> Finaliza a conversa comigo 😢

<b><u>/voltar</u> → </b> Reinicia a conversa

        """,
        reply_markup=ReplyKeyboardRemove(),
        parse_mode=ParseMode.HTML
    )


def iniciar_quiz(update: Update, _: CallbackContext) -> None:
    usuario = update.effective_user

    query = update.callback_query

    query.answer()

    # Cria lista com as opções para escolher
    opcoes = [
        [
            InlineKeyboardButton("BÓRA", callback_data='bora'),
        ],
    ]

    # Monta o teclado com as opçoes
    teclado_com_opcoes = InlineKeyboardMarkup(opcoes)

    query.edit_message_text(
        f'''Eae {usuario.name}!

<b>Pronto para iniciar o teste?</b> 🧠
        ''',
        parse_mode=ParseMode.HTML,
        reply_markup=teclado_com_opcoes
    )

    return QUIZ
