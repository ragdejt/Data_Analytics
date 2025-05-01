import streamlit
from sql.base import add_fornecedores
from functions.streamlit import streamlit_page
from utils.constants import *
fornecedores = streamlit_page(
    titulo_da_pagina="Fornecedores"
)

match fornecedores:
    case "Adicionar":
        name = streamlit.text_input(label="Nome do fornecedor", placeholder="Digite o nome fantasia")
        address = streamlit.text_input(label="Endereço", placeholder="Digite o endereço")
        cnpj = streamlit.text_input(label="CNPJ", placeholder="Digite o CNPJ")
        selected_state = streamlit.selectbox(label="Estado", options=STATES_CITIES.keys())
        city = streamlit.selectbox(label="Cidade", options=STATES_CITIES[selected_state])
        cep = streamlit.text_input(label="CEP", placeholder="Digite o CEP")
        phone =streamlit.text_input(label="Telefone", placeholder="Digite o telefone")
        email = streamlit.text_input(label="Email", placeholder="Digite o email")
        representante = streamlit.text_input(label="Representante", placeholder="Digite o nome do representante")
        bank = streamlit.selectbox(label="Banco", options=BANK)
        agency = streamlit.text_input(label="Agência", placeholder="Digite o numero da agencia")
        account = streamlit.text_input(label="Conta", placeholder="Digite o numero da conta")

        if streamlit.button("Adicionar"):
            add_fornecedores(
                NOME=name,
                ENDEREÇO=address,
                CNPJ=cnpj,
                ESTADO=selected_state,
                CIDADE=city,
                CEP=cep,
                TELEFONE=phone,
                EMAIL=email,
                REPRESENTANTE=representante,
                BANCO=bank,
                AGENCIA=agency,
                CONTA=account
            )
    case "Remover":
        pass