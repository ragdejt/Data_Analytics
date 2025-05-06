import streamlit
from src.utils.constants import MONTHS
from functions.plotly import Graph2dLine

def Graph_TDP():
    graph_tdp_data={
        "Meses":MONTHS,
        "Porcentagem (%)":[1,2,3,4,5,6,7,8,9,10,11,12]
    }
    graph_tdp_2dline = Graph2dLine(
        df=graph_tdp_data,
        X="Meses",
        Y="Porcentagem (%)",
        titulo="Grafico TDP",
        subtitulo="Taxa de Devolução de produto"
    )
    streamlit.plotly_chart(graph_tdp_2dline)