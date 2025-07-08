import flet as ft
from Ciclos import Ciclos
from propriedades_2 import allPropriedades
from otimizacao import otimizarReaquecimento
import webbrowser
from flet.matplotlib_chart import MatplotlibChart
import matplotlib.pyplot as plt

def main(page: ft.Page):
    page.title = "Ferramenta Didática: Ciclo de Rankine"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.theme_mode = ft.ThemeMode.DARK  # Define o tema inicial como escuro
    page.window_maximized = True
    
    
    # # Container para a animação
    # c1 = ft.Container(
    #     ft.Text("Bem-vindo à Ferramenta Didática Ciclo de Rankine!", 
    #              style=ft.TextThemeStyle.HEADLINE_MEDIUM, color=ft.colors.WHITE),
    #     alignment=ft.alignment.center,
    #     width=page.window_width,
    #     height=page.window_height,
    #     bgcolor=ft.colors.GREY_800,  # Tom de cinza mais escuro
    #     padding=20,
    # )

    # c2 = ft.Container(
    #     ft.Text("Vamos começar a explorar!", 
    #              style=ft.TextThemeStyle.HEADLINE_MEDIUM, color=ft.colors.WHITE),
    #     alignment=ft.alignment.center,
    #     width=page.window_width,
    #     height=page.window_height,
    #     bgcolor=ft.colors.GREY_900,  # Tom de cinza um pouco mais claro
    #     padding=20,
    # )
    
    # # Animador que alterna entre c1 e c2
    # c = ft.AnimatedSwitcher(
        
    #     c1,
    #     transition=ft.AnimatedSwitcherTransition.SCALE,  # Transição de escala
    #     duration=1000,  # Duração da transição
    #     reverse_duration=500,
    #     switch_in_curve=ft.AnimationCurve.EASE_IN_OUT,
    #     switch_out_curve=ft.AnimationCurve.EASE_IN_OUT,
    # )

    # # Função para alternar entre as mensagens
    # def animate(e=None):
    #     c.content = c2 if c.content == c1 else c1
    #     c.update()

    # # Adiciona o container à página
    # page.add(c)

    # # Função para iniciar a animação
    # def start_animation():
    #     animate()
    #     # Após 10 segundos, remove a animação
    #     Timer(2, remove_animation).start()  # 10 segundos de animação

    # def remove_animation():
    #     c.content = ft.Text("")  # Remove o conteúdo
    #     c.update()  # Atualiza a página

    # # Inicia a animação após um pequeno delay
    # Timer(2, start_animation).start()  # 0.5 segundos de delay

    # page.update()
    


    # Função para alternar o tema
    def toggle_theme(e):
        page.theme_mode = ft.ThemeMode.LIGHT if page.theme_mode == ft.ThemeMode.DARK else ft.ThemeMode.DARK
        page.update()
#_______________________________________________________________________________



    

#____________________________________________________________________________________
    # Função para exibir alertas no estilo SnackBar
    def show_warning(message):
        page.snack_bar = ft.SnackBar(
            content=ft.Text(message),
            bgcolor=ft.colors.RED,
            duration=3000  # Duração de 3 segundos
        )
        page.snack_bar.open = True
        page.update()
#_____________________________________________________________________

    # Função para mudar o conteúdo da página principal com base na seleção do NavigationDrawer
    def handle_change(e):
        conteudo_pagina.controls.clear()
#_______________________________________________________________________________________________________________

        # Determine qual item foi selecionado pelo índice
        selected_index = e.control.selected_index

        if selected_index == 0:
            conteudo_pagina.controls.append(criar_calculadora_propriedades())
        elif selected_index == 1:
            conteudo_pagina.controls.append(criar_ciclo_simples())
        elif selected_index == 2:
            conteudo_pagina.controls.append(criar_ciclo_reaquecimento())
        elif selected_index == 3:
            conteudo_pagina.controls.append(criar_ciclo_regerativo())
        elif selected_index == 4:
            conteudo_pagina.controls.append(criar_ciclo_regerativo_reaquecimento())

        elif selected_index == 5:
            conteudo_pagina.controls.append(criar_pagina_contato())
        elif selected_index == 6:
            conteudo_pagina.controls.append(criar_pagina_sobre())

        page.update()
#_________________________________________________________________________________________________________________________


#_____________________MUDAR PAGINA DOS EXEMPLOS__________________________
    def exemploSimples(e):
            conteudo_pagina.controls.clear()
            conteudo_pagina.controls.append(pageExemploSimples())
            page.update()

    def exemploReaquecimento(e):
            conteudo_pagina.controls.clear()
            conteudo_pagina.controls.append(pageExemploReaquecimento())
            page.update()
    
    def exemploRegenerativo(e):
            conteudo_pagina.controls.clear()
            conteudo_pagina.controls.append(pageExemploRegenerativo())
            page.update()
    
    def exemploRegerativoReaquecimento(e):
            conteudo_pagina.controls.clear()
            conteudo_pagina.controls.append(pageExemploRegenerativoReaquecimento())
            page.update()
    


    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.ENGINEERING),
        leading_width=40,
        title=ft.Text("Ferramenta Didática Ciclo de Rankine"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.IconButton(ft.icons.WB_SUNNY_OUTLINED, on_click=toggle_theme),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Exemplo Rankine Simples", on_click=exemploSimples),
                    ft.PopupMenuItem(text="Exemplo Rankine Reaquecimento", on_click=exemploReaquecimento),
                    ft.PopupMenuItem(text="Exemplo Rankine Regenerativo", on_click=exemploRegenerativo),
                    ft.PopupMenuItem(text="Exemplo Rankine Regerativo com Reaquecimento", on_click=exemploRegerativoReaquecimento),
                    ft.PopupMenuItem(),  # divider
                    
                ]
            ),
        ],
    )
    

    def mostrar_grafico_t_s(entropias, temperaturas):


        # Cria o gráfico
        fig, ax = plt.subplots()
        ax.plot(entropias, temperaturas, marker='o', linestyle='-', color='b')
        ax.set_title("Diagrama T-s (Temperatura vs. Entropia)")
        ax.set_xlabel("Entropia (kJ/kg·K)")
        ax.set_ylabel("Temperatura (°C)")
        ax.grid(True)

        # Adiciona o gráfico ao Flet
        chart = MatplotlibChart(fig, expand=True)
        
        # Função para fechar o diálogo
        def fechar_dialogo(e):
            dialog.open = False
            page.update()
        # Cria um Dialog para exibir o gráfico
        dialog = ft.AlertDialog(
            title=ft.Text("Gráfico T-s (PRESSIONE esc OU fechar)"),
            content=chart,
            actions=[
                ft.TextButton("Fechar", on_click=fechar_dialogo)
            ],
            actions_alignment=ft.MainAxisAlignment.CENTER,
        )
        page.dialog = dialog
        dialog.open = True

       
        page.update()

    def mostrar_grafico_otimizacao(lista_Pressoesplot, lista_Rendimentosplot, lista_Trabalhosplot):
        # Cria a figura e o eixo principal
        fig, ax1 = plt.subplots()

        # Primeiro eixo vertical (Rendimento)
        ax1.plot(lista_Pressoesplot, lista_Rendimentosplot, color='tab:green',  linestyle='-')
        ax1.set_xlabel('Pressões intermediárias (KPa)')
        ax1.set_ylabel('Rendimento (%)', color='tab:green')
        ax1.tick_params(axis='y', labelcolor='tab:green')

        # Segundo eixo vertical (Trabalhos líquidos)
        ax2 = ax1.twinx()
        ax2.plot(lista_Pressoesplot, lista_Trabalhosplot, color='tab:blue', linestyle='--')
        ax2.set_ylabel('Trabalhos líquidos (kJ/kg)', color='tab:blue')
        ax2.tick_params(axis='y', labelcolor='tab:blue')

        plt.title('Gráfico da otimização da pressão intermediária')
        plt.grid(True)

        # Adiciona o gráfico ao Flet
        chart = MatplotlibChart(fig, expand=True)

        # Função para fechar o diálogo
        def fechar_dialogo(e):
            dialog.open = False
            page.update()

        # Cria um Dialog para exibir o gráfico
        dialog = ft.AlertDialog(
            title=ft.Text("Gráfico de Otimização (PRESSIONE esc OU fechar)"),
            content=chart,
            actions=[
                ft.TextButton("Fechar", on_click=fechar_dialogo)
            ],
            actions_alignment=ft.MainAxisAlignment.CENTER,
        )

        page.dialog = dialog
        dialog.open = True
        page.update()
    
    # Função que cria a interface para o Ciclo de Rankine Simples
    def criar_ciclo_simples():
        
        # Funções para alternar entre temperatura e título
        op1 = 0
        op2 = 0

        # Funções para alternar entre temperatura e título
        def on_temperatura_bomba_change(e):
            nonlocal op1
            if checkbox_temperatura_bomba.value:
                checkbox_titulo_bomba.value = False
                op1 = 2
            page.update()

        def on_titulo_bomba_change(e):
            nonlocal op1
            if checkbox_titulo_bomba.value:
                checkbox_temperatura_bomba.value = False
                op1 = 1
            page.update()

        def on_temperatura_caldeira_change(e):
            nonlocal op2
            if checkbox_temperatura_caldeira.value:
                checkbox_titulo_caldeira.value = False
                op2 = 2
            page.update()

        def on_titulo_caldeira_change(e):
            nonlocal op2
            if checkbox_titulo_caldeira.value:
                checkbox_temperatura_caldeira.value = False
                op2 = 1
            page.update()

        # Campos para a bomba
        bomba_label = ft.Text("A bomba depende de:", size=15, weight=ft.FontWeight.BOLD)
        checkbox_temperatura_bomba = ft.Checkbox(label="TEMPERATURA", on_change=on_temperatura_bomba_change)
        checkbox_titulo_bomba = ft.Checkbox(label="TÍTULO", on_change=on_titulo_bomba_change)

        p1 = ft.TextField(label="Entre com a pressão da bomba (kPa) (ESTADO 1):", width=400)
        t1 = ft.TextField(label="Temperatura da bomba (Selecione TEMPERATURA) (ESTADO 1):", width=400)
        p2 = ft.TextField(label="Entre com a pressão de saída da bomba (kPa) (ESTADO 2):", width=400)

        # Campos para a caldeira
        caldeira_label = ft.Text("A saída da caldeira/entrada da turbina depende de:", size=15, weight=ft.FontWeight.BOLD)
        checkbox_temperatura_caldeira = ft.Checkbox(label="TEMPERATURA", on_change=on_temperatura_caldeira_change)
        checkbox_titulo_caldeira = ft.Checkbox(label="TÍTULO", on_change=on_titulo_caldeira_change)

        x3 = ft.TextField(label="Entre com o título da caldeira em % (Selecione TÍTULO) (ESTADO 3):", width=400)
        t3 = ft.TextField(label="Temperatura da caldeira (Selecione TEMPERATURA) (ESTADO 3):", width=400)

        # Função de cálculo (placeholder)
        def calcular(e):
            
            if not (checkbox_temperatura_bomba.value or checkbox_titulo_bomba.value):
                show_warning("A DEPENDÊNCIA DA BOMBA NÃO FOI MARCADA")
                return

            if not (checkbox_temperatura_caldeira.value or checkbox_titulo_caldeira.value):
                show_warning("A DEPENDÊNCIA DA CALDEIRA NÃO FOI MARCADA")
                return

            if not p1.value:
                show_warning("PREENCHA A PRESSÃO DO ESTADO 1")
                return

            if checkbox_temperatura_bomba.value and not t1.value:
                show_warning("PREENCHA A TEMPERATURA DO ESTADO 1")
                return

            if not p1.value:
                show_warning("PREENCHA A PRESSÃO DO ESTADO 2")
                return

            if checkbox_titulo_caldeira.value and not x3.value:
                show_warning("PREENCHA O TÍTULO DO ESTADO 3")
                return

            if checkbox_temperatura_caldeira.value and not t3.value:
                show_warning("PREENCHA A TEMPERATURA DO ESTADO 3")
                return

            try:
                p1_valor = float(p1.value) * 1000
            except ValueError:
                show_warning("PREENCHA A PRESSÃO DO ESTADO 1 COM UM NÚMERO VÁLIDO")
                return

            if checkbox_temperatura_bomba.value:
                try:
                    t1_valor = float(t1.value) + 273.15
                except ValueError:
                    show_warning("PREENCHA A TEMPERATURA DO ESTADO 1 COM UM NÚMERO VÁLIDO")
                    return
            else:
                t1_valor = None

            try:
                p2_valor = float(p2.value) * 1000
            except ValueError:
                show_warning("PREENCHA A PRESSÃO DO ESTADO 2 COM UM NÚMERO VÁLIDO")
                return

            if checkbox_titulo_caldeira.value:
                try:
                    x3_valor = float(x3.value)
                except ValueError:
                    show_warning("PREENCHA O TÍTULO DO ESTADO 3 COM UM NÚMERO VÁLIDO")
                    return
            else:
                x3_valor = None

            if checkbox_temperatura_caldeira.value:
                try:
                    t3_valor = float(t3.value) + 273.15
                except ValueError:
                    show_warning("PREENCHA A TEMPERATURA DO ESTADO 3 COM UM NÚMERO VÁLIDO")
                    return
            else:
                t3_valor = None

            # Se todas as validações passaram
            resultado = Ciclos.rankineSimples(op1, p1_valor, t1_valor, p2_valor, op2, x3_valor, t3_valor)
            
            
           


        
            ft.Text("Resultados do Ciclo de Rankine Simples:", size=18)

            tabela_resultados.controls.clear()  
                    # Exemplo de tabela para exibir resultados
            tabela_resultados.controls.append(
                ft.DataTable(
                    columns=[
                        ft.DataColumn(label=ft.Text("Estado")),
                        ft.DataColumn(label=ft.Text("Temperatura (°C)")),
                        ft.DataColumn(label=ft.Text("Pressão (kPa)")),
                        ft.DataColumn(label=ft.Text("Entalpia (kJ/kg)")),
                        ft.DataColumn(label=ft.Text("Entropia (kJ/kg·K)")),
                    ],
                    rows=[
                        ft.DataRow(cells=[
                            ft.DataCell(ft.Text("ESTADO 1")),
                            ft.DataCell(ft.Text(str(resultado['temperaturas']["t1"]))),
                            ft.DataCell(ft.Text(str(resultado['pressões']["p1"]))),
                            ft.DataCell(ft.Text(str(resultado['entalpias']["h1"]))),
                            ft.DataCell(ft.Text(str(resultado['entropias']["s1"])))
                        ]),
                        ft.DataRow(cells=[
                            ft.DataCell(ft.Text("ESTADO 2")),
                            ft.DataCell(ft.Text(str(resultado['temperaturas']["t2"]))),
                            ft.DataCell(ft.Text(str(resultado['pressões']["p2"]))),
                            ft.DataCell(ft.Text(str(resultado['entalpias']["h2"]))),
                            ft.DataCell(ft.Text(str(resultado['entropias']["s2"])))
                        ]),
                        ft.DataRow(cells=[
                            ft.DataCell(ft.Text("ESTADO 3")),
                            ft.DataCell(ft.Text(str(resultado['temperaturas']["t3"]))),
                            ft.DataCell(ft.Text(str(resultado['pressões']["p3"]))),
                            ft.DataCell(ft.Text(str(resultado['entalpias']["h3"]))),
                            ft.DataCell(ft.Text(str(resultado['entropias']["s3"])))
                        ]),
                        ft.DataRow(cells=[
                            ft.DataCell(ft.Text("ESTADO 4")),
                            ft.DataCell(ft.Text(str(resultado['temperaturas']["t4"]))),
                            ft.DataCell(ft.Text(str(resultado['pressões']["p4"]))),
                            ft.DataCell(ft.Text(str(resultado['entalpias']["h4"]))),
                            ft.DataCell(ft.Text(str(resultado['entropias']["s4"])))
                        ]),
                        ft.DataRow(cells=[
                            ft.DataCell(ft.Text("-------")),
                            ft.DataCell(ft.Text("-------")),  # Ajuste conforme necessário
                            ft.DataCell(ft.Text("-------")),
                            ft.DataCell(ft.Text("-------")),
                            ft.DataCell(ft.Text("-------"))
                        ]),

                        ft.DataRow(cells=[
                            ft.DataCell(ft.Text("Resultados Ciclo")),
                            ft.DataCell(ft.Text("")),  # Ajuste conforme necessário
                            ft.DataCell(ft.Text("")),
                            ft.DataCell(ft.Text("")),
                            ft.DataCell(ft.Text(""))
                            
                        ]),
                        

                        ft.DataRow(cells=[
                            ft.DataCell(ft.Text("Eficiência")),
                            ft.DataCell(ft.Text(str(resultado["trabalhos"]["eta"]))),  # Ajuste conforme necessário
                            ft.DataCell(ft.Text("")),  
                            ft.DataCell(ft.Text("")),
                            ft.DataCell(ft.Text("")),
                            
                        ]),

                        ft.DataRow(cells=[
                            ft.DataCell(ft.Text("Trabalho da turbina (kJ/kg)")),
                            ft.DataCell(ft.Text(str(resultado["trabalhos"]["wt"]))),  # Ajuste conforme necessário
                            ft.DataCell(ft.Text("")),  
                            ft.DataCell(ft.Text("")),
                            ft.DataCell(ft.Text("")),
                            
                        ]),
                        
                        ft.DataRow(cells=[
                            ft.DataCell(ft.Text("Trabalho da bomba (kJ/kg)")),
                            ft.DataCell(ft.Text(str(resultado["trabalhos"]["wb"]))),  # Ajuste conforme necessário
                            ft.DataCell(ft.Text("")),  
                            ft.DataCell(ft.Text("")),
                            ft.DataCell(ft.Text("")),
                        ]),
                        
                        ft.DataRow(cells=[
                            ft.DataCell(ft.Text("Calor da caldeira (kJ/kg)")),
                            ft.DataCell(ft.Text(str(resultado["trabalhos"]["qh"]))),  # Ajuste conforme necessário
                            ft.DataCell(ft.Text("")),  
                            ft.DataCell(ft.Text("")),
                            ft.DataCell(ft.Text("")),
                        ]),
                    ],
                )
            )
            page.update()
            
            # Extrai os dados de entropia e temperatura
            entropias = list(resultado['entropias'].values())
            temperaturas = list(resultado['temperaturas'].values())
          
            mostrar_grafico_t_s(entropias, temperaturas)
            
            page.update()

        # Função para limpar os campos preenchidos
        def limpar(e):
            p1.value = ""
            t1.value = ""
            p2.value = ""
            x3.value = ""
            t3.value = ""
            checkbox_temperatura_bomba.value = False
            checkbox_titulo_bomba.value = False
            checkbox_temperatura_caldeira.value = False
            checkbox_titulo_caldeira.value = False
            tabela_resultados.controls.clear()
            page.update()

        calcular_btn = ft.ElevatedButton("CALCULAR", on_click=calcular)
        limpar_btn = ft.ElevatedButton("LIMPAR", on_click=limpar)

        # Container para os campos de entrada
        container_esquerda = ft.Column([
            bomba_label,
            ft.Row([checkbox_temperatura_bomba, checkbox_titulo_bomba], alignment=ft.MainAxisAlignment.START),
            p1,
            t1,
            p2,
            ft.Divider(height=20),
            caldeira_label,
            ft.Row([checkbox_temperatura_caldeira, checkbox_titulo_caldeira], alignment=ft.MainAxisAlignment.START),
            x3,
            t3,
            ft.Row([calcular_btn, limpar_btn], alignment=ft.MainAxisAlignment.START)
        ])

        # Container para a tabela de resultados
        tabela_resultados = ft.Column([])

        container_direita = ft.Column([
            
            tabela_resultados
        ])

        # Retorna a interface com os dois containers (esquerda e direita)
        return ft.Row([
            ft.Container(content=container_esquerda, width=500),
            ft.Container(content=container_direita, width=1000)
        ], alignment=ft.MainAxisAlignment.START)
