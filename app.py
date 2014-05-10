from flask import Flask, Response, render_template, request, json, jsonify
from pymongo import MongoClient

# from mongokit import Connection, Document

# configuration
# MONGODB_HOST = 'localhost'
# MONGODB_PORT = 27017

app = Flask(__name__)
app.config.from_object(__name__)


# connection = Connection(app.config['MONGODB_HOST'], app.config['MONGODB_PORT'])
#
#
# def max_length(length):
#     def validate(value):
#         if len(value) <= length:
#             return True
#         raise Exception('%s must be at most %s characters long' % length)
#     return validate
#
# class User(Document):
#     structure = {
#         'name': unicode,
#         'handle': unicode
#     }
#     use_dot_notation = True
#     def __repr__(self):
#         return '<User %r>' % (self.name)
#
# # register the User document with our current connection
# connection.register([User])


def getJSON(js):
  return Response(js, status=200, mimetype='application/json')


@app.route('/')
def index():
  return render_template('index.html')

@app.route('/adduser')
def addUser():
  return render_template('add.html')


@app.route('/api/lang')
def aLang():
  js='{ "am":"Amharic", "ar":"Arabic", "bg":"Bulgarian", "bn":"Bengali", "bo":"Tibetan", "chr":"Cherokee", "da":"Danish", "de":"German", "dv":"Maldivian", "el":"Greek", "en":"English", "es":"Spanish", "fa":"Persian", "fi":"Finnish", "fr":"French", "gu":"Gujarati", "iw":"Hebrew", "hi":"Hindi", "hu":"Hungarian", "hy":"Armenian", "in":"Indonesian", "is":"Icelandic", "it":"Italian", "iu":"Inuktitut", "ja":"Japanese", "ka":"Georgian", "km":"Khmer", "kn":"Kannada", "ko":"Korean", "lo":"Lao", "lt":"Lithuanian", "ml":"Malayalam", "my":"Myanmar", "ne":"Nepali", "nl":"Dutch", "no":"Norwegian", "or":"Oriya", "pa":"Panjabi", "pl":"Polish", "pt":"Portuguese", "ru":"Russian", "si":"Sinhala", "sv":"Swedish", "ta":"Tamil", "te":"Telugu", "th":"Thai", "tl":"Tagalog", "tr":"Turkish", "ur":"Urdu", "vi":"Vietnamese", "zh":"Chinese" }'
  return getJSON(js)


@app.route('/api/stats')
def aUsersLang():
  mongoc = MongoClient(host = 'localhost')
  data = mongoc.natweet.tweets.aggregate({"$group": {"_id": "$lang", "count": {"$sum": 1}, "coords": {"$addToSet":"$coordinates.coordinates"}}})

  return getJSON(json.dumps(data))

# @app.route('/api/user', methods=['POST', 'GET'])
# def aUsers():
#   collection = connection.test.users
#
#   if request.method == 'POST':
#     user = collection.User()
#     user['name'] = request.form['user']
#     user['handle'] = request.form['handle']
#     user.save()
#     return "Success"
#
#   elif request.method == 'GET':
#     users = list(collection.find())
#     return "UserList:"+str(users)



if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0')
