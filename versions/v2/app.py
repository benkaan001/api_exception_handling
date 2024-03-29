from flask import Flask, jsonify, abort
from db import fetch_blogs, fetch_blog, NotAuthorizedError, NotFoundError
from create_db import create_database

app = Flask(__name__)

@app.route('/')
def say_hello():
    return 'Hello'

@app.route('/blogs')
def all_blogs():
    return jsonify(fetch_blogs())


# handle the high level errors
@app.route('/blogs/<id>')
def get_blog(id):
    try:
        return jsonify(fetch_blog(id))
    except NotFoundError:
        abort(404, description="Resource not found.")
    except NotAuthorizedError:
        abort(403, description="Access denied.")

if __name__ == "__main__":
    create_database()
    app.run()