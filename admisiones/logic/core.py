from admisiones.models import Admision

def registrar_admision(paciente, razon):
    if not paciente:
        paciente = "desconocido"
    if not razon:
        razon = "no especificada"

    nueva = Admision.objects.create(paciente=paciente, razon=razon)
    return {
        "mensaje": f"Admision registrada para {nueva.paciente}",
        "razon": nueva.razon
    }
