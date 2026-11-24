import httpx


def fetch_record_sync(
    client: httpx.Client, record_id: int, delay_ms: int = 250, limit: int = 15000
) -> dict:
    url = f"http://127.0.0.1:8000/records/{record_id}"
    response = client.get(url, params={"delay_ms": delay_ms, "limit": limit})
    response.raise_for_status()
    data = response.json()
    return data
