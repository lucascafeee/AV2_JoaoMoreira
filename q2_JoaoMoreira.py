from q1_JoaoMoreira import payment_process_pyth

def rodar_teste(tipo_pagamento, resultado_esperado):
    resultado_obtido = payment_process_pyth(tipo_pagamento)
    assert resultado_obtido == resultado_esperado, f"Falha no teste {tipo_pagamento}: {resultado_obtido}"
    print(f"Teste de '{tipo_pagamento}' passou com sucesso!")

def testes_unitarios():
    casos_de_teste = [
        ('Cash', ['Transaction created', 'Cash received', 'Payment receipt printed', 'Payment receipt returned', 'Transaction completed', 'Transaction closed']),
        ('Credit', ['Transaction created', 'Account credit details requested', 'Payment request sent to bank', 'Payment approved by bank', 'Transaction closed']),
        ('Fund Transfer', ['Transaction created', 'Fund transferred', 'Bank deposit details provided', 'Payment approved by bank', 'Transaction closed']),
        ('Other', ['Transaction cancelled', 'Transaction closed'])
    ]
    
    for tipo_pagamento, resultado_esperado in casos_de_teste:
        rodar_teste(tipo_pagamento, resultado_esperado)
    
    print("Todos os testes unitários foram aprovados com sucesso!")

def teste_de_estresse(iteracoes=1000):
    print("Iniciando teste de estresse...")
    for _ in range(iteracoes):
        testes_unitarios()
    print(f"Todos os testes de estresse foram aprovados após {iteracoes} iterações!")

testes_unitarios()

teste_de_estresse(5) # selecione a quantidade de interaçoes.
