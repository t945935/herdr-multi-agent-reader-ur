# Database کردار

صرف `examples/task_manager/db.py` بدلیں۔ `init_db`، `get_tasks`، `get_task`، `create_task`، `update_task`، `delete_task` فراہم کریں۔ Tests میں `DB_PATH` بدلنے کے قابل ہو؛ connections بند ہوں، writes transaction میں ہوں، values کے لیے parameterized SQL ہو۔ Dynamic column name مقررہ allowlist سے لیں۔ عدم موجودگی پر `None`／`False` کے معنی واضح رکھیں؛ database exception کو خالی list ظاہر نہ کریں۔
