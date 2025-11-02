# ==========================================
# ARCHIVO: utilidades/interfaz_usuario.py
# ==========================================

def presentar_menu_principal():
    print('\n==== SISTEMA DE GESTIÓN DE NACIONES ====\n')
    print('1) Buscar nación por denominación')
    print('2) Filtrar naciones por región continental')
    print('3) Filtrar por intervalo de habitantes')
    print('4) Filtrar por intervalo de área territorial')
    print('5) Ordenar listado de naciones')
    print('6) Visualizar análisis estadístico')
    print('7) Registrar nueva nación')
    print('8) Modificar datos de nación')
    print('9) Remover nación')
    print('10) Finalizar programa')
    
    return input('\nSeleccione una opción (número): ')
