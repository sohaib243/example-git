from flask import Flask ,request ,jsonify
from storage_utility import load_books , update_books
app= Flask(__name__)

books: list = load_books("books.json")

@app.route("/api/v1/books",methods =['GET,POST'])

def handle_books():
    if request.method == 'GET ':
        return jsonify(books)
    elif  request.method == 'POST':
        new_books = request.get.json()
        new_id = max(book['id'] for book in books) + 1  
        new_books['id'] =new_id
        books.append(new_books)
        update_books(books)
        return jsonify(new_books) ,201
def find_by_id(book_id :int):
    result = None
    for book in books:
        if book.get('id') == book_id:
         result = book
         break
        return result


@app.route("/api/v1/books/<int:book_id>",methods =['PUT'])
def handle_book_update(book_id):
        book :dict = find_by_id(book_id)
        if book is None :
            return jsonify({""" the request book not found 
                            Status : 404 """}) 
        new_data = request.get_json()
        book.update(new_data)
        update_books(books)
        return jsonify(book)
@app.route("/api/v1/books/<int:book_id>")
def handle_delete_book():     
        
if __name__ =="__main__":
    app.run(debug=True)