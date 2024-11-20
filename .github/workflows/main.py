
from flet import *
import flet


#------------------------------------------------------------------------------
#FONTS
fonts = {
    'hurricane': r'assets\fonts\Hurricane\Hurricane\Hurricane-Regular.ttf',
    'Inria_Serif': r'assets\fonts\Inria_Serif\InriaSerif-Italic.ttf'
}

#IMAGES-----------------------------------------------------------------------------------
moldura_principal = Container(
                        Image(
                            src = 'assets\images\Modura Principal.png',
                            fit = ImageFit.COVER,
                        ),
                        padding= 0,
                        margin= margin.all(0),
                        
                    )


moldura_principal_2 = Container(
                        content= Image(
                            src= 'assets\images\Modura Principal 2.png',
                            fit= ImageFit.COVER,
                            scale = 0.9
                        ),
                        offset= Offset(0.03, 0),
                        padding= 0,
                        margin= 0
                    )
logo = Image(
    src = 'assets\images\Title.png',
    scale= 0.77,
    offset= Offset(0.03, 0)
)

logo2 = Image('assets\images\Title.png',
    scale= 0.67,
    offset= Offset(-0.05, 0.3),
    
)


#TEXTOS---------------------------------------------------------------------------------
endereco_title = Text(
    "Endereço: ",
    color= '#2C0A49',
    font_family = 'hurricane',
    size= 32,
    weight= FontWeight.W_500
)

endereco_value = Text(
    'AV. Américas, nº 2553, Guanhães - MG',
    font_family = 'Inria_Serif',
    color= 'black',
    size= 19,
)

data_title = Text(
    "Data / Hora: ",
    color= '#2C0A49',
    font_family = 'hurricane',
    size= 32,
    weight= FontWeight.W_500
)               

data_value = Text(
    '09/01/2025 19:30hr',
    font_family= 'inria_Serif',
    color= 'black',
    size= 19,
)



#BOTÕES-------------------------------------------------------------------------------

codigo_convite = TextField(
        text_style= TextStyle(
            color= 'black',
            font_family= 'Inria_Serif',
            size= 30
        ),
        text_align = TextAlign.START,
        label= 'Código do Convite',
        label_style= TextStyle(
            color= 'black',
            font_family= 'hurricane',
            size= 32
        ),
        color = 'black',
        border= InputBorder.UNDERLINE,
        offset = Offset(0, -0.4)

    )

#PopUps----------------------------------------------------------------------------------------------------
location = AlertDialog(
    title = Text(
        value = 'Local de Comemoração',
        size = 30,
        color = '#1D154A'
    ),
    content = Text(
        value = 'Avenida das Américas nº 2955, Bairro X, Guanhães',
        color = '#1D154A'
    ),
    bgcolor = '#E5C9EF',
)

data = AlertDialog(
    title = Text(
        value = 'Informações de Horário',
        size = 30,
        color = '#1D154A'
    ),
    content = Text(
        value = '09/01/2025 19:30hrs',
        color = '#1D154A'
    ),
    bgcolor = '#E5C9EF'
)

presentes = AlertDialog(
    title = Text(
        value = 'Deseja nos Presentear?',
        size = 30,
        color = '#1D154A'
    ),
    content = Text(
        value = 'Chave pix: (31) 98906-8620\nOutros: Entre em contato conosco pelo número: (31) 98842-5816',
        color = '#1D154A'
    ),
    bgcolor = '#E5C9EF',
)

