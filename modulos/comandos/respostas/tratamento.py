from typing import Dict
from modulos.comandos.respostas.aprendizagem.explicacoes import EXPLICACOES
from modulos.comandos.respostas.aprendizagem.python import PYTHON
from modulos.comandos.respostas.aprendizagem.java import JAVA
from modulos.comandos.respostas.aprendizagem.javascript import JAVASCRIPT


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
