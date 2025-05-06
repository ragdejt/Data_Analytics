import streamlit
from src.utils.constants import *
from functions.streamlit import streamlit_page
clientes = streamlit_page(
    titulo_da_pagina="Clientes"
)
match clientes:
    case "Adicionar":
        nome = streamlit.text_input(label="Nome", placeholder="Digite o nome do cliente")
        cpf = streamlit.text_input(label="CPF", placeholder="Digite o CPF do cliente")
        cnpj = streamlit.text_input(label="CNPJ", placeholder="Digite o CNPJ do cliente")
        endereco = streamlit.text_input(label="Endereço", placeholder="Digite o endereço do cliente")
        estado = streamlit.selectbox(label="Estado", options=STATES_CITIES)
        cidade = streamlit.selectbox(label="Cidade", options=STATES_CITIES[estado])
        telefone = streamlit.text_input(label="Telefone", placeholder="Digite o telefone do cliente")
        email = streamlit.text_input(label="E-mail", placeholder="Digite o e-mail do cliente")
        if streamlit.button("Adicionar novo cliente", icon=":material/person_add:",use_container_width=True):
            pass
    case "Remover":
        pass
    case "Editar":
        pass
