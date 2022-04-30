import random

class Die: 
    '''constructor for die'''
    def __init__(self):
        self._value=0
        self.roll()
    def  roll(self):
        self._value=random.randint(1,6)
    
    def get_value(self):
        return self._value
        
class DiceCup: 
    '''Diecup has 6 methods and a constructor itself'''
    def __init__(self,num):
        self._dices=[]
        self._cupofdices=[False,False,False,False,False]
        for die in range(num):
            self._dices.append(Die())

    def roll(self):
        for k in range(0,5):
            if self._cupofdices[k]==False:
                self._dices[k].roll()

    def value(self,index):
        return self._dices[index].get_value()

    def bank(self,index):
        self._cupofdices[index]=True

    def is_banked(self,index):
        if self._cupofdices[index]==True:
            return True
        else:
            return False

    def release(self,index):
        self._cupofdices[index]==False

    def release_all(self):
        for lst in range(5):
            self._cupofdices[lst]=False

class PlayerRoom:
    '''details of players'''
    def __init__(self):
        self._playersinfo=[]

    def set_game(self,Game):
        self._game=Game

    def add_player(self,p2):
        self._playersinfo.append(p2)

    def reset_scores(self):
        for player in range(len(self._playersinfo)):
            self._playersinfo[player].reset_score()

    def play_round(self):
        for player in self._playersinfo:
            player.play_round(self._game)

    def game_finished(self):
        sample_list=[]
        for ply in self._playersinfo:
            sample_list.append(ply.current_score())
        if max(sample_list)>=21:
            return True
        else:
            return False

    def print_scores(self):
        for score in range(len(self._playersinfo)):
            print(self._playersinfo[score]._name ,"score is:", self._playersinfo[score].current_score())

    def print_winner(self):
        for winner in range(len(self._playersinfo)):
            if winner<1:
                if self._playersinfo[winner].current_score()>=21 and self._playersinfo[winner+1].current_score()>=21:
                    print("--------------------")
                    break
            if self._playersinfo[winner].current_score()>=21:
                print("-----  Winner  ----->> ",self._playersinfo[winner]._name,"<<-------")
                break

class ShipOfFools:
    '''

    game logic

    '''
    def __init__(self):
        self.winningscore=33
        self._cupofdices=DiceCup(5)

    def round(self):
        self._cupofdices.release_all()
        '''
        extracted from pseudocode
        
        '''
        has_ship = False
        has_captain = False
        has_crew = False
        ''' This will be the sum of the remaining dice, i.e., the score. '''
        cargo = 0
        self._cupofdices.roll()
        for rnd in range(3):
            sample_lstp=[]
            count=0
            while count<5:
                sample_lstp.append(self._cupofdices._dices[count].get_value())
                count=count+1
            print(sample_lstp)
            if not (has_ship) and (6 in sample_lstp):
                for i in range(5):
                    if sample_lstp[i]==6:
                        self._cupofdices.bank(i)
                        break
                has_ship = True
            else:
                if has_ship:
                    pass
                else:
                    self._cupofdices.roll()
                    '''A ship but not a captain is banked'''
            if (has_ship) and not (has_captain) and (5 in sample_lstp):
                for i in range(5):
                    if sample_lstp[i]==5:
                        self._cupofdices.bank(i)
                        break
                has_captain = True
            else:
                if has_captain:
                    pass
                else:
                    self._cupofdices.roll()
            if has_captain and not has_crew and (4 in sample_lstp):
                for i in range(5):
                    if sample_lstp[i]==4:
                        self._cupofdices.bank(i)
                        break
                has_crew = True
            else:
                if has_crew:
                    pass
                else:
                    self._cupofdices.roll()
            if has_ship and has_captain and has_crew:
                if rnd<2:
                        for j in range(5):
                            if self._cupofdices._dices[j].get_value()>3:
                                self._cupofdices.bank(j)
                            else:
                                self._cupofdices.roll()
                elif rnd==2:
                    for j in range(5):
                        if self._cupofdices.is_banked(j):
                            pass
                        else:
                            self._cupofdices.bank(j)
        if has_ship and has_captain and has_crew:
            cargo = sum(sample_lstp) - 15
            print("cargo:",cargo)
            return cargo
        else:
            print("cargo:",cargo)
            return cargo

class Player:
    '''
    details of players score and reset score
    
    '''
    def __init__(self,playernames):
        self._name=self.set_name(playernames)
        self.scorevalue=0

    def set_name(self,names):
        return names

    def current_score(self):
        return self.scorevalue

    def reset_score(self):
        self.scorevalue=0

    def play_round(self, gamerounds):
        round1=gamerounds
        self.scorevalue=self.scorevalue + round1.round()

if __name__ == "__main__":
    room = PlayerRoom()
    room.set_game(ShipOfFools())
    room.add_player(Player("c1"))
    room.add_player(Player("c2"))
    room.reset_scores()
    while not room.game_finished():
        room.play_round()
        room.print_scores()
    room.print_winner()      
