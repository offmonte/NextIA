# NEXTIA

## Descrição do Projeto

NEXTIA é um sistema de fidelidade integrado a um aplicativo móvel que permite aos clientes acumularem pontos com suas compras. Os pontos podem ser trocados por descontos e brindes, incentivando a lealdade dos clientes e aumentando o ticket médio das vendas. Este projeto inclui uma interface web construída com Streamlit, que se conecta a um banco de dados Azure SQL para gerenciar clientes e recompensas, além de visualizar os dados em gráficos.

## Solução Proposta

A solução é composta por duas tabelas principais:

1. **Clientes**: Armazena informações dos clientes, como CPF, nome e pontos acumulados.
2. **Recompensas**: Registra as recompensas disponíveis, com informações sobre o tipo de recompensa, descrição, data de resgate e o cliente que a resgatou.

### Estrutura do Banco de Dados

**Tabela: Clientes**

| Coluna     | Tipo de Dado   | Descrição                                  |
|------------|----------------|--------------------------------------------|
| id_cliente | INT            | Identificador único do cliente (chave primária, auto-incremento) |
| CPF        | NVARCHAR(11)   | Cadastro de Pessoa Física (único)         |
| nome       | NVARCHAR(100)  | Nome do cliente                            |
| pontos     | INT            | Pontos acumulados pelo cliente             |

**Tabela: Recompensas**

| Coluna            | Tipo de Dado   | Descrição                                  |
|-------------------|----------------|--------------------------------------------|
| id_recompensa     | INT            | Identificador único da recompensa (chave primária, auto-incremento) |
| tipo_recompensa   | NVARCHAR(50)   | Tipo da recompensa (ex: Desconto, Produto) |
| descricao         | NVARCHAR(255)  | Descrição da recompensa                    |
| data_resgate      | DATETIME       | Data em que a recompensa foi resgatada (pode ser NULL) |
| id_cliente        | INT            | Identificador do cliente que resgatou a recompensa (chave estrangeira) |

## Operações CRUD

A aplicação permite realizar as seguintes operações CRUD:

### 1. Criar (Create)

Para adicionar um novo cliente:

**Exemplo de Requisição (JSON)**:
```json
{
    "cpf": "12345678901",
    "nome": "Ana Silva",
    "pontos": 150
}
```
### 2. Ler (Read)
Para obter a lista de clientes:

**Exemplo de Resposta (JSON)**:
```
[
    {
        "id_cliente": 1,
        "cpf": "12345678901",
        "nome": "Ana Silva",
        "pontos": 150
    },
    {
        "id_cliente": 2,
        "cpf": "23456789012",
        "nome": "Carlos Pereira",
        "pontos": 200
    }
]
```

### 3. Atualizar (Update)
Para atualizar os dados de um cliente:

**Exemplo de Resposta (JSON)**:
```
{
    "id_cliente": 1,
    "cpf": "12345678901",
    "nome": "Ana Maria Silva",
    "pontos": 200
}
```

### 4. Deletar (Delete)
Para deletar um cliente pelo id_cliente:

**Exemplo de Resposta (JSON)**:

```
{
    "id_cliente": 1
}
```

## Como Executar

1. **Certifique-se de que o banco de dados Azure SQL está configurado corretamente.**
2. **Clone este repositório.**
3. **Instale as dependências necessárias:**

    ```bash
    pip install streamlit pyodbc pandas matplotlib
    ```

4. **Execute o aplicativo Streamlit:**

    ```bash
    streamlit run app.py
    ```

## Conclusão

NEXTIA é uma solução prática para gerenciar programas de fidelidade, oferecendo uma interface simples para a gestão de clientes e recompensas, além de facilitar a visualização de dados através de gráficos interativos. Contribuições são bem-vindas!

## Integrantes

Bianca Barreto - RM551848

Julia Akemi - RM98032

Lucas Monte - RM551604

Mateus Fattori - RM97904

Pedro Baraldi - RM98060

