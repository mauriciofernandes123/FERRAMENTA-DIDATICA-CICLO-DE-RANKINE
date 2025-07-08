import CoolProp.CoolProp as CP

def allPropriedades(substancia, propriedade1, propriedade2, op1, op2):
    try:
        propriedades = ['P', 'T', 'V', 'U', 'H', 'S', 'Q']
        lista_resultado = {}
        liquidos = {}
        vapores = {}
        fase = None

        # Função para converter unidades
        def converter_unidade(valor, tipo):
            if tipo in ['P', 'U', 'H', 'S']:
                return valor * 1000  # kPa para Pa, kJ/kg para J/kg
            elif tipo == 'T':
                return valor + 273.15  # °C para K
            elif tipo == 'Q':
                return valor
            return valor

        # Converte as unidades das propriedades
        prop1 = converter_unidade(propriedade1, op1)
        prop2 = converter_unidade(propriedade2, op2)

        # Verifica a ordem das propriedades de entrada
        if op1 == 'H' and op2 == 'P':
            # Inverte a ordem das propriedades para P e H
            op1, op2 = op2, op1
            prop1, prop2 = prop2, prop1 

        # Verifica a ordem das propriedades de entrada
        if op1 == 'S' and op2 == 'P':
            
            op1, op2 = op2, op1
            prop1, prop2 = prop2, prop1

         # Verifica a ordem das propriedades de entrada
        if op1 == 'S' and op2 == 'T':
            
            op1, op2 = op2, op1
            prop1, prop2 = prop2, prop1


        # Calcula as propriedades
        for propriedade in propriedades:
            if propriedade == 'V':
                propriedade_coolprop = 'D'  # Densidade no CoolProp
            else:
                propriedade_coolprop = propriedade

            # Calcula a propriedade
            try:
                if propriedade_coolprop == 'D':
                    propriedadeEncontrada = 1 / CP.PropsSI(propriedade_coolprop, op1, prop1, op2, prop2, substancia)
                else:
                    propriedadeEncontrada = CP.PropsSI(propriedade_coolprop, op1, prop1, op2, prop2, substancia)

                # Determina a fase
                if fase is None:
                    fase = CP.PhaseSI(op1, prop1, op2, prop2, substancia)

                # Conversão de unidades para as propriedades específicas
                if propriedade in ['P', 'U', 'H', 'S']:
                    propriedadeEncontrada /= 1000  # J/kg para kJ/kg
                elif propriedade == 'T':
                    propriedadeEncontrada -= 273.15  # K para °C

                # Armazena o resultado
                lista_resultado[propriedade] = round(propriedadeEncontrada, 6)

                # Se a fase for bifásica, calcular líquido e vapor
                if fase == 'twophase':

                    if op1 == 'Q':
                        liquido = CP.PropsSI(propriedade_coolprop, 'Q', 0, op2, prop2, substancia)
                        vapor = CP.PropsSI(propriedade_coolprop, 'Q', 1, op2, prop2, substancia)
                    else:
                        liquido = CP.PropsSI(propriedade_coolprop, op1, prop1, 'Q', 0, substancia)
                        vapor = CP.PropsSI(propriedade_coolprop, op1, prop1, 'Q', 1, substancia)
                    
                    # Converter unidade para as propriedades específicas
                    if propriedade in ['P', 'U', 'H', 'S']:
                        liquido /= 1000
                        vapor /= 1000
                    elif propriedade == 'T':
                        liquido -= 273.15
                        vapor -= 273.15
                    
                    elif propriedade =='V':
                        liquido = 1/liquido
                        vapor = 1/vapor

                    liquidos[propriedade] = round(liquido, 6)
                    vapores[propriedade] = round(vapor, 6)
                else:
                    liquidos[propriedade] = None
                    vapores[propriedade] = None

            except Exception as e:
                lista_resultado[propriedade] = f'Erro: {str(e)}'
                liquidos[propriedade] = None
                vapores[propriedade] = None

        return {
            'propriedades': lista_resultado,
            'liquidos': liquidos,
            'vapores': vapores,
            'fase': fase
        }

    except Exception as e:
        return f'Erro: {str(e)}'