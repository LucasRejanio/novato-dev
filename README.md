<img alt="Telegram" src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" /> <img alt="GitHub Actions" src="https://img.shields.io/badge/github%20actions%20-%232671E5.svg?&style=for-the-badge&logo=github%20actions&logoColor=white"/> <img alt="Python" src="https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white"/> 

[![build](https://img.shields.io/wercker/build/wercker/go-wercker-api.svg)](https://github.com/LucasRejanio/chatbot-telegram/actions)

![banner_novatodev](https://user-images.githubusercontent.com/52427398/116485616-093a2900-a862-11eb-99fe-d6fee3eaadb1.png)

# @NovatoDev

O `@NovatoDev` é um bot no Telegram que tem como objetivo auxiliar alunos iniciantes em programação. Nossa missão é orientar os primeiros passos dos nossos usuários nesse maravilhoso universo. Aqui, esclarecemos conceitos básicos como: preparação de ambiente (instalação), tipagem, operadores, variáveis, IF/ELSE e etc. Mediante a dúvida, retornamos a explicação, exemplos, cursos e a aplicação completa.

## Sumário

- [Processo](#processo)
- [Desenvolvimento](#desenvolvimento)
- [Infraestrutura](#infraestrutura)

### Processo

A imagem abaixo descreve visualmente o processo da conversa. Desde da saudação do bot (Início), passando pelas opções de conteúdo e por fim, apresentando a escolha do usuário em finalizar a conversa ou retorno ao início. Esse processo tem como objetivo facilitar o entendimento acerca do funcionamento do `@NovatoDev` e mapear as saídas e opções à disposição do usuário final.

![processo](https://user-images.githubusercontent.com/52427398/116485787-76e65500-a862-11eb-9c81-a48f19b14966.png)

### Desenvolvimento
[Em construção]

### Infraestrutura

Nossa infraestrutura procura utilizar as melhores práticas DevOps. Com conceitos e processos bem aplicados em pipelines, testes automatizados, gerenciamento de confiabilidade e deploys automáticos.

- [Fluxograma](#fluxograma)
- [Notificação](#notificação)
- [Deploy](#deploy)

##### Fluxograma

No modelo abaixo é possível visualizar todo nosso processo de integração contínua. Utilizamos ferramentas e configurações do próprio github para nos auxiliar e deixar nosso projeto muito mais automatizado, prevenindo assim, erros manuais. Além é claro do aumento da produtividade operacional.

![infraestrutura](https://user-images.githubusercontent.com/52427398/116484557-b1022780-a85f-11eb-8f4c-ab042bf0d329.png)

##### Notificação

Criamos processos para automatizar e alertar nosso time sobre movimentações no repositório do código fonte. Utilizando a ferramenta Github Actions montamos um fluxo para alertar o time sobre novos pull requests e releases.

Aplicação:

![telegramNotifications](https://user-images.githubusercontent.com/52427398/116475257-f7e82100-a84f-11eb-8b85-41b83d910498.png)

##### Deploy

Realizar um deploy no Heroku é simples e tranquilo de se fazer. Exatamente por isso que decidimos automatizar esse processo junto com o lançamento de release. Basicamente utilizamos a actions oficial do Heroku, junto com as boas práticas de segurança do github para aplicar esse modelo.

- Actions: https://github.com/marketplace/actions/deploy-to-heroku

##### Aplicação:  

```yml
    - name: Deploy from Heroku
      uses: akhileshns/heroku-deploy@v3.12.12
      with:
        heroku_api_key: ${{secrets.HEROKU_API_KEY}}
        heroku_app_name: "novato-dev"
        heroku_email: ${{secrets.HEROKU_EMAIL}}
        remote_branch: "main"
      if: env.PR_RELEASE_LABEL > 0
```
