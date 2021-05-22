from flask import Flask, render_template,request
import requests
import smtplib

MY_EMAIL = "testapp.09@yahoo.com"
MY_PASSWORD = "quczzzokfoulmwlg"

app = Flask(__name__)
response = requests.get(url="https://api.npoint.io/0067e63917ca7a5034d9")
posts = response.json()

@app.route("/")
def home_page():
    return render_template("index.html", all_posts=posts )

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/contact", methods=['POST', 'GET'])
def contact_page():
    if request.method == "POST":
        data = request.form
        # name = data["name"]
        # email = data["email"]
        # phone = data["phone"]
        # message = data["message"]
        send_mail(data['name'], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


@app.route("/post/<int:index>")
def post_page(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


def send_mail(name, email, phone, message):
    email_msg = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="raghavkavimandan23@gmail.com",msg=email_msg)







# @app.route("/form-entry", methods=['POST', 'GET'])
# def receive_data():
#     if request.method == "POST":
#         return "<h1> Successfully sent your message</h1>"
#


if __name__ == "__main__":
    app.run(debug=True)