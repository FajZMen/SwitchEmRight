from time import sleep as wait
from random import randint as rng
from random import shuffle
import streamlit as st
import time
from streamlit_extras.stoggle import stoggle
from GameStuffs.Gamedata import switchlayout, switchlayouttest, useraccounts, bannedaccounts, normallb, hardcorelb, achievementsinventory, normalgr, hardcoregr, braindestroyergr, godspeedgr, perfectpercisiongr, makehastegr, sneakyswitchesgr, eminemgr, brainanuerysmgr, examgr, glitchgr

def getstates():
    if "currentlevel" not in st.session_state:
        st.session_state.currentlevel = 1
    if "developerpanelaccess" not in st.session_state:
        st.session_state.developerpanelaccess = False
    if "timeranout" not in st.session_state:
        st.session_state.timeranout = False
    if "levelcleared" not in st.session_state:
        st.session_state.levelcleared = False
    if "start_time" not in st.session_state:
        st.session_state.start_time = time.time()
        st.session_state.max_time = 0
    if 'displayswitches' not in st.session_state:
        st.session_state.displayswitches = True
        st.session_state.displayhints = 0
    if "currentpage" not in st.session_state:
        st.session_state.currentpage = "Main"
    if "loggedin" not in st.session_state:
        st.session_state.loggedin = False
    if "developerlogin" not in st.session_state:
        st.session_state.developerlogin = False
    if "banned" not in st.session_state:
        st.session_state.banned = False
    if "difficulty" not in st.session_state:
        st.session_state.difficulty = "None"
    if "perfect" not in st.session_state:
        st.session_state.perfect = True
    if "givebonus" not in st.session_state:
        st.session_state.givebonus = 0
    if "tutorialstage" not in st.session_state:
        st.session_state.tutorialstage = 0 
    if "glitch" not in st.session_state:
        st.session_state.glitch = 0


# ///// -------------------------------------------------------------- Page ---------------------------------------------------------- /////
def mainpage():
    st.title("Welcome to Switch Em Right! (Game)")
    st.write("A very simple Game where you use your Brain and Reading Skills to toggle switches better!")
    st.write("But before you Play, Please Login (If you already have an account) or Register first!")

def playnormal():
    st.session_state.max_time = 161
    st.session_state.start_time = time.time() 
    st.session_state.displayhints = 3
    st.session_state.currentlevel = 1
    st.session_state.displayswitches = True
    st.session_state.difficulty = "Normal"
    SwitchRandomizer()
    if st.session_state.loggedin:
        st.session_state.currentpage = "NormalGame"
    else:
        st.session_state.currentpage = "DevNormalGame"
    st.rerun()

def hardcoredesc():
    st.title("Hardcore Mode")
    st.write("Brings even more challenge with more things to deal with!")
    stoggle("Settings", """Hardcore mode settings:
        
        --Bad Stuff--
        - You must deal with 20 Switches (Good Luck LOL)
        - You only have 2 Hints per level
        - Gameplay is Much Longer
            
    --Good Stuff--
        - You have much more Time than in Normal Mode
        - Switch States Replay are much slower, making them easier to read
        - Punishments for Wrong Submits are less harsher
    """)

def playhardcore():
    st.session_state.max_time = 245
    st.session_state.start_time = time.time() 
    st.session_state.displayhints = 2
    st.session_state.currentlevel = 1
    st.session_state.difficulty = "Hardcore"
    SwitchRandomizer()
    if st.session_state.loggedin:
        st.session_state.currentpage = "HardGame"
    else:
        st.session_state.currentpage = "DevHardGame"
    st.rerun()

def purememorydesc():
    st.title("Pure Memory Mode")
    stoggle("Settings", """Pure Memory mode settings:
        
        --Bad Stuff--
        - You cannot use Hints, So You must remember ALL of the Switch States at the start!
        - Punishments for Wrong Submits are much Harsher
        - You have less Time than in Normal Mode
            
    --Good Stuff--
        - Switch States Replay repeats 3 times        
        - Switch States Replay are slower, making them easier to read
    """)

def playpurememory():
    st.session_state.max_time = 121
    st.session_state.start_time = time.time() 
    st.session_state.displayhints = 1
    st.session_state.currentlevel = 1
    st.session_state.difficulty = "RememberThem"
    SwitchRandomizer()
    st.session_state.currentpage = "PureMemoryGame"
    st.rerun()

def godspeeddesc():
    st.title("God Speed Mode")
    st.write("Reach as far as you can in 10 minutes!")
    stoggle("Settings", """God Speed mode settings:

        --Bad Stuff--
        - Timer doesnt reset! so better be Fast
        - Switch States Replay are much faster, making them harder to read

    --Good Stuff--
        - You only have to deal with 6 Switches
        - You have Infinite Hints
        - No Punishments for Wrong Submits!
    """)

def playgodspeed():
    st.session_state.max_time = 620
    st.session_state.start_time = time.time() 
    st.session_state.displayhints = 1
    st.session_state.currentlevel = 1
    st.session_state.difficulty = "GodSpeed"
    SwitchRandomizer()
    st.session_state.currentpage = "FastAsFuckGame"
    st.rerun()

def perfectpercisiondesc():
    st.title("Perfect Precision Mode")
    st.write("No Mistakes were made")
    stoggle("Settings", """Perfect Precision mode settings:

        --Bad Stuff--
        - A Single wrong Submit, and its gameover!
        - Hints are Permanently limited (Doesnt Reset). So use them WISELY

    --Good Stuff--
        - There are no Timer
        - You have 25 Hints
        - Switch States Replay are very slow, Making them much easier to read
    """)

def playperfectperc():
    st.session_state.perfect = True
    st.session_state.displayhints = 25
    st.session_state.currentlevel = 1
    st.session_state.difficulty = "PerfectAccuracy"
    SwitchRandomizer()
    st.session_state.currentpage = "PerfectGame"
    st.rerun()

def makehastedesc():
    st.title("Make Haste Mode")
    st.write("Time is still Ticking!")
    stoggle("Settings", """Make Haste mode settings:

        --Bad Stuff--
        - Timer and Hints doesnt reset every level!
        - Punishments for Wrong Submits are much Harsher
        - Switch States Replay are faster, Making them harder to read

    --Good Stuff--
        - Adds 120 seconds to the Timer and 3 Hints for every 5 levels you advance
        - Switch States Replay doesnt get faster as you progress
    """)

def playmakehaste():
    st.session_state.max_time = 120
    st.session_state.start_time = time.time() 
    st.session_state.displayhints = 2
    st.session_state.currentlevel = 1
    st.session_state.givebonus = 0
    st.session_state.difficulty = "Haste"
    SwitchRandomizer()
    st.session_state.currentpage = "YouBetterRunGame"
    st.rerun()

def sneakyswitchesdesc():
    st.title("Sneaky Switches Mode")
    st.write("Wanna see the switch states? Well, find them yourself!")
    stoggle("Settings", """Sneaky Switches mode settings:

        --Bad Stuff--
        - the Switch State Replay will only show 9 switches instead of 10.
        - As you progress, The Switch State Replay will show less and less (To a maximum 5 switches hidden).

    --Good Stuff--
        - Use hints for a chance to find out the Hidden Switches State!
        - You have quite a lot of Time
        - You have 5 Hints per level
        - Switch States Replay are slower, making them easier to read
    """)

