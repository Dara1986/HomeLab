from fastapi import FastAPI

app = FastAPI()
items = []


@app.get("/")
def root():
    return {"Hello": "World"}


@app.post("/items")
def create_item(item: str):
    items.append(item)
    return items


@app.get("/zahl")
def count_item():
    return f"Es befinden sich genau {len(items)} Items in der Liste"


@app.get("/liste")
def show_item():
    if len(items) > 10:
        return "zu viele"
    else:
        return str(items)


@app.delete("/del")
def delete_item():
    if len(items) > 0:
        return items.pop(0)
    else:
        return "leer"


