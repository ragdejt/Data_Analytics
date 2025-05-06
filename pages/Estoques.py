import streamlit
from src.functions.streamlit import streamlit_page

from src.utils.constants import *

estoques = streamlit_page(titulo_da_pagina="Estoques")

match estoques:
    case "Adicionar":
        pass
    case "Remover":
        pass
    case "Editar":
        pass
    case _:
        pass