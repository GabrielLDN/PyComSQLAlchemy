from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import sessionmaker
from faker import Faker

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

fake = Faker()

for i in range(10):
    nome_fake = fake.name()
    idade_fake = fake.random_int(min=18, max=30)
    aluno = Alunos(nome=nome_fake, idade=idade_fake)
    session.add(aluno)
    session.commit()

alunos = session.query(Alunos).all()
for i in alunos:
   print(i.idade, i.nome, i.matricula)
