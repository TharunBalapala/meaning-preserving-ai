from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.enhance import router as enhance_router

app = FastAPI(title="Meaning Preserving AI API")

# Enable CORS (important for frontend connection)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(enhance_router)