from __future__ import annotations

from abc import ABC, abstractmethod


class EstrategiaPagamento(ABC):
    @abstractmethod
    def pagar(self, valor: float) -> str:
        pass


class PagamentoPix(EstrategiaPagamento):
    def pagar(self, valor: float) -> str:
        total = valor * 0.95
        return f"Pago via PIX com 5% de desconto: R$ {total:.2f}" 


class PagamentoCartao(EstrategiaPagamento):
    def pagar(self, valor: float) -> str:
        return f"Pago via Cartão: R$ {valor:.2f}"
