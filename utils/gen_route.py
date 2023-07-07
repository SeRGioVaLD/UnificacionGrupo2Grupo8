import os
    
def route(destino, extension):
    ruta_archivo = str(os.path.abspath(__file__))
    
    subcadenas = ruta_archivo.split("\\")
    resultado = None
    
    while len(subcadenas) != 0:
        final = subcadenas[len(subcadenas)-1]
        if final == destino:
            resultado = "\\".join(subcadenas)
            break
        else:
            aux = subcadenas[:len(subcadenas)-1]
            subcadenas = aux

    if len(subcadenas) == 0:
        return None
    else:
        resultado = resultado + extension
    
        resultado = resultado.replace("\\", "/")
    
        return resultado