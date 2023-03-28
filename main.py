
import random
from fastapi import FastAPI

app = FastAPI()


facts: list[str]

with open("./facts.txt", "r") as f:
    facts = f.readlines()


@app.get("/:id")
def read_root(id: int):
    '''
    Fact about snakes
    '''
    return {id: id, "fact": facts[id + 1].strip()}


@app.get("/random")
def get_random():
    '''
    Free random fact about snakes
    '''
    id = random.randint(0, len(facts) - 1)
    return {id: id, "fact": facts[id].strip()}
