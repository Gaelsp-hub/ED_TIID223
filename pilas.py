# 1. Crear una pila vacía
historial = []

# 2. Apilar / Push (Agregar elementos)
historial.append("google.com")
historial.append("youtube.com")
historial.append("github.com")

print("Historial:", historial)  # ['google.com', 'youtube.com', 'github.com']

# 3. Ver el elemento superior (Peek / Cima)
pagina_actual = historial[-1]
print("Página actual:", pagina_actual)  # github.com

# 4. Desapilar / Pop (Eliminar el último elemento ingresado)
pagina_salida = historial.pop()
print("Saliendo de:", pagina_salida)  # github.com

print("Historial actualizado:", historial)  # ['google.com', 'youtube.com']