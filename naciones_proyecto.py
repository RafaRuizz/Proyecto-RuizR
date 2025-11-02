# ==========================================
# ARCHIVO: programa_principal.py
# ==========================================

from utilidades.cargador_datos import cargar_informacion_csv
from utilidades.interfaz_usuario import presentar_menu_principal
from utilidades.manejadores_opciones import (
    ejecutar_busqueda_nacion,
    ejecutar_filtro_region,
    ejecutar_filtro_habitantes,
    ejecutar_filtro_area,
    ejecutar_ordenamiento_naciones,
    ejecutar_analisis_estadistico,
    ejecutar_agregar_nacion,
    ejecutar_modificar_nacion,
    ejecutar_eliminar_nacion
)


def iniciar_aplicacion():
    # Obtener información desde el archivo CSV
    naciones = cargar_informacion_csv("datos/naciones_globales.csv")
    
    # Ciclo principal de la aplicación
    while True:
        try:
            # Presentar menú y capturar selección
            seleccion = presentar_menu_principal()
            numero_seleccion = int(seleccion) if seleccion.isdigit() else 0

            # Procesar la selección del usuario
            match numero_seleccion:
                case 1:
                    ejecutar_busqueda_nacion(naciones)
                
                case 2:
                    ejecutar_filtro_region(naciones)
                
                case 3:
                    ejecutar_filtro_habitantes(naciones)
                
                case 4:
                    ejecutar_filtro_area(naciones)
                
                case 5:
                    ejecutar_ordenamiento_naciones(naciones)
                
                case 6:
                    ejecutar_analisis_estadistico(naciones)

                case 7:
                    ejecutar_agregar_nacion(naciones, "datos/naciones_globales.csv")

                case 8:
                    ejecutar_modificar_nacion(naciones, "datos/naciones_globales.csv")

                case 9:
                    ejecutar_eliminar_nacion(naciones, "datos/naciones_globales.csv")

                case 10:
                    print("\n¡Gracias por utilizar el Sistema de Gestión de Naciones!")
                    print("Finalizando programa...")
                    break
                
                case _:
                    print('\nLa selección ingresada no es válida')
        
        except ValueError as error:
            print(f"Error: {error}")
        except KeyboardInterrupt:
            print("\n\nPrograma detenido por el usuario (Ctrl+C)")
            print("Finalizando...")
            break
        except Exception as error:
            print(f"Error no esperado: {error}")


if __name__ == "__main__":
    iniciar_aplicacion()
