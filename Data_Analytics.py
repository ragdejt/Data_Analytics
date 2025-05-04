import streamlit
from sql.base import create_table
from utils.constants import *
from functions.streamlit import streamlit_page
from functions.plotly import Graph2dLine, Graph3dLine

DataAnalytics = streamlit_page(
    opcao_barra_lateral=[],
    icone_da_pagina=":material/info:"
    )

if "login" in streamlit.session_state and streamlit.session_state["login"]:
    match DataAnalytics:
        case _:
            streamlit.header("Transforme dados em :green[Decisões estratégicas]!", divider="green")
            streamlit.write("Centralize informações, automatize processos e ganhe eficiência operacional com relatórios em tempo real.")  

            streamlit.write("Isso não é futurismo é ``DataAnalytics``")
            
            with streamlit.expander("Porque Data Analytics ?"):
                streamlit.info("""
                A utilização de um sistema logístico traz inúmeras vantagens para qualquer empresa que busca crescimento, organização e eficiência. 
                Esse tipo de sistema permite que todas as informações essenciais como dados de produtos, fornecedores, funcionários e estoque sejam centralizadas e organizadas de forma clara! 
                Evitando perda de dados e falhas de controle. Além disso, a automação de processos rotineiros reduz o tempo gasto com tarefas manuais e diminui consideravelmente o risco de erros. 
                O que impacta diretamente na produtividade da equipe.
                                
                Outro grande benefício é a geração rápida e confiável de relatórios, que facilita a análise de dados e permite uma tomada de decisões mais estratégica e segura. 
                O controle de estoque também se torna muito mais eficiente, já que o sistema acompanha em tempo real a entrada e saída de produtos! 
                Ajudando a evitar desperdícios, faltas ou excessos de mercadorias. 
                Com uma interface acessível e muitas vezes disponível online, gestores e colaboradores podem acessar informações de qualquer lugar, tornando a administração mais flexível e dinâmica.
                Além disso, um sistema logístico bem estruturado contribui diretamente para a redução de custos operacionais! 
                Pois diminui falhas, retrabalhos e desperdícios, aumentando o lucro e a eficiência geral da empresa. 
                Outro ponto importante é que, com os dados organizados e atualizados, auditorias e análises se tornam muito mais simples e transparentes, fortalecendo a confiança na gestão. 
                Em resumo, investir em um sistema logístico é apostar na organização, no controle e no crescimento sustentável de uma empresa.
                """)
            column1, column2 = streamlit.columns(2)
            with column1:
                with streamlit.expander("✔️ Vantagens"):
                    streamlit.write("``Organização e Centralização de Dados``")
                    streamlit.info("""
                    Um sistema logístico permite que todas as informações importantes da empresa como produtos, fornecedores e funcionários sejam organizadas e armazenadas em um único lugar.
                    Isso elimina a necessidade de planilhas manuais ou anotações dispersas, reduzindo falhas e otimizando o acesso aos dados.
                    """)
                    streamlit.divider()
                    streamlit.write("``Agilidade na Tomada de Decisões``")
                    streamlit.info("""
                    Com dados atualizados em tempo real e relatórios automatizados, a gestão consegue identificar rapidamente problemas e oportunidades.
                    Isso permite uma tomada de decisão mais assertiva, embasada em dados concretos e não em suposições.
                    """)
                    streamlit.divider()
                    streamlit.write("``Redução de Erros e Retrabalho``")
                    streamlit.info("""
                    Ao automatizar cadastros, atualizações e geração de relatórios, o sistema minimiza erros manuais, como duplicidade de informações ou falhas de digitação.
                    Diminuindo a porcentagem de erros isso impacta diretamente no controle de estoque, faturamento ou entrega.
                    """)
                    streamlit.divider()
                    streamlit.write("``Melhor Controle de Estoque e Recursos``")
                    streamlit.info("""
                    Um sistema logístico facilita o acompanhamento do nível de estoque, evitando tanto a falta quanto o excesso de produtos.
                    Isso ajuda na organização de compras, reduz desperdícios e melhora o planejamento de reposição.
                    """)
                    streamlit.divider()
                    streamlit.write("``Otimização do Tempo e Aumento da Produtividade``")
                    streamlit.info("""
                    Automatizando tarefas operacionais que antes consumiam tempo, o sistema libera os colaboradores para se dedicarem a atividades mais estratégicas e produtivas, aumentando o rendimento geral da equipe.
                    """)
                    streamlit.divider()
                    streamlit.write("``Facilidade de Acesso e Monitoramento Remoto``")
                    streamlit.info("""
                    Com uma interface web desenvolvida em streamlit o sistema pode ser acessado de qualquer lugar.
                    Permitindo que gestores monitorem processos, verifiquem informações e gerem relatórios mesmo fora da empresa.
                    """)
                    streamlit.divider()
                    streamlit.write("``Geração de Relatórios Profissionais``")
                    streamlit.info("""
                    A exportação de dados para planilhas Excel permite que informações sejam apresentadas de forma clara e organizada.
                    Sendo ideal para auditorias, reuniões e análises estratégicas, facilitando o controle de resultados.
                    """)
            with column2:
                with streamlit.expander("❌ Desvantagens"):
                    streamlit.write("``Desorganização e Perda de Informações``")
                    streamlit.error("""
                    Sem um sistema, os dados da empresa costumam ficar espalhados em planilhas, anotações manuais ou arquivos soltos.
                    Isso aumenta as chances de perda de informações importantes e dificulta o controle geral, prejudicando a eficiência do negócio.               
                    """)
                    streamlit.divider()
                    streamlit.write("``Tomada de Decisões Lenta e Pouco Confiável``")
                    streamlit.error("""
                    A ausência de relatórios automatizados faz com que as decisões sejam baseadas em informações desatualizadas ou incompletas.
                    Aumentando o risco de escolhas erradas que podem gerar prejuízos para a empresa.               
                    """)
                    streamlit.divider()
                    streamlit.write("``Maior Risco de Erros Manuais``")
                    streamlit.error("""
                    Sem automação, o processo de cadastro, controle de estoque e emissão de relatórios depende do preenchimento manual, o que abre espaço para falhas humanas.
                    Como digitação errada, duplicidade de dados ou perda de registros.               
                    """)
                    streamlit.divider()
                    streamlit.write("``Controle de Estoque Ineficiente``")
                    streamlit.error("""
                    Sem um sistema, o acompanhamento de entradas e saídas de produtos é falho e impreciso!
                    O que pode gerar tanto falta de produtos essenciais quanto excesso de estoque parado, aumentando custos e desperdícios.               
                    """)
                    streamlit.divider()
                    streamlit.write("``Baixa Produtividade da Equipe``")
                    streamlit.error("""
                    Sem a automação de tarefas rotineiras, os colaboradores perdem muito tempo com processos manuais e repetitivos. 
                    O que reduz a produtividade e desvia o foco de atividades realmente importantes para o crescimento da empresa.               
                    """)
                    streamlit.divider()
                    streamlit.write("``Dificuldade de Acesso e Atualização de Dados``")
                    streamlit.error("""
                    Sem uma interface web, o acesso aos dados fica restrito a computadores específicos! 
                    Dificultando a consulta de informações em tempo real e impedindo o monitoramento remoto, especialmente em situações de urgência.               
                    """)
                    streamlit.divider()
                    streamlit.write("``Falta de Relatórios Confiáveis para Análises e Auditorias``")
                    streamlit.error("""
                    Empresas que não utilizam sistemas estruturados enfrentam dificuldade para gerar relatórios detalhados! 
                    Prejudicando o acompanhamento do desempenho, o planejamento estratégico e a transparência em auditorias.               
                    """)
            with streamlit.expander("Sobre nós"):
                streamlit.header("Quem somos")
                streamlit.write(
                """
                ✔️``r4gd3j7``                
                """)
            with streamlit.expander("Contato"):
                streamlit.header("Formulário para contato")
                streamlit.text_input(
                    label="Nome completo",
                    type="default",
                    help="Full name.",
                    placeholder="Digite o nome completo."
                )
                streamlit.text_input(
                    label="Assunto",
                    type="default",
                    help="Subject.",
                    placeholder="Digite o motivo para o contato."
                )
                streamlit.text_input(
                    label="E-mail",
                    type="default",
                    help="E-mail.",
                    placeholder="Digite o e-mail."
                )
                streamlit.text_area(
                    label="Corpo do e-mail",
                    help="E-mail body.",
                    placeholder="Digite a mensagem que deseja encaminhar."
                )
                if streamlit.button("Enviar", use_container_width=True):
                    pass
                streamlit.divider()
            
            streamlit.header(":green[Graficos de desempenho de processos logisticos]", divider="green")
            with streamlit.expander("Graficos"):
                streamlit.write("``TMD - Tempo Médio de Descarga``")
                data1={
                    "X":MONTHS,
                    "Y":[1,2,3,4,5,6,7,8,9,10,11,12]
                }
                graph1 = Graph2dLine(
                    df=data1,
                    X="X",
                    Y="Y",
                    titulo="Grafico TMD",
                    subtitulo="Tempo Médio de Descarga"
                )
                streamlit.plotly_chart(graph1)
                streamlit.info("Identifica gargalos no processo de descarregamento.")
                streamlit.divider()
                streamlit.write("``Número de Veículos Atendidos por Hora/Dia``")
                data2={
                    "X":MONTHS,
                    "Y":[1,2,3,4,5,6,7,8,9,10,11,12]
                }
                graph2 = Graph2dLine(
                    df=data2,
                    X="X",
                    Y="Y",
                    titulo="Grafico VAD",
                    subtitulo="Número de Veículos Atendidos por Dia"
                )
                streamlit.plotly_chart(graph2)
                streamlit.info("Mostra se a equipe/doca está operando em ritmo ideal.")
                streamlit.divider()
                streamlit.write("``Atrasos no Agendamento``")
                data3={
                    "X":MONTHS,
                    "Y":[1,2,3,4,5,6,7,8,9,10,11,12]
                }
                graph3 = Graph2dLine(
                    df=data3,
                    X="X",
                    Y="Y",
                    titulo="Grafico de Atrasos",
                    subtitulo="Horas de atraso após o agendamento"
                )
                streamlit.plotly_chart(graph3)
                streamlit.info("Impacta a programação de motoristas e a eficiência logística.")
                streamlit.divider()
                streamlit.write("``Taxa de Rejeição no Recebimento``")
                data4={
                    "X":MONTHS,
                    "Y":[1,2,3,4,5,6,7,8,9,10,11,12]
                }
                graph4 = Graph2dLine(
                    df=data4,
                    X="X",
                    Y="Y",
                    titulo="Grafico TRR",
                    subtitulo="Taxa de Rejeição no Recebimento"
                )
                streamlit.plotly_chart(graph4)
                streamlit.info("Afeta a qualidade do estoque e pode indicar problemas no transporte.")
                streamlit.divider()
                streamlit.write("``TMC - Tempo Médio de Conferência``")
                data5={
                    "X":MONTHS,
                    "Y":[1,2,3,4,5,6,7,8,9,10,11,12]
                }
                graph5 = Graph2dLine(
                    df=data5,
                    X="X",
                    Y="Y",
                    titulo="Grafico TMC",
                    subtitulo="Tempo Médio de Conferência"
                )
                streamlit.plotly_chart(graph5)
                streamlit.info("Pode revelar lentidão em processos de conferência")
                streamlit.divider()
                streamlit.write("``Tempo de Espera na Fila de Descarga``")
                data6={
                    "X":MONTHS,
                    "Y":[1,2,3,4,5,6,7,8,9,10,11,12]
                }
                graph6 = Graph2dLine(
                    df=data6,
                    X="X",
                    Y="Y",
                    titulo="Grafico TEFD",
                    subtitulo="Tempo de Espera na Fila de Descarga"
                )
                streamlit.plotly_chart(graph6)
                streamlit.info("Avalia o tempo ocioso dos veículos aguardando início da operação.")
                streamlit.divider()
                streamlit.write("``Tempo Total de Permanência do Veículo no CD``")
                data7={
                    "X":MONTHS,
                    "Y":[1,2,3,4,5,6,7,8,9,10,11,12]
                }
                graph7 = Graph2dLine(
                    df=data7,
                    X="X",
                    Y="Y",
                    titulo="Grafico TPV",
                    subtitulo="Tempo Total de Permanência do Veículo no CD"
                )
                streamlit.plotly_chart(graph7)
                streamlit.info("Soma de espera, descarga, conferência e saída. Indica eficiência geral.")
                streamlit.divider()
                streamlit.write("``Taxa de Ocupação da Doca``")
                data8={
                    "X":MONTHS,
                    "Y":[1,2,3,4,5,6,7,8,9,10,11,12]
                }
                graph8 = Graph2dLine(
                    df=data8,
                    X="X",
                    Y="Y",
                    titulo="Grafico TOC",
                    subtitulo="Taxa de Ocupação de Doca"
                )
                streamlit.plotly_chart(graph8)
                streamlit.info("Mede quanto tempo as docas estão ocupadas, útil para balancear turnos e recursos.")
                streamlit.divider()
                streamlit.write("``Produtividade por Operador ou Equipe``")
                data9={
                    "X":MONTHS,
                    "Y":[1,2,3,4,5,6,7,8,9,10,11,12]
                }
                graph9 = Graph2dLine(
                    df=data9,
                    X="X",
                    Y="Y",
                    titulo="Grafico PP-E",
                    subtitulo="Produtividade por Operador ou Equipe"
                )
                streamlit.plotly_chart(graph9)
                streamlit.info("Ajuda a identificar colaboradores com baixa ou alta performance.")
                streamlit.divider()
                streamlit.write("``Tempo Médio de Abertura de Portão até a Doca``")
                data10={
                    "X":MONTHS,
                    "Y":[1,2,3,4,5,6,7,8,9,10,11,12]
                }
                graph10 = Graph2dLine(
                    df=data10,
                    X="X",
                    Y="Y",
                    titulo="Grafico TMA-P/D",
                    subtitulo="Tempo Médio de Abertura de Portão até a Doca"
                )
                streamlit.plotly_chart(graph10)
                streamlit.info("Pode revelar gargalos no acesso interno ao CD.")
                streamlit.divider()
                streamlit.write("``Taxa de Utilização de Agendamentos``")
                data11={
                    "X":MONTHS,
                    "Y":[1,2,3,4,5,6,7,8,9,10,11,12]
                }
                graph11 = Graph2dLine(
                    df=data11,
                    X="X",
                    Y="Y",
                    titulo="Grafico TUA",
                    subtitulo="Taxa de Utilização de Agendamentos"
                )
                streamlit.plotly_chart(graph11)
                streamlit.info("Compara agendamentos previstos com os realizados. Alta taxa pode indicar boa aderência.")
                streamlit.divider()
                streamlit.write("``Desvios de Janela de Agendamento (Adiantos/Atrasos)``")
                data12={
                    "X":MONTHS,
                    "Y":[1,2,3,4,5,6,7,8,9,10,11,12]
                }
                graph12 = Graph2dLine(
                    df=data12,
                    X="X",
                    Y="Y",
                    titulo="Grafico DJA",
                    subtitulo="Desvios de Janela de Agendamento"
                )
                streamlit.plotly_chart(graph12)
                streamlit.info("Permite avaliar a pontualidade dos fornecedores e transportadoras.")
                streamlit.divider()
                streamlit.write("``Taxa de Reentrega ou Devolução de Carga``")
                data13={
                    "X":MONTHS,
                    "Y":[1,2,3,4,5,6,7,8,9,10,11,12]
                }
                graph13 = Graph2dLine(
                    df=data13,
                    X="X",
                    Y="Y",
                    titulo="Grafico RDC",
                    subtitulo="Taxa de Reentrega ou Devolução de Carga"
                )
                streamlit.plotly_chart(graph13)
                streamlit.info("Pode apontar falhas na conferência ou transporte.")
                streamlit.divider()
                streamlit.write("``Tempo de Conferência x Tipo de Produto``")
                data14={
                    "X":MONTHS,
                    "Y":[1,2,3,4,5,6,7,8,9,10,11,12]
                }
                graph14 = Graph2dLine(
                    df=data14,
                    X="X",
                    Y="Y",
                    titulo="Grafico TCxP",
                    subtitulo="Tempo de Conferência x Tipo de Produto"
                )
                streamlit.plotly_chart(graph14)
                streamlit.info("Útil para entender a complexidade por categoria (Ultra congelado, Congelado, Resfriado, Seco")
                    
else:  
    SCRIPT_FOLDER.mkdir(exist_ok=True)
    SQL_FOLDER.mkdir(exist_ok=True)
    EXCEL_FOLDER.mkdir(exist_ok=True)
    create_table()
        

