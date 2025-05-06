import streamlit
from utils.constants import MONTHS
from functions.plotly import Graph2dLine, GraphPizza

def Graph_POE():
    """
    Grafico de Produtividade por Operador de Equipe.
    """
    graph_poe_data={
        "Meses":MONTHS,
        "Produtividade":[1,2,3,4,5,6,7,8,9,10,11,12]
    }
    graph9 = Graph2dLine(
        df=graph_poe_data,
        X="Meses",
        Y="Produtividade",
        titulo="Grafico Linha",
        subtitulo="Produtividade por Operador de Equipe"
    )
    streamlit.plotly_chart(graph9)
