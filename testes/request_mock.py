import httpx
import respx
#import json

URL = 'https://pokeapi.co/api/v2/pokemon/{}'

def get_poke(name):
    try:
        response = httpx.get(URL.format(name))
        data = response.json()
        return f"poke: {data['name']}, weight: {data['weight']}"
        
    except KeyError:
        return 'Poke invalido'
        
    #except json.JSONDecodeError:
        #return 'Poke invalido'
    
    except httpx.InvalidURL:
        return 'Poke invalido'
    
    except httpx.ConnectError:
        return 'Erro de conexao'
    
    except httpx.TimeoutException:
        return 'Erro de conexao'


@respx.mock
def test_poke():
    #Arange
    mockerd_response = httpx.Response(
        200, 
        json={'name': 'ditto', 'weight': 40},
    )
    respx.get(URL.format('ditto')).mock(mockerd_response)
    
    #Act
    result = get_poke('ditto')
    
    #Assert
    assert result == 'poke: ditto, weight: 40'


@respx.mock
def test_wrong_poke():
    mockerd_response = httpx.Response(
        200, 
        json={},
    )
    respx.get(URL.format('bla')).mock(mockerd_response)
    
    result = get_poke('bla')
    assert result == 'Poke invalido'


def test_poke_invalid_url():
    result = get_poke('\x11')
    assert result == 'Poke invalido'


@respx.mock
def test_erro_conexao():
    respx.get(URL.format('ditto')).mock(side_effect=httpx.ConnectError)
    result = get_poke('ditto')    
    assert result == 'Erro de conexao'


@respx.mock
def test_erro_timeout():
    respx.get(URL.format('ditto')).mock(side_effect=httpx.TimeoutException)
    result = get_poke('ditto')    
    assert result == 'Erro de conexao'