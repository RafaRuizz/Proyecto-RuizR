# ==========================================
# ARCHIVO: utilidades/cargador_datos.py
# ==========================================

import csv
import os


def generar_csv(ruta_destino):
    try:
        if not isinstance(ruta_destino, str):
            raise TypeError('El parámetro "ruta_destino" debe ser texto')
        
        carpeta_destino = os.path.dirname(ruta_destino)
        
        if carpeta_destino and not os.path.exists(carpeta_destino):
            os.makedirs(carpeta_destino)
            print(f'Carpeta creada: {carpeta_destino}')
        
        with open(ruta_destino, mode='w', newline='', encoding='utf-8') as archivo_csv:
            columnas = ['nombre', 'poblacion', 'superficie', 'continente']
            escritor_csv = csv.DictWriter(archivo_csv, fieldnames=columnas)
            escritor_csv.writeheader()
        
        print(f'Archivo CSV generado en: {ruta_destino}')
        print(f'  Columnas: {", ".join(columnas)}')
        return True
    
    except PermissionError:
        print(f'\nALERTA: Sin permisos para crear archivo en: {ruta_destino}')
        return False
    
    except OSError as error:
        print(f'\nALERTA: Error del sistema al generar archivo - {error}')
        return False
    
    except Exception as error:
        print(f'\nALERTA: Error no esperado al generar archivo - {error}')
        return False


def cargar_informacion_csv(ruta_archivo, auto_crear=True):
    listado_naciones = []
    
    try:
        if not os.path.exists(ruta_archivo):
            if auto_crear:
                print(f'\nArchivo no localizado: {ruta_archivo}')
                print('\nALERTA: Generando archivo CSV nuevo')
                
                if generar_csv(ruta_archivo):
                    print('\nEl archivo está vacío. Agregue naciones manualmente.')
                    return []
                else:
                    raise FileNotFoundError(f'No fue posible crear: {ruta_archivo}')
            else:
                raise FileNotFoundError(f'Archivo no localizado: {ruta_archivo}')
        
        with open(ruta_archivo, encoding='utf-8') as archivo_csv:
            lector_csv = csv.DictReader(archivo_csv)
            
            for num_linea, linea in enumerate(lector_csv, start=2):
                try:
                    nacion = {
                        'nombre': linea["nombre"].strip(),
                        'poblacion': int(linea["poblacion"]),
                        'superficie': int(linea["superficie"]),
                        'continente': linea["continente"].strip()
                    }
                    listado_naciones.append(nacion)
                except KeyError as error:
                    print(f'\nALERTA: Campo faltante {error} en línea {num_linea}')
                except ValueError as error:
                    print(f'\nALERTA: Dato inválido en línea {num_linea} - {error}')
        
        if len(listado_naciones) != 0:
            print(f'Cargadas {len(listado_naciones)} naciones exitosamente')
        else:
            print("CSV sin información, por favor ingrese datos.")
    
    except (FileNotFoundError, PermissionError) as error:
        print(f'\nALERTA: {error}')
    except Exception as error:
        print(f'\nALERTA: {error}')
    
    return listado_naciones
