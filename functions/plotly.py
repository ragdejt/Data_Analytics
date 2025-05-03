import pandas
import plotly.express
from typing import Optional, Dict
def Graph2dLine(
        df:Dict,
        X:int,
        Y:int,
        titulo:Optional[str] = "Grafico 2d",
        subtitulo:Optional[str] = "Grafico 2d"
    ):
    dataframe = pandas.DataFrame(data=df)
    graph = plotly.express.line(
        data_frame=dataframe,
        x=X,
        y=Y,
        title=titulo,
        subtitle=subtitulo,
        markers=True
    )
    return graph

def Graph3dLine(
    df:Dict,
    X:int,
    Y:int,
    Z:int,
    titulo:Optional[str] = "Grafico 3d",
    subtitulo:Optional[str] = "Grafico 3d"

):
    dataframe = pandas.DataFrame(data=df)
    graph = plotly.express.line_3d(
        data_frame=dataframe,
        x=X,
        y=Y,
        z=Z,
        title=titulo,
        subtitle=subtitulo,
        markers=True
    )
    return graph