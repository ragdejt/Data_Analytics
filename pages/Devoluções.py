import streamlit
from src.functions.streamlit import streamlit_page

from src.utils.constants import *

devolucoes = streamlit_page(titulo_da_pagina="Devoluções")

match devolucoes:
    case "Adicionar":
        pass
    case "Remover":
        pass
    case "Editar":
        pass
    case _:
        pass