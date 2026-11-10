# Developer: grades contract

`examples/grades.py` اور `tests/test_contracts.py` کے grades cases پڑھیں۔ صرف `examples/grades.py` بدلیں؛ موجود tests، website code نہ بدلیں اور دوسرا Agent نہ بنائیں۔

Contract: مضامین عین اردو، انگریزی، ریاضی ہوں؛ score محدود قدر والا `int`／`float` ہو اور `bool`، string، غائب／اضافی مضمون یا 0–100 سے باہر قدر رد ہو۔ Average 60 پر کامیابی ہے؛ خالی student list خالی list دے؛ اصل rounding سے پہلے کے total پر برابر نمبر کی competition ranking ہو اور ان کی input ترتیب برقرار رہے؛ input تبدیل نہ ہو۔

`calculate_total`، `calculate_average`، `get_grade`، `rank_students` interfaces برقرار رکھیں۔ پہلے contract جانچیں اور صرف ضرورت پر اصلاح کریں؛ اگر پہلے ہی درست ہو تو code برقرار رکھیں اور نتیجہ بتائیں، محض فرق پیدا کرنے کے لیے rewrite نہ کریں۔

`.venv/bin/python -m pytest -q tests/test_contracts.py -k 'ranking or scores'` سے تصدیق کریں۔ حقیقی command، exit code، بدلی files اور باقی امور `reports/grade-developer.md` میں لکھیں۔ Manager کے شامل کردہ `task_id` اور `completion_path` کے مطابق completion receipt بھی دیں۔
