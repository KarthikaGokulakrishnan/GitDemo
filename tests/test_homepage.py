import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PageObjects.HomePage import HomePage
from TestData.HomePageData import HomePageData

from Utilities.BaseClass import BaseClass


class Testhomepage(BaseClass):
    def test_formSubmission(self,getData):
        log = self.getlogger()
        # Locators-ID,Name,Class Name,Xpath,CSS Selector,link text
        homePage = HomePage(self.driver)
        homePage.getEmail().send_keys(getData["email"])
        #homePage.getEmail().send_keys(getData[0])
        homePage.getPassword().send_keys(getData["Password"])
        #homePage.getPassword().send_keys(getData[1])
        homePage.getCheckbox().click()
        homePage.getname().send_keys(getData["Name"])
        #homePage.getname().send_keys(getData[2])
        homePage.getoption().click()
        # create XPAth for any element syntax //tagname[@attribute='value'], #id, .classname
        # create CSS Selector for any element syntax tagname[attribute='value']
        # Static Drop Down
        self.selectOptionbyText(homePage.getselect(),getData["Gender"])
        #self.selectOptionbyText(homePage.getselect(), getData[3])
        homePage.getSubmit().click()
        Alertmessage = homePage.getmessage().text
        log.info(Alertmessage)
        assert "Success" in Alertmessage
        homePage.getJob().send_keys("demo")
        homePage.getJob1().clear()
        self.driver.refresh()

    # @pytest.fixture(params=[("email": "karthi@yopmail.com", "Password": "Test@123", "Name": "karthika", "Gender": "Female"),("gokul@yopmail.com", "Test@123", "gokul", "Male")]
    @pytest.fixture(params= HomePageData.getData("TestCase2"))
    def getData(self,request):
        return request.param