def playsneakyswitches():
    st.session_state.max_time = 325
    st.session_state.start_time = time.time() 
    st.session_state.displayhints = 5
    st.session_state.currentlevel = 1
    st.session_state.difficulty = "HiddenSwitches"
    SwitchRandomizer()
    st.session_state.currentpage = "SneakyGame"
    st.rerun()

def eminemdesc():
    st.title("Eminem Mode")
    st.write("Read like you Rap!")
    stoggle("Settings", """Eminem mode settings:

        --Bad Stuff--
        - The Switch States Replay are really fast!
        - The Switch States Replay gets Rapidly faster than other Modes!
        - Punishments for Wrong Submits are very Harsh

    --Good Stuff--
        - You have 10 Hints per level
        - You have a little bit more Time
    """)

def playeminem():
    st.session_state.max_time = 220
    st.session_state.start_time = time.time() 
    st.session_state.displayhints = 10
    st.session_state.currentlevel = 1
    st.session_state.difficulty = "Eminem"
    SwitchRandomizer()
    st.session_state.currentpage = "EminemGame"
    st.rerun()

def brainfucdesc():
    st.title("Brain Aneurysm Mode")
    st.write("Can your Brain even handle this?")
    stoggle("Settings", """Brain Aneurysm mode settings:

        --Bad Stuff--
        - You have to deal with 40 Switches..... Yes, 40 Switches (Have fun staring at the Switch States Replay for 40 Seconds LOL)
        - VERY LONG GAMEPLAY!

    --Good Stuff--
        - You have 4 Hints per level
        - You have a TON of Time
        - Switch States Replay doesnt get faster as you progress
    """)

def playbraindestroyer():
    st.session_state.max_time = 752
    st.session_state.start_time = time.time() 
    st.session_state.displayhints = 4
    st.session_state.currentlevel = 1
    st.session_state.difficulty = "BrainFuck"
    SwitchRandomizer()
    st.session_state.currentpage = "TortureGame"
    st.rerun()

def rngesusdesc():
    st.title("RNGesus Mode")
    st.write("Feelin' lucky? Play this!, Feelin' unlucky? Still play this!")
    stoggle("Settings", """RNGesus mode settings:

        --Bad Stuff--
        - RNG Decides your Run
        - The Amount of Switches you have to deal are Vary between levels!
        - The Switch States Replay speed, The Amount of Hints, and Time Vary as well!
        - If you're Unlucky, too bad.

    --Good Stuff--
        - If You're Lucky, Great!
    """)

def playrngesus():
    st.session_state.max_time = rng(120, 420)
    st.session_state.start_time = time.time() 
    st.session_state.currentlevel = 1
    st.session_state.displayhints = rng(1, 5)
    st.session_state.difficulty = "RNGesus"
    SwitchRandomizer()
    st.session_state.currentpage = "RNGGame"
    st.rerun()

def glitcheddesc():
    st.title("Glitched Mode")
    st.write("Dont worr--- abuot eht egame!? we'rr tyyr fi@@&#@?>< it???")
    stoggle("Settings", """Glitched mode settings:

        --Bad Stuff--
        - Some part of the Game are Glitched!
        - The Switch State Replay cant show the Switch States Properly!
        - The Timer wont show the Time!
        - Hints Sometimes does not work!

    --Good Stuff--
        - Fortunately 
        - The Penalty are Glitched either and they doesnt work
    """)

def playglitched():
    st.session_state.max_time = 416
    st.session_state.start_time = time.time() 
    st.session_state.currentlevel = 1
    st.session_state.displayhints = 6
    st.session_state.glitch = rng(1, 4)
    st.session_state.difficulty = "Glitched"
    SwitchRandomizer()
    st.session_state.currentpage = "GlitchedGame"
    st.rerun()

def loadinggame(): #This shit is fucked
    startingdisp = "Starting Game..."
    startingbar = st.progress(0, text=startingdisp)
    for perct in range(100):
        wait(0.05)
        startingbar.progress(perct + 1, text=startingdisp)
    startingbar.empty()

def endrun():
    switchlayout.clear()
    st.session_state.displayswitches = True
    if st.session_state.difficulty == "Normal": #What an Abomination of code
        normalgr.append({f"User": {st.session_state.displayname}, "Level": st.session_state.currentlevel})
    elif st.session_state.difficulty == "Hardcore":
        hardcoregr.append({f"User": {st.session_state.displayname}, "Level": st.session_state.currentlevel})
    elif st.session_state.difficulty == "RememberThem":
        braindestroyergr.append({f"User": {st.session_state.displayname}, "Level": st.session_state.currentlevel})
    elif st.session_state.difficulty == "GodSpeed":
        godspeedgr.append({f"User": {st.session_state.displayname}, "Level": st.session_state.currentlevel})
    elif st.session_state.difficulty == "PerfectAccuracy":
        perfectpercisiongr.append({f"User": {st.session_state.displayname}, "Level": st.session_state.currentlevel})
    elif st.session_state.difficulty == "Haste":
        makehastegr.append({f"User": {st.session_state.displayname}, "Level": st.session_state.currentlevel})
    elif st.session_state.difficulty == "HiddenSwitches":
        sneakyswitchesgr.append({f"User": {st.session_state.displayname}, "Level": st.session_state.currentlevel})
    elif st.session_state.difficulty == "Eminem":
        eminemgr.append({f"User": {st.session_state.displayname}, "Level": st.session_state.currentlevel})
    elif st.session_state.difficulty == "BrainFuck":
        brainanuerysmgr.append({f"User": {st.session_state.displayname}, "Level": st.session_state.currentlevel})
    elif st.session_state.difficulty == "RNGesus":
        examgr.append({f"User": {st.session_state.displayname}, "Level": st.session_state.currentlevel})
    elif st.session_state.difficulty == "Glitched":
        glitchgr.append({f"User": {st.session_state.displayname}, "Level": st.session_state.currentlevel})

    st.session_state.difficulty = "None"
    if st.session_state.loggedin:
        st.session_state.currentpage = "Main"
    else:
        st.session_state.currentpage = "DevMain"
    st.rerun()

def how2play():
    st.title("How to Play")
    st.write("Welcome to SwitchEmRight! This is a simple game that only uses Brain power and Reading Skills!")
    st.write("If you're new here, you can check out the 'Basics' Page to get started.")

def basicsh2p():
    st.title("Basics")
    st.write("""The game is based on Switches (Who would've though?), and your goal is to match the Switches to the correct state.""")
    st.write("You match the Switch states by toggling them (Clicking it). and once you' think the States are correct, you can press the sumbit button to see the result.")
    st.write("if ALL OF THE SWITCHS are in the correct STATE, you will advance to the next level, but if ONE of the Switches is wrong, you will receive a penalty by deducting the Timer.")
    st.write("But how to know the Switch States? Well, go ahead and advance to the 'Switch States' Page.""")

def switchstatesh2p():
    st.title("Switch States")
    st.write("This is one of the Main part of the Game, the Switch States. They are Random for every Level.")
    st.write("At the start of the Game and every Level, you will be shown the Switch States Replay. They display each of the switch's CORRECT state one by one by the text 'Switch 2: Off', 'Switch 7: On' like that. Heres an Example:")
    st.video("Other/SwitchStateReplayEx.mp4")
    st.write("They are shown in a random order and with a delay for each switch. The Replay gets faster the further you go in the game, making them harder to read (Reaches Maximum speed at level 50). and this is where the reading reflexes part comes in")
    st.write("But what if you dont remember the Switch States or forgot? Well, you can use the thing called HINTS that can be used to Rewatch the Switch States. They are limited but resets every level")

