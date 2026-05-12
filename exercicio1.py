def acao_semaforo(cor:str):
    cor = cor.lower()
    if cor == 'amarelo':
        return 'Atenção'
    elif cor == 'vermelho':
        return 'Pare'
    elif cor == 'verde':
        return 'Siga'
    return 'Cor inválida'