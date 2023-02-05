from bs4 import BeautifulSoup


class TestPyQuestionAnswer:
    def test__header__1(self):
        with open("./index.html") as fp:
            soup = BeautifulSoup(fp, "html.parser")

        assert soup.head.title is not None, "You need a HTML title, see https://www.w3schools.com/html/html_head.asp"

    def test__h1(self):
        with open("./index.html") as fp:
            soup = BeautifulSoup(fp, "html.parser")

        assert soup.body.h1 is not None, "You need a HTML title, see https://www.w3schools.com/tags/tag_hn.asp"