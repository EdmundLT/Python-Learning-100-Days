from random import randint
from flask import Flask
app = Flask(__name__)
ran_number = randint(1, 10)
GIF = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"
high_gif = "https://media.giphy.com/media/BzyTuYCmvSORqs1ABM/giphy.gif"
low_gif = "https://media.giphy.com/media/3o6Zt481isNVuQI1l6/giphy.gif"
correct_gif = "https://media.giphy.com/media/ICOgUNjpvO0PC/giphy.gif"


@app.route('/')
def main():
    return f"<h1>Guess a number between 0 and 9</h1>" \
        f'<img src="{GIF}">'


@app.route('/<int:id>')
def check_answer(id):
    if id < ran_number:
        return f"<h1 style='color: 'red''>Too low, try again!</h1>" \
            f'<img src="{low_gif}">'
    if id > ran_number:
        return f"<h1 style='color: 'purple''>Too high, try again!</h1>" \
            f'<img src="{high_gif}">'
    if id == ran_number:
        return f"<h1 style='color: 'purple''>You found me!</h1>" \
            f'<img src="{correct_gif}">'


if __name__ == "__main__":
    app.run(debug=True)
