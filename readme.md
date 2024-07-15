# AV2 - Projeto de Programação Funcional

Este projeto, intitulado `AV2_JoaoMoreira`, foi desenvolvido para a avaliação AV2 de Programação Funcional na Unifor - Universidade de Fortaleza. Ele explora conceitos avançados de programação funcional, operações com banco de dados MySQL e o desenvolvimento de uma aplicação Flask como um servidor para consultas SQL seguras.

## Estrutura do Projeto

O projeto é composto por módulos Python correspondentes a cada questão da avaliação, seguindo as regras estabelecidas para a utilização da programação funcional e a implementação segura de um servidor Flask para interações com banco de dados.

- `q1_JoaoMoreira.py`: Implementa o diagrama de atividades proposto.
- `q2_JoaoMoreira.py`: Contém testes unitários e de stress para o programa desenvolvido na questão 1.
- `q3_JoaoMoreira.py`: Realiza a integração com um banco de dados MySQL, manipulando as tabelas USERS, VIDEOGAMES, GAMES, e COMPANY.
- `q4_JoaoMoreira.py`: Fornece um Scaffold para facilitar a escrita de consultas SQL complexas envolvendo as tabelas mencionadas.
- `q5_JoaoMoreira.py`: Adapta um dos programas anteriores para funcionar como uma aplicação de servidor Flask, com foco em disponibilidade e segurança.

## Tecnologias Utilizadas

- Python 3
- Flask
- MySQL
- Flask-HTTPAuth para autenticação
- Flask-Bcrypt para hash de senhas
- Outras bibliotecas Python conforme necessário

## Configuração e Execução

### Configuração do Ambiente

1. Certifique-se de ter Python 3 e pip instalados no seu ambiente de desenvolvimento.
2. Instale as dependências necessárias usando pip:
   ```bash
   pip install flask mysql-connector-python flask-httpauth flask-bcrypt
