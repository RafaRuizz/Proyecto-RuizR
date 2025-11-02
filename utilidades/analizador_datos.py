# ==========================================
# ARCHIVO: utilidades/analizador_datos.py
# ==========================================

def calcular_estadisticas(listado_naciones):
    try:
        if not listado_naciones:
            print('Sin datos disponibles.')
            return
        
        if not isinstance(listado_naciones, list):
            raise TypeError('El parámetro "listado_naciones" debe ser lista')
        
        nacion_mas_poblada = max(listado_naciones, key=lambda elemento: elemento['poblacion'])
        nacion_menos_poblada = min(listado_naciones, key=lambda elemento: elemento['poblacion'])
        
        media_habitantes = sum(nacion['poblacion'] for nacion in listado_naciones) / len(listado_naciones)
        media_extension = sum(nacion['superficie'] for nacion in listado_naciones) / len(listado_naciones)
        
        print('\n==== ANÁLISIS ESTADÍSTICO ==== ')
        print(f'- Nación más poblada       : {nacion_mas_poblada["nombre"]} ({nacion_mas_poblada["poblacion"]:,})')
        print(f'- Nación menos poblada     : {nacion_menos_poblada["nombre"]} ({nacion_menos_poblada["poblacion"]:,})')
        print(f'- Media de habitantes      : {media_habitantes:,.0f}')
        print(f'- Media de extensión       : {media_extension:,.0f}')
        
        regiones_conteo = {}
        for nacion in listado_naciones:
            region = nacion['continente']
            regiones_conteo[region] = regiones_conteo.get(region, 0) + 1
        
        print('\nDistribución por región continental:')
        for region, cantidad in regiones_conteo.items():
            print(f'  - {region}: {cantidad}')
    
    except KeyError as error:
        print(f'\nALERTA: Algunas naciones carecen del campo {error}')
    except (TypeError, ValueError) as error:
        print(f'\nALERTA: {error}')
    except ZeroDivisionError:
        print('\nALERTA: Sin naciones para calcular medias')
    except Exception as error:
        print(f'\nALERTA: {error}')
