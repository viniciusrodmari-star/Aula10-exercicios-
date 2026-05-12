def aplicar_cupom(codigo_cupom: str, valor_compra: float):

    codigo_cupom = codigo_cupom.upper()

    if codigo_cupom == "CUPOM10":
        return 0.10

    if codigo_cupom == "CUPOM25" and valor_compra > 100:
        return 0.25

    if codigo_cupom == "DESCONTOVIP" and valor_compra > 500:
        return 0.35

    return 0.0