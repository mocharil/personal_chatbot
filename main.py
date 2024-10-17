from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Inisialisasi aplikasi FastAPI
app = FastAPI()

# Konfigurasi CORS untuk mengizinkan semua origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Mengizinkan semua origin
    allow_credentials=True,
    allow_methods=["*"],  # Mengizinkan semua metode HTTP
    allow_headers=["*"],  # Mengizinkan semua header
)

# Contoh endpoint sederhana
@app.get("/")
async def read_root():
    return {"message": "Welcome to my simple API with CORS enabled"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id, "description": f"This is item {item_id}"}

