from selenium import webdriver
from yeager import walk

# parse the transtitions...
import state_transitions.headerpage
import state_transitions.contacts
import state_transitions.login

walk(driver=webdriver.Chrome())
