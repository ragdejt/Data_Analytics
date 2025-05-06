import streamlit
from src.utils.constants import *
from functions.streamlit import streamlit_page
from sql.base import add_funcionario

funcionarios = streamlit_page(
    titulo_da_pagina="Funcionarios"
)

match funcionarios:
    case "Adicionar":
        name = streamlit.text_input(
            label="Nome.",
            placeholder="Digite o nome."
        )
        address = streamlit.text_input(
            label="Endereço",
            placeholder="Digite o endereço"
        )
        birthday = streamlit.date_input(
            label="Data de nascimento.",
            format="DD/MM/YYYY"
        )
        gender = streamlit.selectbox(
            label="Gênero.",
            index=None,
            placeholder="Selecione o gênero.",
            options=["Masculino", "Feminino"]
        )
        nationality = streamlit.selectbox(
            label="Nacionalidade.",
            index=None,
            placeholder="Selecione a nacionalidade.",
            options=NATIONALITY
        )
        status = streamlit.selectbox(
            label="Estado Civil.",
            index=None,
            placeholder="Selecione o estado civil.",
            options=["Casado", "Solteiro"]
        )
        rg = streamlit.text_input(
            label="RG.",
            placeholder="Digite o RG."
        )
        cpf = streamlit.text_input(
            label="CPF.",
            placeholder="Digite o CPF."
        )
        cnh = streamlit.text_input(
            label="CNH.",
            placeholder="Digite a CNH."
        )
        phone = streamlit.text_input(
            label="Telefone.",
            placeholder="Digite o telefone."
        )
        email = streamlit.text_input(
            label="E-mail.",
            placeholder="Digite o email."
        )
        position = streamlit.selectbox(
            label="Cargo.",
            index=None,
            placeholder="Selecione o cargo.",
            options=POSITION
        )
        contract = streamlit.selectbox(
            label="Contrato.",
            index=None,
            placeholder="Selecione o tipo de contrato.",
            options=["CLT", "PJ"]
        )
        salary = streamlit.slider(
            label="Salario.",
            min_value=1550,
            max_value=10000
        )
        bank = streamlit.selectbox(
            label="Banco.",
            index=None,
            placeholder="Selecione o banco.",
            options=BANK
        )
        agency = streamlit.text_input(
            label="Agência.",
            placeholder="Digite a agência."
        )
        account = streamlit.text_input(
            label="Conta.",
            placeholder="Digite a conta."
        )
        admission = streamlit.date_input(
            label="Data de admissão.",
            format="DD/MM/YYYY"

        )

        if streamlit.button(label="Adicionar", use_container_width=True):
            add_funcionario(
                nome=name,
                endereco=address,
                nascimento=birthday,
                genero=gender,
                nacionalidade=nationality,
                estado_civil=status,
                rg=rg,
                cpf=cpf,
                cnh=cnh,
                telefone=phone,
                email=email,
                cargo=position,
                contrato=contract,
                salario=salary,
                banco=bank,
                agencia=agency,
                conta=account,
                admissao=admission
            )
    case "Remover":
        pass