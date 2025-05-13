import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import UrbanRoutesEsLocators
from Methods import UrbanRoutesEsMethods


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("perfLoggingPrefs", {'enableNetwork': True, 'enablePage': True})
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.get(data.urban_routes_url)
        cls.UrbanRoutesEsMethods = UrbanRoutesEsMethods(cls.driver)

    def test_set_route(self):
        self.UrbanRoutesEsMethods.set_from()
        self.UrbanRoutesEsMethods.set_to()
        address_from = data.address_from
        address_to = data.address_to
        assert self.UrbanRoutesEsMethods.get_from() == address_from
        assert self.UrbanRoutesEsMethods.get_to() == address_to

    def test_select_tariff(self):
        self.UrbanRoutesEsMethods.click_pedir_taxi_button()
        selected_tariff_false = self.UrbanRoutesEsMethods.tarif_selected()
        self.UrbanRoutesEsMethods.click_tarifa_comfort_button()
        selected_tariff = self.UrbanRoutesEsMethods.tarif_selected()
        assert  selected_tariff_false != selected_tariff

    def test_phone_number(self):
        self.UrbanRoutesEsMethods.click_phone_number_display()
        self.UrbanRoutesEsMethods.enter_phone_number()
        self.UrbanRoutesEsMethods.enter_code()
        correct_phone_number = data.phone_number
        phone_number_on_field = self.UrbanRoutesEsMethods.correct_phone_number()
        assert phone_number_on_field == correct_phone_number

    def test_preferred_payment(self):
        initial_payment_method = self.UrbanRoutesEsMethods.card_added()
        self.UrbanRoutesEsMethods.click_ppo()
        self.UrbanRoutesEsMethods.click_add_card()
        self.UrbanRoutesEsMethods.click_card_number_display()
        self.UrbanRoutesEsMethods.input_card_number()
        self.UrbanRoutesEsMethods.click_card_code_display()
        self.UrbanRoutesEsMethods.input_card_code()
        self.UrbanRoutesEsMethods.click_add_button()
        self.UrbanRoutesEsMethods.click_close_button()
        final_payment_method = self.UrbanRoutesEsMethods.card_added()
        assert initial_payment_method != final_payment_method

    def test_driver_message(self):
        self.UrbanRoutesEsMethods.input_driver_message()
        correct_driver_message = data.message_for_driver
        driver_message_on_field = self.UrbanRoutesEsMethods.correct_driver_message()
        assert driver_message_on_field == correct_driver_message

    def test_handkerchief_slide(self):
        slide_not_selected = self.UrbanRoutesEsMethods.handkerchief_slide_selected()
        self.UrbanRoutesEsMethods.slide_handkerchief()
        slide_selected = self.UrbanRoutesEsMethods.handkerchief_slide_selected()
        assert slide_not_selected != slide_selected

    def test_double_icecream(self):
        self.UrbanRoutesEsMethods.first_click_ice_cream()
        self.UrbanRoutesEsMethods.second_click_ice_cream()
        assert self.UrbanRoutesEsMethods.correct_counter_value() == '2'

    def test_order_taxi(self):
        details_not_displayed = self.UrbanRoutesEsMethods.details_button()
        self.UrbanRoutesEsMethods.order_a_taxi_click()
        details_is_displayed = self.UrbanRoutesEsMethods.details_button()
        assert details_not_displayed != details_is_displayed

    def test_driver_info(self):
        self.UrbanRoutesEsMethods.wait_driver_name()
        self.UrbanRoutesEsMethods.displayed_driver_name()
        assert self.UrbanRoutesEsMethods.displayed_driver_name() is True

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
