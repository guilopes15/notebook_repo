from pydantic import BaseModel, field_validator
import re


class Usuario(BaseModel):
    nome: str

    @field_validator('nome')
    @classmethod
    def nome_sem_numeros_ou_caracteres(cls, v):
        # Aceita letras com acento, cedilha e espaço
        if not re.fullmatch(r'[A-Za-zÀ-ÿ\s]+', v):
            raise ValueError('Nome deve conter apenas letras e espaços')
        return v


#class Usuario(BaseModel):
    #nome: str

    #@field_validator('nome')
    #@classmethod
    #def validar_nome(cls, valor: str) -> str:
        #for char in valor:
            #if not (char.isalpha() or char.isspace()):
                #raise ValueError('O nome deve conter apenas letras e espaços')
        #return valor


def validation(data: dict) -> bool:
    return all([
        all([value for value in data.values()]),
        data['idade'] >= 10,
        data['cpf'].isnumeric(), # Obs: rever digitos numericos
        len(data['cpf']) == 11
    ])