from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

data = [
        {
        'id': 1,
        'name': 'User1',
        'email': 'user1@py.com',
        'age': 22,
        'gender': 'male',
    },
        {
        'id': 2,
        'name': 'User2',
        'email': 'user2@py.com',
        'age': 25,
        'gender': 'female',
    },

]

def find_person(person_id):
    for person in data:
        if person['id'] == person_id:
            return person
    return None

# get post put patch delete
class People(Resource):
    def get(self):
        return data
    def post(self):
        new_data = {
            'id': 3,
            'name': 'User3',
            'email': 'user3@py.com',
            'age': 25,
            'gender': 'male',
        } #new_data = request.json   # get from Postman
        data.append(new_data)
        return new_data, 201


class Person(Resource):
    def get(self,person_id):
        person = find_person(person_id)
        if person:
            return person, 200
        return {'message':'Person not found'}, 404
    def put(self,person_id):
        person = find_person(person_id)
        if person:
            person.update(request.json)
            return person
        return {'message':'Person not found'}, 404
    def delete(self,person_id):
        global data
        data = [person for person in data if person['id'] != person_id]
        return {'message':'Person deleted'}, 200


api.add_resource(People, '/people')
api.add_resource(Person, '/people/<int:person_id>')
if __name__ == '__main__':
    app.run(debug=True)







@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
