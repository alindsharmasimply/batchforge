from fastapi import FastAPI
import asyncio

app = FastAPI()


@app.get("/records/{record_id}")
async def get_record(record_id: int, delay_ms: int = 250, limit: int = 15000):
    await asyncio.sleep(delay_ms / 1000)
    return {"id": record_id, "limit": limit}
