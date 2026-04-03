import requests

API_URL = "http://127.0.0.1:8000"

# ── Test 1: GET / ───────────────────────────────────────────
print("=" * 50)
print("TEST 1: GET /")
response = requests.get(f"{API_URL}/")
print(response.json())

# ── Test 2: GET /health ─────────────────────────────────────
print("\n" + "=" * 50)
print("TEST 2: GET /health")
response = requests.get(f"{API_URL}/health")
print(response.json())

# ── Test 3: POST /predict (câu hỏi về lịch sử) ─────────────
print("\n" + "=" * 50)
print("TEST 3: POST /predict - Câu hỏi về lịch sử")
payload = {
    "context": "The Eiffel Tower is a wrought-iron lattice tower on the Champ de Mars in Paris, France. It was constructed from 1887 to 1889 as the centerpiece of the 1889 World's Fair.",
    "question": "When was the Eiffel Tower built?",
}
response = requests.post(f"{API_URL}/predict", json=payload)
print(response.json())

# ── Test 4: POST /predict (câu hỏi về khoa học) ────────────
print("\n" + "=" * 50)
print("TEST 4: POST /predict - Câu hỏi về khoa học")
payload = {
    "context": "Water is a transparent, tasteless, odorless, and nearly colorless chemical substance. Its chemical formula is H2O meaning each molecule contains one oxygen and two hydrogen atoms.",
    "question": "What is the chemical formula of water?",
}
response = requests.post(f"{API_URL}/predict", json=payload)
print(response.json())

# ── Test 5: POST /predict - Lỗi thiếu context ──────────────
print("\n" + "=" * 50)
print("TEST 5: POST /predict - Lỗi thiếu context")
payload = {"context": "", "question": "What is the capital of France?"}
response = requests.post(f"{API_URL}/predict", json=payload)
print(f"Status: {response.status_code}")
print(response.json())
