import datetime
from Classes.customException import customException
from Classes.log_producer import RabbitMQLogger
logger = RabbitMQLogger()


class Player:
    def __init__(self, userid, name):
        self.userid = userid
        self.name = name
        self.cash = 1000
        self.cards = []
        self.is_folded = False

    def __repr__(self):
        return f'Player {self.userid} name:{self.name} Current Cash:{self.cash}\n'

    def __str__(self):
        return f'Player {self.userid}\n name:{self.name}\n Current Cash:{self.cash}'

    def set_cards(self, cards):
        self.cards = cards

    def open_cards(self):
        return f'1st Card:{self.cards[0]}, 2nd Card:{self.cards[1]}'

    def check(self):
        message = f"Player {self.userid},{self.name} Checked"
        status = 'info'
        logger.send_log(message, status)
        print(message)

    def fold(self):
        message = f"Player {self.userid},{self.name} Folded"
        status = 'info'
        logger.send_log(message, status)
        print(message)

    def call(self, amount):
        if self.cash <= amount:
            amount, self.cash = self.cash, 0
        else:
            self.cash -= amount
        message = f"Player {self.userid},{self.name} Called :{amount}"
        status = 'info'
        logger.send_log(message, status)
        print(message)
        return amount

    def player_input_bet(self):
        return int(input("Enter Bet Amount: "))

    def bet(self, oldbet):
        success = False
        while not success:
            try:
                input_amount = self.player_input_bet()
                if oldbet >= input_amount:
                    success = True
                    return self.call(oldbet)
                elif self.cash >= input_amount:
                    self.cash -= input_amount
                    message = f'Player {self.userid},{self.name},{self.cash} Bet :{input_amount}'
                    status = 'info'
                    logger.send_log(message, status)
                    print(message)
                    success = True
                    return input_amount
                else:
                    raise customException()
            except customException as e:
                message = f"Exception Occured: {e} Cash Left:{self.cash}"
                status = 'warning'
                logger.send_log(message, status)
                print(message)
            except ValueError:
                message = "Cant insert string or empty string please try again with numbers"
                status = 'error'
                logger.send_log(message, status)
                print(message)

    def collect_cash(self, amount):
        self.cash += amount