def timerh2p():
    st.title("Timer")
    st.write("""The Timer is a crucial part of the game, as it is the only Thing that can end your Run. when it runs out, the game ends and you have to restart from level 1.""")
    st.image("Other/Timer.png")
    st.write("The Timer Resets when you advance to the next level.")
    st.warning("NOTE: Due to streamlit limitations, the timer doesnt automatically update in display. so in order to see how much time you have left, you must MANUALLY update it by either: Toggling switches, switch pages in the sidebar, or clicking the sumbit button.")

def login(username, password):
    for banacc in bannedaccounts:
        if banacc["username"] == username:
            st.session_state["banned"] = True
            st.session_state["displayname"] = username
            st.session_state["bannedreason"] = banacc["reason"]
            st.rerun()
            return
    for acc in useraccounts:
        if username == "FajZ" and password == "zstleader222":
            st.session_state["developerlogin"] = True
            st.session_state["displayname"] = username
            st.session_state["role"] = "Developer"
            st.session_state["currentpage"] = "DevMain"
            st.rerun()
            return
        elif acc["username"] == username and acc["password"] == password:
            st.session_state["loggedin"] = True
            st.session_state["displayname"] = username
            st.session_state["role"] = "User"
            st.session_state["currentpage"] = "Main"
            st.rerun()
            return
    else:
        st.error("Username atau password salah!")

def register():
    st.title("Register")
    regname = st.text_input("Account Name")
    regpass = st.text_input("Account Password", type="password")
    if st.button("Register"):
        if not regname or not regpass:
            st.error("Username and password must be filled!")
        else:
            for regacc in useraccounts:
                if regacc["username"] == regname:
                    st.error("Sorry but that Username already exists, please use another one.")
                    break

                else:
                    useraccounts.append({"username": regname, "password": regpass})
                    st.success("Account Created! YAY!!!!")
                    wait(1)
                    st.rerun()

def accountcreatortool(userinput, passinput):
    useraccounts.append({"username": userinput, "password": passinput})
    st.success("Account created!")

def accountdeletortool(deluserinput):
    for user in useraccounts:
        if deluserinput == user["username"]:
            useraccounts.remove(user)
            st.success("User Account deleted!")
            break
    else:
        st.error("User Account not found!")

def banaccounts(targetpunishuser, reason):
    for alrban in bannedaccounts:
        if targetpunishuser == alrban["username"]:
            st.error("Account already banned!")
            return

    accountisnotbanned = True

    for acctoban in useraccounts:
        if targetpunishuser == acctoban["username"]:
            bannedaccounts.append({"username": targetpunishuser, "reason": reason})
            st.success("Account Banned!")
            accountisnotbanned = False
            break
    
    if accountisnotbanned:
        st.error("Account not found.")

def unbanaccount(targetpunishuser):
    for unbanacc in bannedaccounts:
        if targetpunishuser == unbanacc["username"]:
            bannedaccounts.remove(unbanacc)
            st.success("Account Unbanned!")
            break
    else:
        st.error("Account not found!")

def gameresults():
    st.title("Game Results")
    pickmode = st.selectbox("Pick a Game Mode", ["Normal", "Hardcore", "Pure Memory", "GodSpeed", "Perfect Percision", "Make Haste", "Sneaky Switches", "Eminem", "Brain Anuerysm", "RNGesus", "Glitched"])
    if pickmode == "Normal":
        st.dataframe(normalgr, width=1000)
    elif pickmode == "Hardcore":
        st.dataframe(hardcoregr, width=1000)
    elif pickmode == "Pure Memory":
        st.dataframe(braindestroyergr, width=1000)
    elif pickmode == "GodSpeed":
        st.dataframe(godspeedgr, width=1000)
    elif pickmode == "Perfect Percision":
        st.dataframe(perfectpercisiongr, width=1000)
    elif pickmode == "Make Haste":
        st.dataframe(makehastegr, width=1000)
    elif pickmode == "Sneaky Switches":
        st.dataframe(sneakyswitchesgr, width=1000)
    elif pickmode == "Eminem":
        st.dataframe(eminemgr, width=1000)
    elif pickmode == "Brain Anuerysm":
        st.dataframe(brainanuerysmgr, width=1000)
    elif pickmode == "RNGesus":
        st.dataframe(examgr, width=1000)
    elif pickmode == "Glitched":
        st.dataframe(glitchgr, width=1000)






# ///// -------------------------------------------------------------- Game ---------------------------------------------------------- /////
def SwitchGame():
    st.title(f"Level {st.session_state.currentlevel}")
    if st.session_state.displayswitches:
        st.write("WATCH AND REMEMBER THE SWITCHES!")
        wait(3)
        SwitchDisplay()
        st.session_state.displayswitches = False
        st.rerun()
    else:
        elapsed_time = time.time() - st.session_state.start_time
        remaining_time = max(0, st.session_state.max_time - elapsed_time)
        progress = 1 - (remaining_time / st.session_state.max_time)
    
        timertext = f"Time Left: {int(remaining_time)}s"
        timerbar = st.progress(progress, text=timertext)
    
        if remaining_time <= 0:
            st.error("Time ran out, you lost")
            if st.button("Back to Menu"):
                endrun()
            return
    
        row1, row2 = st.columns(2)
        with row1:
            switch1 = st.toggle("1")
            switch3 = st.toggle("3")
            switch5 = st.toggle("5")
            switch7 = st.toggle("7")
            switch9 = st.toggle("9")

        with row2:
            switch2 = st.toggle("2")
            switch4 = st.toggle("4")
            switch6 = st.toggle("6")
            switch8 = st.toggle("8")
            switch10 = st.toggle("10")

        if st.button("Submit"):
            SwitchCheck(switch1, switch2, switch3, switch4, switch5, switch6, switch7, switch8, switch9, switch10)
        
        st.write(f"Hints remaining: {st.session_state.displayhints}")
        if st.session_state.displayhints > 0:
            if st.button("Hint"):
               st.session_state.displayswitches = True
               st.session_state.displayhints -= 1
               st.rerun()

def SwitchGameHardcore():
    st.title(f"Level {st.session_state.currentlevel}")
    if st.session_state.displayswitches:
        st.write("CAREFULLY WATCH AND REMEMBER THE SWITCHES!")
        wait(3)
        SwitchDisplayHC()
        st.session_state.displayswitches = False
        st.rerun()
    else:
        elapsed_time = time.time() - st.session_state.start_time
        remaining_time = max(0, st.session_state.max_time - elapsed_time)
        progress = 1 - (remaining_time / st.session_state.max_time)
    
        timertext = f"Time Left: {int(remaining_time)}s"
        timerbar = st.progress(progress, text=timertext)
    
        if remaining_time <= 0:
            st.error("Time ran out, you lost")
            if st.button("Back to Menu"):
                endrun()
            return
    
        row1, row2 = st.columns(2)
        with row1:
            switch1 = st.toggle("1")
            switch3 = st.toggle("3")
            switch5 = st.toggle("5")
            switch7 = st.toggle("7")
            switch9 = st.toggle("9")
            switch11 = st.toggle("11")
            switch13 = st.toggle("13")
            switch15 = st.toggle("15")
            switch17 = st.toggle("17")
            switch19 = st.toggle("19")

        with row2:
            switch2 = st.toggle("2")
            switch4 = st.toggle("4")
            switch6 = st.toggle("6")
            switch8 = st.toggle("8")
            switch10 = st.toggle("10")
            switch12 = st.toggle("12")
            switch14 = st.toggle("14")
            switch16 = st.toggle("16")
            switch18 = st.toggle("18")
            switch20 = st.toggle("20")

        if st.button("Submit"):
            SwitchCheckHC(switch1, switch2, switch3, switch4, switch5, switch6, switch7, switch8, switch9, switch10, switch11, switch12, switch13, switch14, switch15, switch16, switch17, switch18, switch19, switch20)
        
        st.write(f"Hints remaining: {st.session_state.displayhints}")
        if st.session_state.displayhints > 0:
            if st.button("Hint"):
               st.session_state.displayswitches = True
               st.session_state.displayhints -= 1
               st.rerun()

