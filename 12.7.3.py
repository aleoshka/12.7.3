money = input('Какую сумму Вы хотите положить? ')
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
tkb = per_cent['ТКБ']/100*int(money)
skb = per_cent['СКБ']/100*int(money)
vtb = per_cent['ВТБ']/100*int(money)
sbr = per_cent['СКБ']/100*int(money)
total = tkb, skb, vtb, sbr
deposit = list(map(round, total))
print(deposit)
print('Максимальная сумма, которую Вы можете заработать —', max(deposit))
