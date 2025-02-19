from dataclasses import dataclass, KW_ONLY


# Todos os campos após o tipo KW_ONLY são marcados como campos nomeados. 
@dataclass
class Point:
    x: float
    _: KW_ONLY
    y: float
    z: float

p = Point(0, y=1.5, z=2.0)
