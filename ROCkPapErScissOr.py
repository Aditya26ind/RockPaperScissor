import random
class r_p_s_game:
    def __init__(self,name1,name2):
        # initializing the values
        self.list_of_hands=["rock","paper","scissor"]
        self.point_player1 = 0
        self.point_player2 = 0
        self.name1 = name1
        self.name2=name2
    def play(self):
        choose=''
        choose2=""
        # for running loop till user dont choose correct value..
        while True:
            player1 = print(name1, "Enter number between 1 to 3")
            a = int(input())
            if a<=3 and a>0:
                choose=random.choice(self.list_of_hands)
                print(choose)
                break
            else:
                print("Please enter 1 2 or 3")
        while True:
            player2 = print(name2, "Enter number between 1 to 3")
            b = int(input())
            if b <= 3 and a > 0:
                choose2 = random.choice(self.list_of_hands)
                print(choose2)
                break
            else:
                print("Please enter 1 2 or 3")
        # here doing similarity check if else...
        if choose and choose2 in self.list_of_hands:
            if choose2=="rock" and choose=="paper":
                self.point_player1=self.point_player1+1
            elif choose2=="rock" and choose=="scissor":
                self.point_player2 = self.point_player2 + 1
            elif choose2=="paper" and choose=="rock":
                self.point_player2=self.point_player2+1
            elif choose2 == "paper" and choose == "scissor":
                self.point_player1=self.point_player1+1
            elif choose2 == "scissor" and choose == "paper":
                self.point_player2=self.point_player2+1
            elif choose2 == "scissor" and choose == "rock":
                self.point_player1=self.point_player1+1
            if self.point_player1 > self.point_player2:
                return 1
            else:
                return 2
        else:
            return 0
# main ....... #ADITTYA SALABH............
name1=str(input("Enter the Player1 name:"))
name2=str(input("Enter the player2 name:"))
game_on=r_p_s_game(name1,name2)
while True:
    if game_on.point_player1>=5 or game_on.point_player2>=5:
        if game_on.point_player1==5:
            print(f"player1 {name1} wins")
        else:
            print(f"player {name2} wins")
        break
    else:
        lead=game_on.play()
        if game_on.point_player1>game_on.point_player2:
            print(f"{name1} LEADS BY:",game_on.point_player1)
        if game_on.point_player1<game_on.point_player2:
            print(f"{name2} LEADS BY:",game_on.point_player2)
        else:
            print("SAME POINT")


