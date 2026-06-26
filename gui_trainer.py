import flet as ft


def main(page: ft.Page):
    page.add(
        ft.SafeArea(
            expand=True,
            content=ft.Tabs(
                selected_index=0,
                length=3,
                expand=True,
                content=ft.Column(
                    expand=True,
                    controls=[
                        ft.TabBar(
                            tabs=[
                                ft.Tab(label="Enrenamiento"),
                                ft.Tab(label="Análisis"),
                            ]
                        ),
                        ft.TabBarView(
                            expand=True,
                            controls=[
                                ft.Column(
                                    controls=[
                                        ft.Text("Entrenamiento de Red Neuronal",size=24, weight=ft.FontWeight.W_600),
                                        ft.Divider(height=1, color=ft.Colors.WHITE),
                                        ft.Row(
                                            expand = True,
                                            controls=[
                                                ft.Column(
                                                    #spacing = 40,
                                                    width=300,
                                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                    #expand=True,
                                                    controls=[
                                                        ft.Button(content="Añadir Dataset", height=50),
                                                        ft.Text("Canales/Sensores"),
                                                        ft.Container(
                                                            alignment=ft.Alignment.CENTER,
                                                            border=ft.Border.all(width=1, color=ft.Colors.WHITE),
                                                            border_radius=10,
                                                            width=200,
                                                            #height=150,
                                                            #bgcolor= ft.Colors.AMBER,
                                                            content = ft.Column(
                                                                controls = [
                                                                    ft.Row(
                                                                        controls=[
                                                                            ft.Checkbox(),
                                                                            ft.Text("Sensor 1")
                                                                        ]
                                                                    ),
                                                                    ft.Row(
                                                                        controls=[
                                                                            ft.Checkbox(),
                                                                            ft.Text("Sensor 2")
                                                                        ]
                                                                    ),
                                                                    ft.Row(
                                                                        controls=[
                                                                            ft.Checkbox(),
                                                                            ft.Text("Sensor 3")
                                                                        ]
                                                                    ),
                                                                    ft.Row(
                                                                        controls=[
                                                                            ft.Checkbox(),
                                                                            ft.Text("Sensor 4")
                                                                        ]
                                                                    ),
                                                                    ft.Row(
                                                                        controls=[
                                                                            ft.Checkbox(),
                                                                            ft.Text("Sensor 5")
                                                                        ]
                                                                    ),
                                                                    ft.Row(
                                                                        controls=[
                                                                            ft.Checkbox(),
                                                                            ft.Text("Sensor 6")
                                                                        ]
                                                                    ),    
                                                                ]
                                                            )
                                                            
                                                        ),
                                                        ft.Button(content="Entrenar Red Neuronal", height=50),
                                                        ft.Button(content="Guardar keras", height=50),
                                                    ]
                                                ),
                                                ft.VerticalDivider(),
                                                ft.Column(
                                                    expand=True,
                                                    controls=[
                                                        ft.Text("Adios"),
                                                    ]
                                                )
                                            ],
                                        ),
                                    ]
                                ),
                                ft.Column(
                                    controls=[
                                        ft.Text("Tab 2")
                                    ]
                                )
                                
                            ]
                                ),
                    ]
                )
            ),
        ),
    )


if __name__ == "__main__":
    ft.run(main)
