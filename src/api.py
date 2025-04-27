from math import factorial

import numpy as np
from fastapi import FastAPI
from scipy.optimize import linear_sum_assignment


def create_app() -> FastAPI:

    app = FastAPI(docs_url="/swagger")

    @app.get("/challenges/solution-1")
    def solution_1(n: int):

        total = 0
        for i in range(n//2 + 1):
            total += factorial(n-i) // (factorial(i) * factorial(n - 2 * i))

        return total

    @app.get("/challenges/solution-2")
    def solution_2(n: int):

        total = 0
        good = set()
        bad = set()
        for i in range(1, n+1):
            visited = set()
            num = i
            while num not in visited and num != 89:
                visited.add(num)

                if num in good:
                    good |= visited
                    num = 89
                    break
                if num in bad:
                    bad |= visited
                    break

                num = sum(map(lambda c: int(c)**2, str(num)))

            if num == 89:
                total += 1
                good |= visited
            else:
                bad |= visited

        return total

    @app.post("/challenges/solution-3")
    def solution_3(data: list[list[int]]):
        matrix = np.array(data)

        cost = matrix.sum(axis=1, keepdims=True) - matrix

        filas, cols = linear_sum_assignment(cost)
        min_moves = cost[filas, cols].sum()

        return int(min_moves)

    return app
