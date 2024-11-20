from flet import *


body =  View(
            route= '/validation',
            controls=[
                Container(
                    bgcolor= 'red',
                    width = 200,
                    height = 200
                )
            ]
        )

def validation(page: Page):
   page.add(body)

app(validation)