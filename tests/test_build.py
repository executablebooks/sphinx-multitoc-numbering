import pytest
from bs4 import BeautifulSoup as bs

@pytest.mark.sphinx("html", testroot="parts-multipletocs")
def test_multipletocs(app, file_regression):
    app.build()
    outfile = app.outdir/"index.html"

    # get content markup 
    soup = bs(outfile.read_text(encoding="utf8"),"html.parser")
    toctree_wrapper = soup.findAll("div", {"class": "toctree-wrapper"})
    toctrees = ""
    for toctree in toctree_wrapper:
        toctrees += str(toctree)
    toctrees_tags = bs(toctrees,"html.parser")
    file_regression.check(toctrees_tags.prettify(), extension=".html")


@pytest.mark.sphinx("html", testroot="parts-singletoc")
def test_singletoc(app):
    app.build()