import pandas
import streamlit
from sqlalchemy import text
from sql.base import engine
from utils.constants import *
from typing import Optional, Literal, List

def streamlit_page(
    titulo_da_pagina:Optional[str] = SCRIPT_NAME,
    icone_da_pagina:Optional[str] = None,
    layout_da_pagina:Optional[Literal["centered", "wide"]] = "wide",
    status_barra_lateral:Optional[Literal["auto", "expanded", "collapsed"]] = "expanded",
    opcao_barra_lateral:Optional[List[str]] = ["Adicionar", "Remover", "Editar", "Visualizar"],
):  
    """
    Configura e renderiza uma página Streamlit.
    """
    # Configuração inicial da página
    streamlit.set_page_config(
        page_title=titulo_da_pagina,
        page_icon=icone_da_pagina,
        layout=layout_da_pagina,
        
        initial_sidebar_state=status_barra_lateral,
    )

    streamlit.title(f":green[{titulo_da_pagina}]")

    if "login" in streamlit.session_state and streamlit.session_state["login"]:
        option = streamlit.sidebar.selectbox(
        label=titulo_da_pagina,
        options=opcao_barra_lateral,
        index=None,
        placeholder="DataAnalytics")
        streamlit.sidebar.divider()
        match option:
            case "Adicionar":
                streamlit.divider()
                streamlit.subheader(":green[Adicionar]", divider="green")
                streamlit.write("``Todas as alterações realizadas por meio desta interface são automaticamente registradas em logs de auditoria!``")
                
            case "Remover":
                streamlit.divider()
                streamlit.subheader(":green[Remover]", divider="green")
                streamlit.write("``Todas as alterações realizadas por meio desta interface são automaticamente registradas em logs de auditoria!``")

            case "Editar":
                streamlit.divider()
                streamlit.subheader(":green[Editar]", divider="green")
                streamlit.write("``Todas as alterações realizadas por meio desta interface são automaticamente registradas em logs de auditoria!``")

            case "Visualizar":
                streamlit.divider()
                streamlit.title(":green[Visualizar]")
                query = f"SELECT * FROM {titulo_da_pagina}"
                df = pandas.read_sql_query(sql=text(query), con=engine)
                streamlit.dataframe(df)


        if streamlit.sidebar.button("Desconectar", icon=":material/logout:", use_container_width=True):
            print("Disconnecting! [...]")            
            streamlit.session_state["login"] = False
            streamlit.rerun()
        return option
    else:
        streamlit.session_state["usuario"] = None

        streamlit.title("``Sessão não autenticada!``")
        streamlit.info("""
        1. Você não possui permissão para acessar esta página!
        2. Sua sessão atual não possui credenciais válidas ou a autorização necessária para visualizar este conteúdo.
        3. Conecte-se para saber se seu cargo atual permite a visualização ou manipulação deste conteúdo.
        """)
        streamlit.divider()

        with streamlit.expander("Iniciar sessão", expanded=True):
            usuario = streamlit.text_input("Usuario", placeholder="Digite o nome de usuario")
            senha = streamlit.text_input("Senha", type="password", placeholder="Digite a senha de usuario")
    
            if streamlit.button("Conectar", icon=":material/login:", use_container_width=True):
                streamlit.session_state["login"] = True
                streamlit.session_state["usuario"] = usuario
                streamlit.rerun()

        with streamlit.expander("Entre em contato com o administrador do sistema caso acredite que isso seja um erro."):
            streamlit.subheader("``Formulário``", divider="green")
            streamlit.text_input(
                label="Nome completo",
                placeholder="Digite o nome completo."
            )
            streamlit.text_input(
                label="Assunto",
                placeholder="Digite o motivo para o contato."
            )
            streamlit.text_input(
                label="E-mail",
                placeholder="Digite o e-mail."
            )
            streamlit.text_area(
                label="Corpo do e-mail",
                placeholder="Digite a mensagem que deseja encaminhar."
            )
            if streamlit.button("Enviar", use_container_width=True):
                pass
            streamlit.subheader("``Importante``", divider="green")
            streamlit.info("""
            1. Use sempre um e-mail válido e atualizado para facilitar a recuperação.
            2. Se não encontrar o e-mail, aguarde alguns minutos ou verifique a pasta de spam.
            3. Se ainda tiver dificuldades, entre em contato com o suporte técnico.               
            """)

