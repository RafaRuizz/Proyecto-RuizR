# ==========================================
# ARCHIVO: utilidades/manejadores_opciones.py
# ==========================================

from .procesadores import localizar_nacion, aplicar_filtro_region, aplicar_filtro_intervalo
from .organizador import organizar_naciones
from .analizador_datos import calcular_estadisticas
from .visualizador import presentar_con_navegacion
from .gestor_edicion import registrar_nueva_nacion
import csv
import os


def solicitar_confirmacion(pregunta):
    while True:
        respuesta = input(pregunta).strip().lower()
        if respuesta in ('s', 'n'):
            return respuesta == 's'
        print('Respuesta no válida. Ingrese "s" para sí o "n" para no.')


def ejecutar_busqueda_nacion(listado_naciones):
    while True:
        try:
            denominacion = input('Ingrese denominación de nación: ').strip()
            
            if not denominacion:
                raise ValueError('La denominación no puede estar vacía')
            elif any(char.isdigit() for char in denominacion):
                raise TypeError('La denominación no puede contener dígitos')
            
            coincidencias = localizar_nacion(listado_naciones, denominacion)
            
            if coincidencias:
                presentar_con_navegacion(coincidencias, encabezado=f'Naciones que coinciden con "{denominacion}"')
            else:
                print('Sin coincidencias encontradas.')
        
        except (ValueError, TypeError) as error:
            print(f'\nALERTA: {error}. Intente nuevamente.\n')
            continue

        if not solicitar_confirmacion('\n¿Realizar otra búsqueda? (s/n): '):
            break


def ejecutar_filtro_region(listado_naciones):
    while True:
        try:
            region = input('Ingrese región continental: ').strip()
            
            if not region:
                raise ValueError('La región no puede estar vacía')
            elif any(char.isdigit() for char in region):
                raise TypeError('La región no puede contener dígitos')
            
            coincidencias = aplicar_filtro_region(listado_naciones, region)
            
            if coincidencias:
                presentar_con_navegacion(coincidencias, encabezado=f'Naciones en {region.title()}')
            else:
                print(f'Sin naciones en la región "{region}".')
        
        except Exception as error:
            print(f'\nALERTA: {error}. Intente nuevamente.\n')
            continue

        if not solicitar_confirmacion('\n¿Filtrar otra región? (s/n): '):
            break


def ejecutar_filtro_habitantes(listado_naciones):
    while True:
        try:
            try:
                limite_inf = int(input('Ingrese habitantes mínimos: ').strip())
                limite_sup = int(input('Ingrese habitantes máximos: ').strip())
            except ValueError:
                raise ValueError('Debe ingresar únicamente números enteros positivos')
            
            if limite_inf < 0 or limite_sup < 0:
                raise ValueError('Los valores deben ser positivos')
            if limite_inf > limite_sup:
                raise ValueError('El mínimo no puede superar el máximo')

            coincidencias = aplicar_filtro_intervalo(listado_naciones, 'poblacion', limite_inf, limite_sup)
            if coincidencias:
                presentar_con_navegacion(
                    coincidencias,
                    encabezado=f'Naciones con habitantes entre {limite_inf:,} y {limite_sup:,}',
                    estilo_presentacion='habitantes'
                )
            else:
                print('Sin naciones en ese intervalo de habitantes.')

        except Exception as error:
            print(f'\nALERTA: {error}. Intente nuevamente.\n')
            continue

        if not solicitar_confirmacion('\n¿Filtrar otro intervalo de habitantes? (s/n): '):
            break


def ejecutar_filtro_area(listado_naciones):
    while True:
        try:
            try:
                limite_inf = int(input('Ingrese extensión mínima (km²): ').strip())
                limite_sup = int(input('Ingrese extensión máxima (km²): ').strip())
            except ValueError:
                raise ValueError('Debe ingresar únicamente números enteros positivos')
            
            if limite_inf < 0 or limite_sup < 0:
                raise ValueError('Los valores deben ser positivos')
            if limite_inf > limite_sup:
                raise ValueError('El mínimo no puede superar el máximo')

            coincidencias = aplicar_filtro_intervalo(listado_naciones, 'superficie', limite_inf, limite_sup)
            if coincidencias:
                presentar_con_navegacion(
                    coincidencias,
                    encabezado=f'Naciones con extensión entre {limite_inf:,} y {limite_sup:,} km²',
                    estilo_presentacion='extension'
                )
            else:
                print('Sin naciones en ese intervalo de extensión.')

        except Exception as error:
            print(f'\nALERTA: {error}. Intente nuevamente.')
            continue

        if not solicitar_confirmacion('\n¿Filtrar otro intervalo de extensión? (s/n): '):
            break


def ejecutar_ordenamiento_naciones(listado_naciones):
    while True:
        try:
            print('\nCriterios de ordenamiento disponibles:')
            print('  - nombre')
            print('  - poblacion')
            print('  - superficie\n')
            
            criterio = input('Ordenar por: ').lower().strip()
            
            if not criterio:
                raise ValueError('Debe ingresar un criterio de ordenamiento')
            
            criterios_validos = ['nombre', 'poblacion', 'superficie']
            if criterio not in criterios_validos:
                raise ValueError(f'Criterio inválido. Use: {", ".join(criterios_validos)}')
            
            orden_desc = solicitar_confirmacion('¿Orden descendente? (s/n): ')
            
            resultados_ordenados = organizar_naciones(listado_naciones, criterio, orden_desc)
            
            if resultados_ordenados:
                tipo_orden = 'descendente' if orden_desc else 'ascendente'
                
                if criterio == 'poblacion':
                    estilo = 'habitantes'
                elif criterio == 'superficie':
                    estilo = 'extension'
                else:
                    estilo = 'basico'
                
                presentar_con_navegacion(
                    resultados_ordenados,
                    encabezado=f'Naciones ordenadas por {criterio} ({tipo_orden})',
                    estilo_presentacion=estilo
                )
            else:
                print('\nSin naciones para ordenar.')
        
        except Exception as error:
            print(f'\nALERTA: {error}. Intente nuevamente.')
            continue

        if not solicitar_confirmacion('\n¿Ordenar de otra forma? (s/n): '):
            break


