import asyncio

import httpx


async def main():
    async with httpx.AsyncClient() as client:
        response = await asyncio.gather(
            client.get(
                "http://127.0.0.1:8000/records/1",
                params={"delay_ms": 500},
            ),
            client.get(
                "http://127.0.0.1:8000/records/2",
                params={"delay_ms": 500},
            ),
            client.get(
                "http://127.0.0.1:8000/records/3",
                params={"delay_ms": 500},
            ),
            client.get(
                "http://127.0.0.1:8000/records/4",
                params={"delay_ms": 500},
            ),
        )
        print(response)


if __name__ == "__main__":
    asyncio.run(main())
