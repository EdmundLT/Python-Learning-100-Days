from flask import Flask, render_template, request
import requests
from post import Post
POST_API = "https://api.npoint.io/d14c88782d9869af3a7b"
app = Flask(__name__)
response = requests.get(POST_API)
post_list = response.json()


@app.route('/')
def main():
    return render_template("index.html", all_posts=post_list)


@app.route('/index.html')
def home():
    return render_template("index.html", all_posts=post_list)


@app.route('/about.html')
def about():
    return render_template("about.html")


@app.route("/contact.html", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        from sendmail import send_mail
        send_mail(data)
        return render_template("contact.html", success="Successfully sent your message!")
    return render_template("contact.html")


@app.route('/post.html')
def post():
    return render_template("post.html")


@app.route('/post.html/<int:post_id>')
def spec_post(post_id):
    for x in post_list:
        if x["id"] == post_id:
            post = Post(post_id=x["id"], title=x["title"],
                        subtitle=x["subtitle"], body=x["body"])
    return render_template("post.html", post_obj=post, id=post_id)


if __name__ == "__main__":
    app.run(debug=True)