#________________________________________________________________________________________________________________________________



#####################################################################################################
# Função que cria a interface para o Ciclo de Rankine Reaquecimento  
    def criar_ciclo_reaquecimento():  
        # Funções para alternar entre temperatura e título  
        op1 = 0  
        op2 = 0  
        op3 = 0  # Nova variável para a turbina  

        # Funções para alternar entre temperatura e título da bomba  
        def on_temperatura_bomba_change(e):  
            nonlocal op1  
            if checkbox_temperatura_bomba.value:  
                checkbox_titulo_bomba.value = False  
                op1 = 2  
            page.update()  

        def on_titulo_bomba_change(e):  
            nonlocal op1  
            if checkbox_titulo_bomba.value:  
                checkbox_temperatura_bomba.value = False  
                op1 = 1  
            page.update()  

        # Funções para alternar entre temperatura e título da caldeira  
        def on_temperatura_caldeira_change(e):  
            nonlocal op2  
            if checkbox_temperatura_caldeira.value:  
                checkbox_titulo_caldeira.value = False  
                op2 = 2  
            page.update()  

        def on_titulo_caldeira_change(e):  
            nonlocal op2  
            if checkbox_titulo_caldeira.value:  
                checkbox_temperatura_caldeira.value = False  
                op2 = 1 
            page.update()  

        # Funções para alternar entre temperatura e título da turbina  
        def on_temperatura_turbina_change(e):  
            nonlocal op3  
            if checkbox_temperatura_turbina.value:  
                checkbox_titulo_turbina.value = False  
                op3 = 1 
            page.update()  

        def on_titulo_turbina_change(e):  
            nonlocal op3  
            if checkbox_titulo_turbina.value:  
                checkbox_temperatura_turbina.value = False  
                op3 = 1  
            page.update()  

        # Campos para a bomba  
        bomba_label = ft.Text("A bomba depende de:", size=15, weight=ft.FontWeight.BOLD)  
        checkbox_temperatura_bomba = ft.Checkbox(label="TEMPERATURA", on_change=on_temperatura_bomba_change)  
        checkbox_titulo_bomba = ft.Checkbox(label="TÍTULO", on_change=on_titulo_bomba_change)  

        p1 = ft.TextField(label="Entre com a pressão da entrada da bomba (kPa) (ESTADO 1):", width=400)  
        t1 = ft.TextField(label="Temperatura da bomba (Selecione TEMPERATURA) (ESTADO 1):", width=400)  
        p2 = ft.TextField(label="Entre com a pressão de saída da bomba (kPa) (ESTADO 2):", width=400)  

        # Campos para a caldeira  
        caldeira_label = ft.Text("A saída da caldeira/entrada da turbina depende de:", size=15, weight=ft.FontWeight.BOLD)  
        checkbox_temperatura_caldeira = ft.Checkbox(label="TEMPERATURA", on_change=on_temperatura_caldeira_change)  
        checkbox_titulo_caldeira = ft.Checkbox(label="TÍTULO", on_change=on_titulo_caldeira_change)  

        x3 = ft.TextField(label="Entre com o título da caldeira em % (SELECIONE TÍTULO) (ESTADO 3):", width=400)  
        t3 = ft.TextField(label="Temperatura da caldeira (Selecione TEMPERATURA) (ESTADO 3):", width=400)  

        # Campos para a turbina  
        turbina_label = ft.Text("A turbina de baixa pressão depende de:", size=15, weight=ft.FontWeight.BOLD)  
        checkbox_temperatura_turbina = ft.Checkbox(label="TEMPERATURA", on_change=on_temperatura_turbina_change)  
        checkbox_titulo_turbina = ft.Checkbox(label="TÍTULO", on_change=on_titulo_turbina_change)  

        t5 = ft.TextField(label="Temperatura da turbina (SELECIONE TEMPERATURA) (ESTADO 5):", width=400)  
        x5 = ft.TextField(label="Entre com o título da turbina em % (SELECIONE TÍTULO) (ESTADO 5):", width=400)  
        p4 = ft.TextField(label="Pressão intermediária (KPa) (ESTADO 4):", width=400)  

        # Função de cálculo (placeholder)  
        def calcular(e):  
            if not (checkbox_temperatura_bomba.value or checkbox_titulo_bomba.value):  
                show_warning("A DEPENDÊNCIA DA BOMBA NÃO FOI MARCADA")  
                return  

            if not (checkbox_temperatura_caldeira.value or checkbox_titulo_caldeira.value):  
                show_warning("A DEPENDÊNCIA DA CALDEIRA NÃO FOI MARCADA")  
                return  

            if not (checkbox_temperatura_turbina.value or checkbox_titulo_turbina.value):  
                show_warning("A DEPENDÊNCIA DA TURBINA NÃO FOI MARCADA")  
                return  

            if not p1.value:  
                show_warning("PREENCHA A PRESSÃO DO ESTADO 1")  
                return  

            if checkbox_temperatura_bomba.value and not t1.value:  
                show_warning("PREENCHA A TEMPERATURA DO ESTADO 1")  
                return  

            if not p2.value:  
                show_warning("PREENCHA A PRESSÃO DO ESTADO 2")  
                return  

            if checkbox_titulo_caldeira.value and not x3.value:  
                show_warning("PREENCHA O TÍTULO DO ESTADO 3")  
                return  

            if checkbox_temperatura_caldeira.value and not t3.value:  
                show_warning("PREENCHA A TEMPERATURA DO ESTADO 3")  
                return  

            if checkbox_temperatura_turbina.value and not t5.value:  
                show_warning("PREENCHA A TEMPERATURA DO ESTADO 5")  
                return  

            if checkbox_titulo_turbina.value and not x5.value:  
                show_warning("PREENCHA O TÍTULO DO ESTADO 5")  
                return  

            try:  
                p1_valor = float(p1.value) * 1000  
            except ValueError:  
                show_warning("PREENCHA A PRESSÃO DO ESTADO 1 COM UM NÚMERO VÁLIDO")  
                return  

            if checkbox_temperatura_bomba.value:  
                try:  
                    t1_valor = float(t1.value) + 273.15  
                except ValueError:  
                    show_warning("PREENCHA A TEMPERATURA DO ESTADO 1 COM UM NÚMERO VÁLIDO")  
                    return  
            else:  
                t1_valor = None  

            try:  
                p2_valor = float(p2.value) * 1000  
            except ValueError:  
                show_warning("PREENCHA A PRESSÃO DO ESTADO 2 COM UM NÚMERO VÁLIDO")  
                return  
            
            try:  
                p4_valor = float(p4.value) * 1000  
            except ValueError:  
                show_warning("PREENCHA A PRESSÃO DO ESTADO 4 COM UM NÚMERO VÁLIDO")  
                return  


            if checkbox_titulo_caldeira.value:  
                try:  
                    x3_valor = float(x3.value)  
                except ValueError:  
                    show_warning("PREENCHA O TÍTULO DO ESTADO 3 COM UM NÚMERO VÁLIDO")  
                    return  
            else:  
                x3_valor = None  

            if checkbox_temperatura_caldeira.value:  
                try:  
                    t3_valor = float(t3.value) + 273.15  
                except ValueError:  
                    show_warning("PREENCHA A TEMPERATURA DO ESTADO 3 COM UM NÚMERO VÁLIDO")  
                    return  
            else:  
                t3_valor = None  

            if checkbox_temperatura_turbina.value:  
                try:  
                    t5_valor = float(t5.value) + 273.15  
                except ValueError:  
                    show_warning("PREENCHA A TEMPERATURA DO ESTADO 5 COM UM NÚMERO VÁLIDO")  
                    return  
            else:  
                t5_valor = None  

            if checkbox_titulo_turbina.value:  
                try:  
                    x5_valor = float(x5.value)  
                except ValueError:  
                    show_warning("PREENCHA O TÍTULO DO ESTADO 5 COM UM NÚMERO VÁLIDO")  
                    return  
            else:  
                x5_valor = None  

            tabela_resultados.controls.clear()  

            # Se todas as validações passaram  
            resultado = Ciclos.reaquecimento(op1, p1_valor, t1_valor, p2_valor, op2, x3_valor, t3_valor, p4_valor, op3, t5_valor, x5_valor)
            page.update()  

          
            tabela_resultados.controls.clear()  
            # Exemplo de tabela para exibir resultados  
            tabela_resultados.controls.append(  
                ft.DataTable(  
                    columns=[  
                        ft.DataColumn(label=ft.Text("Estado")),  
                        ft.DataColumn(label=ft.Text("Temperatura (°C)")),  
                        ft.DataColumn(label=ft.Text("Pressão (kPa)")),  
                        ft.DataColumn(label=ft.Text("Entalpia (kJ/kg)")),  
                        ft.DataColumn(label=ft.Text("Entropia (kJ/kg·K)")),  
                    ],  
                    rows=[  
                        ft.DataRow(cells=[  
                            ft.DataCell(ft.Text("ESTADO 1")),  
                            ft.DataCell(ft.Text(str(resultado['temperaturas']["t1"]))),  
                            ft.DataCell(ft.Text(str(resultado['pressões']["p1"]))),  
                            ft.DataCell(ft.Text(str(resultado['entalpias']["h1"]))),  
                            ft.DataCell(ft.Text(str(resultado['entropias']["s1"])))  
                        ]),  
                        ft.DataRow(cells=[  
                            ft.DataCell(ft.Text("ESTADO 2")),  
                            ft.DataCell(ft.Text(str(resultado['temperaturas']["t2"]))),  
                            ft.DataCell(ft.Text(str(resultado['pressões']["p2"]))),  
                            ft.DataCell(ft.Text(str(resultado['entalpias']["h2"]))),  
                            ft.DataCell(ft.Text(str(resultado['entropias']["s2"])))  
                        ]),  
                        ft.DataRow(cells=[  
                            ft.DataCell(ft.Text("ESTADO 3")),  
                            ft.DataCell(ft.Text(str(resultado['temperaturas']["t3"]))),  
                            ft.DataCell(ft.Text(str(resultado['pressões']["p3"]))),  
                            ft.DataCell(ft.Text(str(resultado['entalpias']["h3"]))),  
                            ft.DataCell(ft.Text(str(resultado['entropias']["s3"])))  
                        ]),  
                        ft.DataRow(cells=[  
                            ft.DataCell(ft.Text("ESTADO 4")),  
                            ft.DataCell(ft.Text(str(resultado['temperaturas']["t4"]))),  
                            ft.DataCell(ft.Text(str(resultado['pressões']["p4"]))),  
                            ft.DataCell(ft.Text(str(resultado['entalpias']["h4"]))),  
                            ft.DataCell(ft.Text(str(resultado['entropias']["s4"])))  
                        ]),  

                        ft.DataRow(cells=[  
                            ft.DataCell(ft.Text("ESTADO 5")),  
                            ft.DataCell(ft.Text(str(resultado['temperaturas']["t5"]))),  
                            ft.DataCell(ft.Text(str(resultado['pressões']["p5"]))),  
                            ft.DataCell(ft.Text(str(resultado['entalpias']["h5"]))),  
                            ft.DataCell(ft.Text(str(resultado['entropias']["s5"])))  
                        ]),  

                        ft.DataRow(cells=[  
                            ft.DataCell(ft.Text("ESTADO 6")),  
                            ft.DataCell(ft.Text(str(resultado['temperaturas']["t6"]))),  
                            ft.DataCell(ft.Text(str(resultado['pressões']["p6"]))),  
                            ft.DataCell(ft.Text(str(resultado['entalpias']["h6"]))),  
                            ft.DataCell(ft.Text(str(resultado['entropias']["s6"])))  
                        ]),  

                        ft.DataRow(cells=[  
                            ft.DataCell(ft.Text("-------")),  
                            ft.DataCell(ft.Text("-------")),  
                            ft.DataCell(ft.Text("-------")),  
                            ft.DataCell(ft.Text("-------")),  
                            ft.DataCell(ft.Text("-------"))  
                        ]),  
                        ft.DataRow(cells=[  
                            ft.DataCell(ft.Text("Resultados Ciclo")),  
                            ft.DataCell(ft.Text("")),  
                            ft.DataCell(ft.Text("")),  
                            ft.DataCell(ft.Text("")),  
                            ft.DataCell(ft.Text(""))  
                        ]),  
                        ft.DataRow(cells=[  
                            ft.DataCell(ft.Text("Eficiência")),  
                            ft.DataCell(ft.Text(str(resultado["trabalhos"]["eta"]))),  
                            ft.DataCell(ft.Text("")),  
                            ft.DataCell(ft.Text("")),  
                            ft.DataCell(ft.Text(""))  
                        ]),  
                        ft.DataRow(cells=[  
                            ft.DataCell(ft.Text("Trabalho da turbina (kJ/kg)")),  
                            ft.DataCell(ft.Text(str(resultado["trabalhos"]["wt"]))),  
                            ft.DataCell(ft.Text("")),  
                            ft.DataCell(ft.Text("")),  
                            ft.DataCell(ft.Text(""))  
                        ]),  
                        ft.DataRow(cells=[  
                            ft.DataCell(ft.Text("Trabalho da bomba (kJ/kg)")),  
                            ft.DataCell(ft.Text(str(resultado["trabalhos"]["wb"]))),  
                            ft.DataCell(ft.Text("")),  
                            ft.DataCell(ft.Text("")),  
                            ft.DataCell(ft.Text(""))  
                        ]),  
                        ft.DataRow(cells=[  
                            ft.DataCell(ft.Text("Calor da caldeira (kJ/kg)")),  
                            ft.DataCell(ft.Text(str(resultado["trabalhos"]["qh"]))),  
                            ft.DataCell(ft.Text("")),  
                            ft.DataCell(ft.Text("")),  
                            ft.DataCell(ft.Text(""))  
                        ]),  
                    ],  
                )  
            )  
            page.update()
            
            # Extrai os dados de entropia e temperatura
            entropias = list(resultado['entropias'].values())
            temperaturas = list(resultado['temperaturas'].values())
          
            mostrar_grafico_t_s(entropias, temperaturas)
            page.update()
