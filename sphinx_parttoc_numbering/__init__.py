# -*- coding: utf-8 -*-
"""
    part-toctree.py
    ~~~~~~~~~~~~~~~

    An extension to support "Part" in HTML section numbering.
    This is made for Sphinx-1.5
    https://github.com/sphinx-doc/sphinx/issues/3357

    :copyright: Copyright 2007-2016 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from docutils import nodes
from sphinx import addnodes
from sphinx.util import url_re

__version__ = "0.0.1"
"""sphinx-parttoc-numbering version"""

def assign_section_numbers(self, env):
    """Assign a section number to each heading under a numbered toctree."""
    # a list of all docnames whose section numbers changed
    rewrite_needed = []

    assigned = set()
    old_secnumbers = env.toc_secnumbers
    env.toc_secnumbers = {}
    self.last_section_number = 0

    def _walk_toc(node, secnums, depth, titlenode=None):
        # titlenode is the title of the document, it will get assigned a
        # secnumber too, so that it shows up in next/prev/parent rellinks
        for subnode in node.children:
            if isinstance(subnode, nodes.bullet_list):
                if len(numstack) == 1:
                    numstack.append(self.last_section_number)
                else:
                    numstack.append(0)
                _walk_toc(subnode, secnums, depth - 1, titlenode)
                numstack.pop()
                titlenode = None
            elif isinstance(subnode, nodes.list_item):
                _walk_toc(subnode, secnums, depth, titlenode)
                titlenode = None
            elif isinstance(subnode, addnodes.only):
                # at this stage we don't know yet which sections are going
                # to be included; just include all of them, even if it leads
                # to gaps in the numbering
                _walk_toc(subnode, secnums, depth, titlenode)
                titlenode = None
            elif isinstance(subnode, addnodes.compact_paragraph):
                numstack[-1] += 1
                if len(numstack) == 1:
                    number = None  # do not assign number to "Part"
                else:
                    if len(numstack) == 2:
                        self.last_section_number += 1  # increment section number

                    if depth > 0:
                        number = tuple(numstack[1:])  # assign section numbers without part number
                    else:
                        number = None
                secnums[subnode[0]['anchorname']] = \
                    subnode[0]['secnumber'] = number
                if titlenode:
                    titlenode['secnumber'] = number
                    titlenode = None
            elif isinstance(subnode, addnodes.toctree):
                _walk_toctree(subnode, depth)

    def _walk_toctree(toctreenode, depth):
        if depth == 0:
            return
        for (title, ref) in toctreenode['entries']:
            if url_re.match(ref) or ref == 'self':
                # don't mess with those
                continue
            elif ref in assigned:
                env.warn_node('%s is already assigned section numbers '
                                   '(nested numbered toctree?)' % ref,
                                   toctreenode, type='toc', subtype='secnum')
            elif ref in env.tocs:
                secnums = env.toc_secnumbers[ref] = {}
                assigned.add(ref)
                _walk_toc(env.tocs[ref], secnums, depth,
                          env.titles.get(ref))
                if secnums != old_secnumbers.get(ref):
                    rewrite_needed.append(ref)

    for docname in env.numbered_toctrees:
        assigned.add(docname)
        doctree = env.get_doctree(docname)
        for toctreenode in doctree.traverse(addnodes.toctree):
            depth = toctreenode.get('numbered', 0)
            if depth:
                # every numbered toctree gets new numbering
                numstack = [0]
                _walk_toctree(toctreenode, depth)

    return rewrite_needed

def setup(app):
    from sphinx.environment.collectors.toctree import TocTreeCollector
    TocTreeCollector.assign_section_numbers = assign_section_numbers 