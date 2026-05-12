from exercicio4 import calcular_bonus

def test_bonus_bom():
    assert calcular_bonus(2000, "Bom") == 200.0


def test_bonus_excelente():
    assert calcular_bonus(2000, "Excelente") == 400.0


def test_bonus_regular():
    assert calcular_bonus(2000, "Regular") == 40.0


def test_bonus_ruim():
    assert calcular_bonus(2000, "Ruim") == 0.0


def test_bonus_avaliacao_invalida():
    assert calcular_bonus(2000, "Mais ou Menos") == 0.0


def test_bonus_salario_negativo():
    assert calcular_bonus(-2000, "Excelente") == 0.0