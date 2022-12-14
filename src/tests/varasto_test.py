import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.virheellinen_varasto1 = Varasto(-10,-5)
        self.virheellinen_varasto2 = Varasto(-10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)
        self.assertAlmostEqual(self.virheellinen_varasto1.tilavuus, 0)
        self.assertAlmostEqual(self.virheellinen_varasto2.tilavuus, 0)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisaa_saldoa_negatiivisella_luvulla(self):
        self.varasto.lisaa_varastoon(-5)
        
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_ei_voi_lisaa_enemman_kuin_on_tilaa(self):
        self.varasto.lisaa_varastoon(11)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ei_voi_ottaa_negatiivista_maaraa(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.ota_varastosta(-3)

        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_otetaan_loput_kun_maara_saldoa_isompi(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.ota_varastosta(7)

        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_tulostus_oikein(self):
        self.varasto.lisaa_varastoon(5)
        
        self.assertEqual(str(self.varasto), "saldo = 5, vielä tilaa 5")
