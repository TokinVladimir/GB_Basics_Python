'''
Задание 3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике). 
Написать скрипт, который собирает все шаблоны в одну папку templates, например:

|--my_project
   ...
   |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html

Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках 
(они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача, которая решена,
например, во фреймворке django.
'''

import os
import shutil
 
ROOT_DIR = os.path.join(os.path.dirname(__file__), 'my_project')
TMPL_DIR = os.path.join(os.path.dirname(__file__), 'my_project', 'templates')

if not os.path.exists(TMPL_DIR):
    os.mkdir(TMPL_DIR)

for root, dirs, files in os.walk(ROOT_DIR):
    if root.count('templates'):
        for _dir in dirs:
            if not os.path.exists(os.path.join(TMPL_DIR, _dir)):
                src_dir = os.path.join(root, _dir)
                dst_dir = os.path.join(TMPL_DIR, _dir)
                shutil.copytree(src_dir, dst_dir)