#______________________________________________________________________________________________________________________________________________________
        
        # Função de cálculo (placeholder)  
        def otimizar(e):  
            if not (checkbox_temperatura_bomba.value or checkbox_titulo_bomba.value):  
                show_warning("A DEPENDÊNCIA DA BOMBA NÃO FOI MARCADA")  
                return  

            if not (checkbox_temperatura_caldeira.value or checkbox_titulo_caldeira.value):  
                show_warning("A DEPENDÊNCIA DA CALDEIRA NÃO FOI MARCADA")  
                return  

            if not (checkbox_temperatura_turbina.value or checkbox_titulo_turbina.value):  
                show_warning("A DEPENDÊNCIA DA TURBINA NÃO FOI MARCADA")  
                return  

            if not p1.value:  
                show_warning("PREENCHA A PRESSÃO DO ESTADO 1")  
                return  

            if checkbox_temperatura_bomba.value and not t1.value:  
                show_warning("PREENCHA A TEMPERATURA DO ESTADO 1")  
                return  

            if not p2.value:  
                show_warning("PREENCHA A PRESSÃO DO ESTADO 2")  
                return  

            if checkbox_titulo_caldeira.value and not x3.value:  
                show_warning("PREENCHA O TÍTULO DO ESTADO 3")  
                return  

            if checkbox_temperatura_caldeira.value and not t3.value:  
                show_warning("PREENCHA A TEMPERATURA DO ESTADO 3")  
                return  

            if checkbox_temperatura_turbina.value and not t5.value:  
                show_warning("PREENCHA A TEMPERATURA DO ESTADO 5")  
                return  

            if checkbox_titulo_turbina.value and not x5.value:  
                show_warning("PREENCHA O TÍTULO DO ESTADO 5")  
                return  

            try:  
                p1_valor = float(p1.value) * 1000  
            except ValueError:  
                show_warning("PREENCHA A PRESSÃO DO ESTADO 1 COM UM NÚMERO VÁLIDO")  
                return  

            if checkbox_temperatura_bomba.value:  
                try:  
                    t1_valor = float(t1.value) + 273.15  
                except ValueError:  
                    show_warning("PREENCHA A TEMPERATURA DO ESTADO 1 COM UM NÚMERO VÁLIDO")  
                    return  
            else:  
                t1_valor = None  

            try:  
                p2_valor = float(p2.value) * 1000  
            except ValueError:  
                show_warning("PREENCHA A PRESSÃO DO ESTADO 2 COM UM NÚMERO VÁLIDO")  
                return  
            
            try:  
                p4_valor = float(p4.value) * 1000  
            except ValueError:  
                show_warning("PREENCHA A PRESSÃO DO ESTADO 4 COM UM NÚMERO VÁLIDO")  
                return  


            if checkbox_titulo_caldeira.value:  
                try:  
                    x3_valor = float(x3.value)  
                except ValueError:  
                    show_warning("PREENCHA O TÍTULO DO ESTADO 3 COM UM NÚMERO VÁLIDO")  
                    return  
            else:  
                x3_valor = None  

            if checkbox_temperatura_caldeira.value:  
                try:  
                    t3_valor = float(t3.value) + 273.15  
                except ValueError:  
                    show_warning("PREENCHA A TEMPERATURA DO ESTADO 3 COM UM NÚMERO VÁLIDO")  
                    return  
            else:  
                t3_valor = None  

            if checkbox_temperatura_turbina.value:  
                try:  
                    t5_valor = float(t5.value) + 273.15  
                except ValueError:  
                    show_warning("PREENCHA A TEMPERATURA DO ESTADO 5 COM UM NÚMERO VÁLIDO")  
                    return  
            else:  
                t5_valor = None  

            if checkbox_titulo_turbina.value:  
                try:  
                    x5_valor = float(x5.value)  
                except ValueError:  
                    show_warning("PREENCHA O TÍTULO DO ESTADO 5 COM UM NÚMERO VÁLIDO")  
                    return  
            else:  
                x5_valor = None  


            tabela_resultados.controls.clear()  
            # Se todas as validações passaram  
            resultado = otimizarReaquecimento(op1, p1_valor, t1_valor, p2_valor, op2, x3_valor, t3_valor, p4_valor, op3, t5_valor, x5_valor)
          

            ft.Text("Resultados do Ciclo de Rankine com Reaquecimento:", size=18)  
            tabela_resultados.controls.clear()  
            # Exemplo de tabela para exibir resultados  
            tabela_resultados.controls.append(  
                ft.DataTable(  
                    columns=[  
                        ft.DataColumn(label=ft.Text("")),  
                        ft.DataColumn(label=ft.Text("DADOS OTIMIZADOS")),  
                        
                    ],  
                    rows=[  
                        ft.DataRow(cells=[  
                            ft.DataCell(ft.Text("Eficiência máxima")),  
                            ft.DataCell(ft.Text(str(resultado['etamax']))),   
                        ]),  
                        ft.DataRow(cells=[  
                            ft.DataCell(ft.Text("Trabalho líquido máximo (kJ/kg)")),  
                            ft.DataCell(ft.Text(str(resultado['wliqmax']))),   
                        ]),

                        ft.DataRow(cells=[  
                            ft.DataCell(ft.Text("Pressão para eficiência máxima (kPa)")),  
                            ft.DataCell(ft.Text(str(resultado['petamax']))),   
                        ]),

                        ft.DataRow(cells=[  
                            ft.DataCell(ft.Text("Pressão para trabalho máxima (kPa)")),  
                            ft.DataCell(ft.Text(str(resultado['pwmax']))),   
                        ]),
                        
                    ],  
                )  
            )  
            page.update()  
            lista_Pressoesplot = resultado['lista_Pressoesplot']
            lista_Rendimentosplot = resultado['lista_Rendimentosplot']
            lista_Trabalhosplot = resultado['lista_Trabalhosplot']
            mostrar_grafico_otimizacao(lista_Pressoesplot, lista_Rendimentosplot, lista_Trabalhosplot)
        # Função para limpar os campos preenchidos  
        def limpar(e):  
            p1.value = ""  
            t1.value = ""  
            p2.value = ""  
            x3.value = ""  
            t3.value = ""  
            t5.value = ""  
            x5.value = ""  
            p4.value = ""  
            checkbox_temperatura_bomba.value = False  
            checkbox_titulo_bomba.value = False  
            checkbox_temperatura_caldeira.value = False  
            checkbox_titulo_caldeira.value = False  
            checkbox_temperatura_turbina.value = False  
            checkbox_titulo_turbina.value = False  
            tabela_resultados.controls.clear()  
            page.update()  

        calcular_btn = ft.ElevatedButton("CALCULAR", on_click=calcular)  
        limpar_btn = ft.ElevatedButton("LIMPAR", on_click=limpar)  
        otimizar_btn = ft.ElevatedButton("OTIMIZAR ", on_click=otimizar) 

       

        # Container para os campos de entrada  
        container_esquerda = ft.Column([  
            bomba_label,  
            ft.Row([checkbox_temperatura_bomba, checkbox_titulo_bomba], alignment=ft.MainAxisAlignment.START),  
            p1,  
            t1,  
            p2,  
            ft.Divider(height=20),  
            caldeira_label,  
            ft.Row([checkbox_temperatura_caldeira, checkbox_titulo_caldeira], alignment=ft.MainAxisAlignment.START),  
            x3,  
            t3,  
            ft.Divider(height=20), 
            turbina_label,  
            ft.Row([checkbox_temperatura_turbina, checkbox_titulo_turbina], alignment=ft.MainAxisAlignment.START),  
            t5, 
        ])  

         # Container para os campos de entrada  
        container_meio = ft.Column([  
            x5,  
            p4,  
            ft.Row([calcular_btn, otimizar_btn, limpar_btn], alignment=ft.MainAxisAlignment.START)  
        ], alignment=ft.MainAxisAlignment.START)  # Alinhamento para o topo


        # Container para a tabela de resultados  
        tabela_resultados = ft.Column([])  

        container_direita = ft.Column([  
            tabela_resultados  
        ])  

        # Retorna a interface com os dois containers (esquerda e direita)  
        return ft.Row([  
            ft.Container(content=container_esquerda, width=400),  
            ft.Container(content=container_meio, width=350, height=600),  # ajuste aqui
            ft.Container(content=container_direita, width=700)  
        ], alignment=ft.MainAxisAlignment.START)


