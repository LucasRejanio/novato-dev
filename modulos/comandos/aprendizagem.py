from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Update,
)
from telegram.ext import (
    CallbackContext,
)
from telegram import ParseMode
from modulos.comandos.main import LINGUAGEM, RESPOSTA
from modulos.comandos.respostas.utils import TOPICOS_PARA_USUARIO, filtra_resposta


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
            InlineKeyboardButton("Variáveis", callback_data='variaveis'),
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
        text=f"Boa !! Você escolheu {TOPICOS_PARA_USUARIO[query.data]}, agora escolhe a linguagem !!",
        reply_markup=teclado_com_opcoes,
        parse_mode=ParseMode.HTML,
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
