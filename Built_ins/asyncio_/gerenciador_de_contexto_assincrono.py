import asyncio


class GerenciadorAsync:
    async def __aenter__(self):
        print("Entrou no contexto")
        return self

    async def __aexit__(self, exc_type, exc, tb):
        print("Saiu do contexto")

async def exemplo():
    async with GerenciadorAsync():
        print("Dentro do contexto")


def is_gerenciador_assincrono(obj):
    return hasattr(obj, "__aenter__") and hasattr(obj, "__aexit__")


asyncio.run(exemplo())