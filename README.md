# Documentação da API do Jogo Double da Blaze

## Introdução

Esta API permite integrar aplicações externas com o jogo Double da Blaze, uma plataforma de apostas online. Através desta API, é possível realizar login, obter informações da conta do usuário, consultar o saldo da carteira, histórico de apostas e muito mais.

## Autenticação

Para utilizar a API, é necessário realizar um processo de autenticação. Cada usuário possui um `user-x-pswd` único, que deve ser fornecido no cabeçalho de cada requisição. Esse `user-x-pswd` é utilizado para validar a autorização do usuário.

Após fornecer o `user-x-pswd` válido, a API retornará um `access_token` que deve ser utilizado em requisições subsequentes para acessar informações e realizar ações em nome do usuário.

## Obtendo o Access Token

Para obter o `access_token`, faça uma requisição do tipo `POST` para o endpoint `/login`, passando as credenciais do usuário no corpo da requisição:

```http
POST /login
Headers:
  user-x-pswd: <seu_user-x-pswd>
Body:
  {
    "username": "<seu_email>",
    "password": "<sua_senha>"
  }
```

A resposta bem-sucedida conterá o `access_token` no seguinte formato:

```json
{
  "access_token": "<seu_access_token>"
}
```

Copie esse `access_token` e utilize-o no cabeçalho `Authorization` de todas as requisições subsequentes.

## Endpoints

| Endpoint      | Método | Descrição                                                       |
|---------------|--------|-----------------------------------------------------------------|
| `/login`      | `POST`   | Obtém o `access_token` a partir das credenciais do usuário.     |
| `/me`         | `GET`    | Retorna informações sobre a conta do usuário.                   |
| `/wallet`     | `GET`    | Retorna o saldo atual da carteira do usuário.                   |
| `/xp`         | `GET`    | Retorna o nível de experiência do usuário.                      |
| `/recent`     | `GET`    | Retorna o histórico recente de apostas do usuário.              |
| `/current`    | `GET`    | Retorna informações sobre a partida atual.                      |
| `/bet`        | `POST`   | Permite que o usuário realize uma aposta no jogo Double.        |
| `/result`     | `GET`    | Retorna o resultado da última aposta realizada.                 |
| `/bet_result` | `POST` | Permite que o usuário realize uma aposta e aguarde o resultado. |

## Obter Informações da Conta

Endpoint: `GET /me`

```http
Headers:
Authorization: <seu_access_token>
user-x-pswd: <seu_user-x-pswd>
```
Esse endpoint retorna informações sobre a conta do usuário, como username, ID, nível de experiência, etc.

## Consultar Saldo da Carteira

Endpoint: `GET /wallet`

```http
Headers:
Authorization: <seu_access_token>
user-x-pswd: <seu_user-x-pswd>
```

Este endpoint retorna o saldo atual da carteira do usuário.

## Consultar Nível de Experiência

`Endpoint: GET /xp`

```http
Headers:
Authorization: <seu_access_token>
user-x-pswd: <seu_user-x-pswd>
```

Este endpoint retorna o nível de experiência do usuário.

## Consultar Histórico de Apostas

`Endpoint: GET /recent`

```http
Headers:
Authorization: Bearer <seu_access_token>
user-x-pswd: <seu_user-x-pswd>
```

Este endpoint retorna o histórico recente de apostas do usuário.

## Consultar Informações da Partida Atual

`Endpoint: GET /current`

```http
Headers:
Authorization
user-x-pswd: <seu_user-x-pswd>
```

Este endpoint retorna informações sobre a partida atual, como o valor do prêmio, o multiplicador atual, etc.

## Realizar uma Aposta

`Endpoint: POST /bet`

```http
Headers:
Authorization: <seu_access_token>
user-x-pswd: <seu_user-x-pswd>
Body:
{
  "amount": <valor_da_aposta>,
  "color": "<cor_da_aposta>"
}
```

Este endpoint permite que o usuário realize uma aposta no jogo Double. O valor da aposta deve ser um número inteiro ou flutuante e a cor da aposta deve ser 1 para "red", 2 para "black" ou 0 para "white".

## Consultar Resultado da Última Aposta

`Endpoint: GET /result`

```http
Headers:
Authorization: <seu_access_token>
user-x-pswd: <seu_user-x-pswd>
```

Este endpoint retorna o resultado da última aposta realizada pelo usuário.

## Realizar uma Aposta e espera o resultado

`Endpoint: POST /bet_result`

```http
Headers:
Authorization: <seu_access_token>
user-x-pswd: <seu_user-x-pswd>
Body:
{
  "amount": <valor_da_aposta>,
  "color": "<cor_da_aposta>"
}
```

Esse endpoint permite que o usuário realize uma aposta e aguarde o resultado. O valor da aposta deve ser um número inteiro ou flutuante e a cor da aposta deve ser 1 para "red", 2 para "black" ou 0 para "white".

## Considerações de Segurança

- Mantenha seu `user-x-pswd` e `access_token` seguros e não os compartilhe com ninguém.

## Suporte e Contato
Para obter suporte ou reportar problemas, entre em contato por e-mail: batista.marcelo34@gmail.com