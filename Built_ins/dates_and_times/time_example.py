from datetime import time


# Manipula o tempo de forma independente aos dias.
# OBS: O objeto time nao é compativel com o timedelta.
vinte_duas_horas = time(hour=22, minute=0, second=3, microsecond=384)

uma_hora_atras = vinte_duas_horas.replace(hour=21)


hora_do_relogio_digital = '22:00:00'

# Converte a hora em formato iso para um objeto datetime.
time.fromisoformat(hora_do_relogio_digital)

# Converte um datetime em iso.
vinte_duas_horas.isoformat(timespec='seconds')
