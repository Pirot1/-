#гипотеза
print('Гипотиза = В восточной европе рождаемость выше чем в западной Европе')

#библиотеки

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('countries_of_the_world.csv')

#замена NaN

df['Birthrate'].fillna('0',inplace = True)
df['Deathrate'].fillna('0',inplace = True)


#очистка данных в float64

def set_Agriculture(Birthrate):
    if Birthrate == '0':
        return 0
    return float(Birthrate.replace(',','.'))
def set_Industry(Deathrate):
    if Deathrate == '0':
        return 0
    return float(Deathrate.replace(',','.'))

#перевод данных

df['Birthrate'] = df['Birthrate'].apply(set_Agriculture)
df['Deathrate'] = df['Deathrate'].apply(set_Industry)




#Восток

birth = df[df['Region'] > 'EASTERN EUROPE']['Birthrate'].mean()
death = df[df['Region'] > 'EASTERN EUROPE']['Deathrate'].mean()

#Запад

birth1 = df[df['Region'] > 'WESTERN EUROPE']['Birthrate'].mean()
death1 = df[df['Region'] > 'WESTERN EUROPE']['Deathrate'].mean()

#график 1

s = pd.Series(data = [birth,death],index = ['Рождаемость','Смертность'])
s.plot(kind = 'pie',label = 'Естественный прирост')
plt.title('EASTERN EUROPE')
plt.show()

#график 2

s1 = pd.Series(data = [birth1,death1],index = ['Рождаемость','Смертность'])
s1.plot(kind = 'pie',label = 'Естественный прирост')
plt.title('WESTERN EUROPE')
plt.show()

#итог

print('Как вы видите по графику,рождаемость выше смертности,в Восточной Европе!\n Гипотеза подтверждена')

#допполнительный материал

#print(birth)
#print(death)
#print(birth1)
#print(death1)
#temp = df.head(60)
#print(temp)
#print(df.describe())
#print(df.info())