import unittest
from src.control import ControlTalanquera 

class TestControlTanquera(unittest.TestCase):

    def test_succes(self):
        #fixture
        placa = "kzd-112"
        control_talanquera = ControlTalanquera()
    
        #Test        
        revision_placa=control_talanquera.revisar_placas_vehiculo(placa)
        lifting_barrier=control_talanquera.estado_de_talanquera()
        
        #Assertion
        self.assertTrue(revision_placa and lifting_barrier)

    

        
        