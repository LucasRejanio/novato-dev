from typing import Dict
from modulos.comandos.respostas.aprendizagem.explicacoes import EXPLICACOES
from modulos.comandos.respostas.aprendizagem.python import PYTHON
from modulos.comandos.respostas.aprendizagem.java import JAVA
from modulos.comandos.respostas.aprendizagem.javascript import JAVASCRIPT


TOPICOS_PARA_USUARIO = {
    "hello_world": "<u><b>Hello World</b></u>",
    "if_else": "<u><b>If/Else</b></u>",
    "variaveis": "<u><b>Variáveis</b></u>",
    "operadores_logicos": "<u><b>Operadores Lógicos</b></u>",
    "operadores_relacionais": "<u><b>Operadores Relacionais</b></u>",
    "tipagem": "<u><b>Tipagem</b></u>",
    "operacoes_matematicas": "<u><b>Operações Matemáticas</b></u>",
    "curso": "<u><b>Curso</b></u>",
    "instalacao": "<u><b>Instalação</b></u>",
    "curiosidade": "<u><b>Curiosidade</b></u>",
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
