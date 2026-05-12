from exercicio3 import converter_nota_para_conceito

def test_nota_0():
    assert converter_nota_para_conceito(0) == "F"


def test_nota_2_9():
    assert converter_nota_para_conceito(2.9) == "F"


def test_nota_3():
    assert converter_nota_para_conceito(3) == "D"


def test_nota_4_9():
    assert converter_nota_para_conceito(4.9) == "D"


def test_nota_5():
    assert converter_nota_para_conceito(5) == "C"


def test_nota_6_9():
    assert converter_nota_para_conceito(6.9) == "C"


def test_nota_7():
    assert converter_nota_para_conceito(7) == "B"


def test_nota_8_9():
    assert converter_nota_para_conceito(8.9) == "B"


def test_nota_9():
    assert converter_nota_para_conceito(9) == "A"


def test_nota_11():
    assert converter_nota_para_conceito(11) == "Nota Inválida"


def test_nota_menos_0():
    assert converter_nota_para_conceito(-1) == "Nota Inválida"