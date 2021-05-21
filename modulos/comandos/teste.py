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
from modulos.comandos.utils import montar_perguntas


def primeira_pergunta(update: Update, context: CallbackContext) -> None:
    query = update.callback_query

    query.answer()

    context.chat_data["pontuacao"] = 0
    context.chat_data["erro"] = False
    context.chat_data["proxima_pergunta"] = 2

    alternativas = {
        "HTML": "acerto",
        "CSS": "erro",
        "SQL": "erro",
        "Javascript": "erro",
    }

    montar_perguntas(query, 1, alternativas)

    return TESTE

def segunda_pergunta(update: Update, context: CallbackContext) -> None:
    query = update.callback_query

    query.answer()

    if query.data == '2' and context.chat_data["erro"] is False:
        context.chat_data["pontuacao"] += 1

    context.chat_data["erro"] = False
    context.chat_data["proxima_pergunta"] = 3

    alternativas = {
        "2, 4, 6": "acerto",
        "1, 3, 5": "erro",
        "2, 3, 6": "erro",
        "1, 4, 5": "erro",
    }

    montar_perguntas(query, 2, alternativas)

    return TESTE


def terceira_pergunta(update: Update, context: CallbackContext) -> None:
    query = update.callback_query

    query.answer()

    if query.data == '3' and context.chat_data["erro"] is False:
        context.chat_data["pontuacao"] += 1

    context.chat_data["erro"] = False
    context.chat_data["proxima_pergunta"] = 4

    alternativas = {
        "nomeAluno": "acerto",
        "2nota": "erro",
        "rua&Numero": "erro",
        "numero casa": "erro",
    }

    montar_perguntas(query, 3, alternativas)

    return TESTE

def quarta_pergunta(update: Update, context: CallbackContext) -> None:
    query = update.callback_query

    query.answer()

    if query.data == '4' and context.chat_data["erro"] is False:
        context.chat_data["pontuacao"] += 1

    context.chat_data["erro"] = False
    context.chat_data["proxima_pergunta"] = 5

    alternativas = {
        "+": "acerto",
        "*": "erro",
        ">": "erro",
        ";": "erro",
    }

    montar_perguntas(query, 4, alternativas)

    return TESTE


def quinta_pergunta(update: Update, context: CallbackContext) -> None:
    query = update.callback_query

    query.answer()

    if query.data == '5' and context.chat_data["erro"] is False:
        context.chat_data["pontuacao"] += 1

    context.chat_data["erro"] = False
    context.chat_data["proxima_pergunta"] = 6

    alternativas = {
        "Inteiro, Booleano, Caractere, Double": "acerto",
        "Inteiro, Booleano, Tipografia, Double": "erro",
        "Inteiro, Temporal, Caractere, Double": "erro",
        "Temporal, Triple, Caractere, Double": "erro",
    }

    montar_perguntas(query, 5, alternativas)

    return TESTE


def sexta_pergunta(update: Update, context: CallbackContext) -> None:
    query = update.callback_query

    query.answer()

    if query.data == '6' and context.chat_data["erro"] is False:
        context.chat_data["pontuacao"] += 1

    context.chat_data["erro"] = False
    context.chat_data["proxima_pergunta"] = 7

    alternativas = {
        "Calcular o resto de uma divisão inteira": "acerto",
        "Realizar cálculos aritméticos de investimentos": "erro",
        "Calcular porcentagens": "erro",
        "Retornar o módulo matemático (valor absoluto)": "erro",
    }

    montar_perguntas(query, 6, alternativas)

    return RESULTADO

def resposta_errada(update: Update, context: CallbackContext) -> None:
    query = update.callback_query

    query.answer()

    context.chat_data["erro"] = True

    pergunta = context.chat_data["proxima_pergunta"] - 1
    resposta_certa = PERGUNTAS[pergunta]['resposta']

    retornar_proxima_ou_resultado = "0" if context.chat_data["proxima_pergunta"] == 7 else context.chat_data["proxima_pergunta"]
    finalizar_ou_bora = "Finalizar" if context.chat_data["proxima_pergunta"] == 7 else "Borá pra próxima"

    # Cria lista com as opções para escolher
    opcoes = [
        [
            InlineKeyboardButton(finalizar_ou_bora, callback_data=retornar_proxima_ou_resultado),
        ],
    ]

    # Monta o teclado com as opçoes
    teclado_com_opcoes = InlineKeyboardMarkup(opcoes)


    query.edit_message_text(
        text=f"""
Ah não 😫! Resposta errada. 

A resposta correta era: <u><b>{resposta_certa}</b></u>. Mas não desanime!

        """,
        parse_mode=ParseMode.HTML,
        reply_markup=teclado_com_opcoes
    )

    return TESTE if context.chat_data["proxima_pergunta"] < 7 else RESULTADO


def resposta_correta(update: Update, context: CallbackContext) -> None:
    query = update.callback_query

    query.answer()

    retornar_proxima_ou_resultado = "0" if context.chat_data["proxima_pergunta"] == 7 else context.chat_data["proxima_pergunta"]

    finalizar_ou_bora = "Finalizar" if context.chat_data["proxima_pergunta"] == 7 else "Borá pra próxima"

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
        Boa! Resposta correta!🎖
        """,
        parse_mode=ParseMode.HTML,
        reply_markup=teclado_com_opcoes
    )

    return TESTE if context.chat_data["proxima_pergunta"] < 7 else RESULTADO



def resultado(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    parabens = ""

    if query.data == '0' and context.chat_data["erro"] is False:
        context.chat_data["pontuacao"] += 1

    if context.chat_data["pontuacao"] == 6:
        parabens = """
Parabéns você acertou tudo! Continue assim e você irá longe 🏆
        """

    query.edit_message_text(
        text=f"""
Fim do questionário!
{parabens}
Você acertou: {context.chat_data["pontuacao"]} 🎯

<b>Se você está com sede de conhecimento, use o comando <u>/voltar</u> e retorne para o ínicio!</b>

        """,
        parse_mode=ParseMode.HTML,
    )

    return ConversationHandler.END
