import streamlit
from src.sql.base import create_table
from src.functions.streamlit import streamlit_page
from src.utils.constants import SCRIPT_FOLDER, SQL_FOLDER, EXCEL_FOLDER

DataAnalytics = streamlit_page(
    opcao_barra_lateral=[],
    icone_da_pagina=":material/info:"
    )

if "login" in streamlit.session_state and streamlit.session_state["login"]:
    match DataAnalytics:
        case _:
            streamlit.header("Transforme dados em :green[Decisões estratégicas]", divider="green")
            streamlit.write("Centralize informações, automatize processos e ganhe eficiência operacional com relatórios em tempo real.")  

            streamlit.write("Isso não é futurismo é :green[DataAnalytics]!")
            
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
                with streamlit.expander("✔️ :green[Vantagens]"):
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
                with streamlit.expander("❌ :red[Desvantagens]"):
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
                streamlit.subheader(":green[Quem somos]", divider="green")
                streamlit.write(
                """
                ✔️``r4gd3j7``                
                """)
            with streamlit.expander("Contato"):
                streamlit.subheader(":green[Formulário para contato]", divider="green")
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
                
                # Graficos TMD.
                streamlit.subheader(":green[``TMD`` - Tempo Médio de Descarga]", divider="green")
                streamlit.info("Identifica gargalos no processo de descarregamento.")


                streamlit.divider()

                # Graficos VAM.
                streamlit.subheader(":green[``VAM`` - Veículos Atendidos por Mês]", divider="green")
                streamlit.info("Mostra se a equipe/doca está operando em ritmo ideal.")


                streamlit.divider()

                # Grafico TMC.
                streamlit.subheader(":green[``TMC`` - Tempo Médio de Conferência]", divider="green")
                streamlit.info("Pode revelar lentidão em processos de conferência")


                streamlit.divider()

                # Grafico POE.
                streamlit.subheader(":green[``POE`` - Produtividade por Operador de Equipe]", divider="green")
                streamlit.info("Ajuda a identificar colaboradores com baixa ou alta performance.")


                streamlit.divider()

                # Grafico TUA.
                streamlit.subheader(":green[``TUA`` - Taxa de Utilização de Agendamentos]", divider="green")
                streamlit.info("Compara agendamentos previstos com os realizados. Alta taxa pode indicar boa aderência.")


                streamlit.divider()

                # Grafico TRP.

                # Grafico TDP.
                streamlit.subheader(":green[``TDP`` - Taxa de Devolução de produto]", divider="green")
                streamlit.info("Pode apontar falhas na conferência ou transporte.")
                
                
                streamlit.divider()
                
                
                # Grafico TCxTP.
                streamlit.subheader(":green[``TCxTP`` - Tempo de Conferência por Tipo de Produto]", divider="green")
                streamlit.info("Útil para entender a complexidade por categoria (Ultra congelado, Congelado, Resfriado, Seco")


                streamlit.divider()
else:
    SCRIPT_FOLDER.mkdir(exist_ok=True)
    SQL_FOLDER.mkdir(exist_ok=True)
    EXCEL_FOLDER.mkdir(exist_ok=True)
    create_table()
    print("".center(100, "-"))
