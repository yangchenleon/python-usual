#!/usr/bin/env python3

# Convert a text file + a dicttionnary file to a LaTeX file
# Usage : 'python3 texttolatex.py toto.txt'
# or 'python3 texttolatex.py toto.txt toto.dic'
# or 'python3 texttolatex.py toto.txt toto.dic new_toto.tex'
# Output : create a file toto.tex (or new_toto.tex)

import re
import yaml
from .constants import *

#--------------------------------------------------
#--------------------------------------------------

def txt2tex(tex_file):
    txt_file = 'aux.txt'
    dic_file = 'aux.dic' # If no name add a .dic extension

    # Read file object to string
    fic_txt = open(txt_file, 'r', encoding='utf-8')
    text_all = fic_txt.read()
    fic_txt.close()


    # Read dictionnary
    fic_dic = open(dic_file, 'r', encoding='utf-8')
    dictionnary = yaml.load(fic_dic, Loader=yaml.BaseLoader)
    fic_dic.close()


    # Replacements start now
    text_new = text_all

    for i,val in dictionnary.items():
        tag_str = tag+str(i)+tag
        tag_str = rf" ?{tag} ?{i} ?{tag} ?"
        val = val.replace('\\','\\\\')    # double \\ for correct write
        # val = re.escape(val)
        text_new = re.sub(tag_str,val,text_new, flags=re.MULTILINE|re.DOTALL)


    # Write the result
    with open(tex_file, 'w', encoding='utf-8') as fic_tex:
        fic_tex.write(text_new)


