#-*- encoding:utf8 -*-
'''
Created on 2013. 4. 16.

@author: stmkmk
'''
import os, sys

modules = ('PO','BOM','Plan','WIP','INV','QA','KPI','COST')


for module in modules:
    os.makedirs(module)
    