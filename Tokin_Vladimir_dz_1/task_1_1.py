'''
Задание 1
Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
до минуты: <s> сек;
до часа: <m> мин <s> сек;
до суток: <h> час <m> мин <s> сек;
в остальных случаях: <d> дн <h> час <m> мин <s> сек.
'''

def convert_time(duration: int) -> str:

    if duration <= 59:
        result = f'{duration} сек'

    if duration >= 60 and duration <= 3599:
        minutes = duration // 60
        seconds = duration % 60
        result = f'{minutes} мин {seconds} сек'

    if duration >= 3600 and duration <= 86399:
        hours = duration // 3600
        seconds = duration % 3600
        minutes = seconds // 60
        seconds = seconds % 60
        result = f'{hours} час {minutes} мин {seconds} сек'

    if duration >= 86400:
        days = duration // 86400
        seconds = duration % 86400
        hours = seconds // 3600
        seconds= duration % 3600
        minutes = seconds// 60
        seconds = seconds % 60
        result = f'{days} дн {hours} час {minutes} мин {seconds} сек'
    return result

duration = 84000
result = convert_time(duration)
print(result)