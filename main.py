from flask import Flask, render_template
app = Flask(__name__)

@app.route("/public")
def render_public_site():
    return render_template('public.html')

@app.route("/")
def render_login_site():
    return render_template('login.html')

@app.route("/signup")
def render_signup_site():
    return render_template('signup.html')


@app.route("/dashboard")
def render_dashboard_site():
    return render_template('dashboard.html')

@app.route("/courseMat")
def render_course_material_site():
    return render_template('course-material.html')

@app.route("/submissions")
def render_submissions_site():
    return render_template('submissions.html')

@app.route("/submission")
def render_submission_site():
    return render_template('submission.html')
if __name__ == "__main__":
    app.run()
