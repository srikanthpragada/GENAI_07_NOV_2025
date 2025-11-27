"""CRUD CLI for products stored in SQLite `products.db`.

Table: PRODUCTS(pid INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price REAL, qty INTEGER)

Run `python crud.py` to start the interactive menu.
All operations display exception messages and the CLI resumes after errors.
"""
import sqlite3
import sys
import traceback

DB_PATH = "products.db"


def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    try:
        with get_conn() as conn:
            conn.execute(
                """
				CREATE TABLE IF NOT EXISTS PRODUCTS (
					pid INTEGER PRIMARY KEY AUTOINCREMENT,
					name TEXT NOT NULL,
					price REAL NOT NULL,
					qty INTEGER NOT NULL
				)
				"""
            )
    except Exception as e:
        print(f"[init_db] Exception: {e}")
        traceback.print_exc()


def add_product(name, price, qty):
    try:
        with get_conn() as conn:
            cur = conn.execute(
                "INSERT INTO PRODUCTS (name, price, qty) VALUES (?, ?, ?)",
                (name, price, qty),
            )
            pid = cur.lastrowid
            print(f"Product added with pid={pid}")
            return pid
    except Exception as e:
        print(f"[add_product] Exception: {e}")
        traceback.print_exc()
        return None


def get_product(pid):
    try:
        with get_conn() as conn:
            cur = conn.execute("SELECT * FROM PRODUCTS WHERE pid = ?", (pid,))
            row = cur.fetchone()
            return dict(row) if row else None
    except Exception as e:
        print(f"[get_product] Exception: {e}")
        traceback.print_exc()
        return None


def list_products():
    try:
        with get_conn() as conn:
            cur = conn.execute("SELECT * FROM PRODUCTS ORDER BY pid")
            rows = cur.fetchall()
            return [dict(r) for r in rows]
    except Exception as e:
        print(f"[list_products] Exception: {e}")
        traceback.print_exc()
        return []


def update_product(pid, name=None, price=None, qty=None):
    try:
        fields = []
        vals = []
        if name is not None:
            fields.append("name = ?")
            vals.append(name)
        if price is not None:
            fields.append("price = ?")
            vals.append(price)
        if qty is not None:
            fields.append("qty = ?")
            vals.append(qty)
        if not fields:
            print("No fields to update")
            return False
        vals.append(pid)
        sql = f"UPDATE PRODUCTS SET {', '.join(fields)} WHERE pid = ?"
        with get_conn() as conn:
            cur = conn.execute(sql, tuple(vals))
            if cur.rowcount == 0:
                print(f"No product with pid={pid} found")
                return False
            print(f"Product pid={pid} updated")
            return True
    except Exception as e:
        print(f"[update_product] Exception: {e}")
        traceback.print_exc()
        return False


def delete_product(pid):
    try:
        with get_conn() as conn:
            cur = conn.execute("DELETE FROM PRODUCTS WHERE pid = ?", (pid,))
            if cur.rowcount == 0:
                print(f"No product with pid={pid} found")
                return False
            print(f"Product pid={pid} deleted")
            return True
    except Exception as e:
        print(f"[delete_product] Exception: {e}")
        traceback.print_exc()
        return False


def input_with_validation(prompt, cast_func, allow_empty=False):
    while True:
        try:
            raw = input(prompt).strip()
            if allow_empty and raw == "":
                return None
            val = cast_func(raw)
            return val
        except Exception as e:
            print(f"Input error: {e}")
            print("Please try again.")


def menu():
    print("\nProducts CRUD CLI")
    print("1) Add product")
    print("2) Get product by pid")
    print("3) List products")
    print("4) Update product")
    print("5) Delete product")
    print("0) Exit")


def run_cli():
    init_db()
    while True:
        try:
            menu()
            choice = input_with_validation("Select option: ", int)
            if choice == 1:
                name = input_with_validation("Name: ", str)
                price = input_with_validation("Price: ", float)
                qty = input_with_validation("Qty: ", int)
                add_product(name, price, qty)
            elif choice == 2:
                pid = input_with_validation("pid: ", int)
                p = get_product(pid)
                if p:
                    print(p)
                else:
                    print("Product not found")
            elif choice == 3:
                products = list_products()
                if products:
                    for p in products:
                        print(p)
                else:
                    print("No products found")
            elif choice == 4:
                pid = input_with_validation("pid to update: ", int)
                print("Leave a value empty to keep current")
                name = input_with_validation(
                    "New name: ", str, allow_empty=True)
                price = input_with_validation("New price: ", lambda s: float(
                    s) if s != "" else None, allow_empty=True)
                qty = input_with_validation("New qty: ", lambda s: int(
                    s) if s != "" else None, allow_empty=True)
                update_product(pid, name=name, price=price, qty=qty)
            elif choice == 5:
                pid = input_with_validation("pid to delete: ", int)
                confirm = input_with_validation(
                    "Type DELETE to confirm: ", str)
                if confirm == "DELETE":
                    delete_product(pid)
                else:
                    print("Delete cancelled")
            elif choice == 0:
                print("Bye")
                break
            else:
                print("Unknown option")
        except KeyboardInterrupt:
            print("\nInterrupted. Returning to menu.")
            continue
        except Exception as e:
            print(f"[run_cli] Exception: {e}")
            traceback.print_exc()
            print("Operation failed — returning to menu.")


if __name__ == "__main__":
    try:
        run_cli()
    except Exception as e:
        print(f"Fatal error: {e}")
        traceback.print_exc()
        sys.exit(1)
