from dataclasses import dataclass, field
from datetime import datetime
from time_machine import travel
import pytest


db = []


@dataclass
class User:
    name: str
    created_at: datetime = field(default_factory=datetime.now)


def create_user(name):
    user = User(name=name)
    db.append(user)
    return user


def tarefa_periodica():
    if datetime.now().hour == 6:
        print('Enviando relatorio')
        1 / 0
        return True
    else:
        print('Coletando dados')
        return True


@travel('2024-11-06 17:47', tick=False)
def test_create_user():
    user_name = 'test'
    user = User(user_name)
    result = create_user(user_name)
    assert result == user


@travel('2024-11-06 05:00')
def test_tarefa_periodica():
    assert tarefa_periodica()


@travel('2024-11-06 06:00')
def test_fail_tarefa_periodica():
    with pytest.raises(ZeroDivisionError) as ex:
        tarefa_periodica()
        
    assert type(ex.value) == ZeroDivisionError


def tempo():
    print(datetime.now())
    with travel('2024-11-06 06:00', tick=False):
        print(datetime.now())
    print(datetime.now())