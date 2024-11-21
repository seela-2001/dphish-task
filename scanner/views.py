from django.http import JsonResponse
from .tasks import process_ip

def scan_ips(request):
    ip_list = request.POST.get('ips', '').split(',')
    tasks = []
    for ip in ip_list:
        task = process_ip.apply_async(args=[ip.strip()])
        tasks.append(task.id)
    return JsonResponse({"status": "Tasks are being processed", "task_ids": tasks})

