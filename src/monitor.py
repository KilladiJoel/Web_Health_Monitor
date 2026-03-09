import asyncio
import httpx
from datetime import datetime
from typing import List, Dict
class WebsiteSentinel:
    def __init__(self,urls:List[str]):
        self.urls=urls
    async def check_sites(self,client: httpx.AsyncClient,url:str) -> Dict:
        try:
            response=await client.get(url,timeout=5.0)
            status="UP" if response.status_code==200 else "WARNING"
            code=response.status_code
        except Exception as e:
            status="Down"
            code=0
        return {"url":url,
                "status":status,
                "http_code":code,
                "timestamp":datetime.now().strftime("%H:%M:%S")}
    async def run_monitor(self):
        async with httpx.AsyncClient() as client:
            tasks=[self.check_sites(client, url) for url in self.urls]
            results = await asyncio.gather(*tasks)
            return results