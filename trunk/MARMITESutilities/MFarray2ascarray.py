﻿# -*- coding: utf-8 -*-

import os

header_fn = r'E:\00code_ws\LAMATA_new\MF_ws\PEST\00header_asc.txt'
hk_PEST_fn = [r'E:\00code_ws\LAMATA_new\MF_ws\PEST\00hk_l1.ref', r'E:\00code_ws\LAMATA_new\MF_ws\PEST\00hk_l2.ref']
hk_MM_fn = [r'E:\00code_ws\LAMATA_new\MF_ws\00hk_l1.asc', r'E:\00code_ws\LAMATA_new\MF_ws\00hk_l2.asc']
ncol = 60

for l, (fin_fn, fout_fn) in enumerate(zip(hk_PEST_fn, hk_MM_fn)):

    if os.path.exists(fin_fn):
        fin = open(fin_fn, 'r')
    fout = open(fout_fn, 'w')

    if os.path.exists(header_fn):
        header = open(header_fn, 'r')

    for line in header:
        fout.write(line)

    fout.write('\n')

    fin.readline()
    ncol_tmp = 0
    for line in fin:
        line_tmp = line.split()
        for e in line_tmp:
            fout.write(e + ' ')
            ncol_tmp += 1
        if ncol_tmp == ncol:
            ncol_tmp = 0
            fout.write('\n')

    fin.close()
    fout.close()

header.close()

print 'Done!'
