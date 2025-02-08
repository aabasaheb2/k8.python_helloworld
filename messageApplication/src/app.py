from flask import Flask, render_template, request, url_for, redirect
from bson.objectid import ObjectId
from pymongo import MongoClient
from urllib. parse import quote_plus
import variables

app = Flask(__name__, template_folder='templates')

# Create the mongodb client
#client = MongoClient('localhost', 27017)
uri= "mongodb://%s:%s@%s" % (quote_plus(variables.decodedUsername), quote_plus(variables.decodedPassword), 'mongodb-service:27017' )
client = MongoClient(uri)

#db = client.messagesDB # creating DB = messagesDB
db = client['messagesDB']
messagesCollection = db.messagesCollection # creating a collection to store messages"

# Get and Post Route
@app.route("/", methods=('GET', 'POST'))
def index():
    if request.method == "POST":
        message = request.form['message']
        messagesCollection.insert_one({'message': message})
        return redirect(url_for('index')) # redirect the user to home page
    allMessages = messagesCollection.find()
    return render_template('index.html', messagesCollection = allMessages) # get all messages from messagesDB table

#Delete Message
@app.post("/<id>/delete/")
def delete(id):
    messagesCollection.delete_one({"_id":ObjectId(id)})
    return redirect(url_for('index')) # redirecting to index.html using python's redirect method

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)