################################################################################
#____________________CICLO REGENERATIVO____________________________________________________________________
# Função que cria a interface para o Ciclo de Rankine   
    def criar_ciclo_regerativo():  
        # Funções para alternar entre temperatura e título  
        op1 = 0  
        op2 = 0  
        op3 = 0  # Nova variável para a turbina  

        # Funções para alternar entre temperatura e título da bomba  
        def on_temperatura_bomba_change(e):  
            nonlocal op1  
            if checkbox_temperatura_bomba.value:  
                checkbox_titulo_bomba.value = False  
                op1 = 2  
            page.update()  

        def on_titulo_bomba_change(e):  
            nonlocal op1  
            if checkbox_titulo_bomba.value:  
                checkbox_temperatura_bomba.value = False  
                op1 = 1  
            page.update()  

        # Funções para alternar entre temperatura e título da caldeira  
        def on_primeiralei_change_change(e):  
            nonlocal op3  
            if checkbox_primeira_bomba2.value:  
                checkbox_titulo_bomba2.value = False  
                op3 = 1  
            page.update()  

        def on_titulo_bomba2_change(e):  
            nonlocal op3  
            if checkbox_titulo_bomba2.value:  
                checkbox_primeira_bomba2.value = False  
                op3 = 2 
            page.update()  

        # Funções para alternar entre temperatura e título da turbina  
        def on_temperatura_turbina_change(e):  
            nonlocal op2  
            if checkbox_temperatura_turbina.value:  
                checkbox_titulo_turbina.value = False  
                op2 = 1 
            page.update()  

        def on_titulo_turbina_change(e):  
            nonlocal op3  
            if checkbox_titulo_turbina.value:  
                checkbox_temperatura_turbina.value = False  
                op2 = 2  
            page.update()  

        # Campos para a bomba  
        bomba_label = ft.Text("A bomba depende de:", size=15, weight=ft.FontWeight.BOLD)  
        checkbox_temperatura_bomba = ft.Checkbox(label="TEMPERATURA", on_change=on_temperatura_bomba_change)  
        checkbox_titulo_bomba = ft.Checkbox(label="TÍTULO", on_change=on_titulo_bomba_change)  

        p1 = ft.TextField(label="Entre com a pressão da entrada da bomba (kPa) (ESTADO 1):", width=400)  
        t1 = ft.TextField(label="Temperatura da bomba (Selecione TEMPERATURA) (ESTADO 1):", width=400)  
        p2 = ft.TextField(label="Entre com a pressão de saída da bomba (kPa) (ESTADO 2):", width=400)  

        # Campos para a bomba   2
        caldeira_label = ft.Text("A Bomba 2 depende de:", size=15, weight=ft.FontWeight.BOLD)  
        checkbox_primeira_bomba2 = ft.Checkbox(label="ENTALPIA PELA 1° LEI NO AQUECEDOR", on_change=on_primeiralei_change_change)  
        checkbox_titulo_bomba2= ft.Checkbox(label="TÍTULO", on_change=on_titulo_bomba2_change)  

        y = ft.TextField(label="Entre com a fração y (SELECIONE A PRIMEIRA LEI)", width=400)  
        

        # Campos para a turbina  
        turbina_label = ft.Text("A turbina de baixa pressão depende de:", size=15, weight=ft.FontWeight.BOLD)  
        checkbox_temperatura_turbina = ft.Checkbox(label="TEMPERATURA", on_change=on_temperatura_turbina_change)  
        checkbox_titulo_turbina = ft.Checkbox(label="TÍTULO", on_change=on_titulo_turbina_change)  

        t5 = ft.TextField(label="Temperatura da turbina (SELECIONE TEMPERATURA) (ESTADO 5):", width=400)  
        x5 = ft.TextField(label="Entre com o título da turbina em % (SELECIONE TÍTULO) (ESTADO 5):", width=400)  
        p5 = ft.TextField(label="Pressão da turbina de saída (KPa) (ESTADO 5):", width=400)  

        # Função de cálculo (placeholder)  
        def calcular(e):  
            if not (checkbox_temperatura_bomba.value or checkbox_titulo_bomba.value):  
                show_warning("A DEPENDÊNCIA DA BOMBA NÃO FOI MARCADA")  
                return  

            if not (checkbox_primeira_bomba2.value or checkbox_titulo_bomba2.value):  
                show_warning("A DEPENDÊNCIA DA BOMBA 2 NÃO FOI MARCADA")  
                return  

            if not (checkbox_temperatura_turbina.value or checkbox_titulo_turbina.value):  
                show_warning("A DEPENDÊNCIA DA TURBINA NÃO FOI MARCADA")  
                return  

            if not p1.value:  
                show_warning("PREENCHA A PRESSÃO DO ESTADO 1")  
                return  

            if checkbox_temperatura_bomba.value and not t1.value:  
                show_warning("PREENCHA A TEMPERATURA DO ESTADO 1")  
                return  

            if not p2.value:  
                show_warning("PREENCHA A PRESSÃO DO ESTADO 2")  
                return  

           
            if checkbox_primeira_bomba2.value and not y.value:  
                show_warning("PREENCHA A FRAÇÃO")  
                return  

            if checkbox_temperatura_turbina.value and not t5.value:  
                show_warning("PREENCHA A TEMPERATURA DO ESTADO 5")  
                return  

            if checkbox_titulo_turbina.value and not x5.value:  
                show_warning("PREENCHA O TÍTULO DO ESTADO 5")  
                return  

            try:  
                p1_valor = float(p1.value) * 1000  
            except ValueError:  
                show_warning("PREENCHA A PRESSÃO DO ESTADO 1 COM UM NÚMERO VÁLIDO")  
                return  

            if checkbox_temperatura_bomba.value:  
                try:  
                    t1_valor = float(t1.value) + 273.15  
                except ValueError:  
                    show_warning("PREENCHA A TEMPERATURA DO ESTADO 1 COM UM NÚMERO VÁLIDO")  
                    return  
            else:  
                t1_valor = None  

            try:  
                p2_valor = float(p2.value) * 1000  
            except ValueError:  
                show_warning("PREENCHA A PRESSÃO DO ESTADO 2 COM UM NÚMERO VÁLIDO")  
                return  
            
            try:  
                p5_valor = float(p5.value) * 1000  
            except ValueError:  
                show_warning("PREENCHA A PRESSÃO DA TURBINA COM UM NÚMERO VÁLIDO")  
                return  


           
            if checkbox_primeira_bomba2.value:  
                try:  
                    y_valor = float(y.value)  
                except ValueError:  
                    show_warning("PREENCHA A FRAÇÃO COM UM NÚMERO VÁLIDO")  
                    return  
            else:  
                y_valor = None  

            if checkbox_temperatura_turbina.value:  
                try:  
                    t5_valor = float(t5.value) + 273.15  
                except ValueError:  
                    show_warning("PREENCHA A TEMPERATURA DO ESTADO 5 COM UM NÚMERO VÁLIDO")  
                    return  
            else:  
                t5_valor = None  

            if checkbox_titulo_turbina.value:  
                try:  
                    x5_valor = float(x5.value)  
                except ValueError:  
                    show_warning("PREENCHA O TÍTULO DO ESTADO 5 COM UM NÚMERO VÁLIDO")  
                    return  
            else:  
                x5_valor = None  

            tabela_resultados.controls.clear()  
            tabela_resultadosciclo.controls.clear()  

            # Se todas as validações passaram  
            resultado = Ciclos.regenerativo(op1, p1_valor, t1_valor, p2_valor, op2, p5_valor, t5_valor, x5_valor, op3, y_valor)
            page.update()  

            if resultado['erro'] == 10:
                show_warning("VERIFIQUE AS ENTRADAS E TENTE NOVAMENTE")
            else:
                tabela_resultados.controls.clear()  
                # Exemplo de tabela para exibir resultados  
                tabela_resultados.controls.append(  
                    ft.DataTable(  
                        columns=[  
                            ft.DataColumn(label=ft.Text("Estado")),  
                            ft.DataColumn(label=ft.Text("Temperatura (°C)")),  
                            ft.DataColumn(label=ft.Text("Pressão (kPa)")),  
                            ft.DataColumn(label=ft.Text("Entalpia (kJ/kg)")),  
                            ft.DataColumn(label=ft.Text("Entropia (kJ/kg·K)")),  
                        ],  
                        rows=[  
                            ft.DataRow(cells=[  
                                ft.DataCell(ft.Text("ESTADO 1")),  
                                ft.DataCell(ft.Text(str(resultado['temperaturas']["t1"]))),  
                                ft.DataCell(ft.Text(str(resultado['pressões']["p1"]))),  
                                ft.DataCell(ft.Text(str(resultado['entalpias']["h1"]))),  
                                ft.DataCell(ft.Text(str(resultado['entropias']["s1"])))  
                            ]),  
                            ft.DataRow(cells=[  
                                ft.DataCell(ft.Text("ESTADO 2")),  
                                ft.DataCell(ft.Text(str(resultado['temperaturas']["t2"]))),  
                                ft.DataCell(ft.Text(str(resultado['pressões']["p2"]))),  
                                ft.DataCell(ft.Text(str(resultado['entalpias']["h2"]))),  
                                ft.DataCell(ft.Text(str(resultado['entropias']["s2"])))  
                            ]),  
                            ft.DataRow(cells=[  
                                ft.DataCell(ft.Text("ESTADO 3")),  
                                ft.DataCell(ft.Text(str(resultado['temperaturas']["t3"]))),  
                                ft.DataCell(ft.Text(str(resultado['pressões']["p3"]))),  
                                ft.DataCell(ft.Text(str(resultado['entalpias']["h3"]))),  
                                ft.DataCell(ft.Text(str(resultado['entropias']["s3"])))  
                            ]),  
                            ft.DataRow(cells=[  
                                ft.DataCell(ft.Text("ESTADO 4")),  
                                ft.DataCell(ft.Text(str(resultado['temperaturas']["t4"]))),  
                                ft.DataCell(ft.Text(str(resultado['pressões']["p4"]))),  
                                ft.DataCell(ft.Text(str(resultado['entalpias']["h4"]))),  
                                ft.DataCell(ft.Text(str(resultado['entropias']["s4"])))  
                            ]),  
                            ft.DataRow(cells=[  
                                ft.DataCell(ft.Text("ESTADO 5")),  
                                ft.DataCell(ft.Text(str(resultado['temperaturas']["t5"]))),  
                                ft.DataCell(ft.Text(str(resultado['pressões']["p5"]))),  
                                ft.DataCell(ft.Text(str(resultado['entalpias']["h5"]))),  
                                ft.DataCell(ft.Text(str(resultado['entropias']["s5"])))  
                            ]),  

                            ft.DataRow(cells=[  
                                ft.DataCell(ft.Text("ESTADO 6")),  
                                ft.DataCell(ft.Text(str(resultado['temperaturas']["t6"]))),  
                                ft.DataCell(ft.Text(str(resultado['pressões']["p6"]))),  
                                ft.DataCell(ft.Text(str(resultado['entalpias']["h6"]))),  
                                ft.DataCell(ft.Text(str(resultado['entropias']["s6"])))  
                            ]),  
                            ft.DataRow(cells=[  
                                ft.DataCell(ft.Text("ESTADO 7")),  
                                ft.DataCell(ft.Text(str(resultado['temperaturas']["t7"]))),  
                                ft.DataCell(ft.Text(str(resultado['pressões']["p7"]))),  
                                ft.DataCell(ft.Text(str(resultado['entalpias']["h7"]))),  
                                ft.DataCell(ft.Text(str(resultado['entropias']["s7"])))  
                            ]),  
                            

                            
                        ],  
                    )  
                ) 
                page.update()
                tabela_resultadosciclo.controls.clear()
                # Exemplo de tabela para exibir resultados  
                tabela_resultadosciclo.controls.append(  
                    ft.DataTable(  
                        columns=[  
                            ft.DataColumn(label=ft.Text("")),  
                            ft.DataColumn(label=ft.Text("")),  
                            
                        ],  
                        rows=[  
                        
                            ft.DataRow(cells=[  
                                ft.DataCell(ft.Text("Resultados Ciclo")),  
                                ft.DataCell(ft.Text("")),  
                                
                            ]),  
                            ft.DataRow(cells=[  
                                ft.DataCell(ft.Text("Eficiência")),  
                                ft.DataCell(ft.Text(str(resultado["trabalhos"]["eta"]))),  
                                
                            ]),  
                            ft.DataRow(cells=[  
                                ft.DataCell(ft.Text("Trabalho da turbina (kJ/kg)")),  
                                ft.DataCell(ft.Text(str(resultado["trabalhos"]["wt"]))),  
                                
                            ]),  
                            ft.DataRow(cells=[  
                                ft.DataCell(ft.Text("Trabalho da bomba (kJ/kg)")),  
                                ft.DataCell(ft.Text(str(resultado["trabalhos"]["wb"]))),  
                                
                            ]),  
                            ft.DataRow(cells=[  
                                ft.DataCell(ft.Text("Calor da caldeira (kJ/kg)")),  
                                ft.DataCell(ft.Text(str(resultado["trabalhos"]["qh"]))),  
                                
                            ]),  
                            ft.DataRow(cells=[  
                                ft.DataCell(ft.Text("Fração Y")),  
                                ft.DataCell(ft.Text(str(resultado["trabalhos"]["y"]))),  
                                
                            ]),  
                        ],  
                    )  
                ) 
                
                page.update()  

            
