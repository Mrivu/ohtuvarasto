import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.varasto2 = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

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

    def test_laitetaan_enemman_kuin_tilaa(self):
        self.varasto2.lisaa_varastoon(20)
        self.assertAlmostEqual(self.varasto2.saldo, 10)
    
    def test_otetaan_enemman_kuin_tarjolla(self):
        jaljella = self.varasto2.saldo
        self.assertAlmostEqual(self.varasto2.ota_varastosta(20), jaljella)
    
    def test_varasto_luodaan_oikein(self):
        varasto3 = Varasto(-10,-10)
        self.assertAlmostEqual(varasto3.tilavuus, 0)
        self.assertAlmostEqual(varasto3.saldo, 0)
        varasto3 = Varasto(10,20)
        self.assertAlmostEqual(varasto3.saldo, 10)

    def test_ei_nolla(self):
        saldo = self.varasto2.saldo
        self.varasto2.ota_varastosta(-3)
        self.assertAlmostEqual(self.varasto.saldo, saldo)
        saldo = self.varasto2.saldo
        self.varasto2.lisaa_varastoon(-3)
        self.assertAlmostEqual(self.varasto.saldo, saldo)

    def test_str_print(self):
        saldo = self.varasto2.saldo
        mahtuu = self.varasto2.paljonko_mahtuu()
        self.assertAlmostEqual(str(self.varasto2), f"saldo = {saldo}, vielä tilaa {mahtuu}"
)

