# Nome do arquivo: Ciclos.py
# Autor: Maurício Fernandes de Oliveira Assis
# Versão do Python: 3.12.1

import CoolProp.CoolProp as CP  # biblioteca onde serão buscadas as propriedades termodinamicas
import matplotlib.pyplot as plt  # biblioteca onde será plotado os graficos

class Ciclos:
    
    def rankineSimples(op1, p1, t1, p2, op2, x3, t3):
    
        try:
            # Obter os dados de entrada do usuário
            fluid = 'water'
            # ESTADO 1: Entrada da bomba
            # op1= int(input("A bomba depende de: \n 1-Pressao e titulo \n 2-Pressão e temperatura"))
            if op1 == 1:
                # p1 = float(input('Entre com a pressão da bomba (kPa): ')) * 1000  # Converter para Pa
                x1 = 0
                
                # t4 = float(input('Enter the turbine inlet temperature (°C): ')) + 273.15  # Converter para K
                h1 = CP.PropsSI('H', 'P', p1, 'Q', x1, fluid)
                v1 = 1 / CP.PropsSI('D', 'P', p1, 'Q', x1, fluid)
                # v1 = 0.001008
                s1 = CP.PropsSI('S', 'P', p1, 'Q', x1, fluid)
                t1 = CP.PropsSI('T', 'P', p1, 'Q', x1, fluid)

            else:

                # p1 = float(input('Entre com a pressão da bomba (kPa): ')) * 1000  # Converter para Pa
                # t1 = float(input("Entre com a temperatura da bomba: "))
                h1 = CP.PropsSI('H', 'P', p1, 'T', t1, fluid)
                v1 = 1 / CP.PropsSI('V', 'P', p1, 'T', t1, fluid)
                s1 = CP.PropsSI('S', 'P', p1, 'T', t1, fluid)
            

            # ESTADO 2: saída da bomba e entrada da caldeira
            # p2= float(input('Entre com a pressão da saída da bomba (kPa): ')) * 1000
            
            h2_iso = (v1 * (p2 - p1)) + h1

            
            s2 = CP.PropsSI('S', 'P', p2, 'H', h2_iso, fluid)
            t2 = CP.PropsSI('T', 'P', p2, 'H', h2_iso, fluid) + 273.15
            
            # ESTADO 3: saida da caldeira e entrada da turbina
            # op2= int(input("A caldeira depende de: \n 1-Pressao e titulo \n 2-Pressão e temperatura"))
            if op2 == 1:
                p3 = p2
                # x3=float(input("Entre com o titulo da caldeira: "))
                h3 = CP.PropsSI('H', 'P', p3, 'Q', x3, fluid)
                s3 = CP.PropsSI('S', 'P', p3, 'Q', x3, fluid)
                t3 = CP.PropsSI('T', 'P', p3, 'Q', x3, fluid)
            else:
                p3 = p2
                # t3 = float(input("Entre com a temperatura da caldeira: "))
                
                h3 = CP.PropsSI('H', 'P', p3, 'T', t3, fluid)
                s3 = CP.PropsSI('S', 'P', p3, 'T', t3, fluid)

            # ESTADO 4: saida da turbina e entrada do condesador
            s4 = s3
            p4 = p1
            h4 = CP.PropsSI('H', 'P', p4, 'S', s4, fluid)
            t4 = CP.PropsSI('T', 'P', p4, 'S', s4, fluid)

            wt = h3 - h4
            qh = h3 - h2_iso
            wb = h1 - h2_iso

            eta = (wt - abs(wb)) / qh
            
            erro=0
                # Dados do ciclo de Rankine
                
               # entropias = [s1 / 1000, s2 / 1000, s3 / 1000, s4 / 1000, s1 / 1000]
             #   temperaturas = [t1 - 273.15, t2 - 273.15, t3 - 273.15, t4 - 273.15, t1 - 273.15]

                # Nomes dos estados
              #  nomes_estados = ['Estado 1', 'Estado 2', 'Estado 3', 'Estado 4', 'Estado 1']

                # Plotagem do diagrama T-s
            #    plt.plot(entropias, temperaturas, marker='o', linestyle='-')

                # Marcando os pontos no gráfico com legendas dos estados
           #     for i in range(len(entropias)):
           #         plt.text(entropias[i], temperaturas[i], f'{nomes_estados[i]}', ha='right', va='bottom')

                # Configurações do gráfico
            #    plt.title('Ciclo de Rankine no Diagrama T-s')
            #    plt.xlabel('Entropia (kJ/kg*K)')
            #    plt.ylabel('Temperatura (°C)')

                # Mostrar gráfico
            #    plt.show()
               
            # Retornar cada grupo de variáveis em um dicionário para facilitar o acesso
            return {'erro':erro,
                'trabalhos': {
                    'wt': wt/1000,
                    'wb': wb/1000,
                    'qh': qh/1000,
                    'eta': eta
                },
                'pressões': {
                    'p1': p1/1000,
                    'p2': p2/1000,
                    'p3': p3/1000,
                    'p4': p4/1000
                },
                'temperaturas': {
                    't1': t1-273.15,
                    't2': t2-273.15,
                    't3': t3-273.15,
                    't4': t4-273.15,
                    'tinicial': t1-273.15
                },
                'entalpias': {
                    'h1': h1/1000,
                    'h2': h2_iso/1000,
                    'h3': h3/1000,
                    'h4': h4/1000
                },
                'entropias': {
                    's1': s1/1000,
                    's2': s2/1000,
                    's3': s3/1000,
                    's4': s4/1000,
                    'sinicial': s1/1000
                }
            }
        except ValueError or ZeroDivisionError:
            #if x1 < 0 or x1>1 or x3<0 or x3>1:
              #  erro = 10
            erro = 10

            return {'erro':erro}
        
    
           
    def reaquecimento(op1, p1, t1, p2, op2, x3, t3, p4, op3, t5, x5):
        

        try:
            # Ciclo de Rankine com Reaquecimento
            
            # Obter os dados de entrada do usuário
            fluid = 'water'  # fluido de trabalho
            # ESTADO 1: Entrada da bomba
            # op1= int(input("A bomba depende de: \n 1-Pressao e titulo \n 2-Pressão e temperatura")) #capturador da condição da bomba
            if op1 == 1:
                #  p1 = float(input('Entre com a pressão da bomba (kPa): ')) * 1000  # Converter para Pa
                x1 = 0
                # t4 = float(input('Enter the turbine inlet temperature (°C): ')) + 273.15  # Converter para K
                h1 = CP.PropsSI('H', 'P', p1, 'Q', x1, fluid)  # Calcular a entalpia por meio da pressao e titulo
                v1 = 1 / CP.PropsSI('D', 'P', p1, 'Q', x1,
                                    fluid)  # Calcular o volume especifico por meio da pressão e titulo
                s1 = CP.PropsSI('S', 'P', p1, 'Q', x1, fluid)  # Calcular o entropia por meio da pressão e titulo
                t1 = CP.PropsSI('T', 'P', p1, 'Q', x1, fluid)

            elif op1 == 2:
                # p1 = float(input('Entre com a pressão da bomba (kPa): ')) * 1000  # Converter para Pa
                # t1 = float(input("Entre com a temperatura da bomba: ")) + 273.15 # Converter para K
                # t4 = float(input('Enter the turbine inlet temperature (°C): ')) + 273.15  # Converter para K
                h1 = CP.PropsSI('H', 'P', p1, 'T', t1, fluid)  # calcular a entalpia por meio da pressão e temperatura
                v1 = 1 / CP.PropsSI('D', 'P', p1, 'T', t1,
                                    fluid)  # calcular o volume especifico por meio da presssão e temperatura
                s1 = CP.PropsSI('S', 'P', p1, 'T', t1, fluid)  # calcular a entropia por meio da presssão e temperatura

            # ESTADO 2: saída da bomba e entrada da caldeira
            
            # p2= float(input('Entre com a pressão da saída da bomba (kPa): ')) * 1000 # Converter para Pa
            h2_iso = (v1 * (p2 - p1)) + h1  # calculando o h2 isentropico
            s2 = CP.PropsSI('S', 'P', p2, 'H', h2_iso, fluid)  # Calcular a entropia por meio da pressao e entalpia
            t2 = CP.PropsSI('T', 'P', p2, 'H', h2_iso,
                            fluid) + 273.15  # Calcular a temperatura por meio da pressao e entalpia e Converter para K

            # ESTADO 3: saida da caldeira e entrada da turbina de alta pressão
        
            #  op2= int(input("A caldeira depende de: \n 1-Pressao e titulo \n 2-Pressão e temperatura")) #entrar com a condição da caldeira
            if op2 == 1:
                p3 = p2  # condição do ciclo onde as pressões são equivalentes
                #  x3=float(input("Entre com o titulo da caldeira: ")) #entrada do valor do titulo
                h3 = CP.PropsSI('H', 'P', p3, 'Q', x3, fluid)  # Calcular a entalpia por meio da pressao e titulo
                s3 = CP.PropsSI('S', 'P', p3, 'Q', x3, fluid)  # Calcular o entropia por meio da pressão e titulo
                t3 = CP.PropsSI('T', 'P', p3, 'Q', x3, fluid)

            elif op2 == 2:
                p3 = p2  # condição do ciclo onde as pressões são equivalentes
                #   t3 = float(input("Entre com a temperatura de entrada da turbina de alta pressão: ")) + 273.15 #pegar a temperatura em graus celcius e transformar em Kelvin
                h3 = CP.PropsSI('H', 'P', p3, 'T', t3, fluid)  # calcular a entalpia por meio da pressão e temperatura
                s3 = CP.PropsSI('S', 'P', p3, 'T', t3, fluid)  # Calcular a entropia por meio da pressao e entalpia

            # ESTADO 4: saida da turbina alta pressão e entrada do reaquecimento
            
            s4 = s3  # condição do ciclo onde as entropias são equivalentes
            # p4=float(input('Entre com a pressão intermediaria (kPa): ')) * 1000 # Converter para Pa
            h4 = CP.PropsSI('H', 'P', p4, 'S', s4, fluid)  # calcular a entalpia por meio da pressão e entropia
            t4 = CP.PropsSI('T', 'P', p4, 'S', s4, fluid)

            # ESTADO 5:Reaquecimento e entrada da turbina de baixa pressão
            
            #  op3 = int(input("A turbina de alta pressão depende de: \n 1-Pressão e temperatura \n 2-Pressão e titulo \n ")) #entrada da condição da turbina de alta pressão
            if op3 == 1:
                p5=p4
                #  t5 = float(input("Entre com a temperatura de entrada da turbina de baixa pressão: ")) + 273.15 #pegar a temperatura em graus celcius e transformar em Kelvin
                h5 = CP.PropsSI('H', 'P', p5, 'T', t5, fluid)  # calcular a entalpia por meio da pressão e temperatura
                s5 = CP.PropsSI('S', 'P', p5, 'T', t5, fluid)  # Calcular a entropia por meio da pressao e entalpia
            elif op3 == 2:
                p5=p4
                #  x5 = float(input("Entre com o titulo da entrada da turbina de baixa pressão: "))  #entrada do titulo
                h5 = CP.PropsSI('H', 'P', p5, 'Q', x5, fluid)  # Calcular a entalpia por meio da pressao e titulo
                s5 = CP.PropsSI('S', 'P', p5, 'Q', x5, fluid)  # Calcular o entropia por meio da pressão e titulo
                t5 = CP.PropsSI('T', 'P', p5, 'Q', x5, fluid)
            # ESTADO 6: saida da turbina de baixa pressão e entrada do condesador
            
            p6 = p1  # condição do ciclo onde as pressões são equivalentes
            s6 = s5  # condição do ciclo onde as entropias são equivalentes
            h6 = CP.PropsSI('H', 'P', p6, 'S', s6, fluid)  # calcular a entalpia por meio da pressão e entropia
            t6 = CP.PropsSI('T', 'P', p6, 'S', s6, fluid)

            # BALANÇO ENERGÉTICO
            wt = (h3 - h4 + h5 - h6)  # calcular o trabalho da turbina
            qh = (h3 - h2_iso + h5 - h4)  # calular o calor pago na caldeira
            wb = (h1 - h2_iso)  # calcular o trabalho da bomba

            wliq = (wt - abs(wb))  # calcular a eficiencia termica do ciclo
            eta = wliq / qh

           
                
            
            erro =0

                    # Dados do ciclo de Rankine
            entropias = [s1 / 1000, s2 / 1000, s3 / 1000, s4 / 1000, s5 / 1000, s6 / 1000, s1 / 1000]
            temperaturas = [t1 - 273.15, t2 - 273.15, t3 - 273.15, t4 - 273.15, t5 - 273.15, t6 - 273.15, t1 - 273.15]

            # Nomes dos estados
            nomes_estados = ['1', '2', '3', '4', '5', '6', '1']

            # Plotagem do diagrama T-s
            #plt.plot(entropias, temperaturas, marker='o', linestyle='-')

            # Marcando os pontos no gráfico com legendas dos estados
            # for i in range(len(entropias)):
            #     plt.text(entropias[i], temperaturas[i], f'{nomes_estados[i]}', ha='right', va='bottom')

            #  # Configurações do gráfico
            #  plt.title('Diagrama T-s do Ciclo de Rankine')
            # plt.xlabel('Entropia (kJ/kg*K)')
            # plt.ylabel('Temperatura (°C)')

            # Mostrar gráfico
            #  plt.show()
            

            return { "wliq": wliq, "n":eta, "entropias": entropias, "temperaturas":temperaturas, 'erro':erro,
    'trabalhos': {
        'wt': round(wt / 1000, 4),
        'wb': round(wb / 1000, 4),
        'qh': round(qh / 1000, 4),
        'eta': round(eta, 4)
    },
    'pressões': {
        'p1': round(p1 / 1000, 4),
        'p2': round(p2 / 1000, 4),
        'p3': round(p3 / 1000, 4),
        'p4': round(p4 / 1000, 4),
        'p5': round(p5 / 1000, 4),
        'p6': round(p6 / 1000, 4)
    },
    'temperaturas': {
        't1': round(t1 - 273.15, 4),
        't2': round(t2 - 273.15, 4),
        't3': round(t3 - 273.15, 4),
        't4': round(t4 - 273.15, 4),
        't5': round(t5 - 273.15, 4),
        't6': round(t6 - 273.15, 4),
        'tinicial': round(t1 - 273.15, 4)
    },
    'entalpias': {
        'h1': round(h1 / 1000, 4),
        'h2': round(h2_iso / 1000, 4),
        'h3': round(h3 / 1000, 4),
        'h4': round(h4 / 1000, 4),
        'h5': round(h5 / 1000, 4),
        'h6': round(h6 / 1000, 4)
    },
    'entropias': {
        's1': round(s1 / 1000, 4),
        's2': round(s2 / 1000, 4),
        's3': round(s3 / 1000, 4),
        's4': round(s4 / 1000, 4),
        's5': round(s5 / 1000, 4),
        's6': round(s6 / 1000, 4),
        'sinicial': round(s1 / 1000, 4)
    }
}
            
        except ValueError or ZeroDivisionError:
            
            erro = 10

            return {'erro':erro}

            

    
    def regenerativo(op1, p1, t1, p2, op2, p5, t5, x5, op3, y):

        #Ciclo de Rankine com Regenerativo
        
        # Obter os dados de entrada do usuário
        fluid = 'water' #fluido de trabalho
        try:
            #Dados de entrada
            
            #ESTADO 1: Entrada da bomba
        # op1= int(input("A bomba depende de: \n 1-Pressao e titulo \n 2-Pressão e temperatura")) #capturador da condição da bomba
            if op1 == 1:
            # p1 = float(input('Entre com a pressão da bomba (kPa): ')) * 1000  # Converter para Pa
                x1 = 0 #entrada do valor do titulo
                #t4 = float(input('Enter the turbine inlet temperature (°C): ')) + 273.15  # Converter para K
                h1 = CP.PropsSI('H', 'P', p1, 'Q', x1, fluid) #Calcular a entalpia por meio da pressao e titulo
                v1 = 1/CP.PropsSI('D', 'P', p1, 'Q', x1, fluid) #Calcular o volume especifico por meio da pressão e titulo
                s1 = CP.PropsSI('S', 'P', p1, 'Q', x1, fluid)  #Calcular o entropia por meio da pressão e titulo
                t1 = CP.PropsSI('T', 'P', p1, 'Q', x1, fluid)
            elif op1 == 2:
            # p1 = float(input('Entre com a pressão da bomba (kPa): ')) * 1000  # Converter para Pa
            #  t1 = float(input("Entre com a temperatura da bomba: ")) + 273.15 # Converter para K
                # t4 = float(input('Enter the turbine inlet temperature (°C): ')) + 273.15  # Converter para K
                h1 = CP.PropsSI('H', 'P', p1, 'T', t1, fluid) #calcular a entalpia por meio da pressão e temperatura
                v1 = 1/CP.PropsSI('D', 'P', p1, 'T', t1, fluid) #calcular o volume especifico por meio da presssão e temperatura
                s1 = CP.PropsSI('S', 'P', p1, 'T', t1, fluid) #calcular a entropia por meio da presssão e temperatura

        #  p2= float(input('Entre com a pressão da saída da bomba (kPa): ')) * 1000 # Converter para Pa
            h2 = (v1*(p2-p1)) + h1 #calculando o h2 isentropico
            s2 = CP.PropsSI('S', 'P', p2, 'H', h2, fluid)
            t2 = CP.PropsSI('T', 'P', p2, 'H', h2, fluid)

        
        #  op2 = int(input("A turbina depende de: \n 1-Pressão e temperatura \n 2-Pressão e titulo \n ")) #entrada da condição da turbina de alta pressão
            if op2 == 1:
            # p5 =  float(input('Entre com a pressão da turbina (kPa): ')) * 1000
            # t5 = float(input("Entre com a temperatura de entrada da turbina de : ")) + 273.15 #pegar a temperatura em graus celcius e transformar em Kelvin
                h5 = CP.PropsSI('H', 'P', p5, 'T', t5, fluid) #calcular a entalpia por meio da pressão e temperatura
                s5 = CP.PropsSI('S', 'P', p5, 'T', t5, fluid) # Calcular a entropia por meio da pressao e entalpia
            elif op2 == 2:
            # p5 = float(input('Entre com a pressão da turbina (kPa): ')) * 1000
            # x5 = float(input("Entre com o titulo da entrada da turbina : "))  #entrada do titulo
                h5 = CP.PropsSI('H', 'P', p5, 'Q', x5, fluid) #Calcular a entalpia por meio da pressao e titulo
                s5 = CP.PropsSI('S', 'P', p5, 'Q', x5, fluid) #Calcular o entropia por meio da pressão e titulo
                t5 = CP.PropsSI('T', 'P', p5, 'Q', x5, fluid)
            
            #Estado 6: primeira saida da turbina 
            p6=p2
            s6=s5
            h6 = CP.PropsSI('H', 'P', p6, 'S', s6, fluid) #calcular a entalpia por meio da pressão e entropia
            t6 = CP.PropsSI('T', 'P', p6, 'S', s6, fluid)

            #Estado 7: saida turbina 
            p7=p1 #condição do ciclo onde as pressões são equivalentes
            s7=s6 #condição do ciclo onde as entropias são equivalentes
            h7 = CP.PropsSI('H', 'P', p7, 'S', s7, fluid) #calcular a entalpia por meio da pressão e entropia
            t7 = CP.PropsSI('T', 'P', p7, 'S', s7, fluid)

            #Estado 3 aplicando a lei da termodinamica em AAA fechado"
        # op3 = int(input("A segunda bomba depende de: \n 1- Entalpia da primeira lei do misturador \n 2-Título"))
            if op3 == 1:
            # y = float(input('Entre com y: ')) 
                h3 = h6*y + h2*(1-y)
                
                p3= p2
                t3 = CP.PropsSI('T', 'P', p3, 'H', h3, fluid)
                s3 = CP.PropsSI('S', 'P', p3, 'H', h3, fluid)

                #ESTADO 4: saída da bomba II
                p4= p5
                s4 = s3
                t4 = CP.PropsSI('T', 'P', p4, 'S', s4, fluid)
                h4 = CP.PropsSI('H', 'P', p4, 'S', s4, fluid)

            elif op3 == 2:
                p3 = p2
                x3 = 0
                h3 = CP.PropsSI('H', 'P', p3, 'Q', x3, fluid) #Calcular a entalpia por meio da pressao e titulo
                s3 = CP.PropsSI('S', 'P', p3, 'Q', x3, fluid) #Calcular o entropia por meio da pressão e titulo
                t3 = CP.PropsSI('T', 'P', p3, 'Q', x3, fluid)
                v3 = 1/CP.PropsSI('D', 'P', p3, 'Q', x3, fluid)
                #ESTADO 4
                p4 = p5
                h4 = h3 + v3*(p5 - p3)
                y= (h3-h2)/(h6-h2)
                s4 = CP.PropsSI('S', 'P', p4, 'H', h4, fluid) 
                t4 = CP.PropsSI('T', 'P', p4, 'H', h4, fluid) 
                

            
            #BALANÇO ENERGÉTICO
            wt1 = h5 - h6
            wt2= (h6-h7)*(1-y)
            wt=wt1+wt2

            wb1= (h1-h2)*(1-y) #calcular o trabalho da bomba
            wb2 = (h3-h4)
            wb=wb1+wb2

            qh= h5 - h4
            
            eta=(wt - abs(wb))/qh #calcular a eficiencia termica do ciclo
            
            erro=0


    #__________verifica as propriedades dentro da tabela pela entropia___________________
            verificar =False
            valores = [s1, s2, s3, s4, s5, s6 ]
            for valor in valores:
                if valor is None:
                    verificar = True
                    break

            if verificar is True:
                verificar1 = 2
        
            else:
                verificar1 = 1
            
            return {'erro':erro,
        'trabalhos': {
            'wt': round(wt / 1000, 4),
            'wb': round(wb / 1000, 4),
            'qh': round(qh / 1000, 4),
            'eta': round(eta , 4),
            'y': round(y , 4)
        },
        'pressões': {
            'p1': round(p1 / 1000, 4),
            'p2': round(p2 / 1000, 4),
            'p3': round(p3 / 1000, 4),
            'p4': round(p4 / 1000, 4),
            'p5': round(p5 / 1000, 4),
            'p6': round(p6 / 1000, 4),
            'p7': round(p7 / 1000, 4)
        },
        'temperaturas': {
            't1': round(t1 - 273.15, 4),
            't2': round(t2 - 273.15, 4),
            't3': round(t3 - 273.15, 4),
            't4': round(t4 - 273.15, 4),
            't5': round(t5 - 273.15, 4),
            't6': round(t6 - 273.15, 4),
            't7': round(t7 - 273.15, 4)
        },
        'entalpias': {
            'h1': round(h1 / 1000, 4),
            'h2': round(h2 / 1000, 4),
            'h3': round(h3 / 1000, 4),
            'h4': round(h4 / 1000, 4),
            'h5': round(h5 / 1000, 4),
            'h6': round(h6 / 1000, 4),
            'h7': round(h7 / 1000, 4),
        },
        'entropias': {
            's1': round(s1 / 1000, 4),
            's2': round(s2 / 1000, 4),
            's3': round(s3 / 1000, 4),
            's4': round(s4 / 1000, 4),
            's5': round(s5 / 1000, 4),
            's6': round(s6 / 1000, 4),
            's7': round(s7 / 1000, 4),
        }
    }
            
            
        except ValueError or ZeroDivisionError:
           
            erro = 10

            return {'erro':erro}


            

    def regenerativoReaquecimento(m, op1, p1, t1, p2, n, op3, p3, t3, op5, t5, x5, p6, nt, op7, t7, x7 ):

        # Ciclo de Rankine com Reaquecimento
        # Obter os dados de entrada do usuário
        fluid = 'water'  # fluido de trabalho

        try:
            #m =  float(input('Entre com a vazão massica: '))
            # ESTADO 1: Entrada da bomba
            #op1 = int(input("A bomba depende de: \n 1-Pressao e titulo \n 2-Pressão e temperatura"))  # capturador da condição da bomba
            if op1 == 1:
            #  p1 = float(input('Entre com a pressão da bomba (kPa): ')) * 1000  # Converter para Pa
                x1 = 0  # entrada do valor do titulo
                # t4 = float(input('Enter the turbine inlet temperature (°C): ')) + 273.15  # Converter para K
                h1 = CP.PropsSI('H', 'P', p1, 'Q', x1, fluid)  # Calcular a entalpia por meio da pressao e titulo
                v1 = 1 / CP.PropsSI('D', 'P', p1, 'Q', x1, fluid)  # Calcular o volume especifico por meio da pressão e titulo
                s1 = CP.PropsSI('S', 'P', p1, 'Q', x1, fluid)  # Calcular o entropia por meio da pressão e titulo
                t1 = CP.PropsSI('T', 'P', p1, 'Q', x1, fluid)
            elif op1 == 2:
            #  p1 = float(input('Entre com a pressão da bomba (kPa): ')) * 1000  # Converter para Pa
            #  t1 = float(input("Entre com a temperatura da bomba: ")) + 273.15  # Converter para K
                # t4 = float(input('Enter the turbine inlet temperature (°C): ')) + 273.15  # Converter para K
                h1 = CP.PropsSI('H', 'P', p1, 'T', t1, fluid)  # calcular a entalpia por meio da pressão e temperatura
                v1 = 1 / CP.PropsSI('D', 'P', p1, 'T', t1,
                                    fluid)  # calcular o volume especifico por meio da presssão e temperatura
                s1 = CP.PropsSI('S', 'P', p1, 'T', t1, fluid)  # calcular a entropia por meio da presssão e temperatura

            # ESTADO 2: saída da bomba e entrada da caldeira
        

        #  p2 = float(input('Entre com a pressão da saída da bomba I (kPa) (Estado 2): ')) * 1000  # Converter para Pa
            h2_iso = (v1 * (p2 - p1)) + h1  # calculando o h2 isentropico
            s2 = CP.PropsSI('S', 'P', p2, 'H', h2_iso, fluid)
            t2 = CP.PropsSI('T', 'P', p2, 'H', h2_iso, fluid)

        # n =  float(input("Digite a eficiencia da bomba"))

            h2 = (h2_iso - h1 + n*h1)/n

            # Estado 5 entrada da segunda bomba
        # op3 = int(input("A bomba II depende de: \n 1-Pressao e titulo \n 2-Pressão e temperatura"))  # capturador da condição da bomba
            if op3 == 1:
            #   p3 = float(input('Entre com a pressão da bomba (kPa) (Estado 3): ')) * 1000
                x3 = 0
                # t4 = float(input('Enter the turbine inlet temperature (°C): ')) + 273.15  # Converter para K
                h3 = CP.PropsSI('H', 'P', p3, 'Q', x3, fluid)  # Calcular a entalpia por meio da pressao e titulo
                v3 = 1 / CP.PropsSI('D', 'P', p3, 'Q', x3, fluid)  # Calcular o volume especifico por meio da pressão e titulo
                s3 = CP.PropsSI('S', 'P', p3, 'Q', x3, fluid)  # Calcular o entropia por meio da pressão e titulo
                t3 = CP.PropsSI('T', 'P', p3, 'Q', x3, fluid)
            elif op3 == 2:
            #  p3 = float(input('Entre com a pressão da bomba (kPa) (Estado 3): ')) * 1000
            #  t3 = float(input("Entre com a temperatura da bomba: estado 3 ")) + 273.15  # Converter para K
                # t4 = float(input('Enter the turbine inlet temperature (°C): ')) + 273.15  # Converter para K
                h3 = CP.PropsSI('H', 'P', p3, 'T', t3, fluid)  # calcular a entalpia por meio da pressão e temperatura
                v3 = 1 / CP.PropsSI('D', 'P', p3, 'T', t3,
                                    fluid)  # calcular o volume especifico por meio da presssão e temperatura
                s3 = CP.PropsSI('S', 'P', p3, 'T', t3, fluid)  # calcular a entropia por meio da presssão e temperatura
            

            # ESTADO 11: saída da bomba II
        
            p11 = p2
            h11_iso = (v3 * (p11 - p3)) + h3  
            s11 = CP.PropsSI('S', 'P', p11, 'H', h11_iso, fluid)
            t11 = CP.PropsSI('T', 'P', p11, 'H', h11_iso, fluid)

            h11 = (h11_iso - h3 + n*h3)/n

            #ESTADO 5
        # op5 = int(input("A turbina de alta pressão depende de: \n 1-Pressão e temperatura \n 2-Pressão e titulo \n "))  # entrada da condição da turbina de alta pressão
            if op5 == 1:
                p5 = p2
            # t5 = float(input("Entre com a temperatura de entrada da turbina de alta pressão: ")) + 273.15  # pegar a temperatura em graus celcius e transformar em Kelvin
                h5 = CP.PropsSI('H', 'P', p5, 'T', t5, fluid)  # calcular a entalpia por meio da pressão e temperatura
                s5 = CP.PropsSI('S', 'P', p5, 'T', t5, fluid)  # Calcular a entropia por meio da pressao e entalpia
            elif op5 == 2:
                p5 = p2  # Converter para Pa
            #  x5 = float(input("Entre com o titulo da entrada da turbina de alta pressão: (estado 7) "))  # entrada do titulo
                h5 = CP.PropsSI('H', 'P', p5, 'Q', x5, fluid)  # Calcular a entalpia por meio da pressao e titulo
                s5 = CP.PropsSI('S', 'P', p5, 'Q', x5, fluid)  # Calcular o entropia por meio da pressão e titulo
                t5 = CP.PropsSI('T', 'P', p5, 'Q', x5, fluid)

            # Estado 6: primeira saida da turbina de alta pressão
            
        # p6 = float(input('Entre com a pressão saída da turbina (kPa) (Estado 6): ')) * 1000
            s6_iso = s5  # condição do ciclo onde as entropias são equivalentes
            h6_iso = CP.PropsSI('H', 'P', p6, 'S', s6_iso, fluid)  # calcular a entalpia por meio da pressão e entropia
            t6_iso = CP.PropsSI('T', 'P', p6, 'S', s6_iso, fluid)

            #nt =  float(input("Digite a eficiencia da turbinas"))
            h6 =  h5 - nt*h5 + nt*h6_iso
            s6 = CP.PropsSI('S', 'P', p6, 'H', h6, fluid)
            t6 = CP.PropsSI('T', 'P', p6, 'H', h6, fluid)

            #ESTADO 7: ENTRADA DA TURBINA DE BAIXA
        # op7 = int(input("A turbina de baixa pressão depende de: \n 1-Pressão e temperatura \n 2-Pressão e titulo \n "))  # entrada da condição da turbina de alta pressão
            if op7 == 1:
                p7 = p6
            #  t7 = float(input("Entre com a temperatura de entrada da turbina de baixa pressão: ")) + 273.15  # pegar a temperatura em graus celcius e transformar em Kelvin
                h7 = CP.PropsSI('H', 'P', p7, 'T', t7, fluid)  # calcular a entalpia por meio da pressão e temperatura
                s7 = CP.PropsSI('S', 'P', p7, 'T', t7, fluid)  # Calcular a entropia por meio da pressao e entalpia
            elif op7 == 2:
                p7 = p6
            # x7 = float(input("Entre com o titulo da entrada da turbina de baixa pressão: "))  # entrada do titulo
                h7 = CP.PropsSI('H', 'P', p7, 'Q', x7, fluid)  # Calcular a entalpia por meio da pressao e titulo
                s7 = CP.PropsSI('S', 'P', p7, 'Q', x7, fluid)  # Calcular o entropia por meio da pressão e titulo
                t7 = CP.PropsSI('T', 'P', p7, 'Q', x7, fluid)

            # Estado 8: saida turbina de baixa pressão
            p8 = p3
            s8_iso = s7  # condição do ciclo onde as entropias são equivalentes
            h8_iso = CP.PropsSI('H', 'P', p8, 'S', s8_iso, fluid)  # calcular a entalpia por meio da pressão e entropia
            t8_iso = CP.PropsSI('T', 'P', p8, 'S', s8_iso, fluid)

            h8 = h7 - n*h7 + n*h8_iso

            t8 = CP.PropsSI('T', 'P', p8, 'H', h8, fluid) 
            s8 = CP.PropsSI('S', 'P', p8, 'H', h8, fluid)
            
            # Estado 9: saida turbina de baixa pressão
            p9 = p1
            s9_iso = s7  # condição do ciclo onde as entropias são equivalentes
            h9_iso = CP.PropsSI('H', 'P', p9, 'S', s9_iso, fluid)  # calcular a entalpia por meio da pressão e entropia
            t9_iso = CP.PropsSI('T', 'P', p9, 'S', s9_iso, fluid)

            h9 = h7 - n*h7 + n*h9_iso

            s9 = CP.PropsSI('S', 'P', p9, 'H', h9, fluid)
            t9 = CP.PropsSI('T', 'P', p9, 'H', h9, fluid)

            #ESTADO 10
            p10 = p2
            h10 = h3
            s10 = CP.PropsSI('S', 'P', p10, 'H', h10, fluid)
            t10 = CP.PropsSI('S', 'P', p10, 'H', h10, fluid)

            y = (h11 - h2) / (h8 - h3 + h11 - h2)

            h4 = (1-y)*h10 + y*h11
            p4 = p11
            s4 = CP.PropsSI('S', 'P', p4, 'H', h4, fluid)
            t4 = CP.PropsSI('T', 'P', p4, 'H', h4, fluid)
            
            m8 =  y * m 

            wt = m*(h5 - h6) + m*(h7 - h8) + (1-y)* m * (h8 - h9)
            
            wb = (1-y)*m*(h1 - h2) + y*m*(h3 - h11)

            wliq = wt - abs(wb)
            qh1 = m*(h5 - h4)
            qh2 = m*(h7 - h6)
            qh = qh1 + qh2

            eta = wliq / qh


            if eta <= 0 or qh<=0 or wt<=0 or wb>=0:

                if h5<=h4 or h7<=h6: #erro na caldeira
                    erro =1

                elif h6>=h5 or h8>=h7 or h9>=h8: #Erro na turbina
                    erro =2

                elif h1>=h2 or h3>=h11: #erro na bomba
                    erro = 3

            elif  t2<t1: #Erro no estado 1
                erro =4

            elif s2<s1 or t2<t1: #Erro no estado 2
                erro = 5
            
            elif  t3>t11 or t3<t1: #Erro no estado 3
                erro=6

            elif t5< t4 or t5<t6: #Erro no estado 5
                erro = 8

            elif s6<s1 or s6<s4 or t6>t5 or t6>t7: #Erro do estado 6
                erro = 9

            elif s7<s2 or t7<t8: #erro no estado 7
                erro= 10    

            elif y <= 0 or y>=1:
                erro = 11

            else:
                erro =0

    #__________verifica as propriedades dentro da tabela pela entropia___________________
            verificar =False
            valores = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11 ]
            for valor in valores:
                if valor is None:
                    verificar = True
                    break

            if verificar is True:
                verificar1 = 2
        
            else:
                verificar1 = 1
            
            return {
        'trabalhos': {
            'wt': round(wt / 1000, 4),
            'wliq': round(wliq / 1000, 4),
            'wb': round(wb / 1000, 4),
            'qh': round(qh / 1000, 4),
            'eta': round(eta , 4),
            'y': round(y , 4),
            'm8': round(m8 , 4)
        },
        'pressões': {
            'p1': round(p1 / 1000, 4),
            'p2': round(p2 / 1000, 4),
            'p3': round(p3 / 1000, 4),
            'p4': round(p4 / 1000, 4),
            'p5': round(p5 / 1000, 4),
            'p6': round(p6 / 1000, 4),
            'p7': round(p7 / 1000, 4),
            'p8': round(p8 / 1000, 4),
            'p9': round(p9 / 1000, 4),
            'p10': round(p10 / 1000, 4),
            'p11': round(p11 / 1000, 4)
        },
        'temperaturas': {
            't1': round(t1 - 273.15, 4),
            't2': round(t2 - 273.15, 4),
            't3': round(t3 - 273.15, 4),
            't4': round(t4 - 273.15, 4),
            't5': round(t5 - 273.15, 4),
            't6': round(t6 - 273.15, 4),
            't7': round(t7 - 273.15, 4),
            't8': round(t8 - 273.15, 4),
            't9': round(t9 - 273.15, 4),
            't10': round(t10 - 273.15, 4),
            't11': round(t11 - 273.15, 4),
        },
        'entalpias': {
            'h1': round(h1 / 1000, 4),
            'h2': round(h2 / 1000, 4),
            'h3': round(h3 / 1000, 4),
            'h4': round(h4 / 1000, 4),
            'h5': round(h5 / 1000, 4),
            'h6': round(h6 / 1000, 4),
            'h7': round(h7 / 1000, 4),
            'h8': round(h8 / 1000, 4),
            'h9': round(h9 / 1000, 4),
            'h10': round(h10 / 1000, 4),
            'h11': round(h11 / 1000, 4),

        },
        'entropias': {
            's1': round(s1 / 1000, 4),
            's2': round(s2 / 1000, 4),
            's3': round(s3 / 1000, 4),
            's4': round(s4 / 1000, 4),
            's5': round(s5 / 1000, 4),
            's6': round(s6 / 1000, 4),
            's7': round(s7 / 1000, 4),
            's8': round(s8 / 1000, 4),
            's9': round(s9 / 1000, 4),
            's10': round(s10 / 1000, 4),
            's11': round(s11 / 1000, 4),
        }
    }
        
        except ValueError:
            verificar1 = 2

            if verificar1 ==2:
               return verificar1


        

