import calendar


# Exibe todo o calendario do março de 2025
print(calendar.month(2025, 3))

# Exibe todo o calendario do 2025
print(calendar.calendar(2025))

# O primeiro_dia é retornado como um número (0 = segunda, 6 = domingo).
primeiro_dia, dias_no_mes = calendar.monthrange(2025, 3) # output -> 5 31

# Retorna uma matriz. Cada lista dentro da matriz represemta uma semana.
semanas = calendar.monthcalendar(2025, 3)

# Verificando ano bissexto
print(calendar.isleap(2024))  # True 
print(calendar.isleap(2025))  # False

# Conta os anos bissextos entre 2000 e 2029.
print(calendar.leapdays(2000, 2030))  
