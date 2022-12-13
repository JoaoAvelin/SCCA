# SCCA - Sistema de Cálculo e Cobrança Administrativa

## Este projeto visá o cálculo e geração automático das GPS(Guia da Previdência Social) com o juros da taxa selic.

:notebook:
Tabela de conteúdos 
=================
<!--ts-->
   * [Sobre](#Sobre)
   * [Pré-Requisitos](#Pré-Requisitos) 
   * [Instalação](#Instalação) 
   * [Funções do código](#Funções-do-código)
   * [Tecnologias](#Tecnologias)
   * [Autor](#Autor)
<!--te-->

# Sobre
:open_book:
Foi desenvolvido para agilizar e facilitar a geração e o cálculo das GPS, que antes era gerada uma por uma através do LibreOffice oque causava transtornos e muita demora.

# Pré-Requisitos 
:bookmark_tabs:
Antes de começar a instalação desse codígo você precisa ter em sua maquina o [Python](https://www.python.org/downloads/release/python-386/) na versão 3.8.6,
e para o armazenamento dos dados o [XAMPP](https://www.apachefriends.org/pt_br/download.html).

# Instalação
:inbox_tray:
Para instação desse código primeiro clone o git utilizando 

$ git clone <https://github.com/JoaoAvelin/SCCA>

Após isso no diretório que foi clonado você encontrará um arquivo SQL chamado controle_teste, você devera ligar o XAMPP habilitar o APACHE e o MySQL,
depois você vai criar uma base de dados chamado controle_teste com agrupamento (utf8mb4_general_ci), e importar o controle_teste que se encontra
na pasta clonada, deve ser criado uma matricula e uma senha dentro o localhost.

# Funções-do-código
:gear:
- [x] Cadastro de matricula.
- [x] Cadastro de beneficio.
- [x] Cadastro de edição de beneficio.
- [x] Exclusão de dados.
- [x] Geração de PDFS.

# Tecnologias
:hammer_and_wrench:
- [Python](https://www.python.org/downloads/release/python-386/)
- [Xampp](https://www.apachefriends.org/pt_br/download.html)
- [QtDesigner](https://build-system.fman.io/qt-designer-download)

# Autor
:pencil2:
João Vitor Avelino Geraldo :rocket:

Feito por João Vitor Avelino :dart: Entre em contato :wave:

- Email: joao.avelino2002@gmail.com
- Linkedin: [João Vitor Avelino Geraldo](https://www.linkedin.com/in/jo%C3%A3o-vitor-avelino-geraldo-8ba247160)
