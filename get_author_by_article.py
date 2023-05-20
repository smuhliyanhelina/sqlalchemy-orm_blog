from session import session
from models import Article, Author


def main():
    article = session.query(Article).get(1)
    author = session.query(Author).get(article.author_id)
    print(article, article.author_id)



if __name__ == "__main__":
    main()