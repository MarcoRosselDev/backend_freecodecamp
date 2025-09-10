""" type() evalua el tipo de valor """

print(type("hola"))  # <class 'str'>
print(type(10))  # <class 'int'>
print(type(10.3))  # <class 'float'>

""" int() siempre redondea hacia abajo """
entero_redondeado = int(4.9)
print(entero_redondeado)  # 4

""" float() """

print(float(10))  # 10.0

""" str() convierte a string """
print(type(str(200)))  # <class 'str'>

""" se puede usar _ para separar digitos en numeros grandes para una mejor compresion """
big_number = 1_000_000_000_001
print(big_number)
