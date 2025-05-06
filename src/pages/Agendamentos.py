import streamlit
from functions.streamlit import streamlit_page
from sql.base import add_agendamento, get_suppliers_id, session, Agendamentos
from src.utils.constants import *
agendamentos = streamlit_page(
    titulo_da_pagina="Agendamentos",
    icone_da_pagina=":material/calendar_month:"
)

match agendamentos:
    case "Adicionar":
        status = streamlit.selectbox(
            label="Status do agendamento",
            options=APPOINTMENT_STATUS
        )

        fornecedor = streamlit.selectbox(
            label="Fornecedor",
            options=get_suppliers_id()
        )

        tipo_carga = streamlit.selectbox(
            label="Tipo de carga",
            options=CARGO_TYPE
        )

        date = streamlit.date_input(label="Data do agendamento", format="DD/MM/YYYY")

        start_time = streamlit.time_input(label="Hora de chegada")

        finish_time = streamlit.time_input(label="Hora de saida")

        if streamlit.button(label="Adicionar novo agendamento", icon=":material/calendar_add_on:", use_container_width=True):
            add_agendamento(
                status=status,
                fornecedor=fornecedor,
                tipo=tipo_carga,
                data=str(date),
                chegada=str(start_time),
                saida=str(finish_time)
            )
            
            streamlit.toast("Agendamento adicionado com sucesso!")
            streamlit.success("Agendamento adicionado com sucesso!")
    case "Remover":
        identificacao = streamlit.text_input(
        label="ID",
        placeholder="Digite o ID")
        if streamlit.button(label="Procurar agendamento",icon=":material/search:", use_container_width=True):
            query = session.query(Agendamentos.id).filter_by(id=identificacao).first()
            if query:
                streamlit.success("Agendamento encontrado!")              
            else:
                streamlit.error("Agendamento não encontrado!")
        if streamlit.button("Remover agendamento", icon=":material/event_busy:", use_container_width=True):
            query = session.query(Agendamentos).get(identificacao)
            session.delete(query)
            session.commit()
            streamlit.success("Agendamento removido!")              
    case "Editar":
        identificacao = streamlit.text_input(
            label="ID",
            placeholder="Digite o ID")

        if streamlit.button(label="Procurar", icon=":material/search:", use_container_width=True):
            query = session.query(Agendamentos.id).filter_by(id=identificacao).first()
            if query:
                streamlit.success("Agendamento encontrado!")              
            else:
                streamlit.error("Agendamento não encontrado!")

        try:
            status_selected = streamlit.selectbox(label="Status",options=APPOINTMENT_STATUS, index=None, placeholder=SCRIPT_NAME)
            
            selected_cargo = streamlit.selectbox(
                label="Tipo de carga",
                options=CARGO_TYPE,
                index=None,
                placeholder=SCRIPT_NAME
            )

            date_selected = str(streamlit.date_input(label="Data do agendamento", format="DD/MM/YYYY"))

            start_time_selected = str(streamlit.time_input(label="Hora de chegada"))

            finish_time_selected = str(streamlit.time_input(label="Hora de saida"))

            if streamlit.button("Salvar", icon=":material/edit_calendar:", use_container_width=True):
                session.query(Agendamentos).filter_by(id=identificacao).update(
                    {"status":status_selected,
                    "tipo":selected_cargo,
                    "data":date_selected,
                    "chegada":start_time_selected,
                    "saida":finish_time_selected
                })
                session.commit()
                streamlit.success("Status atualizado")
        except Exception:
            session.rollback()
            streamlit.error("Erro ao editar agentamento!")
    case _:
        pass