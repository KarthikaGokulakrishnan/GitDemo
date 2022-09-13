from selenium.webdriver.common.by import By


class PurchasePage:
    def __init__(self,driver):
        self.driver = driver

    Country=(By.ID,"country")
    CountryName=(By.XPATH,"//div[@class='suggestions']/ul/li/a")
    CheckBox=(By.XPATH,"//label[@for='checkbox2']")
    submit = (By.XPATH,"//input[@type='submit']")
    actualMessage=(By.XPATH,"//div[@class='alert alert-success alert-dismissible']")

    def getCountrySug(self):
        return self.driver.find_element(*PurchasePage.Country)

    def getCountryName(self):
        return self.driver.find_elements(*PurchasePage.CountryName)

    def getCheckBox(self):
        return self.driver.find_element(*PurchasePage.CheckBox)
    def getSubmit(self):
        return self.driver.find_element(*PurchasePage.submit)
    def getActualMessage(self):
        return self.driver.find_element(*PurchasePage.actualMessage)