def main():
    print(""" Escolha uma das opcao abaixo:
            1-JUROS SIMPLES
            2-JUROS COMPOSTOS
            3-VALE PRESENTE DE UMA PARCELA FUTURA
            0 - SAIR
          """.upper())
    while True :
        try:
            op=int(input("Escolha uma das opcoes acima:\n"))
            if op == 1:
                juros_simples()
            elif op == 2:
                juros_compostos()
            elif op == 3:
                vale_presente()
            elif op == 0:
                break
        except ValueError:
            print(f"Hum...Utilize um numero valido.\n")


def juros_simples():
    """ Fórmulas:  ● J = C × i × t   ● M = C + J 
    """
    try:
        capital,taxa,tempo=valores()
        vljuros_simples=capital*(taxa/100)*tempo
        montante=capital+vljuros_simples

        print(f"VALOR JUROS SIMPLES: {vljuros_simples:.2f}\nVALOR DO MONTANTE FINAL: {montante:.2f}")
    except Exception as erro :
        print(f"Erro: {erro}")

def valores():
    try:
        capital=float(input("Digite o capital inicial:") )
        taxa=float(input("Digite taxa de juros (ao mês):"))
        tempo=float((input("Digite o tempo (em meses):")))
        return capital,taxa,tempo
    except Exception as erro :
        print(f"Erro: {erro}")
        return None


def juros_compostos():
    """Fórmulas: ● M = C × (1 + i)ᵗ      ● J = M − C 
Onde: 
● C = capital inicial; i = taxa de juros; t = tempo; M = montante final; J = valor dos juros 
    """
    try:
        capital,taxa,tempo=valores()
        montante=capital *(1+ (taxa/100) )**tempo
        VLjuros_compostos= montante-capital
        print(f"VALOR JUROS COMPOSTOS: {VLjuros_compostos:.2f}\nVALOR DO MONTANTE FINAL: {montante:.2f}")
    except Exception as erro :
        print(f"Erro: {erro}")

def vale_presente():
    """Fórmula: ● VP = VF / (1 + i)ᵗ 
Onde: 
● VP = valor presente; VF = valor futuro; i = taxa de juros; t = tempo 
    """
    try:
        vl_futuro=float(input("Digite o valor futuro:"))
        taxa=float(input("Digite taxa de juros em % (ao mês):"))
        tempo=float((input("Digite o tempo (em meses):")))
        valor_presente=vl_futuro/(1+(taxa/100))**tempo
        print(f"O  VALOR PRESENTE  DE UMA PARCELA FUTURA: {valor_presente:.2f}")
    except Exception as erro :
        print(f"Erro: {erro}")
    
