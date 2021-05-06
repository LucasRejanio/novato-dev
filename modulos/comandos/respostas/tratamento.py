from typing import Dict, List, Union
from modulos.comandos.respostas.python import PYTHON
from modulos.comandos.respostas.java import JAVA
from modulos.comandos.respostas.javascript import JAVASCRIPT


def filtra_resposta(linguagem: str, conteudo: str) -> Dict[str, str]:
    resposta = {
        "explicacao": "",
        "exemplo": "",
    }

    if linguagem == "python":
        resposta = monta_resposta(resposta, conteudo_linguagem=PYTHON[conteudo])

    if linguagem == "java":
        resposta = monta_resposta(resposta, conteudo_linguagem=JAVA[conteudo])

    if linguagem == "javascript":
        resposta = monta_resposta(resposta, conteudo_linguagem=JAVASCRIPT[conteudo])

    return resposta


def monta_resposta(resposta: Dict[str, str], conteudo_linguagem: Union[List[str], str]) -> Dict[str, str]:

    if isinstance(conteudo_linguagem, str):
        resposta = {
            "explicacao": conteudo_linguagem
        }
    else: 
        resposta["explicacao"] = conteudo_linguagem[0]
        resposta["exemplo"] = conteudo_linguagem[1]

    return resposta
