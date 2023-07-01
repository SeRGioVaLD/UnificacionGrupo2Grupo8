def formatear_id(id):
    numero_str = str(id)
    ceros_restantes = 6 - len(numero_str)
    if ceros_restantes >= 0:
        numero_relleno = "0" * ceros_restantes + numero_str
    return numero_relleno
