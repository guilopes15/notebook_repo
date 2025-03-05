from datetime import datetime, timedelta, timezone


hoje = datetime.today()

hora = datetime(
    year=2025,
    month=3,
    day=3,
    hour=21,
    minute=5,
    second=15,
    tzinfo=timezone(timedelta(hours=-3), name='Brasilia'),
)

agora = datetime.now()

uma_hora_a_menos = agora - timedelta(hours=1)

ontem_esse_horario = agora - timedelta(days=1)

amanha_esse_horaio = agora + timedelta(days=1)

delta = agora - ontem_esse_horario


# Mudando o fuso de um datetime existente.
noronha = timezone(timedelta(hours=-2))

hora_em_noronha = hora.astimezone(noronha)

hora_em_noronha.time() # datetime.time(22, 5)


# OBS: Como o datetime é uma fusao de objeto date e time, entao podemos
# usar a formatação para strings de ambos os objetos com strftime.