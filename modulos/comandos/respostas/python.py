PYTHON = {
    "hello_world": 
        """
            print("Hello World")
            Pouco né ? É só isso mesmo!   
        """,
    "if/else":
        """
          Python não usa { } para separar os blocos de código, para separar corretamente é preciso identar
          corretamente as linhas seguindo os padrões da linguagem.
            if (expressão booleana):
                // bloco de código 1
            else:
                // bloco de código 2
        """,
    "variaveis":
        """
            Por convenção no Python a criação de variáveis é utilizando o snake case, onde todo o texto é
            em minúsculo e caso o nome da variável seja composto, os demais textos são separados por underline “_”
            numero = 1;
            nome = “Novato”;
            salario = 1235.5;
            maior_de_dade = True;
        """,
    "operadores_logicos":
        """
            Aqui no Python o negócio é um pouco diferente também, no lugar de usar && e || para E e OU,
            nós utilizamos “and”, “or” e também existe o “not” que é para o não lógico
            verdadeiro = True;
            falso = False;
            print(verdadeiro or falso); # True
            print(verdadeiro and falso); # False
            print(not verdadeiro);  # False
        """,
    "operadores_relacionais":
        """
            valorA = 1; # declaração de variável
            valorB = 2;
            valorA == valorB # igualdade
            valorA  != valorB # diferente
            valorA > valorB # maior
            valorA >= valorB # maior ou igual
            valorA < valorB # menor
            valorA <= valorB # menor ou igual
        """,
    "curiosidades":
        """
            A linguagem não recebeu esse nome por causa da espécie de serpente, mas sim do seriado de comédia
            da BBC Monty Python’s Flying Circus da qual Guido van Rossum, criador da linguagem, é um fã.
        """,
    "tipagem":
        """
            Não é possível fazer operações entre tipos diferentes sem antes fazer um cast ( transformação do tipo),
            por exemplo:

            nome = '11'
            print(1 + name)

            Retornará um erro.

            idade = 2; # números inteiros
            sobrenome = “Silva”; # texto
            letra_alfabeto = “a”; # texto
            peso = 70.5; # números com casas decimais
            estudante = True; # verdadeiro ou falso
        """,
    "operacoes_matematicas":
        """
            valorA = 4;
            valorB = 2;

            # adição
            valorA +  valorB = 6

            # subtração
            valorA -  valorB = 2

            # multiplicação
            valorA *  valorB = 8

            # divisão
            valorA  /  valorB = 2

            # resto da divisão
            valorA  %  valor B = 0
        """,
    "curso":
        """
            Essa dica é valiosa, se você curtiu o Python e deseja se tornar um PYTHONISTA raiz, segue um curso
            com muitaaaas aulas e uma excelente didatica:
            Curso inteiramente grátis e disponível na palma da sua mão. Acesse:
            https://youtube.com/playlist?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6
        """,
    "instalacao":
        """
            Caso tenha interesse em começar a escrever suas primeiras linhas de código em Python, segue um
            tutorial prático para instalação do Python: https://www.youtube.com/watch?v=VuKvR1J2LQE
            Obs: Para quem utiliza Linux o Python já vem instalado por padrão na maioria das suas distribuições.
        """
}