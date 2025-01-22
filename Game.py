from time import sleep as wait
import streamlit as st
import time
from GameDirector.Director import getstates, login, leaderboard, leaderboardinfo, register, SwitchGame, SwitchGameHardcore, SwitchGamePureMemory, SwitchGameGodSpeed, SwitchGamePerfect, SwitchGameMakeHaste, SwitchGameSneaky, SwitchGameEminem, SwitchGameBrainDestroyer, SwitchGameRNGesus, SwitchGameGlitch, SwitchRandomizer, whatuthinkurdoing, mainpage, endrun, playnormal, playhardcore, hardcoredesc, purememorydesc, playpurememory, godspeeddesc, playgodspeed, perfectpercisiondesc, playperfectperc, makehastedesc, playmakehaste, sneakyswitchesdesc, playsneakyswitches, eminemdesc, playeminem, brainfucdesc, playbraindestroyer, rngesusdesc, playrngesus, glitcheddesc, playglitched, how2play, basicsh2p, switchstatesh2p, timerh2p, accountcreatortool, accountdeletortool, banaccounts, unbanaccount, gameresults, playtutorial, UpdateBoard, aboutme
from GameStuffs.Gamedata import switchlayout, useraccounts, bugreports, bannedaccounts, suggestions
getstates()
loggedin = st.session_state.get("loggedin", False)
developerlogin = st.session_state.get("developerlogin", False)
banned = st.session_state.get("banned", False)

