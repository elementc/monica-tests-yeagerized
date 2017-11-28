from selenium import webdriver
from yeager import walk, enumerate_transitions
from yeager import state_transition

# parse the transtitions...
import state_transitions.headerpage
import state_transitions.contacts
import state_transitions.login


# walk(50, driver=webdriver.Chrome())
enumerate_transitions()
