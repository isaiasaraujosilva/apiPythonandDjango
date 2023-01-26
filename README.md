# apiPythonandDjango

# Sobre

Projeto desenvolvido para o processo seletivo da Fabrica de Genio. Vaga desenvolvedor Backend Python 

## Desafio
  Desafio - Desenvolvedor Python e Django
  Coordenador: Artur Felipe da Silva Veloso

  Você será o programador back-end de um sistema de pedidos, este sistema será feito por
  um front-end e um back-end, onde o front-end vai desenvolver as telas em um framework
  front-end como (react ou vue) e vai consumir os dados de sua API, que será desenvolvida
  em Python e Django Rest Framework.

## Pré-requisitos.
    * Python 3.10
    * Django 
    * Rest_framework
    * Mysql
    * mysqlcliente
## Instalações

### python no windows 
Instalando o Python 3 no Windows
Para instalar o Python no seu sistema operacional Windows, você precisa baixar o instalador. 

Acesse o site oficial neste link http://python.org.br/instalacao-windows/

### python no ubuntu

Apt-get

Para instalar o Python 3, digite em um terminal:

      sudo apt-get install python3

(Opcional) Para instalar o gerenciador de pacotes pip, digite em um terminal:
      
      sudo apt-get install python3-pip

### django:

  O Django pode ser facilmente instalado dentro de seu ambiente virtual usando o pip.
    Na linha de comando, assegure-se que seu ambiente virtual esteja ativo, e execute o seguinte comando.
    
    pip install django
### Rest_framework pip install rest_framework
        
    Instale usando pip, incluindo quaisquer pacotes opcionais que você deseja...
    
    pip install djangorestframework
    pip install markdown    
    pip install django-filter
    
### Mysql server no Windows atraves do XAMPP
  
  * O XAMPP é uma distribuição do Apache fácil de instalar contendo PHP, MySQL e Perl. Basta fazer o download e iniciar o instalador. É simples assim!
  
  * utilize algum cliente Mysql da sua preferencia para criar o banco "api"
  
  * CREATE DATABASE api;
  
### Mysql server no Ubuntu
    
### Instalando o MySQL
No Ubuntu 20.04, você pode instalar o MySQL usando o repositório de pacotes APT. No momento da redação deste artigo, a versão do MySQL disponível no                   repositório padrão do Ubuntu é a versão 8.0.27.

    1. sudo apt update
    2. sudo apt install mysql-server
    3. sudo systemctl start mysql.service

### Configurando o MySQL
  
    1. sudo mysql
    2. ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '';
    3. exit
### drive python-mysql Mysqlcliente

    pip install mysqlcliente
