import sys
from nao_agent import Nao
import time


if __name__ == "__main__":
    nao = Nao(gui=True) # robot instance

    time.sleep(1.0)

    ## action examples

    # Speak
    nao.speak("I am Nao, I am a robot.")
    time.sleep(2.0)

    # wave hand
    nao.wave(hand='left')
    time.sleep(1.0)
    nao.wave(hand='right')
    time.sleep(1.0)

    # # sit
    # nao.sit()

    # nod head
    nao.nod_head(direction='up_down')
    time.sleep(1.0)
    nao.nod_head(direction='right_left')
    time.sleep(1.0)
    nao.reset_nao_pose()
    

    # turn head
    nao.turn_head(direction='right')
    time.sleep(1.0)
    nao.turn_head(direction='left')
    time.sleep(1.0)
    nao.reset_nao_pose()

    # gaze head
    nao.gaze_head(direction='up')
    time.sleep(1.0)
    nao.gaze_head(direction='down')
    time.sleep(1.0)
    nao.reset_nao_pose()

    # raise arms
    nao.raise_arms(hand='left')
    time.sleep(2.0)
    nao.reset_nao_pose()
    time.sleep(2.0)
    nao.raise_arms(hand='right')
    time.sleep(2.0)
    nao.reset_nao_pose()
    time.sleep(2.0)
    nao.raise_arms(hand='both')
    time.sleep(2.0)
    nao.reset_nao_pose()
    time.sleep(2.0)

    # handshake
    nao.handshake(hand='left')
    time.sleep(2.0)
    nao.reset_nao_pose()
    time.sleep(2.0)
    nao.handshake(hand='right')
    time.sleep(2.0)
    nao.reset_nao_pose()
    time.sleep(2.0)




    # This snippet is a blocking call, just to keep the nao opened
    if sys.version_info[0] >= 3:
      input("Press a key to end the nao")
    else:
      raw_input("Press a key to end the nao")
    
    # Stop the nao
    nao.shutdown()
    