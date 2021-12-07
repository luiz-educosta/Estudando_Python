"""
8. Digtar uma medida em metros e fazer as conversões correspondentes a
km, hm, dam, dm, cm, mm
"""
metro = float(input('Digite uma distância em metros:'))
km = metro / 1000
hm = metro / 100
dam = metro / 10
dm = metro * 10
cm = metro * 100
mm = metro * 1000

print(f'A medida de {metro} metros corresponde a:')
print(f'{km} km')
print(f'{hm} hm')
print(f'{dam} dam')
print(f'{dm} dm')
print(f'{cm} cm')
print(f'{mm} mm')