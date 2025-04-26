from math import factorial

from fastapi import FastAPI

app = FastAPI()


@app.get("/challenges/solution-1")
def solution_1(n: int):

    total = 0
    for i in range(n//2 + 1):
        total += factorial(n-i) // (factorial(i) * factorial(n - 2 * i))

    return total  # {"result": n * 2}
