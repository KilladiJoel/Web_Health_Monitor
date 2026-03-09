import asyncio
from src.monitor import WebsiteSentinel
from src.database import DatabaseManager
INTERVAL_SECOND = 60
async def main():
    targets=["https://www.google.com",
        "https://www.github.com",
        "https://httpstat.us/404",
        "https://this-site-does-not-exist-123.com"]
    sentinel=WebsiteSentinel(targets)
    db=DatabaseManager()
    await db.setup_db()
    print("--- Database Is Ready ---")
    while True:
        print("---- Sentinel Report ----")
        report=await sentinel.run_monitor()
        for entry in report:
            if entry['status']=="DOWN":
                print("!!! ALERT: SITE DOWN !!!")
            print(f"[{entry['timestamp']}] {entry['url']} -> {entry['status']} ({entry['http_code']})")
            await db.save_result(entry['url'],entry['status'],entry['http_code'],entry['timestamp'])
        print(f"--- Sleeping for {INTERVAL_SECOND} second(s)... ---\n")
        await asyncio.sleep(INTERVAL_SECOND)
if __name__=="__main__":
    asyncio.run(main())

