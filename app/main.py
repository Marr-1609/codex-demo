from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health():
    return {"ok": True}


@app.get("/sum")
def sum_endpoint(a: int, b: int):
    return {"sum": a + b}
