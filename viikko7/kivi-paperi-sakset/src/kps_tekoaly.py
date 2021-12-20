from kps import KPS
from tekoaly import Tekoaly

class KPSTekoaly(KPS):
    tekoaly = Tekoaly()
    def _toisen_siirto(self, siirto):
        tko_siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tko_siirto}")
        self.tekoaly.aseta_siirto(siirto)
        return tko_siirto
