from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def health(request):
    return JsonResponse({"status": "ok"}, status=200)

@csrf_exempt
def registrar_admision(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            paciente = data.get('paciente', 'desconocido')
            razon = data.get('razon', 'no especificada')
            return JsonResponse({
                "mensaje": f"Admision registrada para {paciente}",
                "razon": razon
            })
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"mensaje": "Método no permitido"}, status=405)

