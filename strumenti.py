class Strumento:
    def __init__(self, codice,tipo,marca,anno_acquisto,valore):
        self.codice = codice
        self.tipo = tipo
        self.marca = marca
        self.anno_acquisto = int(anno_acquisto)
        self.valore = float(valore)

    def __str__(self):
        return f"[{self.codice}] {self.tipo} - Marca: {self.marca} (Anno: {self.anno_acquisto}, Valore: {self.valore}€)"