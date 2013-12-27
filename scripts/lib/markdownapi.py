#!/usr/bin/env python
# -*- coding: utf-8 -*-

import markdown2

markdownExtras = [
    "footnotes",
    "metadata",
    "smarty-pants",
    "cuddled-lists"
    ]
    
def renderfile ( file ):
    html = markdown2.markdown_path( file , extras = markdownExtras )
    return html
    
def render( data ):
    html = markdown2.markdown( data , extras = markdownExtras )
    return html


if __name__ == '__main__':
    print render ( ' *bo*' )
