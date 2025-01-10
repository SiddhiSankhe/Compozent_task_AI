from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# In-memory database for books
books = []

@app.route('/')
def home_page():
    return render_template("index.html")

# Get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({"books": books})

# Get a book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({"error": "Book not found"}), 404

# Add a new book
@app.route('/books', methods=['POST'])
def add_book():
    data = request.json
    book_id = len(books) + 1
    book = {
        "id": book_id,
        "title": data.get("title"),
        "author": data.get("author"),
        "published_year": data.get("published_year"),
        "genre": data.get("genre"),
        "available": True  # Default availability
    }
    books.append(book)
    return jsonify(book), 201

# Update a book's details
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.json
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        book["title"] = data.get("title", book["title"])
        book["author"] = data.get("author", book["author"])
        book["published_year"] = data.get("published_year", book["published_year"])
        book["genre"] = data.get("genre", book["genre"])
        book["available"] = data.get("available", book["available"])
        return jsonify(book)
    return jsonify({"error": "Book not found"}), 404

# Delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book["id"] != book_id]
    return jsonify({"message": "Book deleted"})

if __name__ == "__main__":
    app.run(debug=True, port=8000)
