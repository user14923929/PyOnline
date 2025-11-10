# 🐍 PyOnline

**PyOnline** is a simple online Python interpreter built with Flask.  
It allows you to write and test Python code directly in your browser — no installation required.

---

## 🚀 Features

- Run Python code in an isolated environment (`exec` with restricted builtins)
- Display output and errors in the browser
- Clean and minimal web interface (HTML + Flask)
- Works on both 32-bit and 64-bit systems
- Supports Python 3.8 and higher

---

## 🧰 Requirements

- Python **3.8+**
- Flask **3.0+** *(or Flask 2.3.x for Python 3.7)*

---

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/user14923929/PyOnline.git
   cd PyOnline
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   *(or manually)*  
   ```bash
   pip install flask
   ```

3. Make sure `index.html` is in the same directory as `main.py`.

---

## ▶️ Run

```bash
python main.py
```

Then open your browser and visit:

👉 **http://127.0.0.1:5000/**

---

## ⚙️ Settings

In `main.py` you can enable debugging:
```python
DEBUG = False
```
Set it to `True` if you want to see detailed error logs.

---

## 🧠 How It Works

PyOnline reads Python code from the HTML form and executes it using:
```python
exec(code)
```
Output and errors are captured via `contextlib.redirect_stdout` and `StringIO`,  
then displayed back in the browser.

---

## ⚠️ Security Warning

Using `exec()` can be dangerous in public environments.  
This project is intended for **local or educational use only**.  
If you plan to deploy it online, use proper sandboxing (e.g. Docker, subprocess isolation, limited permissions).

---

## 📄 License

This project is released under the **MIT License**.  
Feel free to use and modify it.

---

### 💬 Author

**user14923929**  
Created for educational purposes to demonstrate a simple web-based Python interpreter.
