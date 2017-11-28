class OptionNotFoundException(Exception):
    pass

class PageBase:
    def initial_status(self):
        pass

    def __init__(self, driver):
        self.driver = driver
        self.initial_status()

    def choose_from_multiselect(self, select_tag, choice):
        opts = select_tag.find_elements_by_tag_name("option")
        for opt in opts:
            if opt.text.strip() == choice:
                opt.click()
                return
        raise OptionNotFoundException("No such option %s" % choice)
