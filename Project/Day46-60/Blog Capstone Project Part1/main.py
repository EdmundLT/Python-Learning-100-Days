from flask import Flask, render_template
import requests

from post import Post
blog_url = "https://api.npoint.io/c790b4d5cab58020d391"

app = Flask(__name__)
response = requests.get(blog_url)
all_posts = response.json()


@app.route('/')
def home():
    return render_template("index.html", blog_list=all_posts)


@app.route('/blog/<int:post_id>')
def get_post(post_id):

    for x in all_posts:
        if x["id"] == post_id:
            post = Post(post_id=x["id"], title=x["title"],
                        subtitle=x["subtitle"], body=x["body"])
    return render_template("post.html", post_obj=post)


if __name__ == "__main__":
    app.run(debug=True)
