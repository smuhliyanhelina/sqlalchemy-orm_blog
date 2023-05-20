import datetime

from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from session import engine

Base = declarative_base(bind=engine)


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))

    user_name = Column(String(50), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)

    registration_date = Column(
        DateTime,
        nullable=False,
        default=datetime.datetime.now
    )

    articles = relationship("Article", cascade="all, delete, delete-orphan")

    def __repr__(self):
        return f"Author({self.user_name})"


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False, unique=True)
    content = Column(Text, nullable=False)

    publication_date = Column(
        DateTime,
        nullable=False,
        default=datetime.datetime.now
    )

    author_id = Column(
        Integer,
        ForeignKey("authors.id"),
        nullable=False,
    )

    author = relationship("Author")
    hashtags = relationship("Hashtag", secondary="articles_hashtags")

    def __repr__(self):
        return f"Article({self.title})"


class Hashtag(Base):
    __tablename__ = "hashtags"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)

    articles = relationship("Article", secondary="articles_hashtags")

    def __repr__(self):
        return f"Hashtag({self.name})"


articles_hashtags = Table(
    "articles_hashtags",
    Base.metadata,
    Column("article_id", Integer, ForeignKey("articles.id"), primary_key=True),
    Column("hashtag_id", Integer, ForeignKey("hashtags.id"), primary_key=True),
)