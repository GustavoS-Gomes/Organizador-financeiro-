class Parcelamento:
    def __init__(
        self,
        descricao: str,
        valor_parcela_centavos: int,
        numero_parcelas: int,
        ano_inicio: int,
        mes_inicio: int,
    ) -> None:
        self.descricao = descricao
        self.valor_parcela_centavos = valor_parcela_centavos
        self.numero_parcelas = numero_parcelas
        self.ano_inicio = ano_inicio
        self.mes_inicio = mes_inicio

    def parcela_em(self, ano: int, mes: int) -> int:
        raise NotImplementedError("Regra da parcela ainda não implementada.")