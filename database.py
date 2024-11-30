from sqlalchemy import create_engine
from sqlalchemy import String
from sqlalchemy import select
from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Session

class Base(DeclarativeBase):
    pass

engine = create_engine("sqlite+pysqlite:///skills.db", echo=True)

class Skills(Base):
    __tablename__ = 'skills'
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    skillName: Mapped[str] = mapped_column(String()) # Название скилла
    skillDesc: Mapped[str] = mapped_column(String()) # Описание скилла
    skillUrl: Mapped[str] = mapped_column(String()) # Ссылка на видево


def get_skill(id): # Это просто для получения объекта скилла и из него уже можно вытаскивать skillName, skillDesc и skillUrl
    with Session(engine) as session:
        stmt = select(Skills).where(Skills.id == id)
        skill = session.scalar(stmt)
        response ={'skillName':f'{skill.skillName}','skillDesc':f'{skill.skillDesc}','skillUrl':f'{skill.skillUrl}'}
    return response

def get_count():
    with Session(engine) as session:
        row_count = session.query(Skills).count()
        return row_count

# def get_skill_name(id): # Ну тут получаем имя скилла
#     with Session(engine) as session:
#         stmt = select(Skills).where(Skills.id == id)
#         skill = session.scalar(stmt)
#     return skill.skillName

# def get_skill_desc(id): # Ну тут получаем описание скилла
#     with Session(engine) as session:
#         stmt = select(Skills).where(Skills.id == id)
#         skill = session.scalar(stmt)
#     return skill.skillDesc

# def get_skill_url(id): # А тут у нас ссылка на видео вау
#     with Session(engine) as session:
#         stmt = select(Skills).where(Skills.id == id)
#         skill = session.scalar(stmt)
#     return skill.skillUrl



# print(get_skill(1))
# print(get_count())
# print(get_skill_name(1))
# print(get_skill_desc(1))
# print(get_skill_url(1))