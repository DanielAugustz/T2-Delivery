from __future__ import annotations

from abc import ABC, abstractmethod


class Produto(ABC):
    @abstractmethod 
    def get_nome(self) -> str:
        pass

    @abstractmethod
    def get_valor(self) -> float:
        pass


class Pizza(Produto):
    def get_nome(self) -> str:
        return "Pizza Grande"

    def get_valor(self) -> float:
        return 50.0


class Hamburguer(Produto):
    def get_nome(self) -> str:
        return "Hambúrguer Artesanal"

    def get_valor(self) -> float:
        return 30.0


class ProdutoFactory:
    @staticmethod
    def criar_produto(tipo: str) -> Produto:
        t = tipo.strip().upper()
        if t == "PIZZA": 
            return Pizza()
        if t == "BURGER": 
            return Hamburguer()
        raise ValueError("Tipo inválido") 
