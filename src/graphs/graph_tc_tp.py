import streamlit
from utils.constants import MONTHS
from functions.plotly import Graph2dLine

def Graph_TC_TP():
    graph_tc_tp_data={
        "Meses":MONTHS,
        "Seco":[13,32,53,14,5,62,17,48,49,10,11,12],
        "Resfriado":[11,22,34,42,35,6,7,8,79,10,11,12],
        "Congelado":[12,52,63,4,15,46,7,8,9,10,11,12],
        "Ultra Congelado":[51,62,13,44,15,56,71,58,19,10,11,12]
    }
    graph_tc_tp = Graph2dLine(
        df=graph_tc_tp_data,
        X="Meses",
        Y=["Ultra Congelado", "Congelado", "Resfriado", "Seco"],
        titulo="Grafico Linha",
        subtitulo="Tempo de Conferência x Tipo de Produto"
    )
    streamlit.plotly_chart(graph_tc_tp)