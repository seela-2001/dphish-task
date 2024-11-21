from celery import shared_task
import aiohttp
import asyncio
import ipaddress

@shared_task
def validate_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

@shared_task
async def fetch_ip_info(ip):
    url = f"https://ipinfo.io/{ip}/json"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

@shared_task
def process_ip(ip):
    if validate_ip(ip):
        result = asyncio.run(fetch_ip_info(ip))
        return result
    return {"error": "Invalid IP address"}
