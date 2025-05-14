import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listColor = []

    def fillDD(self):
        self._view._ddyear.options.extend([ft.dropdown.Option(text="2015"), ft.dropdown.Option(text="2016"),ft.dropdown.Option(text="2017"),ft.dropdown.Option(text="2018")])
        lista_colori = self._model.get_colori()
        for colore in lista_colori:
            self._view._ddcolor.options.append(ft.dropdown.Option(text=colore))
        self._view._page.update()


    def handle_graph(self, e):
        colore = self._view._ddcolor.value
        anno = self._view._ddyear.value
        if colore is None or colore == "":
            self._view.create_alert("Selezionare il color")
            return
        if anno is None or anno == "":
            self._view.create_alert("Selezionare l'anno")
            return

        self._model.buildgraph(colore, anno)

        self._view.txtOut.controls.clear()

        self._view.txtOut.controls.append(ft.Text("Grafo correttamente creato."))

        self._view.txtOut.controls.append(ft.Text(f"numero di vertici: {self._model.getNumNodi()}, numero di archi: {self._model.getNumArchi()}"))
        listaArchiMilgiori = self._model.getArchiGraficoMigliori()

        self._view.update_page()



    def fillDDProduct(self):
        pass


    def handle_search(self, e):
        pass
