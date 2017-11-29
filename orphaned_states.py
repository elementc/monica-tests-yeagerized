from yeager import orphaned_states, state_transition

# parse the transtitions...
import state_transitions.headerpage
import state_transitions.contacts
import state_transitions.login

@state_transition("contactss-page", "dashboard-page")
def some_bad_funcion(driver):
    pass

if __name__ == "__main__":
    print("Yeager can't find a path from the entry point to these states:")
    for state in orphaned_states():
        print(state)
