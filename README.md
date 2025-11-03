El presente proyecto no incluye video, se defenderá y presentara frente al docente Hualpa

# 🌍 Sistema de Gestión de Naciones

## 📋 Descripción del Programa

Sistema integral de gestión de datos que permite administrar, consultar y analizar información sobre países del mundo. El programa trabaja con datos almacenados en formato CSV y ofrece funcionalidades completas de búsqueda, filtrado, ordenamiento, análisis estadístico y operaciones CRUD (Crear, Leer, Actualizar, Eliminar).

Desarrollado en Python 3.x, utiliza estructuras de datos nativas (listas y diccionarios), manejo de archivos CSV, y modularización mediante funciones especializadas. El sistema está diseñado para ser robusto, intuitivo y fácil de mantener.

### 🎯 Características Principales

- ✅ Búsqueda de naciones por nombre (coincidencia parcial, sin distinción de acentos)
- ✅ Filtrado por continente, rango de población y rango de superficie
- ✅ Ordenamiento múltiple (nombre, población, superficie) en orden ascendente o descendente
- ✅ Análisis estadístico automático (máximos, mínimos, promedios, distribución geográfica)
- ✅ Sistema de navegación paginada para visualizar grandes conjuntos de datos
- ✅ Operaciones CRUD completas (agregar, modificar, eliminar naciones)
- ✅ Persistencia de datos en archivo CSV
- ✅ Validación exhaustiva de entradas y manejo robusto de errores

---

## 🗂️ Estructura del Proyecto

```
proyecto-naciones/
│
├── naciones_proyecto.py          # Archivo principal (punto de entrada)
│
├── datos/
│   └── naciones_globales.csv     # Base de datos en formato CSV
│
└── utilidades/                   # Paquete de módulos
    ├── __init__.py               # Inicializador del paquete
    ├── cargador_datos.py         # Lectura/escritura de archivos CSV
    ├── interfaz_usuario.py       # Presentación del menú principal
    ├── manejadores_opciones.py   # Procesamiento de opciones del menú
    ├── procesadores.py           # Funciones de búsqueda y filtrado
    ├── organizador.py            # Funciones de ordenamiento
    ├── analizador_datos.py       # Cálculos estadísticos
    ├── visualizador.py           # Sistema de presentación con navegación
    └── gestor_edicion.py         # Operaciones de agregar naciones
```

### 📊 Estructura de Datos

Cada nación se representa como un diccionario con la siguiente estructura:

```python
{
    'nombre': 'Argentina',
    'poblacion': 45376763,
    'superficie': 2780400,
    'continente': 'america del sur'
}
```

**Formato del archivo CSV:**
```csv
nombre,poblacion,superficie,continente
argentina,45376763,2780400,america del sur
japon,125800000,377975,asia
brasil,213993437,8515767,america del sur
alemania,83149300,357022,europa
```

---

## 🚀 Instrucciones de Uso

### Requisitos Previos

- Python 3.10 o superior (utiliza características modernas como `match-case`)
- Bibliotecas estándar de Python (no requiere instalación adicional)

### Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/RafaRuizz/ProyectoRuizR.git
   cd ProyectoRuizR
   ```

2. **Verificar estructura de carpetas:**
   ```bash
   # Asegúrese de que existe la carpeta 'utilidades' y 'datos'
   # Si no existe, el programa creará automáticamente el CSV
   ```

3. **Ejecutar el programa:**
   ```bash
   python naciones_proyecto.py
   ```

### Uso del Sistema

Al iniciar el programa, verás el menú principal con 10 opciones:

```
==== SISTEMA DE GESTIÓN DE NACIONES ====

1) Buscar nación por denominación
2) Filtrar naciones por región continental
3) Filtrar por intervalo de habitantes
4) Filtrar por intervalo de área territorial
5) Ordenar listado de naciones
6) Visualizar análisis estadístico
7) Registrar nueva nación
8) Modificar datos de nación
9) Remover nación
10) Finalizar programa

Seleccione una opción (número):
```

---

## 💡 Ejemplos de Entradas y Salidas

### Ejemplo 1: Buscar Nación

**Entrada:**
```
Seleccione una opción: 1
Ingrese denominación de nación: arg
```

**Salida:**
```
================================================================================
Naciones que coinciden con "arg"
Mostrando 1 elemento
================================================================================

  1. argentina - america del sur

--------------------------------------------------------------------------------
Presione Enter para continuar...
```

---

### Ejemplo 2: Filtrar por Continente

**Entrada:**
```
Seleccione una opción: 2
Ingrese región continental: europa
```

**Salida:**
```
================================================================================
Naciones en Europa
Sección 1 de 1 | Mostrando 1-3 de 3 elementos
================================================================================

  1. alemania - europa
  2. francia - europa
  3. españa - europa