def ejecutar_analisis_estadistico(listado_naciones):
    try:
        calcular_estadisticas(listado_naciones)
    except Exception as error:
        print(f'Error al calcular estadísticas: {error}')


def ejecutar_agregar_nacion(listado_naciones, ruta_archivo):
    print("\n==== REGISTRAR NUEVA NACIÓN ====")
    try:
        registrar_nueva_nacion(listado_naciones, ruta_archivo)
    except Exception as error:
        print(f'Error al registrar nación: {error}')


def ejecutar_modificar_nacion(listado_naciones, ruta_archivo):
    print("\n==== MODIFICAR DATOS DE NACIÓN ====")
    
    if not listado_naciones:
        print("No hay naciones registradas para modificar.")
        return
    
    try:
        # Mostrar lista de naciones
        print("\nNaciones disponibles:")
        for idx, nacion in enumerate(listado_naciones, 1):
            print(f"{idx}. {nacion['nombre']}")
        
        seleccion = input("\nIngrese el número de la nación a modificar (0 para cancelar): ").strip()
        
        if not seleccion.isdigit():
            raise ValueError("Debe ingresar un número válido")
        
        indice = int(seleccion) - 1
        
        if indice == -1:
            print("Operación cancelada.")
            return
        
        if indice < 0 or indice >= len(listado_naciones):
            raise ValueError("Número de nación inválido")
        
        nacion_actual = listado_naciones[indice]
        print(f"\nModificando: {nacion_actual['nombre']}")
        print(f"Población actual: {nacion_actual['poblacion']:,}")
        print(f"Superficie actual: {nacion_actual['superficie']:,}")
        print(f"Continente actual: {nacion_actual['continente']}")
        
        # Solicitar nuevos datos
        print("\n(Presione Enter para mantener el valor actual)")
        
        nuevo_nombre = input(f"Nuevo nombre [{nacion_actual['nombre']}]: ").strip()
        if nuevo_nombre:
            nacion_actual['nombre'] = nuevo_nombre
        
        nueva_poblacion = input(f"Nueva población [{nacion_actual['poblacion']:,}]: ").strip()
        if nueva_poblacion:
            nacion_actual['poblacion'] = int(nueva_poblacion)
        
        nueva_superficie = input(f"Nueva superficie [{nacion_actual['superficie']:,}]: ").strip()
        if nueva_superficie:
            nacion_actual['superficie'] = int(nueva_superficie)
        
        nuevo_continente = input(f"Nuevo continente [{nacion_actual['continente']}]: ").strip()
        if nuevo_continente:
            nacion_actual['continente'] = nuevo_continente
        
        # Guardar cambios en el archivo
        with open(ruta_archivo, mode='w', newline='', encoding='utf-8') as archivo:
            columnas = ['nombre', 'poblacion', 'superficie', 'continente']
            escritor = csv.DictWriter(archivo, fieldnames=columnas)
            escritor.writeheader()
            escritor.writerows(listado_naciones)
        
        print("\n✓ Nación modificada exitosamente.")
    
    except ValueError as error:
        print(f"\nALERTA: {error}")
    except Exception as error:
        print(f"\nError al modificar nación: {error}")


def ejecutar_eliminar_nacion(listado_naciones, ruta_archivo):
    print("\n==== REMOVER NACIÓN ====")
    
    if not listado_naciones:
        print("No hay naciones registradas para eliminar.")
        return
    
    try:
        # Mostrar lista de naciones
        print("\nNaciones disponibles:")
        for idx, nacion in enumerate(listado_naciones, 1):
            print(f"{idx}. {nacion['nombre']}")
        
        seleccion = input("\nIngrese el número de la nación a eliminar (0 para cancelar): ").strip()
        
        if not seleccion.isdigit():
            raise ValueError("Debe ingresar un número válido")
        
        indice = int(seleccion) - 1
        
        if indice == -1:
            print("Operación cancelada.")
            return
        
        if indice < 0 or indice >= len(listado_naciones):
            raise ValueError("Número de nación inválido")
        
        nacion_eliminar = listado_naciones[indice]
        
        # Confirmar eliminación
        confirmacion = input(f"\n¿Está seguro de eliminar '{nacion_eliminar['nombre']}'? (s/n): ").strip().lower()
        
        if confirmacion != 's':
            print("Operación cancelada.")
            return
        
        # Eliminar de la lista
        listado_naciones.pop(indice)
        
        # Guardar cambios en el archivo
        with open(ruta_archivo, mode='w', newline='', encoding='utf-8') as archivo:
            columnas = ['nombre', 'poblacion', 'superficie', 'continente']
            escritor = csv.DictWriter(archivo, fieldnames=columnas)
            escritor.writeheader()
            escritor.writerows(listado_naciones)
        
        print(f"\n✓ Nación '{nacion_eliminar['nombre']}' eliminada exitosamente.")
    
    except ValueError as error:
        print(f"\nALERTA: {error}")
    except Exception as error:
        print(f"\nError al eliminar nación: {error}")