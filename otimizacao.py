# Nome do arquivo: otimizacao.py
# Autor: Maurício Fernandes de Oliveira Assis
# Versão do Python: 3.12.1

from Ciclos import Ciclos
import matplotlib.pyplot as plt  # biblioteca onde será plotado os grafico

def otimizarReaquecimento(op1, p1, t1, p2, op2, x3, t3, p4, op3, t5, x5):
    try:
        lista_Trabalhos = []
        lista_Rendimentos = []
        lista_Pressoes = []
        
        intervalo_pressao = p2 - p1

        divisoes = 1000
        
        passo = intervalo_pressao / divisoes
        
        for interacao in range(0, divisoes +1):

            p4 = p1 + interacao * passo
            resultado_otimizacao = Ciclos.reaquecimento(op1, p1, t1, p2, op2, x3, t3, p4, op3, t5, x5)
            
            lista_Pressoes.append(p4)
            lista_Trabalhos.append(resultado_otimizacao['wliq'])
            lista_Rendimentos.append(resultado_otimizacao['n'])

        id_trabalhos = lista_Trabalhos.index(max(lista_Trabalhos))
        trabalho_max = lista_Trabalhos[id_trabalhos]
        p_trabalho_max = lista_Pressoes[id_trabalhos] / 1000

        id_eta =  lista_Rendimentos.index(max(lista_Rendimentos))
    
        eta_max = lista_Rendimentos[id_eta]
        p_eta_max = lista_Pressoes[id_eta] / 1000

    # erro = resultado_otimizacao['erro']

    #____________Gráfico da otimização______________________
        lista_Pressoesplot = []
        lista_Trabalhosplot= []
        lista_Rendimentosplot = []

        for pressoes in lista_Pressoes:
            lista_Pressoesplot.append(pressoes/1000)
        
        for trabalhos in lista_Trabalhos:
            lista_Trabalhosplot.append(trabalhos/1000)
        for rendimento in lista_Rendimentos:
            lista_Rendimentosplot.append(rendimento*100)

        
    ############################################################
        
        return {'etamax': eta_max , 'wliqmax':trabalho_max/1000, 'petamax':p_eta_max, 'pwmax':p_trabalho_max, "lista_Pressoesplot":lista_Pressoesplot, "lista_Trabalhosplot":lista_Trabalhosplot, "lista_Rendimentosplot":lista_Rendimentosplot }
    
    
    except ValueError or ZeroDivisionError:
        return 'erro'    

