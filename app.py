import streamlit as st
import pyodbc
import pandas as pd
import matplotlib.pyplot as plt

# Configurações de conexão
server = 'oracle.fiap.com.br'
database = 'SEU_BANCO_DE_DADOS'
username = 'RM551604'
password = '121102'
driver = '{ODBC Driver 17 for SQL Server}'

# Conexão ao banco de dados
def create_connection():
    conn = pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}')
    return conn

conn = create_connection()

#=========================================

# Função para ler dados de Clientes
def read_clients():
    query = "SELECT * FROM Clientes"
    return pd.read_sql(query, conn)

# Função para criar um novo cliente
def create_client(cpf, nome, pontos):
    query = f"INSERT INTO Clientes (CPF, nome, pontos) VALUES ('{cpf}', '{nome}', {pontos})"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

# Função para atualizar um cliente
def update_client(id_cliente, cpf, nome, pontos):
    query = f"UPDATE Clientes SET CPF = '{cpf}', nome = '{nome}', pontos = {pontos} WHERE id_cliente = {id_cliente}"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

# Função para deletar um cliente
def delete_client(id_cliente):
    query = f"DELETE FROM Clientes WHERE id_cliente = {id_cliente}"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

#=================================


# Função para plotar gráfico de pontos dos clientes
def plot_client_points():
    df = read_clients()
    plt.figure(figsize=(10, 6))
    plt.bar(df['nome'], df['pontos'], color='skyblue')
    plt.xlabel('Clientes')
    plt.ylabel('Pontos')
    plt.title('Pontos dos Clientes')
    st.pyplot(plt)


#===============================

st.title("Sistema de Fidelidade - NEXTIA")

# Formulário para criação de cliente
with st.form("add_client"):
    st.subheader("Adicionar Cliente")
    cpf = st.text_input("CPF")
    nome = st.text_input("Nome")
    pontos = st.number_input("Pontos", min_value=0)
    submitted = st.form_submit_button("Adicionar Cliente")
    if submitted:
        create_client(cpf, nome, pontos)
        st.success("Cliente adicionado com sucesso!")

# Exibir clientes
st.subheader("Clientes Cadastrados")
clients_df = read_clients()
st.dataframe(clients_df)

# Plotar gráfico de pontos dos clientes
st.subheader("Gráfico de Pontos dos Clientes")
plot_client_points()

# Funções para atualizar e deletar clientes
st.subheader("Atualizar ou Deletar Cliente")
client_id = st.number_input("ID do Cliente", min_value=1)
if st.button("Deletar Cliente"):
    delete_client(client_id)
    st.success("Cliente deletado com sucesso!")

# Formulário para atualização
with st.form("update_client"):
    st.subheader("Atualizar Cliente")
    cpf_update = st.text_input("Novo CPF")
    nome_update = st.text_input("Novo Nome")
    pontos_update = st.number_input("Novos Pontos", min_value=0)
    update_submitted = st.form_submit_button("Atualizar Cliente")
    if update_submitted:
        update_client(client_id, cpf_update, nome_update, pontos_update)
        st.success("Cliente atualizado com sucesso!")
