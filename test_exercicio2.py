from exercicio2 import calcular_frete


def test_frete_ate_1kg():
    assert calcular_frete(1.0) == 5.0


def test_frete_acima_de_1kg():
    assert calcular_frete(1.01) == 10.0


def test_frete_ate_5kg():
    assert calcular_frete(5.0) == 10.0


def test_frete_acima_de_5kg():
    assert calcular_frete(5.01) == 18.0


def test_frete_peso_zero():
    assert calcular_frete(0) == 0


def test_frete_peso_negativo():
    assert calcular_frete(-10) == 0