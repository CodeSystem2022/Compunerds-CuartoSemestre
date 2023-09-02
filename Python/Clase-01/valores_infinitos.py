# Importante hacer el import
import math
from decimal import Decimal

# Manejo de valores infinitos
infinito_positivo = float('inf')  # SI O SI debe estar con float
print(f'Infinito positivo: {infinito_positivo}')  # Infinito positivo: inf
print(f'¿Es infinito?: {math.isinf(infinito_positivo)}')  # ¿Es infinito?: True

infinito_negativo = float('-inf')
print(f'Infinito negativo: {infinito_negativo}')  # Infinito positivo: -inf
print(f'¿Es infinito?: {math.isinf(infinito_negativo)}')  # ¿Es infinito?: True

# Módulo math
print('---Con módulo MATH---')
infinito_math_positivo = math.inf
print(f'Infinito positivo: {infinito_math_positivo}')  # Infinito positivo: inf
print(f'¿Es infinito?: {math.isinf(infinito_math_positivo)}')  # ¿Es infinito?: True

infinito_math_negativo= -math.inf
print(f'Infinito positivo: {infinito_math_negativo}')  # Infinito positivo: -inf
print(f'¿Es infinito?: {math.isinf(infinito_math_negativo)}')  # ¿Es infinito?: True

# Módulo decimal
print('---Con módulo DECIMAL---')
infinito_decimal_positivo = Decimal('Infinity')
print(f'Infinito positivo: {infinito_decimal_positivo}')  # Infinito positivo: Infinity
print(f'¿Es infinito?: {math.isinf(infinito_decimal_positivo)}')  # ¿Es infinito?: True

infinito_decimal_negativo= Decimal('-Infinity')
print(f'Infinito positivo: {infinito_decimal_negativo}')  # Infinito positivo: -Infinity
print(f'¿Es infinito?: {math.isinf(infinito_decimal_negativo)}')  # ¿Es infinito?: True
