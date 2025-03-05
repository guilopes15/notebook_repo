from datetime import time, timedelta, timezone, datetime
from zoneinfo import ZoneInfo

horario_de_brasilia = timezone(timedelta(hours=-3), name='Brasilia')

t = time(22,0, tzinfo=horario_de_brasilia)

t.strftime('%I:%M:%S %p - UTC:%z - %Z') # 10:00:00 PM - UTC:-0300 - Brasilia

# Usando ZoneInfo
horario_de_brasilia = datetime(2025, 3, 4, 19, 12, tzinfo=ZoneInfo(
    'America/Sao_Paulo'
    )
)