def SwitchGamePureMemory():
    st.title(f"Level {st.session_state.currentlevel}")
    if st.session_state.displayswitches:
        st.write("FOCUS! WATCH AND REMEMBER THE SWITCHES!")
        wait(3)
        SwitchDisplayPM()
        st.session_state.displayswitches = False
        st.rerun()
    else:
        elapsed_time = time.time() - st.session_state.start_time
        remaining_time = max(0, st.session_state.max_time - elapsed_time)
        progress = 1 - (remaining_time / st.session_state.max_time)
    
        timertext = f"Time Left: {int(remaining_time)}s"
        timerbar = st.progress(progress, text=timertext)
    
        if remaining_time <= 0:
            st.error("Time ran out, you lost")
            if st.button("Back to Menu"):
                endrun()
            return
    
        row1, row2 = st.columns(2)
        with row1:
            switch1 = st.toggle("1")
            switch3 = st.toggle("3")
            switch5 = st.toggle("5")
            switch7 = st.toggle("7")
            switch9 = st.toggle("9")

        with row2:
            switch2 = st.toggle("2")
            switch4 = st.toggle("4")
            switch6 = st.toggle("6")
            switch8 = st.toggle("8")
            switch10 = st.toggle("10")

        if st.button("Submit"):
            SwitchCheckPM(switch1, switch2, switch3, switch4, switch5, switch6, switch7, switch8, switch9, switch10)
        
        st.write("Hints remaining: 0?2@$829&^d%^&*98")
        if st.session_state.displayhints > 0:
            if st.button("Hint?"):
               st.error("Uh Oh")

def SwitchGameGodSpeed():
    st.title(f"Level {st.session_state.currentlevel}")
    if st.session_state.displayswitches:
        st.write("GET READY AND BE FAST!")
        wait(1.5)
        SwitchDisplayGS()
        st.session_state.displayswitches = False
        st.rerun()
    else:
        elapsed_time = time.time() - st.session_state.start_time
        remaining_time = max(0, st.session_state.max_time - elapsed_time)
        progress = 1 - (remaining_time / st.session_state.max_time)
    
        timertext = f"Time Left: {int(remaining_time)}s"
        timerbar = st.progress(progress, text=timertext)
    
        if remaining_time <= 0:
            st.error("Times Up!")
            st.success(f"You've Reached level {st.session_state.currentlevel}!")
            if st.button("Back to Menu"):
                endrun()
            return
    
        row1, row2 = st.columns(2)
        with row1:
            switch1 = st.toggle("1")
            switch3 = st.toggle("3")
            switch5 = st.toggle("5")

        with row2:
            switch2 = st.toggle("2")
            switch4 = st.toggle("4")
            switch6 = st.toggle("6")

        if st.button("Submit"):
            SwitchCheckGS(switch1, switch2, switch3, switch4, switch5, switch6)
        
        st.write(f"Hints remaining: Infinite")
        if st.session_state.displayhints > 0:
            if st.button("Hint"):
               st.session_state.displayswitches = True
               st.rerun()
        st.audio("Other/GodSpeedOST.mp3")
        st.write("Music: Pizza Tower - Pillar John's Revenge Lap 3 Fanmade by Vozaxhi")
    
def SwitchGamePerfect():
    st.title(f"Level {st.session_state.currentlevel}")
    if st.session_state.displayswitches:
        st.write("REMEMBER AND FOCUS!")
        wait(3)
        SwitchDisplayPP()
        st.session_state.displayswitches = False
        st.rerun()
    else:
        if st.session_state.perfect == False:
            st.error("Unlucky, you got it wrong. Better luck next time!")
            st.write(f"You've Reached level {st.session_state.currentlevel}!")
            if st.button("Back to Menu"):
                endrun()
            return

        st.write("Time Left: Error")
        row1, row2 = st.columns(2)
        with row1:
            switch1 = st.toggle("1")
            switch3 = st.toggle("3")
            switch5 = st.toggle("5")
            switch7 = st.toggle("7")
            switch9 = st.toggle("9")

        with row2:
            switch2 = st.toggle("2")
            switch4 = st.toggle("4")
            switch6 = st.toggle("6")
            switch8 = st.toggle("8")
            switch10 = st.toggle("10")

        if st.button("Submit"):
            SwitchCheckPP(switch1, switch2, switch3, switch4, switch5, switch6, switch7, switch8, switch9, switch10)
        
        st.write(f"Hints remaining: {st.session_state.displayhints}")
        if st.session_state.displayhints > 0:
            if st.button("Hint"):
               st.session_state.displayhints -= 1
               st.session_state.displayswitches = True
               st.rerun()

def SwitchGameMakeHaste():
    st.title(f"Level {st.session_state.currentlevel}")
    if st.session_state.displayswitches:
        st.write("BE FAST AND MAKE HASTE! THE CLOCK IS TICKING!")
        wait(3)
        SwitchDisplayMH()
        st.session_state.displayswitches = False
        st.rerun()
    else:
        elapsed_time = time.time() - st.session_state.start_time
        remaining_time = max(0, st.session_state.max_time - elapsed_time)
        progress = 1 - (remaining_time / st.session_state.max_time)
    
        timertext = f"Time Left: {int(remaining_time)}s"
        timerbar = st.progress(progress, text=timertext)
    
        if remaining_time <= 0:
            st.error("Time ran out, you lost")
            if st.button("Back to Menu"):
                endrun()
            return
    
        row1, row2 = st.columns(2)
        with row1:
            switch1 = st.toggle("1")
            switch3 = st.toggle("3")
            switch5 = st.toggle("5")
            switch7 = st.toggle("7")
            switch9 = st.toggle("9")

        with row2:
            switch2 = st.toggle("2")
            switch4 = st.toggle("4")
            switch6 = st.toggle("6")
            switch8 = st.toggle("8")
            switch10 = st.toggle("10")

        if st.button("Submit"):
            SwitchCheckMH(switch1, switch2, switch3, switch4, switch5, switch6, switch7, switch8, switch9, switch10)
        
        st.write(f"Hints remaining: {st.session_state.displayhints}")
        if st.session_state.displayhints > 0:
            if st.button("Hint"):
               st.session_state.displayswitches = True
               st.session_state.displayhints -= 1
               st.rerun()

