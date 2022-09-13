from selenium.webdriver.common.by import By

from PageObjects.PurchasePage import PurchasePage


class ConfirmPage:
    def __init__(self,driver):
        self.driver=driver

    ConfirmCheckout=(By.XPATH,"//button[@class='btn btn-success']")

    def getCK2Button(self):
        self.driver.find_element(*ConfirmPage.ConfirmCheckout).click()
        purchasepage = PurchasePage(self.driver)
        return purchasepage