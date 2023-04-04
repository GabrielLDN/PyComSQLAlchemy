from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:@localhost:3306/home")
Base = declarative_base()

class Alunos(Base):
    __tablename__ = "alunos"
    matricula = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    idade = Column(Integer, nullable=False)

inspector = inspect(engine)

if "alunos" in inspector.get_table_names():
    print("Tabela já existe")
else:
    Base.metadata.create_all(engine)

Session = sessionmaker(engine)
session = Session()

aluno1 = Alunos(nome = "Null",
                idade = "Null"
                )
session.add(aluno1)
session.commit()


alunos = session.query(Alunos).all()
for i in alunos:
   print("IDADE: ",i.idade,"| NOME: ",i.nome,"| Matrícula: ", i.matricula)


# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base


# engine=create_engine("mysql+pymysql://root:@localhost:3306/home")

# Base= declarative_base()

# class Aluno(Base):
#     __tablename__="alunos"
#     matricula = Column(Integer, primary_key=True, autoincrement=True)
#     nome = Column(String(50),nullable=False)
#     idade =Column(Integer, nullable=False)

# inpector = inspect(engine)

# if "alunos" in inspector.get_table_names():
#     print("Tabela já existe")
# else:

# Base.metadata.create_all(engine)