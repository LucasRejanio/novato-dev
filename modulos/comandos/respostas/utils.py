from typing import Dict
from modulos.comandos.respostas.aprendizagem.explicacoes import EXPLICACOES
from modulos.comandos.respostas.aprendizagem.python import PYTHON
from modulos.comandos.respostas.aprendizagem.java import JAVA
from modulos.comandos.respostas.aprendizagem.javascript import JAVASCRIPT


TOPICOS_PARA_USUARIO = {
    "hello_world": "Hello World",
    "if_else": "If/Else",
    "variaveis": "Váriaveis",
    "operadores_logicos": "Operadores Lógicos",
    "operadores_relacionais": "Operadores Relacionais",
    "tipagem": "Tipagem",
    "operacoes_matematicas": "Operações Matemáticas",
    "curso": "Curso",
    "instalacao": "Instalação",
    "curiosidade": "Curiosidade",
}


def filtra_resposta(linguagem: str, conteudo: str) -> Dict[str, str]:
    resposta = {
        "explicacao": "",
        "exemplo": "",
    }

    if linguagem == "python":
        resposta = monta_resposta(PYTHON, conteudo)

    elif linguagem == "java":
        resposta = monta_resposta(JAVA, conteudo)

    elif linguagem == "javascript":
        resposta = monta_resposta(JAVASCRIPT, conteudo)

    return resposta


def monta_resposta(linguagem: Dict[str, str], conteudo: str) -> Dict[str, str]:

    resposta = {
        "explicacao": EXPLICACOES[conteudo],
        "exemplo": linguagem[conteudo],
    }

    return resposta
