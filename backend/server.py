from flask_cors import CORS
from flask_socketio import SocketIO, emit, join_room, emit, send
from flask import Flask, jsonify, request, send_from_directory, redirect, url_for, send_file
from bob_ross import game

import os
# If not set fall back to production for safety
FLASK_ENV =  os.getenv('FLASK_ENV', 'production')
# Set FLASK_SECRET on your production Environment
SECRET_KEY = os.getenv('FLASK_SECRET', 'Secret')


app = Flask(
    __name__,
    static_folder="/dist",
    static_url_path=''
)

CORS(app)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['FLASK_ENV'] = FLASK_ENV
socketio = SocketIO(app, cors_allowed_origins='*')
ROOMS = {} # dict to track active rooms

@socketio.on('create')
def on_create(data):
    """Create a game lobby"""
    gm = game.Info()
    room = gm.game_id
    ROOMS[room] = gm
    join_room(room)
    print(f'Room created -- {room}')

    username = data['username']
    color = data['color']
    ROOMS[room].init_player(username, color)
    ROOMS[room].set_admin(username)
    emit('join_room', {'room': room})

@socketio.on('join')
def on_join(data):
    """Join a game lobby"""
    username = data['username']
    color = data['color']
    room = data['room']
    if room in ROOMS:
        # add player and rebroadcast game object
        ROOMS[room].init_player(username, color)
        join_room(room)
        send(ROOMS[room].to_json(), room=room)
    else:
        emit('error', {'error': 'Unable to join room. Room does not exist.'})

@socketio.on('bet')
def on_bet(data):
    print(data)
    room = data['room']
    username = data['username']
    amount = data['amount']
    square = data['square']
    try:
        ROOMS[room].place_bet(square, username, amount)
        send(ROOMS[room].to_json(), room=room)
    except Exception as e:
        print(e)
        emit('error', {'error': 'Invalid Bet'})

@socketio.on('mark_payout')
def on_payout(data):
    print(data)
    room = data['room']
    payout = data['payout']
    square = data['square']
    ROOMS[room].mark_payout(square, payout)
    send(ROOMS[room].to_json(), room=room)

@socketio.on('start_round')
def on_start(data):
    room = data['room']
    ROOMS[room].start_round()
    send(ROOMS[room].to_json(), room=room)

@socketio.on('end_round')
def on_start(data):
    room = data['room']
    ROOMS[room].end_round()
    send(ROOMS[room].to_json(), room=room)

@app.route('/')
def index():
    return app.send_static_file("index.html")

players = []
@app.route('/players', methods=['GET','POST'])
def get_players():
    if request.method == 'POST':
        post_data = request.get_json()
        players.append({'name': post_data.get('name')})
    return jsonify({'players':players})



if __name__ == '__main__':
    socketio.run(app, port='5000')