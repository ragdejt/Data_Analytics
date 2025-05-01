import streamlit
from functions.streamlit import streamlit_page
from sql.base import add_agendamento, get_suppliers_id
from utils.constants import *
agendamentos = streamlit_page(
    titulo_da_pagina="Agendamentos"
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

        date = streamlit.date_input(label="Data do agendamento")

        start_time = streamlit.time_input(label="Hora de chegada")

        finish_time = streamlit.time_input(label="Hora de saida")

        if streamlit.button(label="Adicionar"):
            try:
                if start_time >= finish_time:
                    streamlit.toast("Horario de chegada não pode ser maior ou igual ao horario de saida!")
                    streamlit.error("Horario de chegada não pode ser maior ou igual ao horario de saida!")
                    raise ValueError
                add_agendamento(
                    status=status,
                    id_fornecedor=fornecedor,
                    tipo=tipo_carga,
                    data=str(date),
                    chegada=str(start_time),
                    saida=str(finish_time)
                )
            except Exception:
                streamlit.toast("Erro ao adicionar novo agendamento!")
                streamlit.error("Erro ao adicionar novo agendamento!")
            else:
                streamlit.toast("Agendamento adicionado com sucesso!")
                streamlit.success("Agendamento adicionado com sucesso!")
    case "Remover":
        pass
