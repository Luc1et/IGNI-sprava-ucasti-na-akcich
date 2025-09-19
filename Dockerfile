# Používám oficiální Python image
FROM python:3.12-slim

# Nastavím pracovní adresář
WORKDIR /app

# Zkopíruju requirements a nainstaluju závislosti
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Zkopíruju celý projekt
COPY . .

# Spustím aplikaci přes uvicorn
CMD ["python", "-m", "uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