def SwitchGameSneaky():
    st.title(f"Level {st.session_state.currentlevel}")
    if st.session_state.displayswitches:
        st.write("SORRY BUT IM NOT GONNA SHOW EM' ALL")
        wait(3)
        SwitchDisplayHnS()
        st.session_state.displayswitches = False
        st.rerun()
    else:
        elapsed_time = time.time() - st.session_state.start_time
        remaining_time = max(0, st.session_state.max_time - elapsed_time)
        progress = 1 - (remaining_time / st.session_state.max_time)
    
        timertext = f"Time Left: {int(remaining_time)}s"
        timerbar = st.progress(progress, text=timertext)
    
        if remaining_time <= 0:
            st.error("Time ran out, you lost")
            if st.button("Back to Menu"):
                endrun()
            return
    
        row1, row2 = st.columns(2)
        with row1:
            switch1 = st.toggle("1")
            switch3 = st.toggle("3")
            switch5 = st.toggle("5")
            switch7 = st.toggle("7")
            switch9 = st.toggle("9")

        with row2:
            switch2 = st.toggle("2")
            switch4 = st.toggle("4")
            switch6 = st.toggle("6")
            switch8 = st.toggle("8")
            switch10 = st.toggle("10")

        if st.button("Submit"):
            SwitchCheckHnS(switch1, switch2, switch3, switch4, switch5, switch6, switch7, switch8, switch9, switch10)
        
        st.write(f"Hints remaining: {st.session_state.displayhints}")
        if st.session_state.displayhints > 0:
            if st.button("Hint"):
               st.session_state.displayswitches = True
               st.session_state.displayhints -= 1
               st.rerun()

def SwitchGameEminem():
    st.title(f"Level {st.session_state.currentlevel}")
    if st.session_state.displayswitches:
        st.write("CAN YOU EVEN READ ME?")
        wait(3)
        SwitchDisplayEM()
        st.session_state.displayswitches = False
        st.rerun()
    else:
        elapsed_time = time.time() - st.session_state.start_time
        remaining_time = max(0, st.session_state.max_time - elapsed_time)
        progress = 1 - (remaining_time / st.session_state.max_time)
    
        timertext = f"Time Left: {int(remaining_time)}s"
        timerbar = st.progress(progress, text=timertext)
    
        if remaining_time <= 0:
            st.error("Time ran out, you lost")
            if st.button("Back to Menu"):
                endrun()
            return
    
        row1, row2 = st.columns(2)
        with row1:
            switch1 = st.toggle("1")
            switch3 = st.toggle("3")
            switch5 = st.toggle("5")
            switch7 = st.toggle("7")
            switch9 = st.toggle("9")

        with row2:
            switch2 = st.toggle("2")
            switch4 = st.toggle("4")
            switch6 = st.toggle("6")
            switch8 = st.toggle("8")
            switch10 = st.toggle("10")

        if st.button("Submit"):
            SwitchCheckEM(switch1, switch2, switch3, switch4, switch5, switch6, switch7, switch8, switch9, switch10)
        
        st.write(f"Hints remaining: {st.session_state.displayhints}")
        if st.session_state.displayhints > 0:
            if st.button("Hint"):
               st.session_state.displayswitches = True
               st.session_state.displayhints -= 1
               st.rerun()

def SwitchGameBrainDestroyer():
    st.title(f"Level {st.session_state.currentlevel}")
    if st.session_state.displayswitches:
        st.write("HAVE FUN WITH THESE SWITCHES!")
        wait(3)
        SwitchDisplayBD()
        st.session_state.displayswitches = False
        st.rerun()
    else:
        elapsed_time = time.time() - st.session_state.start_time
        remaining_time = max(0, st.session_state.max_time - elapsed_time)
        progress = 1 - (remaining_time / st.session_state.max_time)
    
        timertext = f"Time Left: {int(remaining_time)}s"
        timerbar = st.progress(progress, text=timertext)
    
        if remaining_time <= 0:
            st.error("Time ran out, you lost")
            if st.button("Back to Menu"):
                endrun()
            return
    
        row1, row2 = st.columns(2)
        with row1:
            switch1 = st.toggle("1")
            switch3 = st.toggle("3")
            switch5 = st.toggle("5")
            switch7 = st.toggle("7")
            switch9 = st.toggle("9")
            switch11 = st.toggle("11")
            switch13 = st.toggle("13")
            switch15 = st.toggle("15")
            switch17 = st.toggle("17")
            switch19 = st.toggle("19")
            switch21 = st.toggle("21")
            switch23 = st.toggle("23")
            switch25 = st.toggle("25")
            switch27 = st.toggle("27")
            switch29 = st.toggle("29")
            switch31 = st.toggle("31")
            switch33 = st.toggle("33")
            switch35 = st.toggle("35")
            switch37 = st.toggle("37")
            switch39 = st.toggle("39")

        with row2:
            switch2 = st.toggle("2")
            switch4 = st.toggle("4")
            switch6 = st.toggle("6")
            switch8 = st.toggle("8")
            switch10 = st.toggle("10")
            switch12 = st.toggle("12")
            switch14 = st.toggle("14")
            switch16 = st.toggle("16")
            switch18 = st.toggle("18")
            switch20 = st.toggle("20")
            switch22 = st.toggle("22")
            switch24 = st.toggle("24")
            switch26 = st.toggle("26")
            switch28 = st.toggle("28")
            switch30 = st.toggle("30")
            switch32 = st.toggle("32")
            switch34 = st.toggle("34")
            switch36 = st.toggle("36")
            switch38 = st.toggle("38")
            switch40 = st.toggle("40")

        if st.button("Submit"):
            SwitchCheckBD(switch1, switch2, switch3, switch4, switch5, switch6, switch7, switch8, switch9, switch10, switch11, switch12, switch13, switch14, switch15, switch16, switch17, switch18, switch19, switch20, switch21, switch22, switch23, switch24, switch25, switch26, switch27, switch28, switch29, switch30, switch31, switch32, switch33, switch34, switch35, switch36, switch37, switch38, switch39, switch40)
        
        st.write(f"Hints remaining: {st.session_state.displayhints}")
        if st.session_state.displayhints > 0:
            if st.button("Hint"):
               st.session_state.displayswitches = True
               st.session_state.displayhints -= 1
               st.rerun()

def SwitchGameRNGesus(): #Almost done, need testing
    st.title(f"Level {st.session_state.currentlevel}")
    if st.session_state.displayswitches:
        st.write("THE RNGESUS SHALL DECIDES YOUR FATE!")
        wait(3)
        SwitchDisplayRNG()
        st.session_state.displayswitches = False
        st.rerun()
    else:
        elapsed_time = time.time() - st.session_state.start_time
        remaining_time = max(0, st.session_state.max_time - elapsed_time)
        progress = 1 - (remaining_time / st.session_state.max_time)
    
        timertext = f"Time Left: {int(remaining_time)}s"
        timerbar = st.progress(progress, text=timertext)
    
        if remaining_time <= 0:
            st.error("Unlucky! Time ran out, you lost")
            if st.button("Back to Menu"):
                endrun()
            return

        num_switches = len(switchlayout)
        col1, col2 = st.columns(2)
        
        levelswitches = []
        with col1:
            for i in range(0, num_switches, 2):
                levelswitches.append(st.toggle(str(i + 1)))
                
        with col2:
            for i in range(1, num_switches, 2):
                levelswitches.append(st.toggle(str(i + 1)))

        if st.button("Submit"):
            SwitchCheckRNG(levelswitches)
        
        st.write(f"Hints remaining: {st.session_state.displayhints}")
        if st.session_state.displayhints > 0:
            if st.button("Hint"):
               st.session_state.displayswitches = True
               st.session_state.displayhints -= 1
               st.rerun()

