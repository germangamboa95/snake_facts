
import random
from fastapi import FastAPI

app = FastAPI()


facts: list[str]

with open("./facts.txt", "r") as f:
    facts = f.readlines()


@app.get("/")
def read_root():
    '''
    Free random fact about snakes
    '''
    return {"fact": facts[random.randint(0, len(facts) - 1)].strip()}
