from flask_math.calculation.common.NEWTON_METHOD import NEWTON_METHOD
from flask import flash


def Sieve_of_Eratosthenes(N):
    try:
        N = int(N)
        if N >= 2:
            List = list(range(2, N + 1))
            prime_List = []

            MIN = 0
            while MIN < NEWTON_METHOD(N):
                MIN = min(List)
                prime_List.append(MIN)
                List = [i for i in List if i % MIN != 0]
            prime_List = prime_List + List

            n = 15
            Anser = ["Prime numbers less than or equal to " + str(N)]
            for i in range(len(prime_List) // n + 1):
                Anser.append(prime_List[n * i:n * i + n])
        else:
            Anser = ["Error"]
            flash("Error: Please enter a natural number greater than or equal to 2")
    except:
        Anser = ["Error"]
        flash("Error: Please re-enter the input")
    return Anser
