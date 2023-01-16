money = input('Какую сумму Вы хотите положить? ')
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
a = per_cent['ТКБ']/100*int(money)
b = per_cent['СКБ']/100*int(money)
c = per_cent['ВТБ']/100*int(money)
d = per_cent['СКБ']/100*int(money)
R = a, b, c, d
deposit = list(map(round, R))
print(deposit)
print('Максимальная сумма, которую Вы можете заработать —', max(deposit))