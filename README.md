# 🤖 Question Answering API

## Thông tin sinh viên

|               |                  |
| ------------- | ---------------- |
| **Họ và tên** | [Nguyễn Đức Duy] |
| **MSSV**      | [24120294]       |
| **Môn học**   | Tư Duy Tính Toán |

---

## 📌 Model sử dụng

- **Tên model:** `deepset/roberta-base-squad2`
- **Link Hugging Face:** https://huggingface.co/deepset/roberta-base-squad2
- **Task:** Question Answering (Hỏi đáp)

---

## 📖 Mô tả hệ thống

API nhận vào một đoạn văn bản (`context`) và một câu hỏi (`question`), sau đó trả về câu trả lời được **trích xuất trực tiếp** từ đoạn văn bản đó.

---

## ⚙️ Cài đặt thư viện

```bash
pip install -r requirements.txt
```

---

## 🚀 Chạy chương trình

**Chạy local:**

```bash
uvicorn main:app --reload
```

**Chạy trên Google Colab:**
Mở file `notebook.ipynb` và chạy từng cell theo thứ tự.

---

## 📡 Hướng dẫn gọi API

### GET /

```bash
curl http://127.0.0.1:8000/
```

**Response:**

```json
{
  "name": "Question Answering API",
  "model": "deepset/roberta-base-squad2"
}
```

### GET /health

```bash
curl http://127.0.0.1:8000/health
```

**Response:**

```json
{
  "status": "ok",
  "model_loaded": true
}
```

### POST /predict

```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "context": "The Eiffel Tower was built in 1889 in Paris, France.",
    "question": "Where is the Eiffel Tower?"
  }'
```

**Response:**

```json
{
  "answer": "Paris, France",
  "score": 0.9823,
  "start": 38,
  "end": 51
}
```

---

## 🎬 Video Demo



https://github.com/user-attachments/assets/6dab1317-30ff-4494-aa4c-75dbe48f12e8

