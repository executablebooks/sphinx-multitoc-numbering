# Sphinx-parttoc-numbering

```{toctree}
:hidden:

contribute
```
**An extension for continuos numbering of toctree elements across multiple toctrees**.

This package contains a [Sphinx](http://www.sphinx-doc.org/en/master/) extension to continuously number sections across multiple toctrees present in the same document. Also quite useful in [jupyter-book] projects for continuos numbering of chapters across different parts. 

```{warning}
sphinx-parttoc-numbering is in an active development stage and may change rapidly.
```

(example)=
## Examples:

(sphinx-example)=
### Sphinx example

For the following rst code:

```python
Part1

..  toctree::
    :numbered:

    Chap1
    Chap2

Part2

..  toctree::
    :numbered:

    Chap3
```
The resultant html numbering will look something like:


```
Part1

    1. Chap1 Title
    2. Chap2 Title

Part2

    3. Chap3 Title
```

(jb-example)=
### Jupyter-book example

For the following code in `_toc.yml`:

```yaml
- file: intro
  numbered: true

- part: part1
  chapters:
  - file: part1/chapter1
  - file: part1/chapter2

- part: part2
  chapters:
  - file: part2/chapter1
```

The resultant html numbering will look something like:


```
Part1
    1. part1/chapter1 title
    2. part1/chapter2 title
Part2
    3. part2/chapter1 title
```

(getting-started)=
## Getting Started

Since, this repo has not been published to `pypi` yet. To get started with `sphinx-parttoc-numbering`, first clone the Github repo[https://github.com/QuantEcon/sphinx-parttoc-numbering] locally:

```bash

git clone https://github.com/QuantEcon/sphinx-parttoc-numbering
```
and then install using the setup file

```bash

cd sphinx-parttoc-numbering
python setup.py install
```

### Configuration

1. Add this extension to the extensions list in your sphinx project's `conf.py`:

    ```python
        extensions = ["sphinx_parttoc_numbering"]
    ```

2. Use the `:numbered:` option in toctrees  if using {ref}`sphinx-example` or `numbered:true` if using {ref}`jb-example`,