def SwitchGameGlitch(): #Not Done
    st.title(f"Level {st.session_state.currentlevel}")
    if st.session_state.displayswitches:
        st.write("HEHEHE-$ AND SHEITCHW 0@#%?d REBMEMER HAHA!!@)@(#) HWCAT@@}D???")
        wait(3)
        SwitchDisplayG()
        st.session_state.displayswitches = False
        st.rerun()
    else:
        elapsed_time = time.time() - st.session_state.start_time
        remaining_time = max(0, st.session_state.max_time - elapsed_time)
        progress = 1 - (remaining_time / st.session_state.max_time)
        fakeprog = rng(1, 95)
    
        timertext = f"Time Left?"
        timerbar = st.progress(fakeprog, text=timertext)
    
        if remaining_time <= 0:
            st.error("Time ran out, you lost")
            if st.button("Back to Menu"):
                endrun()
            return
    
        row1, row2 = st.columns(2)
        with row1:
            switch1 = st.toggle("1")
            switch3 = st.toggle("3")
            switch5 = st.toggle("5")
            switch7 = st.toggle("7")
            switch9 = st.toggle("9")

        with row2:
            switch2 = st.toggle("2")
            switch4 = st.toggle("4")
            switch6 = st.toggle("6")
            switch8 = st.toggle("8")
            switch10 = st.toggle("10")

        if st.button("Submit"):
            SwitchCheckG(switch1, switch2, switch3, switch4, switch5, switch6, switch7, switch8, switch9, switch10)
        
        st.write(f"Hints remaining: {st.session_state.displayhints}")
        if st.session_state.displayhints > 0:
            if st.button("NITH?@@#!"):
                if st.session_state.glitch == 2:
                    st.error("Y0u TH@O!!T??#%HAH---zzz")
                else:
                    st.session_state.displayswitches = True
                    st.session_state.displayhints -= 1
                    st.rerun()

def SwitchGameExam(): #Idea: 100 switches and graded based on how many correct.
    pass 

def SwitchDisplay():
    delay = 1.0
    lvldispspeed = (st.session_state.currentlevel - 1) * 0.018
    dispdelay = max(0.1, delay - lvldispspeed)
    
    display_area = st.empty()
    
    for repeat in range(1):
        decoyswitches = switchlayout.copy()
        shuffle(decoyswitches)
        
        for switch in decoyswitches:
            display_area.info(f"Switch {switch['SwitchNum']}: {switch['State']}")
            wait(dispdelay)
            
        display_area.empty()
        wait(1)

def SwitchDisplayHC():
    delay = 2.0
    lvldispspeed = (st.session_state.currentlevel - 1) * 0.032
    dispdelay = max(0.4, delay - lvldispspeed)
    
    display_area = st.empty()
    
    for repeat in range(1):
        decoyswitches = switchlayout.copy()
        shuffle(decoyswitches)
        
        for switch in decoyswitches:
            display_area.info(f"Switch {switch['SwitchNum']}: {switch['State']}")
            wait(dispdelay)
            
        display_area.empty()
        wait(1)

def SwitchDisplayPM():
    delay = 1.5
    lvldispspeed = (st.session_state.currentlevel - 1) * 0.024
    dispdelay = max(0.3, delay - lvldispspeed)
    
    display_area = st.empty()
    
    for repeat in range(3):
        decoyswitches = switchlayout.copy()
        shuffle(decoyswitches)
        
        for switch in decoyswitches:
            display_area.info(f"Switch {switch['SwitchNum']}: {switch['State']}")
            wait(dispdelay)
            
        display_area.empty()
        wait(1.5)

def SwitchDisplayGS():
    delay = 0.8
    lvldispspeed = (st.session_state.currentlevel - 1) * 0.01
    dispdelay = max(0.3, delay - lvldispspeed)
    
    display_area = st.empty()
    
    for repeat in range(1):
        decoyswitches = switchlayout.copy()
        shuffle(decoyswitches)
        
        for switch in decoyswitches:
            display_area.info(f"Switch {switch['SwitchNum']}: {switch['State']}")
            wait(dispdelay)
            
        display_area.empty()
        wait(0.5)

def SwitchDisplayPP():
    delay = 2.0
    lvldispspeed = (st.session_state.currentlevel - 1) * 0.032
    dispdelay = max(0.4, delay - lvldispspeed)
    
    display_area = st.empty()
    
    for repeat in range(1):
        decoyswitches = switchlayout.copy()
        shuffle(decoyswitches)
        
        for switch in decoyswitches:
            display_area.info(f"Switch {switch['SwitchNum']}: {switch['State']}")
            wait(dispdelay)
            
        display_area.empty()
        wait(1)

def SwitchDisplayMH():
    display_area = st.empty()
    
    for repeat in range(1):
        decoyswitches = switchlayout.copy()
        shuffle(decoyswitches)
        
        for switch in decoyswitches:
            display_area.info(f"Switch {switch['SwitchNum']}: {switch['State']}")
            wait(0.5)
            
        display_area.empty()
        wait(1)

def SwitchDisplayHnS():
    delay = 1.5
    lvldispspeed = (st.session_state.currentlevel - 1) * 0.022
    dispdelay = max(0.4, delay - lvldispspeed)
    shownswitch = 0
    
    display_area = st.empty()
    if st.session_state.currentlevel > 10:
        shownswitch = 8
    elif st.session_state.currentlevel > 25:
        shownswitch = 7
    elif st.session_state.currentlevel > 40:
        shownswitch = 6
    elif st.session_state.currentlevel > 50:
        shownswitch = 5
    else:
        shownswitch = 9
    
    for repeat in range(1):
        decoyswitches = switchlayout.copy()
        shuffle(decoyswitches)
        
        for switch in decoyswitches:
            if shownswitch > 0:
                display_area.info(f"Switch {switch['SwitchNum']}: {switch['State']}")
                shownswitch -= 1
            else:
                display_area.info(f"Switch ???: ???")
            wait(dispdelay)
            
        display_area.empty()
        wait(1)

def SwitchDisplayEM():
    delay = 0.5
    lvldispspeed = (st.session_state.currentlevel - 1) * 0.02
    dispdelay = max(0.1, delay - lvldispspeed)
    
    display_area = st.empty()
    
    for repeat in range(1):
        decoyswitches = switchlayout.copy()
        shuffle(decoyswitches)
        
        for switch in decoyswitches:
            display_area.info(f"Switch {switch['SwitchNum']}: {switch['State']}")
            wait(dispdelay)
            
        display_area.empty()
        wait(1)

def SwitchDisplayBD():
    display_area = st.empty()
    for repeat in range(1):
        decoyswitches = switchlayout.copy()
        shuffle(decoyswitches)
        
        for switch in decoyswitches:
            display_area.info(f"Switch {switch['SwitchNum']}: {switch['State']}")
            wait(1)
            
        display_area.empty()
        wait(1)

def SwitchDisplayRNG():
    speed_level = rng(1, 5)
    display_delay = 1.0 - (speed_level * 0.16)
        
    display_area = st.empty()
        
    for repeat in range(1):
        decoyswitches = switchlayout.copy()
        shuffle(decoyswitches)
            
        for switch in decoyswitches:
            display_area.info(f"Switch {switch['SwitchNum']}: {switch['State']}")
            wait(display_delay)
                
        display_area.empty()
        wait(1)

