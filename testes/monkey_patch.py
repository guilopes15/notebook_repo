def calculo_idade(dado):
    #do
    return dado


def verifica_idade():
    idade = calculo_idade(10)
    if idade >= 18:
        return 'maior'
    return 'menor'


calculo_idade = lambda x: 80 #stub

print(verifica_idade())

###############################################################

from contextlib import contextmanager
import builtins


def spy_print(message):
    spy_print.message = f'Spy diz: {message}'


@contextmanager
def patch_print():
    #Arrange
    print_original = builtins.print
    builtins.print = spy_print
    
    yield spy_print #Durante o with
    
    #Teardonw
    builtins.print = print_original


def hello():
    print('hello')


with patch_print() as spy: #Spy é um duble de testes
    hello()


print(spy.message)
assert spy.message == 'Spy diz: hello'

################################################################
import httpx


#Fake é um duble de testes
class FakeResponse:
    def __init__(self, url, status_code):
        self.status_code = status_code

    def json(self):
        return {'data': 'fake data'}
        

def fetch_data(url):
    try:
        response = httpx.get(url)
        if response.status_code == 200:
            return response.json()
        return {}
    except httpx.RequestError:
        return {}


def test_fetch_data_deve_retornar_200(monkeypatch):
    monkeypatch.setattr(httpx, "get", lambda url: FakeResponse(url, 200))
    result = fetch_data('https://google.com')
    assert result == {'data': 'fake data'}


def test_fetch_data_deve_retornar_500(monkeypatch):
    monkeypatch.setattr(httpx, "get", lambda url: FakeResponse(url, 500))
    result = fetch_data('https://google.com')
    assert result == {}


def test_fetch_data_deve_retornar_erro(monkeypatch):
    def patch_erro(url):
        raise httpx.TimeoutException('deu ruim')
    
    monkeypatch.setattr(httpx, "get", patch_erro)
    result = fetch_data('https://google.com')
    assert result == {}