#______________________________________________________________________________________________________________________________________________________
        

        # Função para limpar os campos preenchidos  
        def limpar(e):  
            p1.value = ""  
            t1.value = ""  
            p2.value = ""  
         
            y.value = ""  
            t5.value = ""  
            x5.value = ""  
            p5.value = ""  
            checkbox_temperatura_bomba.value = False  
            checkbox_titulo_bomba.value = False  
            checkbox_primeira_bomba2.value = False  
            checkbox_titulo_bomba2.value = False  
            checkbox_temperatura_turbina.value = False  
            checkbox_titulo_turbina.value = False  
            tabela_resultados.controls.clear()  
            tabela_resultadosciclo.controls.clear()
            page.update()  

        calcular_btn = ft.ElevatedButton("CALCULAR", on_click=calcular)  
        limpar_btn = ft.ElevatedButton("LIMPAR", on_click=limpar)  
       

       

        # Container para os campos de entrada  
        container_esquerda = ft.Column([  
            bomba_label,  
            ft.Row([checkbox_temperatura_bomba, checkbox_titulo_bomba], alignment=ft.MainAxisAlignment.START),  
            p1,  
            t1,  
            p2,  
            ft.Divider(height=20),  
            caldeira_label,  
            ft.Row([checkbox_primeira_bomba2, checkbox_titulo_bomba2], alignment=ft.MainAxisAlignment.START),  
            y,  
            ft.Divider(height=20), 
            turbina_label,  
            ft.Row([checkbox_temperatura_turbina, checkbox_titulo_turbina], alignment=ft.MainAxisAlignment.START),  
            t5, 
        ])  
        tabela_resultadosciclo = ft.Column([])  
         # Container para os campos de entrada  
        container_meio = ft.Column([  
            x5,  
            p5,  
            ft.Row([calcular_btn, limpar_btn], alignment=ft.MainAxisAlignment.START)  ,
            tabela_resultadosciclo,
        ], alignment=ft.MainAxisAlignment.START)  # Alinhamento para o topo


        # Container para a tabela de resultados  
        tabela_resultados = ft.Column([])  
        

        container_direita = ft.Column([  
            tabela_resultados  
        ])  

        # Retorna a interface com os dois containers (esquerda e direita)  
        return ft.Row([  
            ft.Container(content=container_esquerda, width=400),  
            ft.Container(content=container_meio, width=350, height=600),  # ajuste aqui
            ft.Container(content=container_direita, width=750)  
        ], alignment=ft.MainAxisAlignment.START)
#___________________________________________________________________________________________________________________________________



