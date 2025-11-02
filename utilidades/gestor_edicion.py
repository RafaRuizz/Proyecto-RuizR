# ==========================================
# ARCHIVO: utilidades/gestor_edicion.py
# ==========================================

import csv
import os


def persistir_nacion(ruta_archivo, nacion):
    try:
        if not os.path.exists(ruta_archivo):
            raise FileNotFoundError("Archivo no localizado.")
        
        with open(ruta_archivo, mode='a', newline='', encoding='utf-8') as archivo:
            columnas = ["nombre", "poblacion", "superficie", "continente"]
            escritor = csv.DictWriter(archivo, fieldnames=columnas)
            escritor.writerow(nacion)
        return True
    
    except FileNotFoundError:
        print("Archivo no localizado.")
        return False
    except Exception as error:
        print(f"Error al guardar: {error}")
        return False


def registrar_nueva_nacion(listado_naciones, ruta_archivo):
    try:
        denominacion = input("Ingrese denominación de la nación: ").strip().lower()
        if not denominacion:
            raise ValueError("La denominación no puede estar vacía.")
        if any(caracter.isdigit() for caracter in denominacion):
            raise TypeError("La denominación no puede contener números.")
        
        habitantes = int(input("Ingrese cantidad de habitantes: "))
        if habitantes <= 0:
            raise ValueError("La cantidad de habitantes debe ser positiva.")
        
        extension = int(input("Ingrese extensión territorial (km²): "))
        if extension <= 0:
            raise ValueError("La extensión debe ser positiva.")
        
        while True:
            region = input("Ingrese región continental: ").strip().lower()
            if not region:
                raise ValueError("La región no puede estar vacía.")
            if any(caracter.isdigit() for caracter in region):
                raise TypeError("La región no puede contener números.")
            
            regiones_validas = ("asia", "america del norte", "america del sur", "oceania", "europa", "africa")
            
            if region not in regiones_validas:
                print(f"La región debe ser una de: {', '.join(regiones_validas)}")
            else:
                break
        
        nacion = {
            'nombre': denominacion,
            'poblacion': habitantes,
            'superficie': extension,
            'continente': region
        }
        
        if persistir_nacion(ruta_archivo, nacion):
            listado_naciones.append(nacion)
            print("\n✓ Nación registrada exitosamente.")
        else:
            print("\n✗ No se pudo registrar la nación.")
    
    except (ValueError, TypeError) as error:
        print(f"ALERTA: {error}. Intente nuevamente.")
    except Exception as error:
        print(f"Error inesperado: {error}")
