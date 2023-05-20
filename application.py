from models import Author, Article
from session import session


def main():
    for author in session.query(Author):
        # articles = session.query(Article).filter_by(author_id=author.id)
        for article in author.articles:
            print(author, article)


if __name__ == "__main__":
    main()