################################################################################
#____________________CICLO REGENERATIVO COM REAQUECIMENTO____________________________________________________________________
# Função que cria a interface para o Ciclo de Rankine REGENERATIVO Reaquecimento  


    def criar_ciclo_regerativo_reaquecimento():  
        # Funções para alternar entre temperatura e título  
        op1 = 0  
        op5 = 0  
        op3 = 0  # Nova variável para a turbina  
        op7 = 0

        # Funções para alternar entre temperatura e título da bomba  
        def on_temperatura_bomba_change(e):  
            nonlocal op1  
            if checkbox_temperatura_bomba.value:  
                checkbox_titulo_bomba.value = False  
                op1 = 2  
            page.update()  

        def on_titulo_bomba_change(e):  
            nonlocal op1  
            if checkbox_titulo_bomba.value:  
                checkbox_temperatura_bomba.value = False  
                op1 = 1  
            page.update()  

        # Funções para alternar entre temperatura e título da caldeira  
        def on_primeiralei_change_change(e):  
            nonlocal op3  
            if checkbox_primeira_bomba2.value:  
                checkbox_titulo_bomba2.value = False  
                op3 = 2  
            page.update()  

        def on_titulo_bomba2_change(e):  
            nonlocal op3  
            if checkbox_titulo_bomba2.value:  
                checkbox_primeira_bomba2.value = False  
                op3 = 1 
            page.update()  

        # Funções para alternar entre temperatura e título da turbina  
        def on_temperatura_turbina_change(e):  
            nonlocal op5 
            if checkbox_temperatura_turbina.value:  
                checkbox_titulo_turbina.value = False  
                op5 = 1 
            page.update()  

        def on_titulo_turbina_change(e):  
            nonlocal op5 
            if checkbox_titulo_turbina.value:  
                checkbox_temperatura_turbina.value = False  
                op5 = 2  
            page.update()  

        # Funções para alternar entre temperatura e título da turbina  
        def on_temperatura_turbinabaixa_change(e):  
            nonlocal op7  
            if checkbox_temperatura_turbinabaixa.value:  
                checkbox_titulo_turbinabaixa.value = False  
                op7 = 1 
            page.update()  

        def on_titulo_turbinabaixa_change(e):  
            nonlocal op7  
            if checkbox_titulo_turbinabaixa.value:  
                checkbox_temperatura_turbinabaixa.value = False  
                op7 = 2  
            page.update()  


        m = ft.TextField(label="Entre com a vazão massica do ciclo", width=400)  
        # Campos para a bomba  
        bomba_label = ft.Text("A bomba depende de:", size=15, weight=ft.FontWeight.BOLD)  
        checkbox_temperatura_bomba = ft.Checkbox(label="TEMPERATURA", on_change=on_temperatura_bomba_change)  
        checkbox_titulo_bomba = ft.Checkbox(label="TÍTULO", on_change=on_titulo_bomba_change)  

        p1 = ft.TextField(label="Entre com a pressão da entrada da bomba (kPa) (ESTADO 1):", width=400)  
        t1 = ft.TextField(label="Temperatura da bomba (Selecione TEMPERATURA) (ESTADO 1):", width=400)  
        p2 = ft.TextField(label="Entre com a pressão de saída da bomba (kPa) (ESTADO 2):", width=400)  

        # Campos para a bomba   2
        caldeira_label = ft.Text("A Bomba 2 depende de:", size=15, weight=ft.FontWeight.BOLD)  
        checkbox_primeira_bomba2 = ft.Checkbox(label="TEMPERATURA", on_change=on_primeiralei_change_change)  
        checkbox_titulo_bomba2= ft.Checkbox(label="TÍTULO", on_change=on_titulo_bomba2_change)  

        p3 = ft.TextField(label="Entre com a pressão de entrada da bomba 2 (Estado 3)", width=400)  
        t3 = ft.TextField(label="Entre com a temperatura de saída da bomba 2", width=400) 
        

        # Campos para a turbina  de alta
        turbina_label = ft.Text("A turbina de alta pressão depende de:", size=15, weight=ft.FontWeight.BOLD)  
        checkbox_temperatura_turbina = ft.Checkbox(label="TEMPERATURA", on_change=on_temperatura_turbina_change)  
        checkbox_titulo_turbina = ft.Checkbox(label="TÍTULO", on_change=on_titulo_turbina_change)  

        t5 = ft.TextField(label="Temperatura da turbina (SELECIONE TEMPERATURA) (ESTADO 5):", width=400)  
        x5 = ft.TextField(label="Entre com o título da turbina em % (SELECIONE TÍTULO) (ESTADO 5):", width=400)  
        p6 = ft.TextField(label="Pressão de saída da turbina de alta (KPa) (ESTADO 6):", width=400)  

        # Campos para a turbina  de baixa
        turbinabaixa_label = ft.Text("A turbina de baixa pressão depende de:", size=15, weight=ft.FontWeight.BOLD)  
        checkbox_temperatura_turbinabaixa = ft.Checkbox(label="TEMPERATURA", on_change=on_temperatura_turbinabaixa_change)  
        checkbox_titulo_turbinabaixa = ft.Checkbox(label="TÍTULO", on_change=on_titulo_turbinabaixa_change)  

        t7 = ft.TextField(label="Temperatura da turbina (SELECIONE TEMPERATURA) (ESTADO 7):", width=400)  
        x7 = ft.TextField(label="Entre com o título da turbina em % (SELECIONE TÍTULO) (ESTADO 7):", width=400)  

        # Campo para eficiencia isentropica
        eficiencia_label = ft.Text("Entre com as eficiências isentrópicas das bombas e turbinas", size=15, weight=ft.FontWeight.BOLD)  
        n = ft.TextField(label="Entre com a eficiência isentrópica das bombas", width=400)  
        nt = ft.TextField(label="Entre com a eficiência isentrópica das turbinas", width=400)  
       

        # Função de cálculo (placeholder)  
        def calcular(e):  
            if not (checkbox_temperatura_bomba.value or checkbox_titulo_bomba.value):  
                show_warning("A DEPENDÊNCIA DA BOMBA NÃO FOI MARCADA")  
                return  

            if not (checkbox_primeira_bomba2.value or checkbox_titulo_bomba2.value):  
                show_warning("A DEPENDÊNCIA DA BOMBA 2 NÃO FOI MARCADA")  
                return  

            if not (checkbox_temperatura_turbina.value or checkbox_titulo_turbina.value):  
                show_warning("A DEPENDÊNCIA DA TURBINA NÃO FOI MARCADA")  
                return  

            if not p1.value:  
                show_warning("PREENCHA A PRESSÃO DO ESTADO 1")  
                return  

            if checkbox_temperatura_bomba.value and not t1.value:  
                show_warning("PREENCHA A TEMPERATURA DO ESTADO 1")  
                return  

            if not p2.value:  
                show_warning("PREENCHA A PRESSÃO DO ESTADO 2")  
                return  

           
            if checkbox_primeira_bomba2.value and not t3.value:  
                show_warning("PREENCHA A TEMPERATURA DO ESTADO 3")  
                return  

            if checkbox_temperatura_turbina.value and not t5.value:  
                show_warning("PREENCHA A TEMPERATURA DO ESTADO 5")  
                return  

            if checkbox_titulo_turbina.value and not x5.value:  
                show_warning("PREENCHA O TÍTULO DO ESTADO 5")  
                return  



            try:  
                m_valor = float(m.value)   
            except ValueError:  
                show_warning("PREENCHA A VAZÃO MASSICA COM UM NÚMERO VÁLIDO")  
                return
            

            try:  
                p1_valor = float(p1.value) * 1000  
            except ValueError:  
                show_warning("PREENCHA A PRESSÃO DO ESTADO 1 COM UM NÚMERO VÁLIDO")  
                return  

            if checkbox_temperatura_bomba.value:  
                try:  
                    t1_valor = float(t1.value) + 273.15  
                except ValueError:  
                    show_warning("PREENCHA A TEMPERATURA DO ESTADO 1 COM UM NÚMERO VÁLIDO")  
                    return  
            else:  
                t1_valor = None  

            try:  
                p2_valor = float(p2.value) * 1000  
            except ValueError:  
                show_warning("PREENCHA A PRESSÃO DO ESTADO 2 COM UM NÚMERO VÁLIDO")  
                return  
            
            try:  
                p3_valor = float(p3.value) * 1000  
            except ValueError:  
                show_warning("PREENCHA A PRESSÃO DA TURBINA COM UM NÚMERO VÁLIDO")  
                return  
            

            try:  
                p6_valor = float(p6.value) * 1000  
            except ValueError:  
                show_warning("PREENCHA A PRESSÃO DA TURBINA COM UM NÚMERO VÁLIDO")  
                return  

            try:  
                n_valor = float(n.value)   /100
            except ValueError:  
                show_warning("PREENCHA A EFICIÊNCIA ISENTRÓPICA DA BOMBA COM UM NÚMERO VÁLIDO")  
                return
            
            try:  
                nt_valor = float(nt.value)   /100
            except ValueError:  
                show_warning("PREENCHA A EFICIÊNCIA ISENTRÓPICA DA TURBINA COM UM NÚMERO VÁLIDO")  
                return
           
            if checkbox_primeira_bomba2.value:  
                try:  
                    t3_valor = float(t3.value)  + 273.15
                except ValueError:  
                    show_warning("PREENCHA A FRAÇÃO COM UM NÚMERO VÁLIDO")  
                    return  
            else:  
                t3_valor = None  

            if checkbox_temperatura_turbina.value:  
                try:  
                    t5_valor = float(t5.value) + 273.15  
                except ValueError:  
                    show_warning("PREENCHA A TEMPERATURA DO ESTADO 5 COM UM NÚMERO VÁLIDO")  
                    return  
            else:  
                t5_valor = None  

            if checkbox_titulo_turbina.value:  
                try:  
                    x5_valor = float(x5.value)  
                except ValueError:  
                    show_warning("PREENCHA O TÍTULO DO ESTADO 5 COM UM NÚMERO VÁLIDO")  
                    return  
            else:  
                x5_valor = None  


            if checkbox_temperatura_turbinabaixa.value:  
                try:  
                    t7_valor = float(t7.value) + 273.15  
                except ValueError:  
                    show_warning("PREENCHA A TEMPERATURA DO ESTADO 5 COM UM NÚMERO VÁLIDO")  
                    return  
            else:  
                t7_valor = None  

            if checkbox_titulo_turbinabaixa.value:  
                try:  
                    x7_valor = float(x7.value)  
                except ValueError:  
                    show_warning("PREENCHA O TÍTULO DO ESTADO 5 COM UM NÚMERO VÁLIDO")  
                    return  
            else:  
                x7_valor = None  


            tabela_resultados.controls.clear()  

            # Se todas as validações passaram  
            resultado = Ciclos.regenerativoReaquecimento(m_valor, op1, p1_valor, t1_valor, p2_valor, n_valor, op3, p3_valor, t3_valor, op5, t5_valor, x5_valor, p6_valor, nt_valor, op7, t7_valor, x7_valor)
            page.update()  
            tabela_resultados.controls.clear()  
            # Exemplo de tabela para exibir resultados  
            tabela_resultados.controls.append(  
                ft.DataTable(  
                    columns=[  
                        ft.DataColumn(label=ft.Text("Resultados do Ciclo")),  
                        ft.DataColumn(label=ft.Text("")),  
                        
                    ],  
                    rows=[  
                        
                        ft.DataRow(cells=[  
                            ft.DataCell(ft.Text("Eficiência")),  
                            ft.DataCell(ft.Text(str(resultado["trabalhos"]["eta"]))),  
                           
                        ]),  
                        ft.DataRow(cells=[  
                            ft.DataCell(ft.Text("Trabalho da turbina")),  
                            ft.DataCell(ft.Text(str(resultado["trabalhos"]["wt"]))),  
                           
                        ]),  
                        ft.DataRow(cells=[  
                            ft.DataCell(ft.Text("Trabalho da bomba ")),  
                            ft.DataCell(ft.Text(str(resultado["trabalhos"]["wb"]))),  
                            
                        ]),  

                        ft.DataRow(cells=[  
                            ft.DataCell(ft.Text("Fluxo de massa extraído da turbina (kg/s) ")),  
                            ft.DataCell(ft.Text(str(resultado["trabalhos"]["m8"]))),  
                            
                        ]), 
                        ft.DataRow(cells=[  
                            ft.DataCell(ft.Text("Calor da caldeira ")),  
                            ft.DataCell(ft.Text(str(resultado["trabalhos"]["qh"]))),  
                            
                        ]),  
                        ft.DataRow(cells=[  
                            ft.DataCell(ft.Text("Fração Y")),  
                            ft.DataCell(ft.Text(str(resultado["trabalhos"]["y"]))),  
                            
                        ]),  
                        ft.DataRow(cells=[  
                            ft.DataCell(ft.Text("Temperatura Estado 8")),  
                            ft.DataCell(ft.Text(str(resultado["temperaturas"]["t8"]))),  
                            
                        ]),  

                        ft.DataRow(cells=[  
                            ft.DataCell(ft.Text("Potência Líquida")),  
                            ft.DataCell(ft.Text(str(resultado["trabalhos"]["wliq"]))),  
                            
                        ]), 
                    ],  
                )  
            )  
            page.update()  
#______________________________________________________________________________________________________________________________________________________
        

        # Função para limpar os campos preenchidos  
        def limpar(e):  
            p1.value = ""  
            t1.value = ""  
            p2.value = ""  
            m.value = ""  
            n.value = ""  
            nt.value = ""  
            p6.value = ""  
            t3.value = ""  
            t5.value = ""  
            x5.value = ""  
            p6.value = ""  
            checkbox_temperatura_bomba.value = False  
            checkbox_titulo_bomba.value = False  
            checkbox_primeira_bomba2.value = False  
            checkbox_titulo_bomba2.value = False  
            checkbox_temperatura_turbina.value = False  
            checkbox_titulo_turbina.value = False  
            checkbox_temperatura_turbinabaixa.value = False  
            checkbox_titulo_turbinabaixa.value = False 
            tabela_resultados.controls.clear()  
            page.update()  

        calcular_btn = ft.ElevatedButton("CALCULAR", on_click=calcular)  
        limpar_btn = ft.ElevatedButton("LIMPAR", on_click=limpar)  
       

       

        # Container para os campos de entrada  
        container_esquerda = ft.Column([  
            m,
            bomba_label,  
            ft.Row([checkbox_temperatura_bomba, checkbox_titulo_bomba], alignment=ft.MainAxisAlignment.START),  
            p1,  
            t1,  
            p2,  
            ft.Divider(height=20),  
            caldeira_label,  
            ft.Row([checkbox_primeira_bomba2, checkbox_titulo_bomba2], alignment=ft.MainAxisAlignment.START),  
            p3,
            t3,  
            ft.Divider(height=20), 
            turbina_label,  
            ft.Row([checkbox_temperatura_turbina, checkbox_titulo_turbina], alignment=ft.MainAxisAlignment.START),  
            
        ])  

         # Container para os campos de entrada  
        container_meio = ft.Column([  
            t5, 
            x5,  
            p6,  
            turbinabaixa_label,  
            ft.Row([checkbox_temperatura_turbinabaixa, checkbox_titulo_turbinabaixa], alignment=ft.MainAxisAlignment.START),  
            x7,
            t7,
            eficiencia_label,
            n,
            nt,
            ft.Row([calcular_btn, limpar_btn], alignment=ft.MainAxisAlignment.START)  
        ], alignment=ft.MainAxisAlignment.START)  # Alinhamento para o topo


        # Container para a tabela de resultados  
        tabela_resultados = ft.Column([])  

        container_direita = ft.Column([  
            tabela_resultados  
        ])  

        # Retorna a interface com os dois containers (esquerda e direita)  
        return ft.Row([  
            ft.Container(content=container_esquerda, width=400),  
            ft.Container(content=container_meio, width=350, height=600),  # ajuste aqui
            ft.Container(content=container_direita, width=700)  
        ], alignment=ft.MainAxisAlignment.START)
