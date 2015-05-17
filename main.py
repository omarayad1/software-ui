from flask import Flask, render_template
app = Flask(__name__)

@app.route("/public")
def render_public_site():
    return render_template('public.html')

if __name__ == "__main__":
    app.run()