def main(page: Page):
    page.fonts = fonts
    page.scroll = ScrollMode.ADAPTIVE
    page.auto_scroll = True
    page.padding = 0
    page.window.width = 640
    page.window.height = 1024
    page.window.resizable = True
    page.bgcolor= 'white'
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    

    def confirmation(e):    
        import pandas as pd
        dt = pd.read_csv(r'assets\database\Convidados.csv', delimiter= ',', encoding = 'latin')

        def close_popup(e):
            confirmacao.open = False
            page.update()

        def confirmar(e):
            dt.loc[dt['Cdg_Convite'] == str(codigo_convite.value).strip(), 'Confirmado'] = True
            dt.to_csv(
                'assets\database\Convidados.csv', sep = ',', index = False, encoding= 'latin'
            )

            confirmacao.open = False
            page.overlay.append(
                AlertDialog(
                    title = Text(
                        'Confirmação bem sucedida!',
                        size = 30,
                        color = '#1D154A'
                    ),

                    content = Text(
                        value = 'Esperamos você para comemorar este mometo conosco! Até lá o/',
                        color = '#1D154A'
                    ),
                    bgcolor = '#E5C9EF',
                    open = True
                )
            )
            page.update()
            
        cdg = str(codigo_convite.value).strip()
        
        if cdg in dt['Cdg_Convite'].values:

            dt_filtrado = dt.query(f'Cdg_Convite == "{cdg}"')
            nome = dt_filtrado['Nome'].values[0]

            confirmacao = AlertDialog(
                modal = True,
                title = Text(
                    value = 'Confirme as Informações',
                    size = 30,
                    color = '#1D154A' 
                ),
                content = Text(
                    value = f'Nome: {nome}\nCódigo Convite: {cdg}',
                    color = '#1D154A'
                ),

                actions = [
                    TextButton(
                        content = Text('Confirmar presença', color = '#1D154A'),
                        on_click = confirmar
                    ),
                    TextButton(
                        content= Text('Cancelar', color = '#1D154A'),
                        on_click = close_popup
                    )
                ],

                bgcolor = '#E5C9EF'

            )

            page.overlay.append(confirmacao)
            confirmacao.open = True
            page.update()

        else:
            page.overlay.append(
                AlertDialog(
                    title = Text(
                        value = 'Código Inválido',
                        size = 30,
                        color = '#1D154A'
                        
                        ),

                        content = Text(
                            value = 'Verifique se o código foi inserido corretamente e tente novamente'
                        )
                    )
                )
            

    def open_location(e):
        page.overlay.append(location)
        location.open = True
        page.update()

    def open_data(e):
        page.overlay.append(data)
        data.open = True
        page.update()
    
    def open_present(e):
        page.overlay.append(presentes)
        presentes.open = True
        page.update()


    def route_change(route):
        page.views.clear()
        page.views.append(
            View(
                '/',
                [
                    Container(
                        Stack([
                            Image(
                                src = 'assets\images\Lavanda.jpg', fit= ImageFit.COVER, scale = 1.15
                            ),
                            Container(
                                content = Column(
                                            [
                                                Text(
                                                    '"Assim, eles já não são dois, mas sim uma só carne.\n Portanto, o que Deus uniu, ninguém separe." \nMateus 19:6',
                                                    style= TextStyle(
                                                        color= "#2C0A49",
                                                        size = 18,
                                                        font_family= 'Inria_Serif',
                                                        italic = True,
                                                        shadow= BoxShadow(0.5, 0.1, 'back')
                                                        ),
                                                    text_align = TextAlign.LEFT
                                                ),
                                                Stack(
                                                    [
                                                        moldura_principal,
                                                        logo
                                                    ],
                                                alignment= alignment.center,
                                                ),
                                                Text(
                                                    'Comemore este momento conosco!\n Sua presença, é importante para nós',
                                                    style = TextStyle(
                                                        color= "#2C0A49",
                                                        size= 22,
                                                        font_family= 'Inria_Serif',
                                                        shadow = BoxShadow(1, 0.2, 'black')
                                                    ),
                                                    text_align= TextAlign.CENTER,
                                                    offset= Offset(0.15, -0.3)
                                                ),
                                                ResponsiveRow(
                                                    [Row(
                                                        [endereco_title, endereco_value],
                                                        alignment= MainAxisAlignment.CENTER
                                                        )],
                                                    spacing= 2,
                                                    run_spacing= 0,
                                                    alignment= MainAxisAlignment.CENTER
                                                ),
                                                ResponsiveRow(
                                                    [Row(
                                                        [data_title, data_value],
                                                        alignment= MainAxisAlignment.CENTER
                                                        )],
                                                    spacing= 2, 
                                                    run_spacing= 10
                                                ),
                                                Container(
                                                    ElevatedButton(
                                                        text= "Confirmar Presença!",
                                                        style= ButtonStyle(
                                                            bgcolor= '#2C174F',
                                                            color= 'white',
                                                            shape= RoundedRectangleBorder(5),
                                                        ),
                                                        scale= 1.4,
                                                        offset= Offset(0.07, 0),
                                                        on_click= lambda _: page.go('/validation')
                                                        
                                                    ),
                                                    height= 160,
                                                    alignment= alignment.center
                                                ),
                                                
                                            ],
                                        alignment = MainAxisAlignment.SPACE_BETWEEN,
                                        spacing= 1
                                    ),
                                #bgcolor= "red",
                                width = 480,
                                height = 840,
                                margin = Margin(10, 80, 10, 10)
                            )
                        ],
                        alignment= alignment.center
                    
                        )
                    )
                ],
                padding= 0,
                scroll = ScrollMode.ADAPTIVE,
                auto_scroll= True
            )
        )

        if page.route == '/validation':
            page.views.append(
                View(
                    '/validation',
                    [
                        Container(
                            Column([
                                Stack([
                                    Image(
                                        src = 'assets\images\Lavanda.jpg', fit= ImageFit.CONTAIN, scale = 1.23
                                    ),
                                    moldura_principal_2,
                                    Container(
                                        Column(
                                            [
                                                logo2,
                                                TextField(
                                                    text_style= TextStyle(
                                                        color= 'black',
                                                        font_family= 'Inria_Serif',
                                                        size= 30
                                                    ),
                                                    text_align = TextAlign.START,
                                                    label= 'Nome Completo',
                                                    label_style= TextStyle(
                                                        color= 'black',
                                                        font_family= 'hurricane',
                                                        size= 32
                                                    ),
                                                    color = 'black',
                                                    border= InputBorder.UNDERLINE,
                                                    offset = Offset(0, -0.4)

                                                ),
                                                codigo_convite,
                                                ElevatedButton(
                                                    text = "Validar Convite",
                                                    style = ButtonStyle(
                                                        bgcolor = '#2C174F',
                                                        color = 'white',
                                                        shape = RoundedRectangleBorder(5),
                                                        
                                                    ),
                                                    offset = Offset(0.3, -1.5),
                                                    scale = 1.3,
                                                    on_click = confirmation,
                                                    width = 250,       
                                                )
                                            ],
                                            alignment = MainAxisAlignment.CENTER,
                                            spacing= 40,
                                            run_spacing= 0,
                                            width= 400
                                        )
                                    ),
                                ],
                                
                                alignment= alignment.center
                            ),
                            ResponsiveRow(
                                [
                                    Container(
                                        Image(
                                            src= 'assets\images\Local.png',
                                            scale= 0.85,
                                        ),
                                        col= 4,
                                        ink= True,
                                        on_click = open_location
                                    ),
                                    Container(
                                        Image(
                                            src = 'assets\images\Horário.png',
                                            scale= 0.85,
                                            col = 4
                                        ),
                                        col= 4,
                                        ink= True,
                                        on_click = open_data
                                    ),
                                    Container(
                                        Image(
                                            src = 'assets\images\Presentes.png',
                                            scale = 0.85,
                                            col = 4
                                        ),
                                        col= 4,
                                        ink= True,
                                        on_click = open_present
                                    )
                                ],
                                height= 100,
                                spacing = 0,
                                run_spacing= 0,
                                offset= Offset(0, -1.2)
                            )
                    ], run_spacing= 0, spacing= 0)
                )
            ],
            padding= 0,
            scroll= ScrollMode.ADAPTIVE,
            auto_scroll= True
        )
    )
            
        page.update()


    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)




flet.app(target = main)