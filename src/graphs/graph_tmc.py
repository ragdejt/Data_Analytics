import streamlit
from src.utils.constants import MONTHS
from functions.plotly import Graph2dLine, GraphPizza

def Graph_TMC():
    """
    Grafico de Tempo Médio de Conferência.
    """
    graph_tmc_data={
        "Meses":MONTHS,
        "Minutos":[1,2,3,4,5,6,7,8,9,10,11,12]
    }
    graph_tmc_pie = GraphPizza(
        df=graph_tmc_data,
        names=graph_tmc_data["Meses"],
        values=graph_tmc_data["Minutos"],
        titulo="Grafico Pizza",
        subtitulo="Tempo Médio de Conferência"
    )
    streamlit.plotly_chart(graph_tmc_pie)

    graph_tmc_2dline = Graph2dLine(
        df=graph_tmc_data,
        X="Meses",
        Y="Minutos",
        titulo="Grafico Linha",
        subtitulo="Tempo Médio de Conferência"
    )
    streamlit.plotly_chart(graph_tmc_2dline)
