'''
Задание 1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:

|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp

Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); 
как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект; 
можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?
'''

'''
Тут конечно можно было бы использовать просто словарь, но я решил вынести его в json.
Не понятно как работать в этом случае с еще одним уровнем вложенности ((
'''

import os
from pathlib import *
import json

current_dir = Path.cwd()

with open('dir_list.json') as f:
    content = json.load(f)

for i, (key, value) in enumerate(content.items()):
    key_dir = os.path.join(current_dir,  key)
    if not os.path.exists(key):
        os.mkdir(key)
        
    for val in value:
        val_dir = os.path.join(key_dir,  val)
        if not os.path.exists(val_dir):
            os.mkdir(val_dir)