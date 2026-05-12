def calcular_bonus(salario_base: float, avaliacao: str):
    avaliacao = avaliacao.lower()

    if salario_base < 0:
        return 0.0

    if avaliacao == "excelente":
        return salario_base * 0.20

    elif avaliacao == "bom":
        return salario_base * 0.10

    elif avaliacao == "regular":
        return salario_base * 0.02

    return 0.0