import random
import string

BOARD_SQUARES =  [ ('Trees_None', 10), ('Trees_Both', 2), ('Trees_Deciduous', 2), ('Trees_Coniferous', 2),
                   ('Features_Grass', 2), ('Features_River', 3), ('Features_Lake', 3), ('Features_Boulders', 3),
                   ('Features_Clouds', 2), ('Features_Sun', 3), ('Features_Ocean', 12), ('Features_Night', 12),
                   ('Mountains_None', 2), ('Mountains_Snow Capped', 4) , ('Mountains_1', 4), ('Mountains_2+', 4),
                   ('Manmade_Any Manmade', 4), ('Manmade_Fence', 12), ('Manmade_Bridge', 50), ('Manmade_Human Figure',100),
                   ('Manmade_Cabin', 3), ('Windows_0', 2), ('Windows_1', 2), ('Windows_2', 2),
                   ('Isms_Happy accidents', 2), ("Isms_Let's get crazy", 2), ("Isms_It's your world", 2),
                   ("Isms_Dark to show the light", 2), ("Devils_0", 2), ("Devils_1", 2), ('Devils_2+', 2),
                   ('Weird Frame_Weird Frame', 8)]

STARTING_CHIPS = 25

class Info(object):
    def __init__(self):
        self.game_id = self.generate_room_id()
        self.players = {}
        self.game_state = self.init_game()
        self.admin = ''
        self.is_started = False

    def init_game(self):
        game = {sq[0]: {'odds':sq[1], 'bets':{},'payout':False} for sq in BOARD_SQUARES}
        game["Devils_0"]['payout'] = True
        return game

    def init_player(self, name, color):
        self.players[name] = {
            'name': name,
            'color': color,
            'chips': STARTING_CHIPS,
        }
        return self.players

    def set_admin(self, username):
        self.admin = username

    def start_round(self):
        self.is_started = True

    def end_round(self):
        for sq, cell in self.game_state.items():
            if cell['payout']:
                for username, amount in cell['bets'].items():
                    self.players[username]['chips'] += (cell['odds'] + 1) * amount
        self.game_state = self.init_game()
        self.is_started = False

    def to_json(self):
        """Serialize object to JSON"""
        return {
            'game_id': self.game_id,
            'players': self.players,
            'game_state': self.game_state,
            'admin': self.admin,
            'is_started': self.is_started
        }

    def place_bet(self, square, username, amount):
        bets = self.game_state[square]['bets']
        if username in bets:
            prev_bet = bets[username]
            del bets[username]
            self.players[username]['chips'] += prev_bet
            if amount == 0:
                return
        if ((amount > 0) & (amount <= self.players[username]['chips'])):
            bets[username] = amount
            self.players[username]['chips'] -= amount
        else:
            raise Exception('Invalid Bet')

    def mark_payout(self, square, value):
        category = square.split('_')[0]
        print(category)
        if category == 'Isms': #payout immediately and clear bets
            cell = self.game_state[square]
            print(cell)
            for username, amount in cell['bets'].items():
                    self.players[username]['chips'] += (cell['odds'] + 1) * amount
            cell['bets'] = {}
        if category in ['Devils', 'Mountains', 'Trees', 'Windows']:
            squares = [sq for sq in self.game_state.keys() if category in sq]
            for sq in squares:
                self.game_state[sq]['payout'] = False
        self.game_state[square]['payout'] = value
        

    
    @classmethod
    def generate_room_id(cls):
        """Generate a random room ID"""
        id_length = 5
        return ''.join(random.SystemRandom().choice(
            string.ascii_uppercase) for _ in range(id_length))
