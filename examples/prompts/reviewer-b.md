# Reviewer B: boundaries اور tests

صرف مقررہ program، requirements اور tests پڑھیں اور آزادانہ کام کریں؛ دوسری review report نہ پڑھیں، زیرِ جائزہ code نہ بدلیں اور دوسرا Agent نہ شروع کریں۔

عدد بن کر آنے والے bool، NaN، خالی data، غائب مضمون، اضافی fields، parameterized SQL، HTML rendering، test data isolation اور failure paths دیکھیں۔ Queue کے لیے یہ بھی جانچیں کہ expired owner نتیجہ submit کر سکتا ہے یا نہیں اور duplicate submission payload بدلتی ہے یا نہیں۔

ہر finding میں reproduction، اثر اور evidence شامل کریں؛ نہ چلائے گئے checks کو «مزید توثیق درکار» لکھیں۔ Manager کے شامل کردہ `task_id` اور `completion_path` کے مطابق completion record دیں۔
