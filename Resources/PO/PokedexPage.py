from Resources.Locators.locators import Locators

class PokedexPage():

    def __init__(self, driver):
        self.driver = driver

        self.pokedex_search_id = "searchInput"
        self.search_id = "search"
        self.first_result_xpath = "/html/body/div[4]/section[5]/ul/li/figure/a/img"
        self.pokedex_button_xpath = Locators.pokedex_button_xpath

    def enter_pokedex(self, pokedex):
        self.driver.find_element_by_id(self.pokedex_search_id).clear()
        self.driver.find_element_by_id(self.pokedex_search_id).send_keys(pokedex)

    def click_search(self):
        self.driver.find_element_by_id(self.search_id).click()

    def click_result(self):
        self.driver.find_element_by_xpath(self.first_result_xpath).click()

    def click_pokedex(self):
        self.driver.find_element_by_xpath(self.pokedex_button_xpath).click()