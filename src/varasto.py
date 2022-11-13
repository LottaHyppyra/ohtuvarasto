"""Luokka varasto."""
class Varasto:
    """Luokka varasto, jolla tilavuus ja saldo."""
    def __init__(self, tilavuus, alku_saldo = 0) -> None:
        """Konstruktorissa määritetään varaston tilavuus ja saldo."""
        self.tilavuus = max(0.0, tilavuus)
        self.saldo = min(max(0.0, alku_saldo), tilavuus)
    def paljonko_mahtuu(self):
        """Palauttaa paljonko varastoon vielä mahtuu."""
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        """Lisää parametrin verran varastoon, jos mahtuu."""
        if maara < 0:
            return
        if maara <= self.paljonko_mahtuu():
            self.saldo = self.saldo + maara
        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara):
        """Ottaa parametrin verran pois tilavuudesta, jos mahdollista."""
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0

            return kaikki_mita_voidaan

        self.saldo = self.saldo - maara
        return maara

    def __str__(self):
        """Kertoo varaston saldon ja paljon tilaa vielä jäljellä"""
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
    