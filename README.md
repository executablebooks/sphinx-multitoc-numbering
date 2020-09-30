# sphinx-multitoc-numbering

[![Documentation Status][rtd-badge]][rtd-link]
[![Github-CI][github-ci]][github-link]
[![Coverage Status][codecov-badge]][codecov-link]

**A Sphinx extension to support continuous numbering of sections across multiple tocs in HTML output**.

This package contains a [Sphinx](http://www.sphinx-doc.org/en/master/) extension to continuously number sections across multiple toctrees present in the same document. Also quite useful in [jupyter-book](https://jupyterbook.org/) projects for continuous numbering of chapters across different parts.

## Get started

To get started with `sphinx-multitoc-numbering`, first install it through `pip`:

```
pip install sphinx-multitoc-numbering
```

then, add `sphinx_multitoc_numbering` to your sphinx `extensions` in the `conf.py`

```python
...
extensions = ["sphinx_multitoc_numbering"]
...
```

## Documentation

See the [sphinx-multitoc-numbering documentation](https://sphinx-multitoc-numbering.readthedocs.io/en/latest/) for more information.

## Contributing

We welcome all contributions! See the [EBP Contributing Guide](https://executablebooks.org/en/latest/contributing.html) for general details.

[rtd-badge]: https://readthedocs.org/projects/sphinx-multitoc-numbering/badge/?version=latest
[rtd-link]: https://sphinx-multitoc-numbering.readthedocs.io/en/latest/?badge=latest
[github-ci]: https://github.com/executablebooks/sphinx-multitoc-numbering/workflows/continuous-integration/badge.svg?branch=master
[github-link]: https://github.com/executablebooks/sphinx-multitoc-numbering
[codecov-badge]: https://codecov.io/gh/executablebooks/sphinx-multitoc-numbering/branch/master/graph/badge.svg
[codecov-link]: https://codecov.io/gh/executablebooks/sphinx-multitoc-numbering
