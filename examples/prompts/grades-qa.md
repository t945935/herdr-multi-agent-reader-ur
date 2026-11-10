# QA: grades system

`examples/grades.py` کا interface اور `tests/test_contracts.py` کے موجودہ grades cases پڑھیں۔ Contract کی آزادانہ جانچ کریں؛ code نہ بدلیں، موجود tests نہ حذف کریں، Developer کی self-review نہ پڑھیں، اور کوئی دوسرا Agent شروع نہ کریں۔

صرف `tests/test_grades_review.py` میں اضافہ یا تبدیلی کریں، اور report `reports/grade-qa.md` میں لکھیں۔ تین مضامین کا مجموعہ، 0／100／60 boundaries، bool／NaN／string، خالی data، نام، 1／1／3 برابر نمبر کی ranking، rounding سے پہلے precision اور input میں تبدیلی دیکھیے۔

pytest استعمال کریں۔ اگر موجودہ tests کسی case کو کافی طور پر cover کرتے ہیں تو پہلے وجہ بتائیں؛ صرف حقیقی کمی میں مفید test شامل کریں، بعینہٖ نقل نہ کریں۔ FastAPI، SQLite یا website CRUD نہ جانچیں؛ یہ grades task ہے۔

Tests حقیقتاً چلائیں اور command، exit code، findings اور نہ چلائے گئے checks محفوظ کریں۔ Manager کے شامل کردہ `task_id` اور `completion_path` کے مطابق receipt دیں؛ `artifacts` میں اپنی report اور test file درج کریں۔
