import pytest
from bs4 import BeautifulSoup as bs


@pytest.mark.sphinx("html", testroot="parts-multipletocs")
def test_multipletocs(app, file_regression):
    app.build()
    outfile = app.outdir / "index.html"

    # get content markup
    soup = bs(outfile.read_text(encoding="utf8"), "html.parser")
    toctree_wrapper = soup.findAll("div", {"class": "toctree-wrapper"})
    toctrees = ""
    for toctree in toctree_wrapper:
        toctrees += str(toctree)
    toctrees_tags = bs(toctrees, "html.parser")
    file_regression.check(toctrees_tags.prettify(), extension=".html")
    assert "3. Part 2" in str(toctrees_tags)
    assert "3.1. Chapter 3" in str(toctrees_tags)


@pytest.mark.sphinx("html", testroot="parts-singletoc")
def test_singletoc(app, file_regression):
    app.build()
    outfile = app.outdir / "index.html"

    # get content markup
    soup = bs(outfile.read_text(encoding="utf8"), "html.parser")
    toctree_wrapper = soup.findAll("div", {"class": "toctree-wrapper"})[0]
    file_regression.check(toctree_wrapper.prettify(), extension=".html")
    assert "3. Part 2" in str(toctree_wrapper)
    assert "3.1. Chapter 3" in str(toctree_wrapper)


@pytest.mark.sphinx("html", testroot="parts-mixed-numbering")
def test_mixed(app, file_regression):
    app.build()
    outfile = app.outdir / "index.html"

    # get content markup
    soup = bs(outfile.read_text(encoding="utf8"), "html.parser")
    toctree_wrapper = soup.findAll("div", {"class": "toctree-wrapper"})[0]
    file_regression.check(toctree_wrapper.prettify(), extension=".html")
    assert "2. Chapter 2" in str(toctree_wrapper)
    assert ">Part 2" in str(toctree_wrapper)
    assert ">Chapter 3" in str(toctree_wrapper)


@pytest.mark.sphinx("html", testroot="nested-toctree")
def test_nested(app, file_regression):
    app.build()
    outfile = app.outdir / "index.html"

    # get content markup
    soup = bs(outfile.read_text(encoding="utf8"), "html.parser")
    toctree_wrapper = soup.findAll("div", {"class": "toctree-wrapper"})[0]
    file_regression.check(toctree_wrapper.prettify(), extension=".html")
    assert "1. Chapter 1" in str(toctree_wrapper)
    assert "2. Chapter 2" in str(toctree_wrapper)
    assert "3. Chapter 3" in str(toctree_wrapper)
    assert "4. Chapter 4" in str(toctree_wrapper)
