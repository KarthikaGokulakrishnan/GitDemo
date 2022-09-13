from selenium.webdriver.common.by import By

from PageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:
    def __init__(self,driver):
        self.driver=driver


    cardTitle=(By.XPATH,"//div[@class='card h-100']")
    productName=(By.XPATH, "div/h4/a")
    addButton=(By.XPATH,"(//div[@class='card-footer']/button)")
    checkoutButton=(By.XPATH,"//div/ul/li/a")

    def getCardTitle(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getProductName(self):
        return self.driver.find_element(*CheckOutPage.productName)

    def getAddButton(self):
        return self.driver.find_element(*CheckOutPage.addButton)

    def getCheckOutButton(self):
        self.driver.find_element(*CheckOutPage.checkoutButton).click()
        confirm = ConfirmPage(self.driver)
        return confirm