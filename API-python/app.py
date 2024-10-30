import streamlit as st
from cruds import create_cliente, read_cliente, update_cliente, delete_cliente, create_recompensa, read_recompensa, update_recompensa, delete_recompensa

st.title("NextIA")

# Seleção de entidade
entidade = st.sidebar.selectbox("Selecione a Entidade", ["Clientes", "Recompensas"])

if entidade == "Clientes":
    opcao = st.sidebar.selectbox("Operação", ["Criar", "Ler", "Atualizar", "Deletar"])
    
    if opcao == "Criar":
        st.header("Adicionar Novo Cliente")
        cpf = st.text_input("CPF")
        nome = st.text_input("Nome")
        pontos = st.number_input("Pontos", min_value=0, step=1)
        if st.button("Criar Cliente"):
            create_cliente(cpf, nome, pontos)
    
    elif opcao == "Ler":
        st.header("Consultar Cliente")
        id_cliente = st.number_input("ID do Cliente", min_value=1, step=1)
        if st.button("Consultar"):
            cliente = read_cliente(id_cliente)
            st.write(cliente)
    
    elif opcao == "Atualizar":
        st.header("Atualizar Cliente")
        id_cliente = st.number_input("ID do Cliente", min_value=1, step=1)
        cpf = st.text_input("Novo CPF (opcional)")
        nome = st.text_input("Novo Nome (opcional)")
        pontos = st.number_input("Novos Pontos (opcional)", min_value=0, step=1)
        if st.button("Atualizar Cliente"):
            update_cliente(id_cliente, cpf, nome, pontos)
    
    elif opcao == "Deletar":
        st.header("Remover Cliente")
        id_cliente = st.number_input("ID do Cliente", min_value=1, step=1)
        if st.button("Deletar Cliente"):
            delete_cliente(id_cliente)

elif entidade == "Recompensas":
    opcao = st.sidebar.selectbox("Operação", ["Criar", "Ler", "Atualizar", "Deletar"])

    if opcao == "Criar":
        st.header("Adicionar Nova Recompensa")
        tipo_recompensa = st.text_input("Tipo de Recompensa")
        descricao = st.text_input("Descrição")
        data_resgate = st.date_input("Data de Resgate")
        id_cliente = st.number_input("ID do Cliente", min_value=1, step=1)
        if st.button("Criar Recompensa"):
            create_recompensa(tipo_recompensa, descricao, data_resgate, id_cliente)
    
    elif opcao == "Ler":
        st.header("Consultar Recompensa")
        id_recompensa = st.number_input("ID da Recompensa", min_value=1, step=1)
        if st.button("Consultar"):
            recompensa = read_recompensa(id_recompensa)
            st.write(recompensa)
    
    elif opcao == "Atualizar":
        st.header("Atualizar Recompensa")
        id_recompensa = st.number_input("ID da Recompensa", min_value=1, step=1)
        tipo_recompensa = st.text_input("Novo Tipo de Recompensa (opcional)")
        descricao = st.text_input("Nova Descrição (opcional)")
        data_resgate = st.date_input("Nova Data de Resgate (opcional)")
        id_cliente = st.number_input("Novo ID do Cliente (opcional)", min_value=1, step=1)
        if st.button("Atualizar Recompensa"):
            update_recompensa(id_recompensa, tipo_recompensa, descricao, data_resgate, id_cliente)
    
    elif opcao == "Deletar":
        st.header("Remover Recompensa")
        id_recompensa = st.number_input("ID da Recompensa", min_value=1, step=1)
        if st.button("Deletar Recompensa"):
            delete_recompensa(id_recompensa)
