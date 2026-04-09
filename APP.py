from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# MongoDB Atlas connection
client = MongoClient("mongodb+srv://JUNAITH:junaith17092006@cluster0.i5odykk.mongodb.net/")
db = client['notesdb']
collection = db['notes']

# Home route (READ)
@app.route('/')
def home():
    all_notes = collection.find()
    return render_template('index.html', notes=all_notes)

# Add note (CREATE)
@app.route('/add', methods=['POST'])
def add_note():
    note = request.form['note']
    collection.insert_one({"note": note})
    return redirect('/')   # 🔥 FIX (no duplication)

# Delete note (DELETE)
@app.route('/delete/<id>')
def delete_note(id):
    collection.delete_one({"_id": ObjectId(id)})
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)