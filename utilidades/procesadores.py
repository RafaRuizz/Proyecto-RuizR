# ==========================================
# ARCHIVO: utilidades/procesadores.py
# ==========================================

import unicodedata


def eliminar_acentos(cadena_texto):
    return ''.join(
        caracter for caracter in unicodedata.normalize('NFD', cadena_texto)
        if unicodedata.category(caracter) != 'Mn'
    )


def localizar_nacion(listado_naciones, denominacion):
    try:
        if not isinstance(listado_naciones, list):
            raise TypeError("El parámetro 'listado_naciones' debe ser lista")
        if not isinstance(denominacion, str):
            raise TypeError("El parámetro 'denominacion' debe ser texto")
        
        coincidencias = [
            nacion for nacion in listado_naciones 
            if eliminar_acentos(denominacion.lower()) in eliminar_acentos(nacion["nombre"].lower())
        ]
        return coincidencias
    
    except KeyError:
        print("\nALERTA: Algunas naciones carecen del campo 'nombre'")
        return []
    except (TypeError, AttributeError) as error:
        print(f"\nALERTA: {error}")
        return []


def aplicar_filtro_region(listado_naciones, region_continental):
    try:
        if not isinstance(listado_naciones, list):
            raise TypeError("El parámetro 'listado_naciones' debe ser lista")
        if not isinstance(region_continental, str):
            raise TypeError("El parámetro 'region_continental' debe ser texto")
        
        return [
            nacion for nacion in listado_naciones 
            if eliminar_acentos(nacion["continente"].lower()) == eliminar_acentos(region_continental.lower())
        ]
    
    except KeyError:
        print("\nALERTA: Algunas naciones carecen del campo 'continente'")
        return []
    
    except (TypeError, AttributeError) as error:
        print(f"\nALERTA: {error}")
        return []


def aplicar_filtro_intervalo(listado_naciones, atributo, limite_inferior, limite_superior):
    try:
        if not isinstance(listado_naciones, list):
            raise TypeError("El parámetro 'listado_naciones' debe ser lista")
        if not isinstance(atributo, str):
            raise TypeError("El parámetro 'atributo' debe ser texto")
        
        return [
            nacion for nacion in listado_naciones 
            if limite_inferior <= nacion[atributo] <= limite_superior
        ]
    
    except KeyError:
        print(f"\nALERTA: Algunas naciones carecen del campo '{atributo}'")
        return []

    except (TypeError, ValueError) as error:
        print(f"\nALERTA: {error}")
        return []
