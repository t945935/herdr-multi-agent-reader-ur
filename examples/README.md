# مثالوں کا مجموعہ

تمام commands extracted project root سے چلائیں؛ package imports میں `examples.*` استعمال ہوتا ہے۔

Grades exercise کے prompts `prompts/grades-developer.md` اور `prompts/grades-qa.md` ہیں؛ `prompts/qa.md` website کے لیے مخصوص ہے۔ Reference version محفوظ رکھنے کی خاطر Agent سے اپنی مشقی copy میں کام کرائیں۔

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m pytest -q tests
.venv/bin/python -m examples.pipeline
```

| باب | آغاز کی file | قبولیت |
|---|---|---|
| 1 | `calculator.py` | بنیادی ریاضی، صفر سے تقسیم اور types |
| 2 | `grades.py` | score boundaries، مضمون کی کمی، برابر نمبر کی competition ranking |
| 3 | `../scripts/probe_herdr.py --live` | نیا shell Pane، run/read/wait اور cleanup |
| 4 | `../scripts/team.py` | مرحلہ وار dispatch، منفرد task ID، artifacts کی جانچ |
| 5 | `prompts/reviewer-a.md`، `reviewer-b.md` | دو آزاد reviews اور Manager کا فیصلہ |
| 6 | `handoff.py` | file موجودگی، project scope اور SHA-256 |
| 7 | `task_manager/` | CRUD، validation، static page، restart persistence |
| 8 | `research.py` | claims، sources، quotes اور uncertainty status |
| 9 | `pipeline.py` | exit code، timeout، acceptance اور ناکامی پر رکنا |
| 10 | `queue.py` | duplicate submission، lease، restart recovery، dead letter اور concurrency |

Website شروع کریں:

```bash
.venv/bin/python -m uvicorn examples.task_manager.main:app --host 0.0.0.0 --port 8000
```

Browser میں `http://localhost:8000/` کھولیں۔ عام مشق کا data `examples/data/tasks.db` میں محفوظ ہوتا ہے؛ خودکار tests عارضی directory استعمال کرتے ہیں اور اس database کو نہیں چھوتے۔

Background queue example محدود تعداد میں خالص حسابی کام کرتا ہے، کوئی paid model استعمال نہیں کرتا۔ حقیقی model dispatch صرف `scripts/team.py` سے ہوتا ہے؛ پہلے متعلقہ CLI نصب کرکے sign-in کریں۔
