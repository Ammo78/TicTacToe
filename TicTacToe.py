from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button

p1=input("enter player 1(X) name-")
p2=input("enter player 2(O) name-")
m=["X","O","X","O","X","O","X","O","X"]
q=[p1,p2,p1,p2,p1,p2,p1,p2,p1]
n=0
o=1

class TicTacToeGame(Widget):
    def start(self):
        global q
        global n
        self.ids.b1.disabled=False
        self.ids.b2.disabled=False
        self.ids.b3.disabled=False
        self.ids.b4.disabled=False
        self.ids.b5.disabled=False
        self.ids.b6.disabled=False
        self.ids.b7.disabled=False
        self.ids.b8.disabled=False
        self.ids.b9.disabled=False
        self.ids.b10.disabled=True
        self.ids.L.text=f"{q[n]} turn"
    def change_text(self,buttonid):
        global m
        global n
        global q
        if buttonid==1:
            self.ids.b1.text=m[n]
            self.ids.b1.disabled=True
        elif buttonid==2:
            self.ids.b2.text=m[n]
            self.ids.b2.disabled=True
        elif buttonid==3:
            self.ids.b3.text=m[n]
            self.ids.b3.disabled=True
        elif buttonid==4:
            self.ids.b4.text=m[n]
            self.ids.b4.disabled=True
        elif buttonid==5:
            self.ids.b5.text=m[n]
            self.ids.b5.disabled=True
        elif buttonid==6:
            self.ids.b6.text=m[n]
            self.ids.b6.disabled=True
        elif buttonid==7:
            self.ids.b7.text=m[n]
            self.ids.b7.disabled=True
        elif buttonid==8:
            self.ids.b8.text=m[n]
            self.ids.b8.disabled=True
        elif buttonid==9:
            self.ids.b9.text=m[n]
            self.ids.b9.disabled=True
    def check_win(self):
        global q
        global n
        global o
        global p1
        global p2
        if (self.ids.b1.text==self.ids.b2.text==self.ids.b3.text=="X") or (self.ids.b4.text==self.ids.b5.text==self.ids.b6.text=="X") or (self.ids.b7.text==self.ids.b8.text==self.ids.b9.text=="X") or (self.ids.b1.text==self.ids.b4.text==self.ids.b7.text=="X") or (self.ids.b2.text==self.ids.b5.text==self.ids.b8.text=="X") or (self.ids.b3.text==self.ids.b6.text==self.ids.b9.text=="X") or (self.ids.b1.text==self.ids.b5.text==self.ids.b9.text=="X") or (self.ids.b3.text==self.ids.b5.text==self.ids.b7.text=="X"):
            self.ids.L.text=f"{p1} wins!"
            self.ids.b0.disabled=False
            self.ids.b1.disabled=True
            self.ids.b2.disabled=True
            self.ids.b3.disabled=True
            self.ids.b4.disabled=True
            self.ids.b5.disabled=True
            self.ids.b6.disabled=True
            self.ids.b7.disabled=True
            self.ids.b8.disabled=True
            self.ids.b9.disabled=True
        elif (self.ids.b1.text==self.ids.b2.text==self.ids.b3.text=="O") or (self.ids.b4.text==self.ids.b5.text==self.ids.b6.text=="O") or (self.ids.b7.text==self.ids.b8.text==self.ids.b9.text=="O") or (self.ids.b1.text==self.ids.b4.text==self.ids.b7.text=="O") or (self.ids.b2.text==self.ids.b5.text==self.ids.b8.text=="O") or (self.ids.b3.text==self.ids.b6.text==self.ids.b9.text=="O") or (self.ids.b1.text==self.ids.b5.text==self.ids.b9.text=="O") or (self.ids.b3.text==self.ids.b5.text==self.ids.b7.text=="O"):
            self.ids.L.text=f"{p2} wins!"
            self.ids.b0.disabled=False
            self.ids.b1.disabled=True
            self.ids.b2.disabled=True
            self.ids.b3.disabled=True
            self.ids.b4.disabled=True
            self.ids.b5.disabled=True
            self.ids.b6.disabled=True
            self.ids.b7.disabled=True
            self.ids.b8.disabled=True
            self.ids.b9.disabled=True
        elif o==9:
            self.ids.L.text="It's a tie!"
            self.ids.b0.disabled=False
            self.ids.b1.disabled=True
            self.ids.b2.disabled=True
            self.ids.b3.disabled=True
            self.ids.b4.disabled=True
            self.ids.b5.disabled=True
            self.ids.b6.disabled=True
            self.ids.b7.disabled=True
            self.ids.b8.disabled=True
            self.ids.b9.disabled=True
        else:
            self.ids.L.text=f"{q[n+1]} turn"
            n+=1
            o+=1
    def try_again(self):
        global n
        global o
        self.ids.b0.disabled=True
        self.ids.b1.disabled=False
        self.ids.b2.disabled=False
        self.ids.b3.disabled=False
        self.ids.b4.disabled=False
        self.ids.b5.disabled=False
        self.ids.b6.disabled=False
        self.ids.b7.disabled=False
        self.ids.b8.disabled=False
        self.ids.b9.disabled=False
        self.ids.b1.text=""
        self.ids.b2.text=""
        self.ids.b3.text=""
        self.ids.b4.text=""
        self.ids.b5.text=""
        self.ids.b6.text=""
        self.ids.b7.text=""
        self.ids.b8.text=""
        self.ids.b9.text=""
        o=1
        n=0
        self.ids.L.text=f"{q[n]} turn"
           
            

class TicTacToeApp(App):
    def build(self):
        return TicTacToeGame()

if __name__=="__main__":
    TicTacToeApp().run()
