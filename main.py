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

@app.route("/discussions")
def render_discussions_site():
    return render_template('discussions.html')

@app.route("/discussion")
def render_discussion_site():
    return render_template('discussion.html')


@app.route("/live")
def render_live_site():
    return render_template('live.html')

@app.route("/profile")
def render_profile_site():
    return render_template('profile.html')

@app.route("/profile-email")
def render_profile_email_site():
    return render_template('profile-email.html')

@app.route("/inbox")
def render_inbox_site():
    return render_template('inbox.html')

@app.route("/message")
def render_message_site():
    return render_template('message.html')


@app.route("/sendMessage")
def render_send_message_site():
    return render_template('sendMessage.html')
if __name__ == "__main__":
    app.run()
