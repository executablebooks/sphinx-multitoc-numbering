import shutil
import pytest
from sphinx.testing.path import path

pytest_plugins = "sphinx.testing.fixtures"


@pytest.fixture
def rootdir(tmpdir):
    src = path(__file__).parent.abspath() / "roots"
    dst = tmpdir.join("roots")
    shutil.copytree(src, dst)
    roots = path(dst)
    yield roots
    shutil.rmtree(dst)

@pytest.fixture
def warnings():
    def read(app):
        return app._warning.getvalue().strip()

    return read
