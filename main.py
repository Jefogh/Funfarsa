import flet as ft

def main(page):
    page.title = "Flet App"
    page.add(ft.Text("Hello, this is a Flet app running as a web app!"))

if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER)
