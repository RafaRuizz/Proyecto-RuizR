# ==========================================
# ARCHIVO: utilidades/visualizador.py
# ==========================================

def dar_formato_nacion(nacion, indice, estilo_presentacion='basico'):
    try:
        if estilo_presentacion == 'habitantes':
            return f'  {indice}. {nacion["nombre"]}: {nacion["poblacion"]:,} habitantes'
        
        elif estilo_presentacion == 'extension':
            return f'  {indice}. {nacion["nombre"]}: {nacion["superficie"]:,} km²'
        
        elif estilo_presentacion == 'detallado':
            return (f'  {indice}. {nacion["nombre"]}\n'
                    f'      Región: {nacion["continente"]}\n'
                    f'      Habitantes: {nacion["poblacion"]:,} personas\n'
                    f'      Extensión: {nacion["superficie"]:,} km²')
        
        else:
            return f'  {indice}. {nacion["nombre"]} - {nacion["continente"]}'
    
    except KeyError as error:
        return f'  {indice}. Error: Campo faltante {error}'
    except (TypeError, ValueError) as error:
        return f'  {indice}. Error de presentación: {error}'


def presentar_seccion(elementos, indice_inicio, encabezado, estilo_presentacion='basico'):
    print('\n' + '=' * 80)
    print(f'{encabezado}')
    print('=' * 80, '\n')
    
    for posicion, elemento in enumerate(elementos, start=indice_inicio):
        print(dar_formato_nacion(elemento, posicion, estilo_presentacion))
    
    print('\n' + '-' * 80)


def presentar_con_navegacion(resultados, elementos_por_seccion=10, encabezado='Resultados', estilo_presentacion='basico'):
    try:
        if not resultados:
            print('\nSin resultados para presentar.')
            return
        
        if not isinstance(elementos_por_seccion, int) or elementos_por_seccion <= 0:
            elementos_por_seccion = 10

        cantidad_total = len(resultados)
        total_secciones = (cantidad_total + elementos_por_seccion - 1) // elementos_por_seccion
        
        if cantidad_total <= 10:
            encabezado_completo = f'{encabezado}\nMostrando {cantidad_total} elemento{"s" if cantidad_total != 1 else ""}'
            presentar_seccion(resultados, 1, encabezado_completo, estilo_presentacion)
            input('Presione Enter para continuar...')
            return
        
        seccion_activa = 1

        while True:
            posicion_inicio = (seccion_activa - 1) * elementos_por_seccion
            posicion_fin = min(posicion_inicio + elementos_por_seccion, cantidad_total)
            elementos_seccion = resultados[posicion_inicio:posicion_fin]
            
            encabezado_seccion = f'{encabezado}\nSección {seccion_activa} de {total_secciones} | Mostrando {posicion_inicio + 1}-{posicion_fin} de {cantidad_total} elementos'
            presentar_seccion(elementos_seccion, posicion_inicio + 1, encabezado_seccion, estilo_presentacion)
            
            opciones_navegacion = []
            
            if seccion_activa < total_secciones:
                opciones_navegacion.append('Enter = Siguiente')
            else:
                opciones_navegacion.append('Enter = Volver al inicio')
            
            if total_secciones >= 2 and seccion_activa > 1:
                opciones_navegacion.append('R = Retroceder')
            
            if total_secciones > 2:
                opciones_navegacion.append('[Número] = Ir a sección')
            
            if total_secciones >= 2:
                opciones_navegacion.append('T = Terminar')
            
            print(' | '.join(opciones_navegacion))
            print('-' * 80)

            comando = input('\nSeleccione una opción: ').lower().strip()

            if comando == 't' and total_secciones >= 2:
                break

            elif comando == 'r' and seccion_activa > 1:
                seccion_activa -= 1
            
            elif comando == 'r' and seccion_activa == 1:
                print('\nYa está en la primera sección.')
                input('Presione Enter para continuar...')
    
            elif comando == '':
                if seccion_activa < total_secciones:
                    seccion_activa += 1
                else:
                    seccion_activa = 1

            elif comando.isdigit() and total_secciones > 2:
                seccion_destino = int(comando)
                if 1 <= seccion_destino <= total_secciones:
                    seccion_activa = seccion_destino
                else:
                    print(f'\nSección inválida. Debe estar entre 1 y {total_secciones}.')
                    input('Presione Enter para continuar...')
            
            else:
                print(f'\nOpción "{comando}" no reconocida.')
                input('Presione Enter para continuar...')

    except KeyboardInterrupt:
        print('\n\nALERTA: Navegación interrumpida por usuario')
    except Exception as error:
        print(f'\nALERTA: Error en visualizador - {error}')
