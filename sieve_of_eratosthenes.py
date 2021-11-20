import argparse
import time

if __name__ == "__main__":
    start_time = time.time()

    parser = argparse.ArgumentParser(description="Chunked Sieve Of Eratosthenes")
    parser.add_argument("-u", "--upper_bound", help="Upper bound for calculating the prime numbers.", type=int, default=100)
    args = parser.parse_args()

    upper_bound = args.upper_bound
    sieve = [True] * upper_bound
    primes = []

    for prim_candidate in range(2, upper_bound):
        if sieve[prim_candidate]:
            primes.append(prim_candidate)
            for not_prime in range(prim_candidate * 2, upper_bound, prim_candidate):
                sieve[not_prime] = False

    stop_time = time.time()

    print(f"Execution time: {round(stop_time - start_time)}s")
    print(f"Number of primes: {len(primes)}")
#    print(primes)
