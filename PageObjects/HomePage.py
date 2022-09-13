from selenium.webdriver.common.by import By

from PageObjects.CheckOutPage import CheckOutPage


class HomePage:
    def __init__(self,driver):
        self.driver = driver

    shop = (By.LINK_TEXT, "Shop")
    email = (By.NAME, "email")
    Password = (By.ID, "exampleInputPassword1")
    chekbox = (By.ID, "exampleCheck1")
    Name = (By.CSS_SELECTOR, "input[name='name']")
    option = (By.CSS_SELECTOR, "input[value='option1']")
    select = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@type='submit']")
    job = (By.XPATH, "(//input[@type='text'])[3]")
    job1 = (By.XPATH, "(//input[@type='text'])[3]")
    message = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")


    def ShopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        CardTitle = CheckOutPage(self.driver)
        return CardTitle
    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.Password)

    def getCheckbox(self):
        return self.driver.find_element(*HomePage.chekbox)

    def getname(self):
        return self.driver.find_element(*HomePage.Name)

    def getoption(self):
        return self.driver.find_element(*HomePage.option)

    def getselect(self):
        return self.driver.find_element(*HomePage.select)

    def getSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getJob(self):
        return self.driver.find_element(*HomePage.job)

    def getmessage(self):
        return self.driver.find_element(*HomePage.message)

    def getJob1(self):
        return self.driver.find_element(*HomePage.job1)
