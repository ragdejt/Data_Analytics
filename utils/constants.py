from pathlib import Path

USER_HOME = Path.home()

SCRIPT_NAME = "DataAnalytics"

SCRIPT_FOLDER = USER_HOME / (SCRIPT_NAME)

SQL_FOLDER = SCRIPT_FOLDER / ("Bancos de dados SQL")

EXCEL_FOLDER = SCRIPT_FOLDER / ("Tabelas de dados Excel")



CARGO_TYPE = ["Ultra Congelado", "Congelado", "Resfriado", "Seco"]

APPOINTMENT_STATUS = ["Em andamento", "Concluido", "Pendente"]

STATES_CITIES = {
    "São Paulo":["São Paulo", "Campinas", "Hortolândia", "Sumaré"],
    "Rio de janeiro":["Rio de janeiro"],
    "Santa Catarina":[""],
    "Minas Gerais":[""],
    "Rio grande do norte":[""],
}

NATIONALITY = [
    "Estadunidense",       
    "Brasileira",          
    "Mexicana",            
    "Colombiana",          
    "Argentina",           
    "Canadense",           
    "Peruana",             
    "Venezuelana",         
    "Chilena",             
    "Guatemalteca"
]

POSITION = [
    "Analista de Logística",
    "Coordenador de Logística",
    "Gerente de Logística",
    "Supervisor de Armazenagem",
    "Operador de Empilhadeira",
    "Gestor de Cadeia de Suprimentos (Supply Chain Manager)",
    "Especialista em Compras",
    "Analista de Estoques",
    "Planejador de Demanda",
    "Supervisor de Transportes",
    "Motorista de Carga (Caminhoneiro)",
    "Despachante Aduaneiro",
    "Coordenador de Distribuição",
    "Analista de Fretes",
    "Consultor de Logística",
    "Supervisor de Centro de Distribuição (CD)",
    "Operador de Logística (Warehouse)",
    "Gestor de Frota",
    "Analista de Roteirização",
    "Especialista em Logística Reversa"
]

BANK = [
    "Banco do Brasil",
    "Caixa Econômica Federal",
    "Itaú Unibanco",
    "Bradesco",
    "Santander",
    "Nubank",
    "Banco Inter",
    "Sicoob",
    "Sicredi",
    "Banco Safra"
]