--------------------------------------------------------------------------------
Enter = Volver al inicio | T = Terminar
--------------------------------------------------------------------------------
```

---

### Ejemplo 3: Filtrar por Rango de Población

**Entrada:**
```
Seleccione una opción: 3
Ingrese habitantes mínimos: 50000000
Ingrese habitantes máximos: 150000000
```

**Salida:**
```
================================================================================
Naciones con habitantes entre 50,000,000 y 150,000,000
Sección 1 de 1 | Mostrando 1-4 de 4 elementos
================================================================================

  1. alemania: 83,149,300 habitantes
  2. francia: 67,399,000 habitantes
  3. italia: 59,554,000 habitantes
  4. españa: 47,351,567 habitantes

--------------------------------------------------------------------------------
```

---

### Ejemplo 4: Ordenar por Población

**Entrada:**
```
Seleccione una opción: 5
Ordenar por: poblacion
¿Orden descendente? (s/n): s
```

**Salida:**
```
================================================================================
Naciones ordenadas por poblacion (descendente)
Sección 1 de 2 | Mostrando 1-10 de 15 elementos
================================================================================

  1. china: 1,412,000,000 habitantes
  2. india: 1,380,000,000 habitantes
  3. estados unidos: 331,900,000 habitantes
  4. indonesia: 273,500,000 habitantes
  5. pakistan: 225,200,000 habitantes
  6. brasil: 213,993,437 habitantes
  7. nigeria: 211,400,000 habitantes
  8. bangladesh: 169,800,000 habitantes
  9. rusia: 145,900,000 habitantes
  10. mexico: 128,900,000 habitantes

--------------------------------------------------------------------------------
Enter = Siguiente | [Número] = Ir a sección | T = Terminar
--------------------------------------------------------------------------------
```

---

### Ejemplo 5: Análisis Estadístico

**Entrada:**
```
Seleccione una opción: 6
```

**Salida:**
```
==== ANÁLISIS ESTADÍSTICO ====
- Nación más poblada       : china (1,412,000,000)
- Nación menos poblada     : vaticano (800)
- Media de habitantes      : 37,500,000
- Media de extensión       : 275,000

Distribución por región continental:
  - asia: 48
  - europa: 44
  - africa: 54
  - america del norte: 23
  - america del sur: 12
  - oceania: 14
```

---

### Ejemplo 6: Agregar Nueva Nación

**Entrada:**
```
Seleccione una opción: 7
Ingrese denominación de la nación: uruguay
Ingrese cantidad de habitantes: 3473727
Ingrese extensión territorial (km²): 176215
Ingrese región continental: america del sur
```

**Salida:**
```
✓ Nación registrada exitosamente.
```

---

### Ejemplo 7: Modificar Nación

**Entrada:**
```
Seleccione una opción: 8

Naciones disponibles:
1. argentina
2. brasil
3. chile

Ingrese el número de la nación a modificar (0 para cancelar): 1

Modificando: argentina
Población actual: 45,376,763
Superficie actual: 2,780,400
Continente actual: america del sur

(Presione Enter para mantener el valor actual)
Nuevo nombre [argentina]: 
Nueva población [45,376,763]: 46000000
Nueva superficie [2,780,400]: 
Nuevo continente [america del sur]: 
```

**Salida:**
```
✓ Nación modificada exitosamente.
```

---

### Ejemplo 8: Eliminar Nación

**Entrada:**
```
Seleccione una opción: 9

Naciones disponibles:
1. argentina
2. brasil
3. chile

