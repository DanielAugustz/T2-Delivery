from __future__ import annotations

from typing import List


class FakeDB:
    _instancia: FakeDB | None = None 
 
    def __new__(cls) -> FakeDB:
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.pedidos: List[str] = []
        return cls._instancia 

    @classmethod
    def get_instancia(cls) -> FakeDB:
        return cls() 