def SwitchDisplayG():
    delay = 1.0
    lvldispspeed = (st.session_state.currentlevel - 1) * 0.016
    dispdelay = max(0.2, delay - lvldispspeed)
    
    display_area = st.empty()
    
    for repeat in range(1):
        decoyswitches = switchlayout.copy()
        shuffle(decoyswitches)
        
        for switch in decoyswitches:
            numorstate = rng(1, 3)
            if numorstate == 1:
                display_area.info(f"Switch {switch['SwitchNum']}: ???")
            elif numorstate == 3:
                display_area.info(f"Switch ???: {switch['State']}")
            else:
                display_area.info(f"Switch {switch['SwitchNum']}: {switch['State']}")
            wait(dispdelay)
            
        display_area.empty()
        wait(1)

def SwitchRandomizer():
    if st.session_state.difficulty == "Normal" or st.session_state.difficulty == "RememberThem" or st.session_state.difficulty == "PerfectAccuracy" or st.session_state.difficulty == "Haste" or st.session_state.difficulty == "HiddenSwitches" or st.session_state.difficulty == "Eminem" or st.session_state.difficulty == "Glitched" or st.session_state.difficulty == "Tutorial":
        for r in range(10):
            onoroff = rng(0, 1)
            if onoroff == 0:
                switchlayout.append({"SwitchNum": r + 1, "State": "On"})
            else:
                switchlayout.append({"SwitchNum": r + 1, "State": "Off"})
    elif st.session_state.difficulty == "BrainFuck":
        for r in range(40):
            onoroff = rng(0, 1)
            if onoroff == 0:
                switchlayout.append({"SwitchNum": r + 1, "State": "On"})
            else:
                switchlayout.append({"SwitchNum": r + 1, "State": "Off"})
    elif st.session_state.difficulty == "Hardcore":
        for r in range(20):
            onoroff = rng(0, 1)
            if onoroff == 0:
                switchlayout.append({"SwitchNum": r + 1, "State": "On"})
            else:
                switchlayout.append({"SwitchNum": r + 1, "State": "Off"})
    elif st.session_state.difficulty == "GodSpeed":
        for r in range(6):
            onoroff = rng(0, 1)
            if onoroff == 0:                
                switchlayout.append({"SwitchNum": r + 1, "State": "On"})
            else:
                switchlayout.append({"SwitchNum": r + 1, "State": "Off"})
    elif st.session_state.difficulty == "RNGesus":
        rngswitches = rng(2, 20)
        for r in range(rngswitches):
            onoroff = rng(0, 1)
            if onoroff == 0:
                switchlayout.append({"SwitchNum": r + 1, "State": "On"})
            else:
                switchlayout.append({"SwitchNum": r + 1, "State": "Off"})

def SwitchCheck(switch1, switch2, switch3, switch4, switch5, switch6, switch7, switch8, switch9, switch10):
    switches = [switch1, switch2, switch3, switch4, switch5, switch6, switch7, switch8, switch9, switch10]
    correct = sum(1 for switch, layout in zip(switches, switchlayout) 
                 if (switch and layout["State"] == "On") or (not switch and layout["State"] == "Off"))

    if correct == 10:
        st.success("You got em all Correct!")
        st.session_state.currentlevel += 1
        st.session_state.start_time = time.time() 
        st.session_state.displayswitches = True
        st.session_state.displayhints = 3
        switchlayout.clear()
        SwitchRandomizer()
        wait(1.5)
        st.rerun()
    else:
        st.session_state.start_time -= 15
        st.error("One of the Switches is wrong")

def SwitchCheckHC(switch1, switch2, switch3, switch4, switch5, switch6, switch7, switch8, switch9, switch10, switch11, switch12, switch13, switch14, switch15, switch16, switch17, switch18, switch19, switch20):
    switches = [switch1, switch2, switch3, switch4, switch5, switch6, switch7, switch8, switch9, switch10, switch11, switch12, switch13, switch14, switch15, switch16, switch17, switch18, switch19, switch20]
    correct = sum(1 for switch, layout in zip(switches, switchlayout) 
                 if (switch and layout["State"] == "On") or (not switch and layout["State"] == "Off"))

    if correct == 20:
        st.success("You got em all Correct!")
        st.session_state.currentlevel += 1
        st.session_state.start_time = time.time() 
        st.session_state.displayswitches = True
        st.session_state.displayhints = 2
        switchlayout.clear()
        SwitchRandomizer()
        wait(1.5)
        st.rerun()
    else:
        st.session_state.start_time -= 10
        st.error("One of the Switches is wrong")

def SwitchCheckPM(switch1, switch2, switch3, switch4, switch5, switch6, switch7, switch8, switch9, switch10):
    switches = [switch1, switch2, switch3, switch4, switch5, switch6, switch7, switch8, switch9, switch10]
    correct = sum(1 for switch, layout in zip(switches, switchlayout) 
                 if (switch and layout["State"] == "On") or (not switch and layout["State"] == "Off"))

    if correct == 10:
        st.success("You got em all Correct!")
        st.session_state.currentlevel += 1
        st.session_state.start_time = time.time() 
        st.session_state.displayswitches = True
        st.session_state.displayhints = 1
        switchlayout.clear()
        SwitchRandomizer()
        wait(1.5)
        st.rerun()
    else:
        st.session_state.start_time -= 30
        st.error("One of the Switches is wrong")

def SwitchCheckGS(switch1, switch2, switch3, switch4, switch5, switch6):
    switches = [switch1, switch2, switch3, switch4, switch5, switch6]
    correct = sum(1 for switch, layout in zip(switches, switchlayout) 
                 if (switch and layout["State"] == "On") or (not switch and layout["State"] == "Off"))

    if correct == 6:
        st.success("You got em all Correct!")
        st.session_state.currentlevel += 1
        st.session_state.displayswitches = True
        switchlayout.clear()
        SwitchRandomizer()
        wait(1)
        st.rerun()
    else:
        st.error("One of the Switches is wrong")

def SwitchCheckPP(switch1, switch2, switch3, switch4, switch5, switch6, switch7, switch8, switch9, switch10):
    switches = [switch1, switch2, switch3, switch4, switch5, switch6, switch7, switch8, switch9, switch10]
    correct = sum(1 for switch, layout in zip(switches, switchlayout) 
                 if (switch and layout["State"] == "On") or (not switch and layout["State"] == "Off"))

    if correct == 10:
        st.success("You got em all Correct!")
        st.session_state.currentlevel += 1
        st.session_state.displayswitches = True
        switchlayout.clear()
        SwitchRandomizer()
        wait(1)
        st.rerun()
    else:
        st.session_state.perfect = False
        st.rerun()

def SwitchCheckMH(switch1, switch2, switch3, switch4, switch5, switch6, switch7, switch8, switch9, switch10):
    switches = [switch1, switch2, switch3, switch4, switch5, switch6, switch7, switch8, switch9, switch10]
    correct = sum(1 for switch, layout in zip(switches, switchlayout) 
                 if (switch and layout["State"] == "On") or (not switch and layout["State"] == "Off"))

    if correct == 10:
        st.success("You got em all Correct!")
        st.session_state.givebonus += 1
        if st.session_state.givebonus == 5:
            st.session_state.start_time += 120
            st.session_state.displayhints += 3
            st.session_state.givebonus = 0
    
        st.session_state.currentlevel += 1
        st.session_state.displayswitches = True
        switchlayout.clear()
        SwitchRandomizer()
        wait(1.5)
        st.rerun()
    else:
        st.session_state.start_time -= 20
        st.error("One of the Switches is wrong")

