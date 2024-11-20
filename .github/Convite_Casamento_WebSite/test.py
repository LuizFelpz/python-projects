from flet import *

def main(page: Page):
    def route_change(route):
        page.views.clear()
        page.views.append(
            View(
                '/',
                [
                    AppBar(
                        title= Text('Main', color= 'white'),
                        bgcolor= colors.DEEP_PURPLE_800,
                        
                    ),
                    ElevatedButton(
                            text= 'proxima_página',
                            on_click= lambda _: page.go('/next-page')
                        )
                ]
            )
        )

        if page.route == '/next-page':
            page.views.append(
                View(
                    '/next-page',
                    [
                        AppBar(
                            title= Text('Próxima Página'),
                            bgcolor= colors.PURPLE_300,
                            
                        ),
                        ElevatedButton(
                            text= 'Main',
                            on_click = lambda _: page.go('/')
                        )
                    ]
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


app(main, view= WEB_BROWSER)
