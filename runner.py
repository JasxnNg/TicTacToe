import sys 
sys.path.insert(0, './src')
from tictactoe import *

while True: 
    p1 = Player("computer", exp_rate=0)
    
    p1.loadPolicy("src/policy_p1")

    p2 = HumanPlayer("human")

    st = State(p1, p2)
    st.play2()