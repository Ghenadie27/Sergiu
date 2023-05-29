from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message


app = Flask(__name__)
app.secret_key = "hello"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


app.config['DEBUG'] = True
app.config['TESTING'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
#app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
# app.config['MAIL_DEBUG'] = True
app.config['MAIL_USERNAME'] = 'pharmamix@gmail.com'
app.config['MAIL_PASSWORD'] = 'Car_4'
app.config['MAIL_DEFAULT_SENDER'] = 'pharmamix@gmail.com'
app.config['MAIL_MAX_EMAILS'] = None
# app.config['MAIL_SUPPRESS_SEND'] = False
app.config['MAIL_ASCII_ATTACHMENTS'] = False

mail = Mail(app)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        phone = request.form.get("phone")
        email = request.form.get("email")
        zip_code = request.form.get("zip_code")
        service = request.form.get("service")
        message = request.form.get('message')

        if not first_name or not last_name \
                or not phone or not email or not zip_code or not message:
            #flash("All Form Fields Required...")
            return render_template('contact.html', faulthandler=True)
        else:
            msg = Message(subject="Contractors",
                          sender="pharmamix27@gmail.com",
                          recipients=[f"{email}"])
            msg.body = f"Dear {first_name},\nThank you for interest in our services! " \
                       f"We will get back to you as soon as possible."
            mail.send(msg)

            msg_1 = Message(subject=f"Mail from {email}",
                            body=f"Name: {first_name, last_name}\nE-mail:"
                                                               f"{email}\nPhone: "
                                 f"{phone} Zip code: {zip_code}\n"
                                                               f"Service: "
                                 f"{service}\n\n{message}",
                            sender="pharmamix27@gmail.com",
                            recipients=["pharmamix27@gmail.com"])
            mail.send(msg_1)
            return render_template("contact.html", success=True)

    return render_template('contact.html')


@app.route('/gallery')
def gallery():
    return render_template('gallery.html')


if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host='0.0.0.0')