import httpx

from batchforge.cpu import count_primes
from batchforge.fetch import fetch_record_sync


def batch_io_heavy(ids: list[int] | None = None):
    if ids is None:
        ids = []
    results = []
    with httpx.Client() as client:
        for id in ids:
            response = fetch_record_sync(
                client=client, record_id=id, delay_ms=250, limit=100
            )
            count_result = count_primes(100)
            results.append({"record": response, "primes": count_result})
    return results


def batch_cpu_heavy(ids: list[int] | None = None):
    if ids is None:
        ids = []
    results = []
    with httpx.Client() as client:
        for id in ids:
            response = fetch_record_sync(
                client=client, record_id=id, delay_ms=0, limit=250000
            )
            count_result = count_primes(250000)
            results.append({"record": response, "primes": count_result})
    return results


print(batch_io_heavy([1, 2, 3, 4, 5, 6, 7, 8]))
print(batch_cpu_heavy([1, 2, 3, 4, 5, 6, 7, 8]))
