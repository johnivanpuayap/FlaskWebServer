from flask import Flask

app = Flask(__name__)


# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"


# Adding Different Routes using the app.route decorator
@app.route("/bye")
def bye():
    return "<p>Bye!</p>"


# Creating Variables
@app.route("/<name>")
def greet(name):
    return f"<p>Hello there, {name.capitalize()}!</p>"


# Render HTML and Add Inline Style
@app.route("/")
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph.</p>' \
           '<img' \
           '    src="https://www.vets4pets.com/siteassets/species/cat/kitten/tiny-kitten-in-sunlight.jpg?w=585&scale=down' \
           '    alt="picture of a kitten' \
           '    width="300px' \
           '/>' \
           '<div style="width: 100%; height: 0; padding-bottom: 99%; position: relative">' \
           '    <iframe' \
           '        src="https://giphy.com/embed/3oriO0OEd9QIDdllqo"' \
           '        width="100%"' \
           '        height="100%"' \
           '        style="position: absolute"' \
           '        frameborder="0"' \
           '        class="giphy-embed"' \
           '        allowfullscreen' \
           '    ></iframe>' \
           '</div>' \
           '<p>' \
           '    <a href="https://giphy.com/gifs/jerseydemic-3oriO0OEd9QIDdllqo">via GIPHY</a>' \
           '</p>'


# Run the server without using the terminal
if __name__ == "__main__":
    app.run(debug=True)
