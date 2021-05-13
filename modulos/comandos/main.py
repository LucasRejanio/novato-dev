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



ESCOLHA, LINGUAGEM, RESPOSTA = range(3)


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
        'Até  mais, espero que tenha aprendido muito! 🖖', reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END

def ajudar(update: Update, _: CallbackContext) -> int:
    update.message.reply_text(
        """
Comandos disponíveis:

<b><u>/cancelar</u>  -> </b> finaliza a conversa comigo 😢
<b><u>/voltar</u> -> </b> reinicia a conversa
        """,
        reply_markup=ReplyKeyboardRemove(),
        parse_mode=ParseMode.HTML
    )


def teste_de_conhecimento(update: Update, _: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        'Testes em construção, inicie o bot novamente com /start'
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
        [
            InlineKeyboardButton("Oper. Relacionais", callback_data='operadores_relacionais'),
            InlineKeyboardButton("Tipagem", callback_data='tipagem')
        ],
        [
            InlineKeyboardButton("Oper. Matemáticas", callback_data='operacoes_matematicas'),
            InlineKeyboardButton("Instalação", callback_data='instalacao'),
        ],
        [
            InlineKeyboardButton("Curiosidade", callback_data='curiosidade'),
            InlineKeyboardButton("Curso", callback_data='curso'),
        ],
    ]

    # Monta o teclado com as opçoes
    teclado_com_opcoes = InlineKeyboardMarkup(opcoes)

    query.edit_message_text(
        f'''Olá {usuario.name} !

<b>O que você deseja aprender?</b> 🧠
        ''',
        parse_mode=ParseMode.HTML,
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

    return RESPOSTA

def resposta(update: Update, context: CallbackContext) -> None:
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    query.answer()

    context.user_data["linguagem"] = query.data.lower()

    resposta_final = filtra_resposta(
        linguagem=context.user_data["linguagem"],
        conteudo=context.user_data["topico"]
    )

    query.edit_message_text(
        text=f"""
<b>Explicação:</b>
    {resposta_final['explicacao']}
<b>Exemplo:</b>
    {resposta_final['exemplo']}
<b>Se você está com sede de conhecimento, use o comando <u>/voltar</u> e retorne para o ínicio!</b>
 
        """,
        parse_mode=ParseMode.HTML,
    )
