'''
Created on 2013. 4. 1.

@author: stmkmk

'''
import os, glob

ROOT_DIR = r'D:\rollin-check'
formList = glob.glob(os.path.join(ROOT_DIR,'source_form_0327','*.fmb'))


for formName in formList:
    command = 'frmcmp.exe batch=yes module_type=form userid=devs/devs@erpprod forms_doc=YES WINDOW_STATE=MINIMIZE module='+formName
    os.system(command)