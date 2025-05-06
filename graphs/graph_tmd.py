import streamlit
from utils.constants import MONTHS
from functions.plotly import GraphPizza, Graph2dLine

def Graph_TMD():
    """
    Grafico de Tempo Médio de Descarga.
    """
    graph_tmd_data={
        "Meses":MONTHS,
        "Ultra Congelado":[10,20,30,40,50,60,70,80,90,100,110,120],
        "Congelado":[1,2,3,4,5,6,7,8,9,10,11,12],
        "Resfriado":[11,22,33,44,55,66,77,88,99,109,119,129],
        "Seco":[37,41,56,68,74,81,90,20,25,37,41, 45]
    }

    graph_tmd_pie = GraphPizza(
        df=graph_tmd_data,
        names=graph_tmd_data["Meses"],
        values=[10,20,30,40,50,60,70,80,90,100,110,120],
        titulo="Grafico Pizza",
        subtitulo="Tempo Médio de Descarga"
    )
    graph_tmd_pie.update_layout(
        yaxis_title="Minutos",
        xaxis_title="Meses"
    )
    streamlit.plotly_chart(graph_tmd_pie)

    graph_tmd_2dline = Graph2dLine(
        df=graph_tmd_data,
        X="Meses",
        Y=["Ultra Congelado","Congelado", "Resfriado", "Seco"],
        titulo="Grafico Linha",
        subtitulo="Tempo Médio de Descarga"
    )
    graph_tmd_2dline.update_layout(
        yaxis_title="Minutos",
        xaxis_title="Meses"
    )
    streamlit.plotly_chart(graph_tmd_2dline)