Ingrese el número de la nación a eliminar (0 para cancelar): 3
¿Está seguro de eliminar 'chile'? (s/n): s
```

**Salida:**
```
✓ Nación 'chile' eliminada exitosamente.
```

---

## 🔧 Funcionalidades Detalladas

### 1️⃣ Búsqueda de Naciones
- Búsqueda por coincidencia parcial (buscar "arg" encuentra "Argentina")
- Sin distinción entre mayúsculas y minúsculas
- Elimina acentos para mejorar resultados (buscar "Mexico" encuentra "México")
- Validación: no permite campos vacíos ni números en el nombre

### 2️⃣ Filtros Disponibles

**Por Continente:**
- Regiones válidas: Asia, América del Norte, América del Sur, Oceanía, Europa, África
- Comparación sin distinción de mayúsculas ni acentos

**Por Población:**
- Rango de habitantes (mínimo y máximo)
- Validación de números positivos
- Verificación de rango coherente (mínimo ≤ máximo)

**Por Superficie:**
- Rango de área territorial en km²
- Mismas validaciones que población

### 3️⃣ Ordenamiento
**Criterios disponibles:**
- Nombre (alfabético)
- Población (numérico)
- Superficie (numérico)

**Modos:**
- Ascendente (A-Z, menor a mayor)
- Descendente (Z-A, mayor a menor)

### 4️⃣ Estadísticas Calculadas
- Nación con mayor población
- Nación con menor población
- Promedio de población mundial
- Promedio de superficie territorial
- Cantidad de naciones por continente

### 5️⃣ Operaciones CRUD
- **Create:** Agregar nuevas naciones con validación completa
- **Read:** Lectura automática al iniciar el programa
- **Update:** Modificar cualquier campo de una nación existente
- **Delete:** Eliminar naciones con confirmación de seguridad

### 6️⃣ Sistema de Navegación
- Visualización paginada (10 elementos por página)
- Controles intuitivos:
  - **Enter:** Siguiente página
  - **R:** Página anterior
  - **[Número]:** Ir a página específica
  - **T:** Terminar y volver al menú

---

## 🛡️ Validaciones y Manejo de Errores

### Validaciones Implementadas

✅ **Entrada de Texto:**
- Campos no pueden estar vacíos
- Nombres y regiones no pueden contener números
- Normalización automática (minúsculas, sin acentos)

✅ **Entrada Numérica:**
- Solo acepta números enteros positivos
- Validación de rangos coherentes (min ≤ max)
- Manejo de conversiones inválidas

✅ **Operaciones con Archivos:**
- Creación automática de archivo CSV si no existe
- Verificación de permisos de lectura/escritura
- Manejo de archivos corruptos o con formato incorrecto

✅ **Selecciones de Usuario:**
- Índices válidos al seleccionar naciones
- Confirmaciones antes de operaciones destructivas
- Opciones de cancelación en todas las operaciones

### Excepciones Manejadas

- `ValueError` - Conversiones numéricas inválidas
- `TypeError` - Tipos de datos incorrectos
- `KeyError` - Campos faltantes en diccionarios
- `FileNotFoundError` - Archivos no encontrados
- `PermissionError` - Sin permisos de acceso
- `KeyboardInterrupt` - Interrupción por Ctrl+C
- `Exception` - Errores genéricos no esperados

---

## 👤 Autor del Proyecto

### Rafael Ruiz

**Desarrollo completo del sistema:**
- Arquitectura y diseño de la estructura modular
- Implementación de todos los módulos del paquete `utilidades/`
- Desarrollo de módulos de búsqueda y filtrado (`procesadores.py`)
- Implementación del sistema de navegación paginada (`visualizador.py`)
- Desarrollo del módulo de carga y persistencia de datos (`cargador_datos.py`)
- Implementación de operaciones CRUD completas (`gestor_edicion.py`, `manejadores_opciones.py`)
- Módulo de análisis estadístico (`analizador_datos.py`)
- Sistema de ordenamiento (`organizador.py`)
- Interfaz de usuario y menú principal (`interfaz_usuario.py`)
- Validaciones exhaustivas y manejo de errores
- Documentación y comentarios del código
- Pruebas de integración y casos de uso
- Elaboración de documentación técnica

---

## 📚 Conceptos Aplicados

### Estructuras de Datos
- **Listas:** Almacenamiento dinámico de múltiples naciones
- **Diccionarios:** Representación estructurada de cada nación con claves descriptivas
- **List Comprehensions:** Filtrado eficiente de datos

### Programación Funcional
- Modularización: una función = una responsabilidad
- Funciones de orden superior (`map`, `filter`, `sorted`)
- Expresiones lambda para operaciones concisas

### Control de Flujo
- `match-case` para el menú principal (Python 3.10+)
- Bucles `while` para navegación y repetición de operaciones
- Estructuras condicionales anidadas para validaciones

### Manejo de Archivos
- Context managers (`with`) para operación segura de archivos
- Módulo `csv` para lectura y escritura estructurada
- Creación automática de archivos inexistentes

### Algoritmos
- Ordenamiento con `sorted()` y funciones key
- Búsqueda lineal con normalización de texto
- Cálculos estadísticos (min, max, promedio, conteo)

---

## 🔄 Flujo de Operaciones

```
1. INICIO → Cargar datos desde CSV
              ↓
2. ¿Archivo existe? → NO → Crear archivo vacío
              ↓ SÍ
3. Leer y parsear datos
              ↓
4. Mostrar MENÚ PRINCIPAL
              ↓
5. Capturar opción del usuario
              ↓
6. ¿Opción válida? → NO → Mostrar error → Volver a 4
              ↓ SÍ
7. Ejecutar función correspondiente
              ↓
8. ¿Operación modifica datos? → SÍ → Guardar en CSV
              ↓ NO
9. Mostrar resultados
              ↓
10. ¿Usuario quiere continuar? → SÍ → Volver a 4
              ↓ NO
11. ¿Salir del programa? → SÍ → FIN
              ↓ NO
12. Volver a 4
```

---

## 📖 Bibliografía

- Python Software Foundation. (2024). *Python 3.12 Documentation*. https://docs.python.org/3/
- Van Rossum, G., & Drake, F. L. (2009). *Python 3 Reference Manual*. CreateSpace.
- McKinney, W. (2017). *Python for Data Analysis*. O'Reilly Media.
- Lutz, M. (2013). *Learning Python* (5th ed.). O'Reilly Media.
- Documentación oficial del módulo CSV: https://docs.python.org/3/library/csv.html

---

## 📄 Licencia

Este proyecto fue desarrollado como Trabajo Práctico Integrador para la materia **Programación 1** de la **Tecnicatura Universitaria en Programación**.

---

**Fecha de entrega:** [Completar con fecha]  
**Institución:** Tecnicatura Universitaria en Programación  
**Materia:** Programación 1  
**Docente:** Rigoni Cinthia  
**Estudiante:** Rafael Ruiz
