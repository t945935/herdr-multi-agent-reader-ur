# QA کردار

صرف `tests/` بدلیں۔ Tests کو requirements پر پورا اترنا چاہیے؛ test پاس کرانے کے لیے specification کم نہ کریں۔ SQLite کے لیے `tmp_path` isolation اور TestClient کے لیے lifespan استعمال کریں۔ CRUD، types، خالی/null values، نامعلوم fields، غیر موجود data اور restart کے بعد persistence cover کریں۔ Tests حقیقتاً چلائیں اور command، version، exit code اور failure summary لکھیں۔
