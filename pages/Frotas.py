import streamlit
from src.functions.streamlit import streamlit_page

from src.utils.constants import *

frotas = streamlit_page(titulo_da_pagina="Frotas")

match frotas:
    case "Adicionar":
        pass
    case "Remover":
        pass
    case "Editar":
        pass
    case _:
        pass