#___________________________________________________________________________________________________________________________________


    


    def criar_calculadora_propriedades():
        # Widget para a logo
        logo = ft.Image(src="ufob.png", height=200)

        # Widget Dropdown para a propriedade desejada
        propriedade_desejada = ft.Dropdown(
            label="Propriedade desejada:",
            options=[
                ft.dropdown.Option("Todas"),
               # ft.dropdown.Option("Pressão"),
               # ft.dropdown.Option("Temperatura"),
              #  ft.dropdown.Option("Volume específico"),
             #   ft.dropdown.Option("Energia interna"),
              #  ft.dropdown.Option("Entalpia"),
               # ft.dropdown.Option("Entropia"),
              #  ft.dropdown.Option("Título"),
            ],
            width=200
        )

        # Widget Dropdown para selecionar o fluido
        fluido = ft.Dropdown(
            label="Fluido:",
            options=[
                ft.dropdown.Option("Water"),
                ft.dropdown.Option("1-Butene"),
                ft.dropdown.Option("Acetone"),
                ft.dropdown.Option("Ammonia"),
                ft.dropdown.Option("Benzene"),
                ft.dropdown.Option("CarbonDioxide"),
                ft.dropdown.Option("CarbonMonoxide"),
                ft.dropdown.Option("Ethane"),
                ft.dropdown.Option("Ethanol"),
                ft.dropdown.Option("Helium"),
                ft.dropdown.Option("Hydrogen"),
                ft.dropdown.Option("Methane"),
                ft.dropdown.Option("Methanol"),
                ft.dropdown.Option("Nitrogen"),
                ft.dropdown.Option("Oxygen"),
                ft.dropdown.Option("Propyne"),
                ft.dropdown.Option("R113"),
                ft.dropdown.Option("R114"),
                ft.dropdown.Option("R115"),
                ft.dropdown.Option("R116"),
                ft.dropdown.Option("R123"),
                ft.dropdown.Option("R124"),
                ft.dropdown.Option("R125"),
                ft.dropdown.Option("R134a"),
                ft.dropdown.Option("R141b"),
                ft.dropdown.Option("R142b"),
                ft.dropdown.Option("R143a"),
                ft.dropdown.Option("R218"),
                ft.dropdown.Option("R410A"),
                
                ft.dropdown.Option("Propylene"),
                ft.dropdown.Option("R22"),
                ft.dropdown.Option("n-Butane"),
                ft.dropdown.Option("n-Propane"),
            ],
            width=200
        )

        # Seleção de variável para a propriedade 1
        propriedade_1_tipo = ft.Dropdown(
            label="Selecione a propriedade 1:",
            options=[
                ft.dropdown.Option("Pressão"),
                ft.dropdown.Option("Temperatura"),
            
                ft.dropdown.Option("Energia interna"),
                ft.dropdown.Option("Entalpia"),
                ft.dropdown.Option("Entropia"),
                ft.dropdown.Option("Título"),
            ],
            width=200
        )

        # Campo de entrada para a propriedade 1
        propriedade_1 = ft.TextField(
            label="Valor da propriedade 1:",
            width=200
        )

        # Seleção de variável para a propriedade 2
        propriedade_2_tipo = ft.Dropdown(
            label="Selecione a propriedade 2:",
            options=[
                ft.dropdown.Option("Pressão"),
                ft.dropdown.Option("Temperatura"),
                
                ft.dropdown.Option("Energia interna"),
                ft.dropdown.Option("Entalpia"),
                ft.dropdown.Option("Entropia"),
                ft.dropdown.Option("Título"),
            ],
            width=200
        )

        # Campo de entrada para a propriedade 2
        propriedade_2 = ft.TextField(
            label="Valor da propriedade 2:",
            width=200
        )

        # Placeholder para o resultado
        resultado_texto = ft.Text("")
        resultado_saturado = ft.Text("")
        
        # Container para a tabela
        tabela_container = ft.Column()

      

       # Função para calcular a propriedade
        def calcular(e):
            # Captura as entradas
            substancia = fluido.value
            propriedade = propriedade_desejada.value
            op1 = propriedade_1_tipo.value
            op2 = propriedade_2_tipo.value
            propriedade = 'Todas'
            if not op1:
                show_warning("A DEPENDÊNCIA DA PROPRIEDADE 1 NÃO FOI MARCADA")
                return

            if op1 == op2 or op1 == propriedade or op2 == propriedade:
                show_warning("AS PROPRIEDADES SELECIONADAS SÃO IGUAIS")
                return

            if not op2:
                show_warning("A DEPENDÊNCIA DA PROPRIEDADE 2 NÃO FOI MARCADA")
                return

            if not substancia:
                show_warning("O FLUIDO DE TRABALHO NÃO FOI SELECIONADO")
                return

            

            opcoes = {
                'Pressão': 'P',
                'Temperatura': 'T',
                'Volume específico': 'V',
                'Energia interna': 'U',
                'Entalpia': 'H',
                'Entropia': 'S',
                'Título': 'Q'
            }
            
            propriedade = opcoes.get(propriedade, propriedade)
            op1 = opcoes.get(op1, op1)
            op2 = opcoes.get(op2, op2)

            # Verifica se as combinações de propriedades são válidas
            if (op1 == 'H' and op2 == 'T') or (op1 == 'T' and op2 == 'H'):
                show_warning("COMBINAÇÃO INVÁLIDA: Entalpia (H) e Temperatura (T) não podem ser usadas juntas.")
                return

            if op1 == 'U' and op2 == 'T':
                show_warning("COMBINAÇÃO INVÁLIDA: Energia interna (U) e Temperatura (T) não podem ser usadas juntas.")
                return
            

            

            try:
                propriedade1_valor = float(propriedade_1.value)
            except ValueError:
                show_warning("PREENCHA A PROPRIEDADE 1 COM UM NÚMERO VÁLIDO")
                return

            try:
                propriedade2_valor = float(propriedade_2.value)
            except ValueError:
                show_warning("PREENCHA A PROPRIEDADE 2 COM UM NÚMERO VÁLIDO")
                return
            
            # Verifica se a qualidade (Título) está no intervalo válido
            if op1 == 'Q' and (propriedade1_valor < 0 or propriedade1_valor > 1):
                show_warning("Erro: Título (Q) deve estar entre 0 e 1.")
                return
            if op2 == 'Q' and (propriedade2_valor < 0 or propriedade2_valor > 1):
                show_warning("Erro: Título (Q) deve estar entre 0 e 1.")
                return
            
            if op1 == 'T' and op2 == 'U':
                show_warning("COMBINAÇÃO INVÁLIDA: Temperatura (T) e Energia interna (U) não podem ser usadas juntas.")
                return
            if (op2 == 'Q' and op2 in ['S', 'U', 'H']) or (op2 == 'Q' and op1 in ['S', 'U', 'H']):
                show_warning("COMBINAÇÃO INVÁLIDA: Título (Q) não pode ser usado com Entropia (S), Energia interna (U) ou Entalpia (H).")
                return
            
            # Limpa a tabela antes de adicionar novos resultados
            tabela_container.controls.clear()

            if propriedade == "Todas":
                resultado = allPropriedades(substancia, propriedade1_valor, propriedade2_valor, op1, op2)
                print(resultado)
                if  'Erro' == e:
                    show_warning("PROPRIEDADE NÃO ENCONTRADA, VERIFIQUE E TENTE NOVAMENTE")
                    return
                if resultado['fase'] == 'twophase':
                    tabela_container.controls.append(
                    ft.Row(
                        [
                            ft.DataTable(
                                columns=[
                                    ft.DataColumn(label=ft.Text("Propriedade")),
                                    ft.DataColumn(label=ft.Text("Resultado")),
                                    ft.DataColumn(label=ft.Text("Líquido Saturado")),
                                    ft.DataColumn(label=ft.Text("Vapor Saturado")),
                                ],
                                rows=[
                                    ft.DataRow(cells=[
                                        ft.DataCell(ft.Text("Pressão (kPa)")),
                                        ft.DataCell(ft.Text(str(resultado['propriedades']["P"]))),
                                        ft.DataCell(ft.Text(str(resultado['liquidos']["P"]))),
                                        ft.DataCell(ft.Text(str(resultado['vapores']["P"]))),
                                    ]),
                                    ft.DataRow(cells=[
                                        ft.DataCell(ft.Text("Temperatura (°C)")),
                                        ft.DataCell(ft.Text(str(resultado['propriedades']["T"]))),
                                        ft.DataCell(ft.Text(str(resultado['liquidos']["T"]))),
                                        ft.DataCell(ft.Text(str(resultado['vapores']["T"]))),
                                    ]),
                                    ft.DataRow(cells=[
                                        ft.DataCell(ft.Text("Volume específico (m³/kg)")),
                                        ft.DataCell(ft.Text(str(resultado['propriedades']["V"]))),
                                        ft.DataCell(ft.Text(str(resultado['liquidos']["V"]))),
                                        ft.DataCell(ft.Text(str(resultado['vapores']["V"]))),
                                    ]),
                                    ft.DataRow(cells=[
                                        ft.DataCell(ft.Text("Energia interna (kJ/kg)")),
                                        ft.DataCell(ft.Text(str(resultado['propriedades']["U"]))),
                                        ft.DataCell(ft.Text(str(resultado['liquidos']["U"]))),
                                        ft.DataCell(ft.Text(str(resultado['vapores']["U"]))),
                                    ]),
                                    ft.DataRow(cells=[
                                        ft.DataCell(ft.Text("Entalpia (kJ/kg)")),
                                        ft.DataCell(ft.Text(str(resultado['propriedades']["H"]))),
                                        ft.DataCell(ft.Text(str(resultado['liquidos']["H"]))),
                                        ft.DataCell(ft.Text(str(resultado['vapores']["H"]))),
                                    ]),
                                    ft.DataRow(cells=[
                                        ft.DataCell(ft.Text("Entropia (kJ/kg·K)")),
                                        ft.DataCell(ft.Text(str(resultado['propriedades']["S"]))),
                                        ft.DataCell(ft.Text(str(resultado['liquidos']["S"]))),
                                        ft.DataCell(ft.Text(str(resultado['vapores']["S"]))),
                                    ]),
                                ],
                            ),
                        ],
                        scroll=ft.ScrollMode.ALWAYS,  # Força o scroll horizontal sempre que necessário
                        width=600  # Ajuste a largura conforme necessário
                    )
                )

                    page.update()
                else:
                    tabela_container.controls.append(
                    ft.Row(
                        [
                            ft.DataTable(
                                columns=[
                                    ft.DataColumn(label=ft.Text("Propriedade")),
                                    ft.DataColumn(label=ft.Text("Resultado")),
                                ],
                                rows=[
                                    ft.DataRow(cells=[
                                        ft.DataCell(ft.Text("Pressão (kPa)")),
                                        ft.DataCell(ft.Text(str(resultado['propriedades']["P"]))),
                                    ]),
                                    ft.DataRow(cells=[
                                        ft.DataCell(ft.Text("Temperatura (°C)")),
                                        ft.DataCell(ft.Text(str(resultado['propriedades']["T"]))),
                                    ]),
                                    ft.DataRow(cells=[
                                        ft.DataCell(ft.Text("Volume específico (m³/kg)")),
                                        ft.DataCell(ft.Text(str(resultado['propriedades']["V"]))),
                                    ]),
                                    ft.DataRow(cells=[
                                        ft.DataCell(ft.Text("Energia interna (kJ/kg)")),
                                        ft.DataCell(ft.Text(str(resultado['propriedades']["U"]))),
                                    ]),
                                    ft.DataRow(cells=[
                                        ft.DataCell(ft.Text("Entalpia (kJ/kg)")),
                                        ft.DataCell(ft.Text(str(resultado['propriedades']["H"]))),
                                    ]),
                                    ft.DataRow(cells=[
                                        ft.DataCell(ft.Text("Entropia (kJ/kg·K)")),
                                        ft.DataCell(ft.Text(str(resultado['propriedades']["S"]))),
                                    ]),
                                ],
                            ),
                        ],
                        scroll=ft.ScrollMode.ALWAYS,  # Força a rolagem horizontal
                        width=600  # Ajuste a largura conforme necessário
                    )
                )

                page.update()

                
            

                
        # Função para limpar campos
        def limpar(e):
            propriedade_1.value = ""
            propriedade_2.value = ""
            resultado_texto.value = ""
            resultado_saturado.value = ""
            tabela_container.controls.clear()
            propriedade_1_tipo.value = False
            propriedade_2_tipo.value = False
            fluido.value = False
            propriedade_desejada.value = False
            page.update()

        # Botões de calcular e limpar
        calcular_btn = ft.ElevatedButton("CALCULAR", on_click=calcular)
        limpar_btn = ft.ElevatedButton("LIMPAR", on_click=limpar)

                # Container para os inputs
        inputs_container = ft.Column(
            [
                ft.Row([logo, ft.Text("Universidade Federal do Oeste da Bahia \nCampus Multidisciplinar de Bom Jesus da Lapa \nColegiado de Engenharia Mecânica \n \n \nDesenvolvido por: Maurício Fernandes", size=16)], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([ft.Text("Calculadora de Propriedades", font_family="Comic Sans MS", size=30)], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([ fluido], alignment=ft.MainAxisAlignment.END),
                ft.Row([propriedade_1_tipo, propriedade_1], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([propriedade_2_tipo, propriedade_2], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([calcular_btn, limpar_btn], alignment=ft.MainAxisAlignment.CENTER),
                resultado_texto,
                resultado_saturado,
                
            ],
            alignment=ft.MainAxisAlignment.CENTER,  # Centraliza os itens verticalmente
            
        )

        # Layout final com dois containers, centralizados vertical e horizontalmente
        layout = ft.Row(
            [
                ft.Container(content=inputs_container, alignment=ft.alignment.center),  # Centraliza o container de inputs
                ft.VerticalDivider(),  # Divisor vertical
                ft.Container(content=tabela_container, alignment=ft.alignment.center),  # Centraliza o container da tabela
                
            ],
            alignment=ft.MainAxisAlignment.CENTER,  # Centraliza na vertical
        )
        

        # Retornar o layout ajustado
        return layout

#__________________________PÁGINAS DOS EXEMPLOS_____________________________________________________
        # Função exemplo do ciclo
    def pageExemploSimples():
        # Definindo a imagem (Substitua pelo caminho correto da imagem)
        imagem_caminho = "exemplos/simples.png"  # Caminho da imagem enviada

        # Container para a imagem à esquerda
        imagem_ciclo = ft.Image(
            src=imagem_caminho,
            width=1000,  # Aumentando a largura da imagem
            fit=ft.ImageFit.CONTAIN
        )

        # Texto explicativo à direita com ajuste de scroll
        texto_explicativo = ft.Text(
            "Exemplo 10.3 - Çengel 7ª Edição\n\n"
        "Considere uma usina a vapor de água operando segundo o ciclo de Rankine ideal. "
        "Vapor entra na turbina a 3 MPa e 350 ºC e é condensado no condensador à pressão de 10 kPa. "
        "Determine (a) a eficiência térmica dessa usina, (b) a eficiência térmica se o vapor for superaquecido a 600 ºC e não a 350 ºC, "
        "e (c) a eficiência térmica se a pressão da caldeira for elevada até 15 MPa enquanto a temperatura na entrada da turbina é mantida a 600 ºC.",
            size=20,  # Aumentando o tamanho do texto
            
        )

        # Layout horizontal para imagem e texto
        conteudo = ft.Row(
            controls=[
                ft.Container(
                    content=imagem_ciclo,
                    alignment=ft.alignment.center,  # Centraliza a imagem verticalmente
                    expand=True
                ),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text("Exemplo de Ciclo Rankine", size=20, color=ft.colors.BLUE, weight=ft.FontWeight.BOLD),
                            texto_explicativo
                        ],
                        scroll=ft.ScrollMode.AUTO  # Adiciona barra de rolagem caso o texto ultrapasse o limite
                    ),
                    padding=20,
                    width=400  # Definindo uma largura fixa para garantir que o texto não passe dos limites
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,  # Centraliza o conteúdo no eixo horizontal
            vertical_alignment=ft.CrossAxisAlignment.CENTER  # Centraliza o conteúdo no eixo vertical
        )

        return conteudo
    
        # Função exemplo do ciclo
    def pageExemploReaquecimento():
        # Definindo a imagem (Substitua pelo caminho correto da imagem)
        imagem_caminho = "exemplos/reaquecimento1.png"  # Caminho da imagem enviada

        # Container para a imagem à esquerda
        imagem_ciclo = ft.Image(
            src=imagem_caminho,
            width=1000,  # Aumentando a largura da imagem
            fit=ft.ImageFit.CONTAIN
        )

        # Texto explicativo à direita com ajuste de scroll
        texto_explicativo = ft.Text(
            "10.35 - Çengel 7ª Edição\n\n"
            "Uma usina de potência a vapor de água opera no ciclo de Rankine ideal com reaquecimento. "
            "Vapor entra na turbina de alta pressão a 6 MPa e 400 ºC, saindo a 2 MPa. "
            "Em seguida, o vapor é reaquecido a uma pressão constante até 400 ºC antes de expandir "
            "até 20 kPa na turbina de baixa pressão. Determine o trabalho produzido pelas turbinas em kJ/kg "
            "e a eficiência térmica do ciclo. Mostre também o ciclo em um diagrama T-s que inclua as linhas "
            "de saturação.",
            size=20,  # Aumentando o tamanho do texto
            
        )

        # Layout horizontal para imagem e texto
        conteudo = ft.Row(
            controls=[
                ft.Container(
                    content=imagem_ciclo,
                    alignment=ft.alignment.center,  # Centraliza a imagem verticalmente
                    expand=True
                ),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text("Exemplo de Ciclo Rankine", size=20, color=ft.colors.BLUE, weight=ft.FontWeight.BOLD),
                            texto_explicativo
                        ],
                        scroll=ft.ScrollMode.AUTO  # Adiciona barra de rolagem caso o texto ultrapasse o limite
                    ),
                    padding=20,
                    width=400  # Definindo uma largura fixa para garantir que o texto não passe dos limites
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,  # Centraliza o conteúdo no eixo horizontal
            vertical_alignment=ft.CrossAxisAlignment.CENTER  # Centraliza o conteúdo no eixo vertical
        )

        return conteudo
    
        # Função exemplo do ciclo
    def pageExemploRegenerativo():
        # Definindo a imagem (Substitua pelo caminho correto da imagem)
        imagem_caminho = "exemplos/regenerativo.png"  # Caminho da imagem enviada

        # Container para a imagem à esquerda
        imagem_ciclo = ft.Image(
            src=imagem_caminho,
            width=1000,  # Aumentando a largura da imagem
            fit=ft.ImageFit.CONTAIN
        )

        # Texto explicativo à direita com ajuste de scroll
        texto_explicativo = ft.Text(
            "Exemplo 10.5 - Çengel 7ª Edição\n\n"
        "Considere uma usina de potência a vapor de água que opera segundo o ciclo de Rankine regenerativo ideal "
        "com um aquecedor de água de alimentação aberto. Vapor entra na turbina a 15 MPa e 600 ºC e é condensado "
        "no condensador à pressão de 10 kPa. Parte do vapor deixa a turbina a uma pressão de 1,2 MPa e entra no "
        "aquecedor de água de alimentação aberto. Determine a fração de vapor extraída da turbina e a eficiência "
        "térmica do ciclo.",
            size=20,  # Aumentando o tamanho do texto
            
        )

        # Layout horizontal para imagem e texto
        conteudo = ft.Row(
            controls=[
                ft.Container(
                    content=imagem_ciclo,
                    alignment=ft.alignment.center,  # Centraliza a imagem verticalmente
                    expand=True
                ),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text("Exemplo de Ciclo Rankine", size=20, color=ft.colors.BLUE, weight=ft.FontWeight.BOLD),
                            texto_explicativo
                        ],
                        scroll=ft.ScrollMode.AUTO  # Adiciona barra de rolagem caso o texto ultrapasse o limite
                    ),
                    padding=20,
                    width=400  # Definindo uma largura fixa para garantir que o texto não passe dos limites
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,  # Centraliza o conteúdo no eixo horizontal
            vertical_alignment=ft.CrossAxisAlignment.CENTER  # Centraliza o conteúdo no eixo vertical
        )

        return conteudo
    
        # Função exemplo do ciclo
    def pageExemploRegenerativoReaquecimento():
        # Definindo a imagem (Substitua pelo caminho correto da imagem)
        imagem_caminho = "exemplos/regenerativocomreaquecimento.png"  # Caminho da imagem enviada

        # Container para a imagem à esquerda
        imagem_ciclo = ft.Image(
            src=imagem_caminho,
            width=1000,  # Aumentando a largura da imagem
            fit=ft.ImageFit.CONTAIN
        )

        # Texto explicativo à direita com ajuste de scroll
        texto_explicativo = ft.Text(
             "10-60 - Çengel 7ª Edição\n\n"
        "Uma usina de potência a vapor opera no ciclo de Rankine com reaquecimento e regeneração com um aquecedor de água de "
        "alimentação fechado. Vapor entra na turbina a 8 MPa e 500 ºC com uma vazão de 15 kg/s e é condensado no condensador a "
        "uma pressão de 20 kPa. O vapor é reaquecido a 3 MPa até 500 ºC. Parte do vapor, extraído da turbina de baixa pressão a 1,0 MPa, "
        "é completamente condensado no aquecedor de água de alimentação e bombeado até 8 MPa antes de se misturar à água de alimentação "
        "à mesma pressão. Considerando uma eficiência isentrópica de 88% para a turbina e para a bomba, determine (a) a temperatura do vapor "
        "na entrada do aquecedor de água de alimentação, (b) o fluxo de massa do vapor extraído da turbina para o aquecedor de água de alimentação, "
        "(c) a potência líquida e (d) a eficiência térmica.\n\n"
        "Respostas: (a) 350 ºC; (b) 2,64 kg/s; (c) 16,2 MW; (d) 36,7%.",
            size=16,  # Aumentando o tamanho do texto
            
        )

        # Layout horizontal para imagem e texto
        conteudo = ft.Row(
            controls=[
                ft.Container(
                    content=imagem_ciclo,
                    alignment=ft.alignment.center,  # Centraliza a imagem verticalmente
                    expand=True
                ),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text("Exemplo de Ciclo Rankine", size=20, color=ft.colors.BLUE, weight=ft.FontWeight.BOLD),
                            texto_explicativo
                        ],
                        scroll=ft.ScrollMode.AUTO  # Adiciona barra de rolagem caso o texto ultrapasse o limite
                    ),
                    padding=20,
                    width=400  # Definindo uma largura fixa para garantir que o texto não passe dos limites
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,  # Centraliza o conteúdo no eixo horizontal
            vertical_alignment=ft.CrossAxisAlignment.CENTER  # Centraliza o conteúdo no eixo vertical
        )

        return conteudo
