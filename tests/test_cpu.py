from batchforge.cpu import count_primes


def test_count_primes():
    assert count_primes(5) == 2
    assert count_primes(10) == 4
    assert count_primes(30) == 10
    assert count_primes(100) == 25
    assert count_primes(1000) == 168
    assert count_primes(10000) == 1229
    assert count_primes(100000) == 9592
    assert count_primes(200000) == 17984
