from fastapi import FastAPI

# vytvoření instance aplikace
app = FastAPI(title="IGNI – správa účasti na akcích", version="0.1.0")


# základní route pro test
@app.get("/")
def read_root():
    return {"message": "Hello IGNI! 🚀"}
