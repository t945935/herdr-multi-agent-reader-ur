# اردو Reader Resources

یہ اردو edition کا companion package ہے۔ Happy eBook نے اردو ترجمہ اور ان companion resources کی عوامی تقسیم کی اجازت کی تصدیق کی ہے؛ تاہم اس package کو کتاب کے ساتھ فراہم کردہ مواد کے طور پر استعمال کیا جائے گا، اور اس سے کوئی وسیع open-source license نہیں ملتا۔

## تقاضے

- WSL2／Ubuntu یا مناسب Linux terminal، Python 3.12 اور dependencies نصب کرنے کے لیے network access۔
- حقیقی Herdr tasks کے لیے Herdr TUI اور پہلے سے configured/signed-in Agent CLI۔ Reference tests کو model account درکار نہیں۔

## v1.0.0 حاصل کرنا

- Release page: https://github.com/t945935/herdr-multi-agent-reader-ur/releases/tag/v1.0.0
- ZIP: https://github.com/t945935/herdr-multi-agent-reader-ur/releases/download/v1.0.0/herdr-multi-agent-reader-ur.zip
- SHA-256 list: https://github.com/t945935/herdr-multi-agent-reader-ur/releases/download/v1.0.0/SHA256SUMS.txt

یہ links release شائع ہونے کے بعد فعال ہوں گے۔ SHA-256 کی اصل قدر اسی release asset کی `SHA256SUMS.txt` سے لیں۔

## نصب اور tests

Commands کو اس directory سے چلائیں جس میں `examples/` اور `tests/` ہوں:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m pytest -q tests
.venv/bin/python -m examples.pipeline
```

پیکیج میں API names، JSON keys، CLI commands اور external library outputs کو جہاں ضروری ہو اصل شکل میں رکھا گیا ہے۔ Tests کا حقیقی output ہی نتیجہ ہے۔

`fonts/` میں Noto Nastaliq Urdu اور SIL Open Font License 1.1 موجود ہیں؛ فونٹ کتاب/reader package کے اندر embed ہو سکتا ہے۔ یہ فونٹ لائسنس باقی کتاب یا reader code کی عوامی تقسیم کی اجازت نہیں دیتا۔
