from __future__ import annotations

from typing import List

from delivery.fake_db import FakeDB
from delivery.estrategias_pagamento import (
    EstrategiaPagamento,
    PagamentoCartao,
    PagamentoPix,
)
from delivery.produtos import ProdutoFactory

class DeliveryFacade:
    def __init__(self) -> None: 
        self._db = FakeDB.get_instancia()

    def realizar_pedido_completo( 
        self, tipo_produto: str, metodo_pagamento: str 
    ) -> dict:  
        linhas: List[str] = [] 
        linhas.append("--- Ultimo Pedido Feito ---") 

        produto = ProdutoFactory.criar_produto(tipo_produto) 
        valor = produto.get_valor()

        m = metodo_pagamento.strip().upper()
        if m == "PIX": 
            estrategia: EstrategiaPagamento = PagamentoPix() 
        else: 
            estrategia = PagamentoCartao() 

        linhas.append(f"Valor do produto: R$ {valor:.2f}")
        linhas.append(estrategia.pagar(valor))

        self._db.pedidos.append(produto.get_nome()) 
        linhas.append(
            f"Total de pedidos: {len(self._db.pedidos)}"
        )

        return {"log": linhas, "produto": produto.get_nome(), "valor": valor} 

    def listar_pedidos(self) -> dict:
        return {
            "pedidos": self._db.pedidos,
            "total": len(self._db.pedidos),
        }
