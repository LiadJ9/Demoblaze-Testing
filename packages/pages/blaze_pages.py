import packages.utilities.blaze_driver as bu
import packages.constructors.blaze_locators as bl


class BasePage(object):
    def __init__(self, my_driver):
        self.my_driver = my_driver


class GeneralPage(BasePage):
    def find_alert(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.alert_is_present())
        alert = self.my_driver.switch_to.alert
        return alert


class HeaderPage(BasePage):
    def click_home_button(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.HL.Home,)))
        home = self.my_driver.find_element(*bl.HL.Home)
        home.click()

    def click_contact_button(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.HL.Contact,)))
        contact = self.my_driver.find_element(*bl.HL.Contact)
        contact.click()

    def click_about_us_button(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.HL.About_us,)))
        about = self.my_driver.find_element(*bl.HL.About_us)
        about.click()

    def click_cart_button(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.HL.Cart,)))
        cart = self.my_driver.find_element(*bl.HL.Cart)
        cart.click()

    def click_login_button(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.HL.Login,)))
        login = self.my_driver.find_element(*bl.HL.Login)
        login.click()

    def click_signup_button(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.HL.Signup,)))
        signup = self.my_driver.find_element(*bl.HL.Signup)
        signup.click()

    def click_logo_button(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.HL.Logo_redirect,)))
        home = self.my_driver.find_element(*bl.HL.Logo_redirect)
        home.click()


class MainPage(BasePage):
    def click_phone_category(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.MainPageLocators.Phone_cat,)))
        phonecat = self.my_driver.find_element(*bl.MainPageLocators.Phone_cat)
        phonecat.click()

    def click_laptop_category(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.MainPageLocators.Laptop_cat,)))
        laptopcat = self.my_driver.find_element(*bl.MainPageLocators.Laptop_cat)
        laptopcat.click()

    def click_monitor_category(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.MainPageLocators.Monitor_cat,)))
        monitorcat = self.my_driver.find_element(*bl.MainPageLocators.Monitor_cat)
        monitorcat.click()

    def click_right_arrow(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.MainPageLocators.Carousel_next,)))
        carnext = self.my_driver.find_element(*bl.MainPageLocators.Carousel_next)
        carnext.click()

    def click_left_arrow(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.MainPageLocators.Carousel_previous,)))
        carprev = self.my_driver.find_element(*bl.MainPageLocators.Carousel_previous)
        carprev.click()

    def click_slide1(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.MainPageLocators.Carousel_slide1,)))
        slide1 = self.my_driver.find_element(*bl.MainPageLocators.Carousel_slide1)
        slide1.click()

    def click_slide2(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.MainPageLocators.Carousel_slide2,)))
        slide2 = self.my_driver.find_element(*bl.MainPageLocators.Carousel_slide2)
        slide2.click()

    def click_slide3(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.MainPageLocators.Carousel_slide3,)))
        slide3 = self.my_driver.find_element(*bl.MainPageLocators.Carousel_slide3)
        slide3.click()

    def click_previous(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.MainPageLocators.Previous,)))
        previouscat = self.my_driver.find_element(*bl.MainPageLocators.Previous)
        previouscat.click()

    def click_next(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.MainPageLocators.Next,)))
        nextcat = self.my_driver.find_element(*bl.MainPageLocators.Next)
        nextcat.click()


class ContactPage(BasePage):
    def insert_mail(self, email):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.CL.Contact_email,)))
        mail_slot = self.my_driver.find_element(*bl.CL.Contact_email)
        mail_slot.click()
        mail_slot.send_keys(email)

    def insert_contact_name(self, contact_name):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.CL.Contact_name,)))
        contact_slot = self.my_driver.find_element(*bl.CL.Contact_name)
        contact_slot.click()
        contact_slot.send_keys(contact_name)

    def msg_contents(self, message):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.CL.Send_message,)))
        msg_slot = self.my_driver.find_element(*bl.CL.Send_message)
        msg_slot.click()
        msg_slot.send_keys(message)

    def click_send(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.CL.Send_message,)))
        sendmsg = self.my_driver.find_element(*bl.CL.Send_message)
        sendmsg.click()


class AboutPage(BasePage):
    def click_big_play(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.AboutUsLocators.Big_Play_button,)))
        bigplay = self.my_driver.find_element(*bl.AboutUsLocators.Big_Play_button)
        bigplay.click()
