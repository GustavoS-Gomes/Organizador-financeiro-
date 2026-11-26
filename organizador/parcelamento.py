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

    def parcela_em(self, ano: int, mes: int) -> int | None:
        if mes < 1 or mes > 12:
            raise ValueError(f"Mês inválido: {mes}. Use um valor de 1 a 12.")
        if self.numero_parcelas < 1:
            raise ValueError("O número de parcelas deve ser pelo menos 1.")
        if self.mes_inicio < 1 or self.mes_inicio > 12:
            raise ValueError(f"Mês de início inválido: {self.mes_inicio}. Use um valor de 1 a 12.")

        numero_parcela = (ano * 12 + mes) - (self.ano_inicio * 12 + self.mes_inicio) + 1

        if 1 <= numero_parcela <= self.numero_parcelas:
            return numero_parcela
        return None