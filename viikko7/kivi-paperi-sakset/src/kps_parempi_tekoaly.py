from kps import KPS
from tekoaly_parannettu import TekoalyParannettu

class KPSParempiTekoaly(KPS):
    tekoaly = TekoalyParannettu(10)
    def _onko_ok_siirto(self, siirto):
        tko_siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tko_siirto}")
        self.tekoaly.aseta_siirto(siirto)
        return tko_siirto

