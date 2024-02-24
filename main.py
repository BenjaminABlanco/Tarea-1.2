import pandas as pd
datos = pd.read_csv('Fullmetadata.csv')
# print(datos)
print('\n')

print('Encuentra la cantidad de goles totales hechos por cada posición.')

columnas = datos[['position','goals']]
resultado = columnas.groupby('position')['goals'].sum().reset_index()
print(resultado)

print('\n')
print('¿Cuál fue el equipo que más goles hizo cada año?')

columnas = datos[['year', 'team_name', 'goals']]
condicion = columnas.groupby(['year','team_name'])['goals'].sum().reset_index(name='Total')
team_with_most_goals_by_year = condicion.loc[condicion.groupby('year')['Total'].idxmax()]
print(team_with_most_goals_by_year)

print('\n')
print('¿Cuál fue el jugador que más goles hizo cada año?')

columnas = datos[['year', 'player_name', 'goals']]
condicion = columnas.groupby(['year','player_name'])['goals'].sum().reset_index(name='Total')
player_with_max_goals_per_year = condicion.loc[condicion.groupby('year')['Total'].idxmax()]
print(player_with_max_goals_per_year)

print('\n')
print('¿Qué posición es la que más tiempo juega?')

col = datos[['position','time']]
mas = col.groupby('position')['time'].mean().nlargest(1)
print(mas)

print('\n')
print('¿Qué posición es la que menos tiempo juega?')

menos = datos.groupby('position')['time'].mean().nsmallest(1)
print(menos)

print('\n')
print('¿Qué porcentaje de goles son hechos con asistencias?')

total_goles = datos['goals'].sum()
total_asistencias = datos['assists'].sum()
total_goles_assists = (total_asistencias/total_goles)*100
print(f'{total_goles_assists} %')
print('\n')