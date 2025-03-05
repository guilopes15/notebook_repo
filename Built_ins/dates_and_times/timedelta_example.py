from datetime import date, timedelta


hoje = date.today()

# Manipulando as datas. 
# A ideia é fazer contas usando o objeto timedelta.
ontem = hoje + timedelta(days=1)

amanha = hoje - timedelta(days=1)

semana_que_vem = hoje + timedelta(days=7)
