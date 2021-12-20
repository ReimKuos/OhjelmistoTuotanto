from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

class KiviPaperiSaksetPeli:

    def aloita(self):
        while True:
            vastaus = self.ota_pelimuoto()
            peli = self.aseta_pelimuoto(vastaus)
            if peli is None:
                break
            peli.pelaa()

    def ota_pelimuoto(self):
        print(
            "Valitse pelataanko"
            "\n (a) Ihmistä vastaan"
            "\n (b) Tekoälyä vastaan"
            "\n (c) Parannettua tekoälyä vastaan"
            "\nMuilla valinnoilla lopetetaan"
        )
        vastaus = input()
        return vastaus

    def aseta_pelimuoto(self, vastaus):
        if vastaus.endswith("a"):
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )
            return KPSPelaajaVsPelaaja()
        elif vastaus.endswith("b"):
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )
            return KPSTekoaly()
        elif vastaus.endswith("c"):
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )
            return KPSParempiTekoaly()
        else:
            return None