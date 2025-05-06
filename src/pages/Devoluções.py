import streamlit
from functions.streamlit import streamlit_page

from utils.constants import *

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