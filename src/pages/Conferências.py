import streamlit
from functions.streamlit import streamlit_page

from src.utils.constants import *

conferencias = streamlit_page(titulo_da_pagina="Conferências")

match conferencias:
    case "Adicionar":
        pass
    case "Remover":
        pass
    case "Editar":
        pass
    case _:
        pass