if not loggedin and not developerlogin and not banned:
    loginpage = st.sidebar.radio("Welcome!", ["Welcome", "Login", "Register"])

    if loginpage == "Welcome":
        mainpage()

    if loginpage == "Login":
        st.title("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            login(username, password)

    if loginpage == "Register":
        register()

if st.session_state.loggedin:
    if st.session_state.currentpage == "Main":
        gamepage = st.sidebar.radio(f"Welcome {st.session_state.displayname}", ["Play", "How2Play", "Leaderboard", "Report Bugs", "Suggestion", "Updates", "About Dev"])
        if gamepage == "Play":
            difficulies = st.tabs(["Normal", "Hardcore"])
            with difficulies[0]:
                st.title("Normal Mode")
                st.write("Play with the base settings and difficulty of the game (RECOMMENDED FOR NEW PLAYERS)")
                if st.button("Play Normal"):
                    playnormal()
            with difficulies[1]:
                hardcoredesc()
                if st.button("Play Hardcore"):
                    playhardcore()
        if gamepage == "How2Play":
            h2p = st.tabs(["How 2 Play", "Basics", "Switch States", "Timer"])
            with h2p[0]:
                how2play()
            with h2p[1]:
                basicsh2p()
            with h2p[2]:
                switchstatesh2p()
            with h2p[3]:
                timerh2p()
        if gamepage == "Leaderboard":
            ldtab = st.tabs(["Leaderboard", "Info"])
            with ldtab[0]:
                leaderboard()
            with ldtab[1]:
                leaderboardinfo()
        if gamepage == "Report Bugs":
            st.title("Report Bugs")
            bugreport = st.text_input("Report a bug")
            if st.button("Report Bug"):
                bugreports.append({"User": st.session_state.displayname, "Bug": bugreport})
                st.success("Report Sent!, Thanks")
        if gamepage == "Suggestion":
            st.title("Suggestion Box")
            st.write("Here you can give me your Ideas for the game like Gamemodes, Features, etc!")
            if suggestions:
                st.dataframe(suggestions)
            if st.button("Refresh"):
                st.rerun()
            suggestion = st.chat_input("Send me your Ideas here!")
            if suggestion:
                suggestions.append({"User": st.session_state.displayname, "Idea": suggestion})
                st.rerun()
        if gamepage == "Updates":
            UpdateBoard()
        if gamepage == "About Dev":
            aboutme()

        if st.sidebar.button("Logout"):
            st.session_state.loggedin = False
            st.rerun()

    elif st.session_state.currentpage == "NormalGame":
        if st.sidebar.button("End Game"):
            endrun()
        SwitchGame()

    elif st.session_state.currentpage == "HardGame":
        if st.sidebar.button("End Game"):
            endrun()
        SwitchGameHardcore()

elif st.session_state.developerlogin:
    if st.session_state.currentpage == "DevMain":
        st.sidebar.title("Welcome Developer FajZ!")
        devpage = st.sidebar.radio("Dev Page", ["How2Play", "Play", "Leaderboard", "Achievements", "Updates", "About Dev", "Dev Panel"])
        if devpage == "How2Play":
            h2p = st.tabs(["How 2 Play", "Basics", "Switch States", "Timer"])
            with h2p[0]:
                how2play()
            with h2p[1]:
                basicsh2p()
            with h2p[2]:
                switchstatesh2p()
            with h2p[3]:
                timerh2p()
        if devpage == "Play":
            st.write("Hint: Hold SHIFT + MOUSE WHEEL to scroll through the Gamemodes")
            devdiff = st.tabs(["Normal", "Hardcore", "Pure Memory", "GodSpeed", "Perfect Percision", "Make Haste", "Sneaky Switches", "Eminem", "Brain Aneurysm", "RNGesus", "Glitched", "Tutorial"])
            with devdiff[0]:
                st.title("Normal Mode")
                st.write("Play with the base settings and difficulty of the game (RECOMMENDED FOR NEW PLAYERS)")
                if st.button("Play Normal Mode"):
                    playnormal()
            with devdiff[1]:
                hardcoredesc()
                if st.button("Play Hardcore Mode"):
                    playhardcore()
            with devdiff[2]:
                purememorydesc()
                if st.button("Play Pure Memory Mode"):
                    playpurememory()
            with devdiff[3]:
                godspeeddesc()
                if st.button("Play God Speed Mode"):
                    playgodspeed()
            with devdiff[4]:
                perfectpercisiondesc()
                if st.button("Play Perfect Percision Mode"):
                    playperfectperc()
            with devdiff[5]:
                makehastedesc()
                if st.button("Play Make Haste Mode"):
                    playmakehaste()
            with devdiff[6]:
                sneakyswitchesdesc()
                if st.button("Play Sneaky Switches Mode"):
                    playsneakyswitches()
            with devdiff[7]:
                eminemdesc()
                if st.button("Play Eminem Mode"):
                    playeminem()
            with devdiff[8]:
                brainfucdesc()
                if st.button("Play Brain Aneurysm Mode"):
                    playbraindestroyer()
            with devdiff[9]:
                rngesusdesc()
                if st.button("Play RNGesus Mode"):
                    playrngesus()
            with devdiff[10]:
                glitcheddesc()
                if st.button("Play Glitched Mode"):
                    playglitched()
            with devdiff[11]:
                st.title("Tutorial")
                st.write("You Read all the Instructions on the How2Play Page and still confused? Then go ahead enter a Tutorial Game for a quick rundown!")
                if st.button("Play Tutorial Mode"):
                    playtutorial()
        if devpage == "Leaderboard":
            lddevtab = st.tabs(["Leaderboard", "Info"])
            with lddevtab[0]:
                leaderboard()
            with lddevtab[1]:
                leaderboardinfo()
        if devpage == "Achievements":
            st.title("Achievements")
        if devpage == "Updates":
            UpdateBoard()
        if devpage == "About Dev":
            aboutme()
        if devpage == "Dev Panel":
            st.title("Dev Panel")
            if st.session_state.developerpanelaccess == False:
                getaccesbruh = st.text_input("To get access you must enter the Forbidden Password", type="password")
                if st.button("Submit"):
                    if getaccesbruh == "ThisIsTheApexDeveloperPanelPasswordToGetAccess2222222":
                        st.session_state.developerpanelaccess = True
                        st.rerun()
                    else:
                        whatuthinkurdoing()
            else:
                devpaneltab = st.tabs(["Account Bank", "Create Account", "Delete Account", "Ban Account", "Bug Reports", "Suggestions", "Game Results"])
                with devpaneltab[0]:
                    st.dataframe(useraccounts)
                with devpaneltab[1]:
                    st.title("Create Accounts")
                    username = st.text_input("Username")
                    password = st.text_input("Password", type="password")
                    if st.button("Create Account"):
                        accountcreatortool(username, password)
                with devpaneltab[2]:
                    st.title("Delete Accounts")
                    deluserinput = st.text_input("Target Username")
                    if st.button("Delete Account"):
                        accountdeletortool(deluserinput)
                with devpaneltab[3]:
                    st.title("Ban Accounts")
                    targetpunishuser = st.text_input("Target Account")
                    reason = st.text_input("Reason")
                    if st.button("Ban Account"):
                        banaccounts(targetpunishuser, reason)
                    if st.button("Unban Account"):
                        unbanaccount(targetpunishuser)
                    if bannedaccounts:
                        st.dataframe(bannedaccounts)
                with devpaneltab[4]:
                    st.title("Bug Reports")
                    if bugreports:
                        st.dataframe(bugreports)
                    else:
                        st.error("No Reports yet")
                with devpaneltab[5]:
                    st.title("Suggestions")
                    if suggestions:
                        st.dataframe(suggestions, width=1000)
                    else:
                        st.error("No Suggestions yet")
                    suggestreply = st.chat_input("Chat here")
                    if suggestreply:
                        suggestions.append({"User": "FajZ (Developer)", "Idea": suggestreply})
                        st.rerun()
                    if st.button("Refresh"):
                        st.rerun()
                with devpaneltab[6]:
                    gameresults()

        if st.sidebar.button("Logout"):
            st.session_state.developerpanelaccess = False
            st.session_state.developerlogin = False
            st.rerun()

    elif st.session_state.currentpage == "DevNormalGame":
        if st.sidebar.button("End Game"):
            endrun()
        SwitchGame()

    elif st.session_state.currentpage == "DevHardGame":
        if st.sidebar.button("End Game"):
            endrun()
        SwitchGameHardcore()

    elif st.session_state.currentpage == "PureMemoryGame":
        if st.sidebar.button("End Game"):
            endrun()
        SwitchGamePureMemory()

    elif st.session_state.currentpage == "FastAsFuckGame":
        if st.sidebar.button("End Game"):
            endrun()
        SwitchGameGodSpeed()

    elif st.session_state.currentpage == "PerfectGame":
        if st.sidebar.button("End Game"):
            endrun()
        SwitchGamePerfect()

    elif st.session_state.currentpage == "YouBetterRunGame":
        if st.sidebar.button("End Game"):
            endrun()
        SwitchGameMakeHaste()

    elif st.session_state.currentpage == "SneakyGame":
        if st.sidebar.button("End Game"):
            endrun()
        SwitchGameSneaky()

    elif st.session_state.currentpage == "EminemGame":
        if st.sidebar.button("End Game"):
            endrun()
        SwitchGameEminem()

    elif st.session_state.currentpage == "TortureGame":
        if st.sidebar.button("End Game"):
            endrun()
        SwitchGameBrainDestroyer()

    elif st.session_state.currentpage == "RNGGame":
        if st.sidebar.button("End Game"):
            endrun()
        SwitchGameRNGesus()

    elif st.session_state.currentpage == "GlitchedGame":
        if st.sidebar.button("End Game"):
            endrun()
        SwitchGameGlitch()

    elif st.session_state.currentpage == "No":
        devgamepage = st.tabs(["Game", "Cheat Panel"])
        if st.sidebar.button("End Game"):
            endrun()
        with devgamepage[0]:
            SwitchGame()
        with devgamepage[1]:
            st.title("Cheat Panel")
            cheattab = st.tabs(["Current Layout", "Other"])
            with cheattab[0]:
                st.dataframe(switchlayout)
            with cheattab[1]:
                st.title("huh")

elif st.session_state.banned:
    st.title("This Account has been Banned!")
    st.write(f"Reason: {st.session_state.bannedreason}")

    if st.sidebar.button("Logout"):
        st.session_state.banned = False
        st.rerun()
