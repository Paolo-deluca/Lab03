from strumenti import Strumento


class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.nome = nome
        self.responsabile = responsabile
        self.strumenti = {}
        self.prestiti = {}

        self.ultimo_id_strumento = 0
        self.ultimo_id_prestito = 0
    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        # TODO

        file = open(file_path, "r")

        for riga in file:
            riga = riga.strip()
            riga = riga.split(",")
            codice = riga[0]
            strumento = riga[1]
            marca = riga[2]
            anno_acquisto = riga[3]
            valore = riga[4]
            nuovo_strumento = Strumento(codice, strumento, marca, anno_acquisto, valore)
            self.strumenti[codice] = nuovo_strumento
        file.close()



    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO
        self.ultimo_id_strumento += 1
        cod = f"S{self.ultimo_id_strumento}"


        nuovo_strumento = Strumento(cod, tipo, marca, anno_acquisto, valore)

        self.strumenti[cod] = nuovo_strumento

        return nuovo_strumento
    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        # TODO
        lista_strumenti = list(self.strumenti.values())
        return sorted(lista_strumenti, key=lambda s: s.marca)


    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        # TODO
        if id_strumento not in self.strumenti:
            raise Exception(
                f"Errore: Lo strumento '{id_strumento}' non esiste nel deposito!"
            )

        for prestito in self.prestiti.values():
            if prestito["id_strumento"] == id_strumento:
                raise Exception(
                    f"Errore: Lo strumento '{id_strumento}' è già in prestito!"
                )

        self.ultimo_id_prestito += 1
        cod_prestito = f"P{self.ultimo_id_prestito}"

        self.prestiti[cod_prestito] = {
            "id_strumento": id_strumento,
            "cognome": cognome_allievo,
            "data": data,
        }

        return f"[{cod_prestito}] Strumento: {id_strumento} | Allievo: {cognome_allievo} | Data: {data}"
    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO
        if id_prestito in self.prestiti:
            del self.prestiti[id_prestito]
        else:
            raise Exception(f"Errore: l'id inserito o è sbagliato o non esiste")
