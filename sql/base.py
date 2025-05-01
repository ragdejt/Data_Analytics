from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import PendingRollbackError
from utils.constants import SQL_FOLDER
Base = declarative_base()
engine = create_engine(f"sqlite:///{SQL_FOLDER / "DataAnalytics.db"}", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Tabela Agendamentos.
class Agendamentos(Base):
    __tablename__ = "Agendamentos"
    ID = Column(Integer, autoincrement=True, primary_key=True)
    STATUS = Column(String)
    FORNECEDOR = Column(String)
    TIPO = Column(String)
    DATA = Column(String)
    CHEGADA = Column(String)
    SAIDA = Column(String)

def add_agendamento(
    status:str,
    fornecedor:int,
    tipo:str,
    data:str,
    chegada:str,
    saida:str
):
    try:
        session.add(Agendamentos(
        STATUS = status,
        FORNECEDOR = fornecedor,
        TIPO = tipo,
        DATA = data,
        CHEGADA = chegada,
        SAIDA = saida
        ))
        session.commit()
    except PendingRollbackError:
        session.rollback()



def rem_agendamento(id_agendamento):
    query = session.query(Agendamentos).get(id_agendamento)
    if query:
        session.delete(query)
        session.commit()

# Tabela Clientes.
class Clientes(Base):
    __tablename__ = "Clientes"
    Id = Column(Integer, autoincrement=True, primary_key=True)
    Nome = Column(String)
    CNPJ = Column(String, unique=True)
    Rua = Column(String)
    Numero = Column(String)
    Bairro = Column(String)
    Cidade = Column(String)
    Telefone = Column(String)
    Email = Column(String)
    Responsavel = Column(String)

# Tabela Conferências.
class Conferencias(Base):
    __tablename__ = "Conferências"
    Id = Column(Integer, autoincrement=True, primary_key=True)

# Tabela Devoluções.
class Devoluções(Base):
    __tablename__ = "Devoluções"
    Id = Column(Integer, autoincrement=True, primary_key=True)

# Tabela Estoques.
class Estoques(Base):
    __tablename__ = "Estoques"
    id = Column(Integer, autoincrement=True, primary_key=True)
    categoria = Column(String) # Ultra Congelado, Congelado, Resfriado, Seco.

# Tabela Expedições.
class Expedicoes(Base):
    __tablename__ = "Expedições"
    Id = Column(Integer, autoincrement=True, primary_key=True)

# Tabela Fornecedores.
class Fornecedores(Base):
    __tablename__ = "Fornecedores"
    ID = Column(Integer, autoincrement=True, primary_key=True)
    NOME = Column(String)
    CNPJ = Column(String, unique=True)
    ENDEREÇO = Column(String)
    CIDADE = Column(String)
    ESTADO = Column(String)
    CEP = Column(String)
    TELEFONE = Column(String)
    EMAIL = Column(String)
    REPRESENTANTE = Column(String)
    BANCO = Column(String)  
    AGENCIA = Column(String)  
    CONTA = Column(String)

def add_fornecedores(
    NOME:str,
    CNPJ:str,
    ENDEREÇO:str,
    CIDADE:str,
    ESTADO:str,
    CEP:str,
    TELEFONE:str,
    EMAIL:str,
    REPRESENTANTE:str,
    BANCO:str,
    AGENCIA:str,
    CONTA:str
):
    try:
        session.add(Fornecedores(
            NOME = NOME, 
            ENDEREÇO = ENDEREÇO, 
            CNPJ = CNPJ, 
            CIDADE = CIDADE, 
            ESTADO = ESTADO, 
            CEP = CEP, 
            TELEFONE = TELEFONE, 
            EMAIL = EMAIL, 
            REPRESENTANTE = REPRESENTANTE, 
            BANCO = BANCO, 
            AGENCIA = AGENCIA, 
            CONTA = CONTA
        ))
        session.commit()
    except PendingRollbackError:
        session.rollback()

# Tabela Frotas.
class Frotas(Base):
    __tablename__ = "Frotas"
    Id = Column(Integer, autoincrement=True, primary_key=True)
    Placa = Column(String)
    Tipo = Column(String)
    Marca = Column(String)
    Ano = Column(Integer)
    Cor = Column(String)
    Tara = Column(String)
    Peso = Column(String)
    Volume = Column(Integer)

# Tabela Funcionarios.
class Funcionarios(Base):
    __tablename__ = "Funcionarios"
    id = Column(Integer, autoincrement=True, primary_key=True)
    nome = Column(String, unique=True)
    endereco = Column(String)
    nascimento = Column(String)
    genero =Column(String)
    nacionalidade = Column(String)
    estado_civil = Column(String)
    rg = Column(String, unique=True)
    cpf = Column(String, unique=True)
    cnh = Column(String, unique=True)
    telefone = Column(String)
    email = Column(String)
    cargo = Column(String)
    contrato = Column(String)
    salario = Column(String)
    banco = Column(String)
    agencia = Column(String)
    conta = Column(String)
    admissao = Column(String)

def add_funcionario(
    nome:str,
    endereco:str,
    nascimento:str,
    genero:str,
    nacionalidade:str,
    estado_civil:str,
    rg:str,
    cpf:str,
    cnh:str,
    telefone:str,
    email:str,
    cargo:str,
    contrato:str,
    salario:str,
    banco:str,
    agencia:str,
    conta:str,
    admissao:str
):  
    try:
        session.add(Funcionarios(
            nome = nome,
            endereço = endereco,
            nascimento = nascimento,
            genero = genero,
            nacionalidade = nacionalidade,
            estado_civil = estado_civil,
            rg = rg,
            cpf = cpf,
            cnh = cnh,
            telefone = telefone,
            email = email,
            cargo = cargo,
            contrato = contrato,
            salario = salario,
            banco = banco,
            agencia = agencia,
            conta = conta,
            admissao = admissao
        ))
        session.commit()
    except PendingRollbackError:
        session.rollback()

def rem_funcionario(id_funcionario):
    query = session.query(Funcionarios).get(id_funcionario)
    if query:
        session.delete(query)
        session.commit()

# Tabela Pedidos.
class Pedidos(Base):
    __tablename__ = "Pedidos"
    Id = Column(Integer, autoincrement=True, primary_key=True)
    Id_Cliente = Column(Integer)     
    Data_Pedido = Column(String)
    Data_Entrega = Column(String)
    Status = Column(String)          
    Valor_Total = Column(String)

# Tabela Produtos.
class Produtos(Base):
    __tablename__ = "Produtos"
    Id = Column(Integer, autoincrement=True, primary_key=True)
    Nome = Column(String)
    SKU = Column(String, unique=True)
    Descricao = Column(String)
    Peso = Column(String)
    Volume = Column(String)
    Codigo_Barras = Column(String)
    Categoria = Column(String)
    Preco = Column(String)

# Tabela Recebimentos.
class Recebimentos(Base):
    __tablename__ = "Recebimentos"
    Id = Column(Integer, autoincrement=True, primary_key=True)

# Tabela Separações.
class Separacoes(Base):
    __tablename__ = "Separações"
    Id = Column(Integer, autoincrement=True, primary_key=True)
    Id_Pedido = Column(Integer)     
    Id_Funcionario = Column(Integer)
    Data_Hora_Inicio = Column(String)
    Data_Hora_Fim = Column(String)
    Status = Column(String) # Concluido, Pendente, Em andamento.



def get_suppliers_id():
    data = session.query(Fornecedores.NOME).all()
    data_list = []
    for id in data:
        data_list.append(id[0])
    return data_list



def create_table():
    Base.metadata.create_all(engine)