#______________________________________________________________________________________________________________________________________________________________


################################################################################################
#______________________PAGINA CONTATOS__________________________________________________
    
    
    def abrir_web_site(e):  
        webbrowser.open("https://github.com/mauriciofernandes123")  # Abre a URL no navegador padrão  

    def abrir_web_link(e):  
        webbrowser.open("https://www.linkedin.com/in/mauricio-fernandes-9382491b9/")  # Abre a URL no navegador padrão  

    def criar_pagina_contato():  
        # Informações de contato  
        contato_label = ft.Text("Entre em Contato:", size=24, weight=ft.FontWeight.BOLD)  
        nome = ft.Text("Maurício Fernandes de Oliveira Assis", size=20)  
        email = ft.Row(  
            controls=[  
                ft.Icon(ft.icons.EMAIL, size=24),  
                ft.Text("mauricio.a3347@ufob.edu.br", size=20)  
            ],  
            alignment=ft.MainAxisAlignment.CENTER  
        )  
        
        # Botão para abrir a URL no navegador  
        botao_web = ft.ElevatedButton("Abrir GitHub", on_click=abrir_web_site, width=200)  
        # Botão para abrir a URL no navegador  
        botao_web1 = ft.ElevatedButton("Abrir LinkedIn", on_click=abrir_web_link, width=200)  
        # Container para adicionar padding  
        return ft.Container(  
            content=ft.Column(  
                controls=[  
                    contato_label,  
                    nome,  
                    email,  
                    botao_web ,
                    botao_web1
                ],  
                alignment=ft.MainAxisAlignment.CENTER,  
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,  
            ),  
            padding=ft.padding.all(20),  # Ajusta o padding do container  
            width=600,  # Ajusta a largura da coluna  
            height=500, # Ajusta a altura da coluna  
        )  
#_________________________________________________________________________________


####################################################################
#_____________________PÁGINA SOBRE________________________________________
    def criar_pagina_sobre():  
        # Título da página  
        sobre_label = ft.Text("SOBRE", size=24, weight=ft.FontWeight.BOLD)  

        # Descrição do software  
        descricao = ft.Text(  
            "Nosso software foi especialmente desenvolvido para atender às necessidades específicas dos estudantes de Engenharia Mecânica na Universidade Federal do Oeste da Bahia. Ao enfrentar os desafios das disciplinas de Termodinâmica Básica, Termodinâmica Aplicada, Refrigeração e Sistemas Térmicos.\n\n"  
            "Com o software, os estudantes têm acesso a uma ampla gama de recursos, incluindo:\n\n"  
            "1- Cálculo Preciso de Propriedades Termodinâmicas: O software oferece capacidade de calcular propriedades como pressão, temperatura, volume específico, entalpia e entropia para diversas substâncias. Esses cálculos precisos são essenciais para análises termodinâmicas detalhadas e projetos de sistemas térmicos.\n\n"  
            "2- Simulações de Ciclos de Rankine: Uma parte vital do estudo da engenharia mecânica é a compreensão dos ciclos termodinâmicos, especialmente o ciclo de Rankine. Nosso software permite simular diferentes configurações de ciclo de Rankine, desde ciclos ideais até cenários mais complexos, permitindo uma compreensão aprofundada do processo de geração de energia térmica.\n\n"  
            "3- Interface Intuitiva e Amigável: Reconhecendo a importância da facilidade de uso, o software foi projetado com uma interface de usuário intuitiva. Isso permite que os alunos naveguem facilmente pelos recursos e realizem análises complexas com facilidade, sem se preocupar com a curva de aprendizado do software.\n\n"  
            "4- Suporte Didático Integrado: Além de ser uma ferramenta de cálculo, o software também serve como um recurso didático valioso. Ele está integrado ao material do curso, fornecendo exemplos práticos e exercícios que ajudam os alunos a consolidar seu conhecimento teórico e aplicá-lo em situações do mundo real.\n\n"  
            "Junte-se a nós para aprimorar a educação em engenharia mecânica! Contribua com suas habilidades de desenvolvimento para fazer parte deste projeto inovador.\n\n"  
            "Para obter informações detalhadas sobre o uso do software e como ser um desenvolvedor, consulte o Guia de Usuário.",  
            size=17,  
           
        )  

        # Container para adicionar padding e fundo  
        return ft.Container(  
            content=ft.Column(  
                controls=[  
                    sobre_label,  
                    descricao  
                ],  
                alignment=ft.MainAxisAlignment.START,  
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,  
            ),  
            padding=ft.padding.all(20),  # Ajusta o padding do container  
            
            width=1300,  # Ajusta a largura da coluna  
            height=500, # Ajusta a altura da coluna  
        )  

    # Definir a estrutura do NavigationDrawer
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.HOME, label="Início"),
            ft.NavigationDestination(icon=ft.icons.LOOKS_TWO, label="Simples"),
            ft.NavigationDestination(icon=ft.icons.LOOKS_3, label="Reaquecimento"),
            ft.NavigationDestination(icon=ft.icons.LOOKS_4, label="Regenerativo"),
            ft.NavigationDestination(icon=ft.icons.LOOKS_5, label="Regenerativo Com Reaquecimento"),
            ft.NavigationDestination(icon=ft.icons.CONTACT_SUPPORT, label="Contato"),
            ft.NavigationDestination(icon=ft.icons.INFO, label="Sobre"),
        ],
        selected_index=0,
        on_change=handle_change,
    )

    # Conteúdo inicial da página
    conteudo_pagina = criar_calculadora_propriedades()

    # Adiciona o botão de alternância de tema ao cabeçalho
    header = ft.Row([
        ft.IconButton(ft.icons.BRIGHTNESS_4, on_click=toggle_theme)  # Adiciona o botão de tema
    ], alignment=ft.MainAxisAlignment.END)

    

    page.add(
        ft.Column([
            

            conteudo_pagina,
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.START)
    )


    
# Executa a aplicação Flet
ft.app(target=main)
