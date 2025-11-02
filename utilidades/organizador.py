# ==========================================
# ARCHIVO: utilidades/organizador.py
# ==========================================

def organizar_naciones(listado_naciones, criterio_orden, orden_inverso=False):
    try:
        if not isinstance(listado_naciones, list):
            raise TypeError("El parámetro 'listado_naciones' debe ser lista")
        
        if not listado_naciones:
            print("Advertencia: El listado de naciones está vacío")
            return []
        
        if not isinstance(criterio_orden, str):
            raise TypeError("El parámetro 'criterio_orden' debe ser texto")
        
        if not criterio_orden.strip():
            raise ValueError("El parámetro 'criterio_orden' no puede estar vacío")
        
        if not isinstance(orden_inverso, bool):
            raise TypeError("El parámetro 'orden_inverso' debe ser True o False")
        
        criterios_permitidos = {"nombre", "poblacion", "superficie", "continente"}
        if criterio_orden not in criterios_permitidos:
            raise ValueError(f"Criterio inválido. Use: {', '.join(criterios_permitidos)}")
        
        for posicion, nacion in enumerate(listado_naciones):
            if not isinstance(nacion, dict):
                raise TypeError(f"Elemento en posición {posicion} no es diccionario")
            
            if criterio_orden not in nacion:
                raise KeyError(f"Nación en posición {posicion} carece de '{criterio_orden}'")
        
        naciones_organizadas = sorted(listado_naciones, key=lambda elemento: elemento[criterio_orden], reverse=orden_inverso)
        
        return naciones_organizadas
    
    except (TypeError, ValueError, KeyError, Exception) as error:
        print(f"\nAviso: {error}")
        return []
