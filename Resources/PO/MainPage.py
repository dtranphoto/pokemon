from Resources.Locators.locators import Locators

class MainPage():

    def __init__(self, driver):
        self.driver = driver

        self.pokedex_button_xpath = Locators.pokedex_button_xpath
        self.video_game_button_xpath = Locators.video_game_button_xpath
        self.trading_card_button_xpath = Locators.trading_card_button_xpath
        self.tv_button_xpath = Locators.tv_button_xpath
        self.play_button_xpath = Locators.play_button_xpath
        self.news_button_xpath = Locators.news_button_xpath

    def click_pokedex(self):
        self.driver.find_element_by_xpath(self.pokedex_button_xpath).click()

    def click_video_game(self):
        self.driver.find_element_by_xpath(self.video_game_button_xpath).click()

    def click_tcg(self):
        self.driver.find_element_by_xpath(self.trading_card_button_xpath).click()

    def click_tv(self):
        self.driver.find_element_by_xpath(self.tv_button_xpath).click()

    def click_play(self):
        self.driver.find_element_by_xpath(self.play_button_xpath).click()

    def click_news(self):
        self.driver.find_element_by_xpath(self.news_button_xpath).click()