def SwitchCheckHnS(switch1, switch2, switch3, switch4, switch5, switch6, switch7, switch8, switch9, switch10):
    switches = [switch1, switch2, switch3, switch4, switch5, switch6, switch7, switch8, switch9, switch10]
    correct = sum(1 for switch, layout in zip(switches, switchlayout) 
                 if (switch and layout["State"] == "On") or (not switch and layout["State"] == "Off"))

    if correct == 10:
        st.success("You got em all Correct!")
        st.session_state.currentlevel += 1
        st.session_state.start_time = time.time() 
        st.session_state.displayswitches = True
        st.session_state.displayhints = 5
        switchlayout.clear()
        SwitchRandomizer()
        wait(1.5)
        st.rerun()
    else:
        st.session_state.start_time -= 15
        st.error("One of the Switches is wrong")

def SwitchCheckEM(switch1, switch2, switch3, switch4, switch5, switch6, switch7, switch8, switch9, switch10):
    switches = [switch1, switch2, switch3, switch4, switch5, switch6, switch7, switch8, switch9, switch10]
    correct = sum(1 for switch, layout in zip(switches, switchlayout) 
                 if (switch and layout["State"] == "On") or (not switch and layout["State"] == "Off"))

    if correct == 10:
        st.success("You got em all Correct!")
        st.session_state.currentlevel += 1
        st.session_state.start_time = time.time() 
        st.session_state.displayswitches = True
        st.session_state.displayhints = 10
        switchlayout.clear()
        SwitchRandomizer()
        wait(1.5)
        st.rerun()
    else:
        st.session_state.start_time -= 40
        st.error("One of the Switches is wrong")

def SwitchCheckBD(switch1, switch2, switch3, switch4, switch5, switch6, switch7, switch8, switch9, switch10, switch11, switch12, switch13, switch14, switch15, switch16, switch17, switch18, switch19, switch20, switch21, switch22, switch23, switch24, switch25, switch26, switch27, switch28, switch29, switch30, switch31, switch32, switch33, switch34, switch35, switch36, switch37, switch38, switch39, switch40):
    switches = [switch1, switch2, switch3, switch4, switch5, switch6, switch7, switch8, switch9, switch10, switch11, switch12, switch13, switch14, switch15, switch16, switch17, switch18, switch19, switch20, switch21, switch22, switch23, switch24, switch25, switch26, switch27, switch28, switch29, switch30, switch31, switch32, switch33, switch34, switch35, switch36, switch37, switch38, switch39, switch40]
    correct = sum(1 for switch, layout in zip(switches, switchlayout) 
                 if (switch and layout["State"] == "On") or (not switch and layout["State"] == "Off"))

    if correct == 40:
        st.success("You got em all Correct!")
        st.session_state.currentlevel += 1
        st.session_state.displayswitches = True
        st.session_state.displayhints = 4
        switchlayout.clear()
        SwitchRandomizer()
        wait(1.5)
        st.session_state.start_time = time.time() 
        st.rerun()
    else:
        st.session_state.start_time -= 15
        st.error("One of the Switches is wrong")

def SwitchCheckRNG(levelswitches):
    correct = sum(1 for switch, layout in zip(levelswitches, switchlayout) 
                 if (switch and layout["State"] == "On") or (not switch and layout["State"] == "Off"))

    if correct == len(switchlayout):
        st.success("You got em all Correct!")
        st.session_state.currentlevel += 1
        st.session_state.max_time = rng(60, 320)
        st.session_state.displayhints = rng(1, 5)
        st.session_state.displayswitches = True
        switchlayout.clear()
        SwitchRandomizer()
        wait(1.5)
        st.session_state.start_time = time.time()
        st.rerun()
    else:
        st.session_state.start_time -= 15
        st.error("One of the Switches is wrong")

def SwitchCheckG(switch1, switch2, switch3, switch4, switch5, switch6, switch7, switch8, switch9, switch10):
    switches = [switch1, switch2, switch3, switch4, switch5, switch6, switch7, switch8, switch9, switch10]
    correct = sum(1 for switch, layout in zip(switches, switchlayout) 
                 if (switch and layout["State"] == "On") or (not switch and layout["State"] == "Off"))

    if correct == 10:
        st.success("HOW!-Di--@?>}@$!%@####")
        st.session_state.currentlevel += 1
        st.session_state.start_time = time.time() 
        st.session_state.glitch = rng(1, 4)
        st.session_state.displayswitches = True
        st.session_state.displayhints = 6
        switchlayout.clear()
        SwitchRandomizer()
        wait(1.5)
        st.rerun()
    else:
        st.error("UH-0H B4D D3C####CION?!?!?!")

def whatuthinkurdoing():
    lel = rng(1, 5)
    if lel == 1:
        st.error("You are not the Developer bud, GET OUT!!!!!")
    elif lel == 2:
        st.error("Its the easiest password in the world, how can you not get it?")
    elif lel == 3:
        st.error("Nice Try, you should try use your Personal Password accounts like Google, Steam, etc and see if it works.")
    elif lel == 4:
        st.error("How about pay me 200$ and I'll let you in? Sound good right?")
    elif lel == 5:
        st.error("Keep trying, im almost finished")

def achievementpage():
    pass

def leaderboard():
    st.title("Leaderboard") 
    selectgamemode = st.selectbox("Select Game Mode", ["Normal", "Hardcore"])
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write(":medal: Rank")
    with col2:
        st.write("Player") 
    with col3:
        st.write(":checkered_flag: Level")

    data = normallb if selectgamemode == "Normal" else hardcorelb
    for i, entry in enumerate(data, 1):
        with col1:
            st.write(f"#{i}")
        with col2:
            st.write(entry['name'])
        with col3: 
            st.write(entry['level'])

def leaderboardinfo():
    st.write("This is the Place where Players who achieved great Runs are Displayed!")
    st.write("The leaderboard Updates around 2 days to 2 weeks. so if you beat one of the top ten Players and haven't seen your name, Please wait")
    st.title("How 2 Enter")
    st.write("At the end of your run, you must atleast reach level 20 or higher. Below that is ignored")
    st.write("Also theres no need to DM/Contact me a proof of your run. The game automatically saves your Run and send it to me.")

def playtutorial():
    st.session_state.max_time = 161
    st.session_state.displayhints = 3
    st.session_state.currentlevel = 1
    st.session_state.tutorialstage = 0 
    st.session_state.displayswitches = True
    st.session_state.difficulty = "Tutorial"
    SwitchRandomizer()
    if st.session_state.loggedin:
        st.session_state.currentpage = "TutorialGame"
    else:
        st.session_state.currentpage = "DevTutorialGame"
    st.rerun()

def aboutme():
    st.image("Other/HEHEHEHA.jpeg")
    st.title("About Me")
    st.write("Hiya there!, im Fajar or FajZ whatever you wanna call me with, an Indonesian Developer who made this dumb silly web project cuz im bored. anyway have fun xd.")

def UpdateBoard():
    st.title("Updates")
    stoggle("v1.0.0", """Changes:

        - Initial Release, nothing special.
    """)
