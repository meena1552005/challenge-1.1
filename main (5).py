class Player:
    def play(self):
        pass  # This is a placeholder method that can be overridden in subclasses

class Batsman(Player):
    def play(self):
        print("The Batsman is Batting.")
    
class Bowler(Player):
    def play(self):
        print("The Bowler is Bowling.")

batsman = Batsman()
bowler = Bowler()

batsman.play()
bowler.play()
