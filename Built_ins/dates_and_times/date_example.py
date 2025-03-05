from datetime import date



# Cria uma data especifica
date(day=7, month=7, year=2007)

hoje = date.today()

hoje.day
hoje.month
hoje.year

# O metodo replace cria um novo objeto datetime
ontem = hoje.replace(day=hoje.day - 1 )

# passado < presente < futuro