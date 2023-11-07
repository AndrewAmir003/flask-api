from application import app, db # This app is not the app.py but the app used in __init__.py
from flask import request, jsonify
from application.models import FriendsCharacter

def format_character(character):
    return {
        'name': character.name,
        'age': character.age,
        'catch_phrase': character.catch_phrase
    }

@app.route('/') # Home route
def hello_world():
    return '<p>Hello World!!!</p>'

@app.route('/characters', methods=['POST'])
def create_character():
    data = request.json
    
    if not data:
        return jsonify(error = 'NO JSON DATA'), 400
    
    try:
        character = FriendsCharacter(data['name'], 
        data['age'], 
        data['catch_phrase']
        )

        db.session.add(character)
        db.session.commit()

        return jsonify(id=character.id, 
        name=character.name, 
        age=character.age, 
        catch_phrase=character.catch_phrase
        ), 201 # return data to users using key value pairs

    except Exception as e:
        return jsonify(error = 'Failed to create the character'), 500

@app.route('/characters', methods=['GET']) # GET ROUTE
def get_characters():
    characters = FriendsCharacter.query.all()
    character_list = [format_character(character) for character in characters]
    return jsonify(Characters=character_list)
    
    # for character in characters:
    #     character_list.append(format_character(character))
    # return {
    #     'Character': character_list
    # }

@app.route('/characters/<id>', methods=['GET'])
def get_character(id): 
    character = FriendsCharacter.query.filter_by(id=id).first() # Return first of a potentially larger result
    
    if character is None:
        return jsonify('Character cannot be found'), 404
    
    return jsonify(id=character.id, name=character.name, age=character.age, catch_phrase=character.catch_phrase)

@app.route('/characters/<id>', methods=['DELETE']) # DELETE ROUTE
def delete_character(id):
    character = FriendsCharacter.query.filter_by(id=id).first()
    db.session.delete(character)
    db.session.commit()
    return 'Character Deleted'

@app.route('/characters/<id>', methods=['PATCH']) # UPDATE ROUTE
def update_character(id):
    character = FriendsCharacter.query.filter_by(id=id)
    data = request.json
    character.update(dict(name=data['name'], age=data['age'], catch_phrase=data['catch_phrase']))
    db.session.commit()
    updatedCharacter = character.first()
    return jsonify(id=updatedCharacter.id, name=updatedCharacter.name, age=updatedCharacter.age, catch_phrase=updatedCharacter.catch_phrase)
