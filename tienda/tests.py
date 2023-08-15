from django.test import TestCase
from tienda.models import Orden
from datetime import datetime
from django.utils import timezone
import zoneinfo

class TiendaViewsTests(TestCase):
    def test_v_index(self):
        '''
            Debe entregar todos los registros
            si no existen filtros
        '''
        respuesta = self.client.get("/")
        ords = respuesta.context["ordenes"]
        self.assertEqual(0, len(ords))

        newo = Orden()
        newo.cliente = "Fernandito"
        newo.fecha = "2023-12-12"
        newo.fecha_envio = "2023-12-12"
        newo.direccion = "El eden 111"
        newo.save()

        respuesta = self.client.get("/")
        ords = respuesta.context["ordenes"]
        self.assertEqual(1, len(ords))

    
    def test_v_index_filtros(self):
        '''
            Entrega los registros con filtros de fecha
        '''
        newo = Orden()
        newo.cliente = "Soledad"
        newo.fecha = "2022-12-12"
        newo.fecha_envio = datetime(2022, 12, 12).\
            astimezone(zoneinfo.ZoneInfo('America/Santiago'))
        newo.direccion = "El eden 111"
        newo.save()

        newo = Orden()
        newo.cliente = "Cristina"
        newo.fecha = "2023-12-12"
        newo.fecha_envio = datetime(2023, 12, 12).\
            astimezone(zoneinfo.ZoneInfo('America/Santiago'))
        newo.direccion = "Puerto libertad 222"
        newo.save()

        res = self.client.get("/?fecha_inicio=%s&fecha_fin=%s" % (
            '2023-11-01',
            '2023-12-25',
        ))

        ords = res.context["ordenes"]
        self.assertEqual(1, len(ords))
        self.assertEqual("Cristina", ords.first().cliente)
        self.assertEqual("Puerto libertad 222", ords.first().direccion)


    def test_v_index_filtros_fecha_envio(self):
        '''
            Defe filtrar por la fecha de envío
        '''
        newo = Orden()
        newo.cliente = "Soledad"
        newo.fecha = "2022-12-12"
        newo.fecha_envio = datetime(2022, 12, 12).\
            astimezone(zoneinfo.ZoneInfo('America/Santiago'))
        newo.direccion = "El eden 111"
        newo.save()

        newo = Orden()
        newo.cliente = "Cristina"
        newo.fecha = "2023-12-12"
        newo.fecha_envio = datetime(2023, 12, 12).\
            astimezone(zoneinfo.ZoneInfo('America/Santiago'))
        newo.direccion = "Puerto libertad 222"
        newo.save()

        res = self.client.get("/?fecha_e_inicio=%s&fecha_e_fin=%s" % (
            '2023-11-01',
            '2023-12-25',
        ))

        ords = res.context["ordenes"]
        self.assertEqual(1, len(ords))
        self.assertEqual("Cristina", ords.first().cliente)
        self.assertEqual("Puerto libertad 222", ords.first().direccion)

