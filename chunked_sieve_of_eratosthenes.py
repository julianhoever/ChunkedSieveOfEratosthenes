import argparse
from math import ceil
import time

if __name__ == "__main__":
    start_time = time.time()

    parser = argparse.ArgumentParser(description="Chunked Sieve Of Eratosthenes")
    parser.add_argument("-u", "--upper_bound", help="Upper bound for calculating the prime numbers.", type=int, default=100)
    parser.add_argument("-c", "--chunk_size", help="Chunk size.", type=int, default=10)
    args = parser.parse_args()

    upper_bound = args.upper_bound
    chunk_size = args.chunk_size
    primes = []

    for chunk in range(ceil(upper_bound / chunk_size)):
        lower_chunk_bound = chunk * chunk_size
        upper_chunk_bound = lower_chunk_bound + chunk_size

        if upper_chunk_bound > upper_bound:
            upper_chunk_bound = upper_bound

        sieve = [True] * (upper_chunk_bound - lower_chunk_bound)

        for prime in primes:
            smallest_factor = ceil(lower_chunk_bound / prime)
            for not_prime in range(smallest_factor * prime, upper_chunk_bound, prime):
                sieve[not_prime % chunk_size] = False

        for prim_candidate in range(lower_chunk_bound if lower_chunk_bound >= 2 else 2, upper_chunk_bound):
            if sieve[prim_candidate % chunk_size]:
                primes.append(prim_candidate)
                for not_prime in range(prim_candidate * 2, upper_chunk_bound, prim_candidate):
                    sieve[not_prime % chunk_size] = False

    stop_time = time.time()

    print(f"Execution time: {round(stop_time - start_time)}s")
    print(f"Number of primes: {len(primes)}")
#    print(primes)
