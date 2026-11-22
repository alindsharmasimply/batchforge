import asyncio

import httpx


async def main():
    async with httpx.AsyncClient() as client:
        response1 = await client.get(
            "http://127.0.0.1:8000/records/1",
            params={"delay_ms": 500},
        )
        response2 = await client.get(
            "http://127.0.0.1:8000/records/2",
            params={"delay_ms": 500},
        )
        response3 = await client.get(
            "http://127.0.0.1:8000/records/3",
            params={"delay_ms": 500},
        )
        response4 = await client.get(
            "http://127.0.0.1:8000/records/4",
            params={"delay_ms": 500},
        )
        print(response1)
        print(response2)
        print(response3)
        print(response4)


if __name__ == "__main__":
    asyncio.run(main())
