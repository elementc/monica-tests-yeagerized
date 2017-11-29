from yeager import reachable_states

# parse the transtitions...
import state_transitions.headerpage
import state_transitions.contacts
import state_transitions.login

if __name__ == "__main__":
    print("Yeager can find a path from the entry point to these states:")
    for state in reachable_states():
        print(state)
