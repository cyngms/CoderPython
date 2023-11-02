champs = {1990: 'Alemania',
          1994: 'Brasil',
          1998: 'Francia',
          2002: 'Brasil',
          2006: 'Italia',
          2010: 'Espana',
          2014: 'Alemania',
          2018: 'Francia',
          2022: 'Argentina'}
print(champs)
year = int(input("Year?"))

if (year in champs):
    print(champs[year])
else:
    print("None")