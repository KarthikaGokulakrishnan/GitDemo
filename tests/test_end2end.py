import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.CheckOutPage import CheckOutPage
from PageObjects.ConfirmPage import ConfirmPage
from PageObjects.HomePage import HomePage
from PageObjects.PurchasePage import PurchasePage
from Utilities.BaseClass import BaseClass


class Homepage:
    pass


class Testone(BaseClass):

    def test_end2end(self):
        log=self.getlogger()
        homePage = HomePage(self.driver)
        CardTitle= homePage.ShopItems()
        devicesList = CardTitle.getCardTitle()
        log.info("Getting all the titles")
        i=-1
        for devicesLists in devicesList:
            i = i + 1
            products = devicesLists.text
            log.info(products.encode("utf-8"))
            if products == "Nokia Edge":

                # devicesLists.find_element(By.XPATH,"(//div[@class='card-footer']/button)[3]").click()
                CardTitle.getAddButton()[i].click()
        confirm = CardTitle.getCheckOutButton()
        # confirm = ConfirmPage(self.driver)
        purchasepage = confirm.getCK2Button()
        log.info("Entering Country Name as India")
        purchasepage.getCountrySug().send_keys("ind")
        self.VerifylinkPresence("suggestions")
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "suggestions")))
        countries = purchasepage.getCountryName()
        log.info(len(countries))
        for country in countries:
            if country.text == "India":
                country.click()
                break
        purchasepage.getCheckBox().click()
        purchasepage.getSubmit().click()
        # actualMessage1=driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']/strong").text
        actualMessage2 = purchasepage.getActualMessage().text
        # actualMessage=actualMessage1+actualMessage2
        log.info("text received from thr application is"+actualMessage2)
        assert "Success! Thank you! Your order will be delivered in next few weeks :-)." in actualMessage2





