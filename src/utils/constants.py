from pathlib import Path

USER_HOME = Path.home()

SCRIPT_NAME = "Data_Analytics-1.0.0"

SCRIPT_FOLDER = USER_HOME / (SCRIPT_NAME)

SQL_FOLDER = SCRIPT_FOLDER / ("Bancos de dados SQL")

EXCEL_FOLDER = SCRIPT_FOLDER / ("Tabelas de dados Excel")

CARGO_TYPE = ["Ultra Congelado", "Congelado", "Resfriado", "Seco"]

APPOINTMENT_STATUS = ["Em andamento", "Concluido", "Pendente"]

MONTHS = [
    "Janeiro",
    "Fevereiro",
    "Março",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Outubro",
    "Novembro",
    "Dezembro"
]

STATES_CITIES = {
    "São Paulo":[
        "São Paulo",
        "Guarulhos",
        "Campinas",
        "São Bernardo do Campo",
        "Santo André",
        "Osasco",
        "Sorocaba",
        "Ribeirão Preto",
        "São José dos Campos",
        "São José do Rio Preto"
    ],
    "Rio de janeiro":[
       "Rio de Janeiro",
        "São Gonçalo",
        "Duque de Caxias",
        "Nova Iguaçu",
        "Campos dos Goytacazes",
        "Belford Roxo",
        "Niterói",
        "São João de Meriti",
        "Petrópolis",
        "Volta Redonda"
    ],
    "Santa Catarina":[
        "Joinville",
        "Florianópolis",
        "Blumenau",
        "São José",
        "Chapecó",
        "Itajaí",
        "Criciúma",
        "Jaraguá do Sul",
        "Palhoça",
        "Lages"
    ],
    "Minas Gerais":[
        "Belo Horizonte",
        "Uberlândia",
        "Contagem",
        "Juiz de Fora",
        "Montes Claros",
        "Betim",
        "Uberaba",
        "Ribeirão das Neves",
        "Governador Valadares",
        "Divinópolis"
    ],
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