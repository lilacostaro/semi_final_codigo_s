
# Desafio SEMIFINAL /código[s] 

Este projeto foi desenvolvido a partir do desafio proposto [neste documento](), 
para a semi-final da primeira edição do bootcamp Código[s], uma parceria da [Stone]()
e a [How Bootcamps](). 



## Referência e Bibliotecas

 - [Python](https://www.python.org/)
 - [Django](https://www.djangoproject.com/)
 - [Django REST framework](https://www.django-rest-framework.org/)
 - [Djoser](https://djoser.readthedocs.io/en/latest/getting_started.html)
 - [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/index.html)
 - [python-decouple](https://github.com/henriquebastos/python-decouple/)
 - [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/index.html)
## Descrição do projeto

O projeto foi escrito em Python utilizando as bibliotecas Django e Django Rest Framework
com a intenção de simular um banco digital onde on clientes possam abrir contas.
Fazer depositos, saques e transferencias. O usário tambem deve ser capaz de consultar o seu saldo, 
e listar toda a movimentação na sua conta.

## Estrutura

Foi criado um Django Project chamado "banco_stone", e dentro dele os seguintes apps:

- Account_holders - Este app é responsavel por:
    - Subscrever a classe de Usuarios nativa do Django, para que os campos de cadastro do cliente podessem ser remodelados. Os campos definidos foram:
        - email
        - first_name
        - last_name
        - account_type (pessoa fisica ou pessoa juridica)
        - cpf_cnpj
        - is_staff
        - is_active
        - date_joined

- Accounts - Este app é utilizado para as ações envolvendo a conta bancaria do usuario:
    - Criar uma nova conta, uma vez registrado, o cliente precisa fornecer uma token de 4 digitos que sera usado para validação das transações realizadas, a partir disso as informações da conta bancaria são geradas nesse passo. Elas são:
        - client_id 
        - agency 
        - account_number 
        - balance 
        - token 
        - is_active 
        - created_at 
        - updated_at
    - Listar as informações da conta bancaria
    
- Authentication - Este app fica responsavel pela parte de autenticação do usuario. Contem a URL de Registro de usuario e as URLs para gerar e atualizar o token de segurança.
- Transactions - Este app é responsavel pelas transações bancarias. A partir dele voce pode:
    - Realizar depositos na sua conta.
    - Realizar saque na sua conta.
    - Realizar transferencias da sua conta para outra.
    - Listar toda a movimentação na sua conta.
    - A tabela para este banco de dados contem os campos:
        - user_id
        - account_number 
        - value 
        - transaction_type 
        - created_at 


## Instalação

- Faça o clone do projeto usando o comando

```bash
  git clone https://github.com/lilacostaro/
```
- Crie uma ambiente virtual usando venv
```bash
  python3 -m venv /path/to/new/virtual/environment

```
- Ative o seu ambiente virtual, o comando varia de acordo com o seu OS

```bash
POSIX

bash/zsh
$ source <venv>/bin/activate

fish

$ source <venv>/bin/activate.fish

csh/tcsh

$ source <venv>/bin/activate.csh

PowerShell Core

$ <venv>/bin/Activate.ps1

Windows

cmd.exe

C:\> <venv>\Scripts\activate.bat

PowerShell

PS C:\> <venv>\Scripts\Activate.ps1
```
- Instale as dependencias do projeto
```bash
 pip install -r requirements.txt
```
- Migre as tabelas do database
```bash
   python manage.py migrate
```
Inicie o servidor
```bash
   python manage.py runserver
```

## Documentação

Uma vez que os projeto esteja rodando, a documentação completa pode ser encontrada nos links abaixo.
- [redoc](http://127.0.0.1:8000/redoc/)
- [docs](http://127.0.0.1:8000/docs/)


## Autora

- [@lilacostaro](https://www.github.com/lilacostaro)

