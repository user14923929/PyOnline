from flask import Flask, request, render_template_string
import io
import contextlib

app = Flask(__name__)
DEBUG = False # If there are problems with the program, then install the location and replace False with True.

with open("index.html", encoding="utf-8") as file:
    HTML_PAGE = file.read()

@app.route("/", methods=["GET", "POST"])
def index():
    code = request.form.get("code", """# TODO: Enter Python code here\nprint("Create and test programs on the python (not cython) with PyOnline!")""")
    output = None

    if request.method == "POST":
        buffer = io.StringIO()
        try:
            with contextlib.redirect_stdout(buffer), contextlib.redirect_stderr(buffer):
                # You are safety, baby!
                exec(code, {"__builtins__": {"print": print, "range": range, "len": len}})
        except Exception as e:
            print("Error:", e, file=buffer)
        output = buffer.getvalue()

    return render_template_string(HTML_PAGE, code=code, output=output)

if __name__ == "__main__":
    app.run(debug=DEBUG)
