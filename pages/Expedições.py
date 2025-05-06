import streamlit
from functions.streamlit import streamlit_page

from utils.constants import *

expedicoes = streamlit_page(titulo_da_pagina="Expedições")

match expedicoes:
    case "Adicionar":
        pass
    case "Remover":
        pass
    case "Editar":
        pass
    case _:
        pass