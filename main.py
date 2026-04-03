from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import pipeline

# ── App setup ──────────────────────────────────────────────
app = FastAPI(
    title="Question Answering API",
    description="API để trả lời câu hỏi dựa trên đoạn văn bản cho trước, sử dụng model deepset/roberta-base-squad2.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Load model (chỉ load 1 lần khi khởi động) ──────────────
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

# ── Threshold ──────────────────────────────────────────────
CONFIDENCE_THRESHOLD = 0.25


# ── Schema ─────────────────────────────────────────────────
class QARequest(BaseModel):
    context: str
    question: str


# ── Endpoints ──────────────────────────────────────────────
@app.get("/")
def root():
    return {
        "name": "Question Answering API",
        "description": "Nhận vào một đoạn văn bản (context) và một câu hỏi (question), trả về câu trả lời được trích xuất từ đoạn văn.",
        "model": "deepset/roberta-base-squad2",
        "endpoints": {
            "GET  /": "Thông tin API",
            "GET  /health": "Kiểm tra trạng thái hệ thống",
            "POST /predict": "Trả lời câu hỏi từ đoạn văn bản",
        },
    }


@app.get("/health")
def health():
    return {"status": "ok", "model_loaded": qa_pipeline is not None}


@app.post("/predict")
def predict(body: QARequest):
    # Validate input
    if not body.context or not body.context.strip():
        raise HTTPException(status_code=400, detail="'context' không được để trống.")
    if not body.question or not body.question.strip():
        raise HTTPException(status_code=400, detail="'question' không được để trống.")
    if len(body.context) > 5000:
        raise HTTPException(
            status_code=400, detail="'context' không được vượt quá 5000 ký tự."
        )

    # Run model
    try:
        result = qa_pipeline(question=body.question, context=body.context)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi khi chạy model: {str(e)}")

    # Confidence check
    confident = result["score"] >= CONFIDENCE_THRESHOLD
    answer = result["answer"] if confident else "I'm not sure about this answer."

    return {
        "answer": answer,
        "score": round(result["score"], 4),
        "start": result["start"],
        "end": result["end"],
        "confident": confident,
    }
