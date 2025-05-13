from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import data
from selenium.webdriver import Keys
from retrivecode import retrieve_code
from locators import UrbanRoutesEsLocators


class UrbanRoutesEsMethods:
    def __init__(self, driver):
        self.driver = driver
        self.locators = UrbanRoutesEsLocators

    def set_from(self):
        WebDriverWait(self.driver, 2).until(
            EC.visibility_of_element_located(UrbanRoutesEsLocators.from_field))
        self.driver.find_element(*UrbanRoutesEsLocators.from_field).send_keys(data.address_from)

    def set_to(self):
        WebDriverWait(self.driver, 2).until(
            EC.visibility_of_element_located(UrbanRoutesEsLocators.to_field))
        self.driver.find_element(*UrbanRoutesEsLocators.to_field).send_keys(data.address_to)

    def get_from(self):
        return self.driver.find_element(*UrbanRoutesEsLocators.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*UrbanRoutesEsLocators.to_field).get_property('value')

    def click_pedir_taxi_button(self):
        self.driver.find_element(*UrbanRoutesEsLocators.PEDIR_TAXI_BUTTON).click()

    def click_tarifa_comfort_button(self):
        WebDriverWait(self.driver, 2).until(
            EC.element_to_be_clickable(UrbanRoutesEsLocators.TARIFA_COMFORT_BUTTON))
        self.driver.find_element(*UrbanRoutesEsLocators.TARIFA_COMFORT_BUTTON).click()

    def tarif_selected(self):
        return self.driver.find_element(*UrbanRoutesEsLocators.TARIFA_COMFORT_SELECTED).is_displayed()

    def click_phone_number_display(self):
        self.driver.find_element(*UrbanRoutesEsLocators.PHONE_NUMBER_DISPLAY).click()

    def enter_phone_number(self):
        WebDriverWait(self.driver, 2).until(
            EC.visibility_of_element_located(UrbanRoutesEsLocators.PHONE_INPUT_FIELD)).send_keys(data.phone_number)
        self.driver.find_element(*UrbanRoutesEsLocators.NEXT_BUTTON).click()

    def enter_code(self):
        phonecodehelper = retrieve_code(self.driver)
        code = phonecodehelper.retrieve_phone_code(self.driver)
        WebDriverWait(self.driver, 2).until(
            EC.visibility_of_element_located(UrbanRoutesEsLocators.CODE_INPUT_FIELD))
        self.driver.find_element(*UrbanRoutesEsLocators.CODE_INPUT_FIELD).send_keys(code)
        self.driver.find_element(*UrbanRoutesEsLocators.CONFIRM_BUTTON).click()

    def correct_phone_number(self):
        return self.driver.find_element(*UrbanRoutesEsLocators.PHONE_NUMBER_FILLED).text


    def click_ppo(self):
        WebDriverWait(self.driver, 2).until(
            EC.visibility_of_element_located(UrbanRoutesEsLocators.PREFERRED_PAYMENT_OPTION)).click()

    def click_add_card(self):
        WebDriverWait(self.driver, 2).until(
            EC.visibility_of_element_located(UrbanRoutesEsLocators.ADD_CARD)).click()

    def click_card_number_display(self):
        WebDriverWait(self.driver, 2).until(
            EC.visibility_of_element_located(UrbanRoutesEsLocators.CARD_NUMBER_DISPLAY))

    def input_card_number(self):
        self.driver.find_element(*UrbanRoutesEsLocators.CARD_NUMBER_INPUT).send_keys(data.card_number)

    def click_card_code_display(self):
        self.driver.find_element(*UrbanRoutesEsLocators.CARD_CODE_DISPLAY)

    def input_card_code(self):
        self.driver.find_element(*UrbanRoutesEsLocators.CARD_CODE_DISPLAY).send_keys(data.card_code)
        self.driver.find_element(*UrbanRoutesEsLocators.CARD_CODE_DISPLAY).send_keys(Keys.TAB)

    def click_add_button(self):
        WebDriverWait(self.driver, 2).until(
            EC.visibility_of_element_located(UrbanRoutesEsLocators.ADD_BUTTON)).click()

    def click_close_button(self):
        WebDriverWait(self.driver, 2).until(
            EC.visibility_of_element_located(UrbanRoutesEsLocators.CLOSE_BUTTON)).click()

    def card_added(self):
        return self.driver.find_element(*UrbanRoutesEsLocators.PP_VALUE).text

    def input_driver_message(self):
        self.driver.find_element(*UrbanRoutesEsLocators.DRIVER_MESSAGE_INPUT).send_keys(data.message_for_driver)

    def correct_driver_message(self):
        return self.driver.find_element(*UrbanRoutesEsLocators.DRIVER_MESSAGE_INPUT).get_property('value')

    def slide_handkerchief(self):
        self.driver.find_element(*UrbanRoutesEsLocators.HANDKERCHIEF_SLIDE).click()

    def handkerchief_slide_selected(self):
        return self.driver.find_element(*UrbanRoutesEsLocators.HANDKERCHIEF_SLIDE_SELECTED).is_selected

    def first_click_ice_cream(self):
        self.driver.find_element(*UrbanRoutesEsLocators.ICE_CREAM_PLUS).click()

    def correct_counter_value(self):
        return self.driver.find_element(*UrbanRoutesEsLocators.COUNTER_VALUE).text

    def second_click_ice_cream(self):
        WebDriverWait(self.driver, 2).until(
            EC.visibility_of_element_located(UrbanRoutesEsLocators.ICE_CREAM_PLUS)).click()

    def order_a_taxi_click(self):
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(UrbanRoutesEsLocators.ORDER_A_TAXI))
        self.driver.find_element(*UrbanRoutesEsLocators.ORDER_A_TAXI).click()

    def details_button(self):
        return self.driver.find_element(*UrbanRoutesEsLocators.DETALLES_BUTTON).is_displayed()

    def displayed_driver_name(self):
        return self.driver.find_element(*UrbanRoutesEsLocators.DRIVER_NAME).is_located()

    def wait_driver_name(self):
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(UrbanRoutesEsLocators.DRIVER_NAME))


