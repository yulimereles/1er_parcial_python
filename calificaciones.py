import pandas as pd
import matplotlib.pyplot as plt

# Datos de calificaciones
calificaciones = [
    {"nombre": "Juan", "matematicas": 85, "ciencias": 90, "historia": 75},
    {"nombre": "María", "matematicas": 70, "ciencias": 80, "historia": 85},
    {"nombre": "Pedro", "matematicas": 95, "ciencias": 75, "historia": 90},
    {"nombre": "Ana", "matematicas": 80, "ciencias": 85, "historia": 80},
    {"nombre": "Luis", "matematicas": 75, "ciencias": 70, "historia": 95},
    {"nombre": "Sofía", "matematicas": 90, "ciencias": 85, "historia": 75},
    {"nombre": "Carlos", "matematicas": 85, "ciencias": 90, "historia": 80},
    {"nombre": "Elena", "matematicas": 70, "ciencias": 75, "historia": 85},
    {"nombre": "Javier", "matematicas": 80, "ciencias": 85, "historia": 90},
    {"nombre": "Laura", "matematicas": 75, "ciencias": 70, "historia": 95},
    {"nombre": "Diego", "matematicas": 90, "ciencias": 85, "historia": 75},
    {"nombre": "Paula", "matematicas": 85, "ciencias": 90, "historia": 80},
    {"nombre": "Carmen", "matematicas": 70, "ciencias": 75, "historia": 85}
]

datos_estudiantes = pd.DataFrame(calificaciones)

# Calculando promedios y porcentajes de aprobación
matematica_promedio = datos_estudiantes['matematicas'].mean()
ciencias_promedio = datos_estudiantes['ciencias'].mean()
historia_promedio = datos_estudiantes['historia'].mean()

aprobados_matematica = (datos_estudiantes['matematicas'] >= 60).mean() * 100
aprobados_ciencias = (datos_estudiantes['ciencias'] >= 60).mean() * 100
aprobados_historia = (datos_estudiantes['historia'] >= 60).mean() * 100

# Estudiantes con las calificaciones más altas
top_mate = datos_estudiantes.loc[datos_estudiantes['matematicas'].idxmax()]
top_ciencia = datos_estudiantes.loc[datos_estudiantes['ciencias'].idxmax()]
top_historia = datos_estudiantes.loc[datos_estudiantes['historia'].idxmax()]

# Creando el DataFrame de Frecuencia
df_estudiantes_frecuencia = pd.DataFrame([
    {'Nombre': estudiante['nombre'], 'Promedio': (estudiante['matematicas'] + estudiante['ciencias'] + estudiante['historia']) / 3}
    for estudiante in calificaciones
])

# Mostrando resultados
print('Promedio  calificaciones:')
print(f'Matemáticas: {matematica_promedio}')
print(f'Ciencias: {ciencias_promedio}')
print(f'Historia: {historia_promedio}')

print('\n Estudiantes que aprobaron:')
print(f'Matemáticas: {aprobados_matematica}%')
print(f'Ciencias: {aprobados_ciencias}%')
print(f'Historia: {aprobados_historia}%')

print('\n Calificaciones más altas:')
print(f'Matemáticas: {top_mate["nombre"]} - {top_mate["matematicas"]}')
print(f'Ciencias: {top_ciencia["nombre"]} - {top_ciencia["ciencias"]}')
print(f'Historia: {top_historia["nombre"]} - {top_historia["historia"]}')

# Gráfico de promedio de estudiantes
plt.plot(df_estudiantes_frecuencia['Nombre'], df_estudiantes_frecuencia['Promedio'])
plt.xlabel('Nombre')
plt.ylabel('Promedio')
plt.title('Promedio de Estudiantes')
plt.grid()
plt.show()
