import requests, bs4

s=requests.get('https://sinoptik.com.ru/погода-амстердам')

b=bs4.BeautifulSoup(s.text, "html.parser")

p=b.select('.rSide .description')
pogoda=p[0].getText()
print(pogoda.strip() + "\n")

p3=b.select('.temperature .p3')
pogoda1=p3[0].getText()
p4=b.select('.temperature .p4')
pogoda2=p4[0].getText()
print('Утром: ' + pogoda1 + ' ' + pogoda2)

p5=b.select('.temperature .p5')
pogoda3=p5[0].getText()
p6=b.select('.temperature .p6')
pogoda4=p6[0].getText()
print('Днём: ' + pogoda3 + ' ' + pogoda4)

p7=b.select('.temperature .p7')
pogoda5=p7[0].getText()
p8=b.select('.temperature .p8')
pogoda6=p8[0].getText()
print('Вечером: ' + pogoda5 + ' ' + pogoda6)

p1=b.select('.temperature .p1')
pogoda7=p1[0].getText()
p2=b.select('.temperature .p2')
pogoda8=p2[0].getText()
print('Ночью: ' + pogoda7 + ' ' + pogoda8)


# Диапазон
p_min=b.select('.temperature .min')
pogoda_min=p_min[0].getText()
p_max=b.select('.temperature .max')
pogoda_max=p_max[0].getText()
print('\nСегодня: ' + pogoda_min + ' ' + pogoda_max)


# Диапазон прогноз на завтра и послезавтра
pogoda_min_1=p_min[1].getText()
pogoda_max_1=p_max[1].getText()
print('Завтра: ' + pogoda_min_1 + ' ' + pogoda_max_1)

pogoda_min_2=p_min[2].getText()
pogoda_max_2=p_max[2].getText()
print('Послезавтра: ' + pogoda_min_2 + ' ' + pogoda_max_2)
