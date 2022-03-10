from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/bye')
def bye():
    return "bye!"


if __name__ == "__main__":
    app.run()

# from time import sleep


# def decorator_function(function):
#     def wrapper_function():
#         sleep(2)
#         function()
#     return wrapper_function

# @decorator_function
# def say_hello():
#     print("hello")


# def say_bye():
#     print("bye")


# def say_greeting():
#     print("how are you")
