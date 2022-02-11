'''
Задание 5.
Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
Например:

>>> get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]
Документировать код функции.

Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках (когда каждое слово можно использовать только в одной шутке)?
Сможете ли вы сделать аргументы именованными?
'''
import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(count: int) -> list:
    """Возвращает список шуток в количестве count"""
    list_out = []
   
    for i in range(count):  
        list_out.extend([random.choice(nouns) + " " + random.choice(adverbs) + " " + random.choice(adjectives)])
    return list_out

print(get_jokes(2))
print(get_jokes(10))

def get_jokes_adv(count: list, Flag: bool) -> list:
    """Возвращает список шуток в количестве count
    Если активирован флаг, шутки не повторяются"""
    list_out = []
   
    for i in range(count):

        if Flag == True and count > 5:
            print("You cannot use a value greater than 5")
            break
        
        elem_nouns = random.choice(nouns)
        elem_adverbs = random.choice(adverbs)
        elem_adjectives = random.choice(adjectives)

        list_out.extend([elem_nouns + " " + elem_adverbs + " " + elem_adjectives])
        
        if Flag == True:
            nouns.remove(elem_nouns)
            adverbs.remove(elem_adverbs)
            adjectives.remove(elem_adjectives)
   
    return list_out

print(get_jokes_adv(4, True))
