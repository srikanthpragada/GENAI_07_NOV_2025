# Products CRUD (SQLite)

Simple interactive CRUD CLI for a SQLite database `products.db`.

Table: `PRODUCTS` (pid INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price REAL, qty INTEGER)

Requirements
- Python 3 (stdlib only; uses `sqlite3`).

Run (PowerShell)

```powershell
python .\crud.py
```

Usage
- Add, list, update, get, and delete products via the interactive menu.
- All operations print exception messages and return to the menu on error.

Notes
- The database file `products.db` is created in the same directory on first run.
- For delete, you must type `DELETE` to confirm.
