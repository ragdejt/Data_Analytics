import streamlit
from src.utils.constants import MONTHS
from functions.plotly import Graph2dLine

def Graph_TUA():
    """
    Grafico de Taxa de Utilização de Agendamentos.
    """
    data11={
        "Meses":MONTHS,
        "Porcentagem (%)":[1,2,3,4,5,6,7,8,9,10,11,12]
    }
    graph11 = Graph2dLine(
        df=data11,
        X="Meses",
        Y="Porcentagem (%)",
        titulo="Grafico Linha",
        subtitulo="Taxa de Utilização de Agendamentos"
    )
    streamlit.plotly_chart(graph11)
    
