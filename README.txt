TPI Programación I - Sistema de Gestión de Países

Alumno: Santiago Tomás Meza | Materia: Programación I | Docente Titular: Alberto Cortez | Docente Tutor: Matías Torres | Tecnicatura Universitaria en Programación - UTN | Fecha: Junio 2026

DESCRIPCIÓN
Aplicación en consola desarrollada en Python 3 que permite gestionar información de países (nombre, población, superficie, continente). Los datos se almacenan en un archivo CSV y se cargan al iniciar el programa.
El sistema incluye operaciones de: visualización en tabla alineada, agregar nuevos países (con validaciones), actualizar población y superficie, búsqueda por coincidencia parcial, filtrado por continente/rango de población/rango de superficie, ordenamiento ascendente/descendente por nombre/población/superficie, estadísticas (país con mayor/menor población, promedios, cantidad por continente), guardado manual o al salir.

INSTRUCCIONES DE EJECUCIÓN
1. Asegurar Python 3.x instalado.
2. Clonar el repositorio o descargar los archivos.
3. Colocar el archivo paises.csv en la misma carpeta que main.py.
4. Abrir una terminal en esa carpeta y ejecutar:
   python main.py

ESTRUCTURA DEL PROYECTO
TPI_Gestion_Paises/
├── main.py               # Código fuente completo
├── paises.csv            # Archivo CSV con datos iniciales
└── README.md             # Este archivo

EJEMPLOS DE USO

Mostrar países en tabla:
   Lista de Paises   
Nombre             | Población     | Superficie      | Continente
--------------------------------------------------------------------
Argentina          | 45376763      | 2780400    km²  | America
Brasil             | 213993437     | 8515767    km²  | America
Alemania           | 83149300      | 357022     km²  | Europa

Agregar un país:
   Agregar Pais   
Nombre del pais: Chile
Poblacion: 19500000
Superficie (km²): 756102
Seleccione un continente:
1. Africa
2. America
...
Opción: 2
País agregado correctamente.

Filtrar por continente:
   Filtrar Pais   
1. Por continente
...
Seleccione una opcion: 1
Seleccione un continente: 2 (America)
[se muestran solo países de América]

Ordenar por población descendente:
   Ordenar Pais   
1. Nombre
2. Poblacion
3. Superficie
Seleccione criterio: 2
Ascendente (A) o Descendente (D): D

   Paises Ordenados   
Nombre             | Población     | Superficie      | Continente
--------------------------------------------------------------------
Brasil             | 213993437     | 8515767    km²  | America
Japón              | 125800000     | 377975     km²  | Asia
...

Estadísticas:
   Estadisticas   
País con mayor población: Brasil (213993437)
País con menor población: Chile (19500000)
Promedio de población   : 123456789.00
Promedio de superficie  : 1234567.00 km²

Cantidad de países por continente:
 - America    : 3
 - Asia       : 2
 - Europa     : 1

VIDEO DEMOSTRATIVO
https://drive.google.com/file/d/1_DR_YMxeviso1-kmjguoPnaySOQneSgQ/view?usp=drive_link

INFORME PDF
https://github.com/Santiago0321/TPI-Gestion-Paises/blob/main/TPI_Programacion1_MezaSantiago.pdf

REQUISITOS TÉCNICOS
- Python 3.x estándar (sin bibliotecas externas).
- El archivo paises.csv debe tener el siguiente formato (con encabezado):
  nombre,poblacion,superficie,continente
  Argentina,45376763,2780400,America
  ...

ESTADO DEL PROYECTO
Completo – todas las funcionalidades implementadas y validadas.

CONTACTO
Ante cualquier duda, abrir un issue en el repositorio o contactar al alumno vía aula virtual.
