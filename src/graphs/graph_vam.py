import streamlit
from utils.constants import MONTHS
from functions.plotly import GraphPizza, Graph2dLine

def Graph_VAM():
    """
    Grafico de Veículos Atendidos por Mês.
    """
    graph_vam_data={
        "Meses":MONTHS,
        "Veiculos Atendidos":[14,26,38,41,57,60,77,84,97,101,111,102]
    }
    graph_vam_pie = GraphPizza(
        df=graph_vam_data,
        names=graph_vam_data["Meses"],
        values=graph_vam_data["Veiculos Atendidos"],
        titulo="Grafico Pizza",
        subtitulo="Veículos Atendidos por Mês"
    )
    streamlit.plotly_chart(graph_vam_pie)

    graph_vam_2dline = Graph2dLine(
        df=graph_vam_data,
        X="Meses",
        Y="Veiculos Atendidos",
        titulo="Grafico Linha",
        subtitulo="Veículos Atendidos por Mês"
    )
    streamlit.plotly_chart(graph_vam_2dline)
