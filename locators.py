from selenium.webdriver.common.by import By


class UrbanRoutesEsLocators:
    from_field = (By.ID, 'from')

    to_field = (By.ID, 'to')

    PEDIR_TAXI_BUTTON = (By.XPATH, "//button[text()='Pedir un taxi']")

    TARIFA_COMFORT_BUTTON = (By.XPATH, "//div[text()='Comfort']")

    TARIFA_COMFORT_SELECTED = (By.XPATH, "//button[@data-for='tariff-card-4']")

    PHONE_NUMBER_DISPLAY = (By.XPATH, "//div[text()='Número de teléfono']")

    PHONE_NUMBER_FILLED = (By.CSS_SELECTOR, ".np-text")

    PHONE_INPUT_FIELD = (By.ID, "phone")

    NEXT_BUTTON = (By.XPATH, "//button[text()='Siguiente']")

    CODE_INPUT_FIELD = (By.XPATH, '//*[@id="code"]')

    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Confirmar']")

    PREFERRED_PAYMENT_OPTION = (By.CSS_SELECTOR, '.pp-button')

    ADD_CARD = (By.XPATH, "//div[text()='Agregar tarjeta']")

    CARD_NUMBER_DISPLAY = (By.XPATH, '//*[@id="number"]')

    CARD_NUMBER_INPUT = (By.ID, "number")

    CARD_CODE_DISPLAY = (By.XPATH, "//input[@placeholder='12']")

    CARD_CODE_INPUT = (By.ID, "code")

    ADD_BUTTON = (By.XPATH, "//button[text()='Agregar']")

    CLOSE_BUTTON = (By.CSS_SELECTOR, '.payment-picker .close-button')

    PP_VALUE = (By.CLASS_NAME, "pp-value-text")

    DRIVER_MESSAGE_INPUT = (By.ID, "comment")

    HANDKERCHIEF_SLIDE = (By.XPATH, "/html/body/div/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span")

    HANDKERCHIEF_SLIDE_SELECTED = (By.XPATH, '/html/body/div/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/input')

    ICE_CREAM_PLUS = (By.XPATH, "/html/body/div/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]")

    COUNTER_VALUE = (By.XPATH, "/html/body/div/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[2]")

    ORDER_A_TAXI = (By.CSS_SELECTOR, ".smart-button")

    DETALLES_BUTTON = (By.CSS_SELECTOR,"div.order-btn-group:nth-child(2) > button:nth-child(1)")

    DRIVER_NAME = (By.XPATH, '//*[@id="root"]/div/div[5]/div[2]/div[2]/div[1]/div[1]/div[2]')

