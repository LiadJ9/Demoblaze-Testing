import random

import packages.utilities.blaze_driver as bu
import packages.constructors.blaze_locators as bl


class BasePage(object):
    def __init__(self, my_driver):
        self.my_driver = my_driver


class GeneralPage(BasePage):

    # Finds built in browser alert - used for gathering alert text and dismissing alerts

    def find_alert(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.alert_is_present())
        alert = self.my_driver.switch_to.alert
        return alert

    # Creates a new account

    def create_existing_account(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located(bl.HL.Signup))
        header = HeaderPage(self.my_driver)
        signup = SignupPage(self.my_driver)
        general = GeneralPage(self.my_driver)
        header.click_signup_button()
        temp_password = general.randomusrpswd()
        temp_username = general.randomusrpswd()
        signup.signup_password(temp_password)
        signup.signup_name(temp_username)
        signup.click_signup_submit()
        alert = general.find_alert()
        alert.accept()
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located(bl.HL.Signup))
        bu.sleep(2)
        return temp_username, temp_password

    # Logs into existing account created by the function above - not required but if the account doesn't exist the function will fail

    def log_in_existing_account(self, username, password):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located(bl.HL.Login))
        header = HeaderPage(self.my_driver)
        login = LoginPage(self.my_driver)
        header.click_login_button()
        login.login_pass(password)
        login.login_name(username)
        login.click_login_submit()
        bu.sleep(1)

    # Generates random  8 letter/number string for user in passwords/names
    @staticmethod
    def randomusrpswd():
        number = bu.string.digits
        letter = bu.string.ascii_letters
        letters = (''.join(random.choice(letter) for _ in range(4)))
        numero = (''.join(random.choice(number) for _ in range(4)))
        return f'{letters}{numero}'

    # Generates random item link between 1 and 9 to ensure test reliability

    @staticmethod
    def random_item():
        url = ('https://www.demoblaze.com/prod.html?idp_='+(str(random.randint(1, 9))))
        return f'{url}'


# HEADER PAGE FUNCTIONS

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

    def click_logout_button(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.HL.logout,)))
        logout = self.my_driver.find_element(*bl.HL.logout)
        logout.click()


class MainPage(BasePage):
    def click_phone_category(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.MPL.Phone_cat,)))
        phonecat = self.my_driver.find_element(*bl.MPL.Phone_cat)
        phonecat.click()

    def click_laptop_category(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.MPL.Laptop_cat,)))
        laptopcat = self.my_driver.find_element(*bl.MPL.Laptop_cat)
        laptopcat.click()

    def click_monitor_category(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.MPL.Monitor_cat,)))
        monitorcat = self.my_driver.find_element(*bl.MPL.Monitor_cat)
        monitorcat.click()

    def click_right_arrow(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.MPL.Carousel_next,)))
        carnext = self.my_driver.find_element(*bl.MPL.Carousel_next)
        carnext.click()

    def click_left_arrow(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.MPL.Carousel_previous,)))
        carprev = self.my_driver.find_element(*bl.MPL.Carousel_previous)
        carprev.click()

    def click_slide1(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.MPL.Carousel_slide1,)))
        slide1 = self.my_driver.find_element(*bl.MPL.Carousel_slide1)
        slide1.click()

    def click_slide2(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.MPL.Carousel_slide2,)))
        slide2 = self.my_driver.find_element(*bl.MPL.Carousel_slide2)
        slide2.click()

    def click_slide3(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.MPL.Carousel_slide3,)))
        slide3 = self.my_driver.find_element(*bl.MPL.Carousel_slide3)
        slide3.click()

    def click_previous(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.MPL.Previous,)))
        previouscat = self.my_driver.find_element(*bl.MPL.Previous)
        previouscat.click()

    def click_next(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.MPL.Next,)))
        nextcat = self.my_driver.find_element(*bl.MPL.Next)
        nextcat.click()

    def click_add_to_cart(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.MPL.Add_to_cart,)))
        add = self.my_driver.find_element(*bl.MPL.Add_to_cart)
        add.click()


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
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.CL.Message_box,)))
        msg_slot = self.my_driver.find_element(*bl.CL.Message_box)
        msg_slot.click()
        msg_slot.send_keys(message)

    def click_send(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.CL.Send_message,)))
        sendmsg = self.my_driver.find_element(*bl.CL.Send_message)
        sendmsg.click()

    def click_cancel(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.CL.Cancel_button,)))
        sendcncl = self.my_driver.find_element(*bl.CL.Cancel_button)
        sendcncl.click()


class AboutPage(BasePage):
    def click_big_play(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.AUL.Big_Play_button,)))
        bigplay = self.my_driver.find_element(*bl.AUL.Big_Play_button)
        bigplay.click()

    def click_exit_button(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.AUL.Close_button,)))
        close = self.my_driver.find_element(*bl.AUL.Close_button)
        close.click()

    def click_sound_button(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.AUL.Sound_OnOff,)))
        sound = self.my_driver.find_element(*bl.AUL.Sound_OnOff)
        sound.click()

    def click_play_button(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.AUL.Play_button,)))
        play = self.my_driver.find_element(*bl.AUL.Play_button)
        play.click()

    def click_fullscreen(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.AUL.Fullscreen,)))
        fullscr = self.my_driver.find_element(*bl.AUL.Fullscreen)
        fullscr.click()

    def drag_sound_slider(self, sound):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.AUL.Sound_OnOff,)))
        soundslide = self.my_driver.find_element(*bl.AUL.Sound_slider)
        volume = self.my_driver.find_element(*bl.AUL.Sound_OnOff)
        actions = bu.AC.ActionChains(self.my_driver)
        actions.move_to_element(volume).perform()
        actions.move_to_element(soundslide).perform()
        actions.click_and_hold().perform()
        actions.move_by_offset(sound, 0).perform()
        actions.release().perform()


class SignupPage(BasePage):
    def click_signup_submit(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.SignUpLocators.Signup_submit,)))
        signup = self.my_driver.find_element(*bl.SignUpLocators.Signup_submit)
        signup.click()

    def click_signup_cancel(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.SignUpLocators.Signup_cancel,)))
        signup = self.my_driver.find_element(*bl.SignUpLocators.Signup_cancel)
        signup.click()

    def signup_name(self, name):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.SignUpLocators.Signup_username,)))
        signup_name = self.my_driver.find_element(*bl.SignUpLocators.Signup_username)
        signup_name.click()
        signup_name.send_keys(name)

    def signup_password(self, passwd):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.SignUpLocators.Signup_password,)))
        signup_pass = self.my_driver.find_element(*bl.SignUpLocators.Signup_password)
        signup_pass.click()
        signup_pass.send_keys(passwd)

    def signup_name_clear(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.SignUpLocators.Signup_username,)))
        signup_name = self.my_driver.find_element(*bl.SignUpLocators.Signup_username)
        signup_name.click()
        signup_name.send_keys(bu.Keys.CLEAR)

    def signup_pass_clear(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.SignUpLocators.Signup_password,)))
        signup_pass = self.my_driver.find_element(*bl.SignUpLocators.Signup_password)
        signup_pass.click()
        signup_pass.send_keys(bu.Keys.CLEAR)


class LoginPage(BasePage):
    def click_login_submit(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.LogInLocators.Login_submit,)))
        login = self.my_driver.find_element(*bl.LogInLocators.Login_submit)
        login.click()

    def click_login_cancel(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.LogInLocators.Login_cancel,)))
        cancel = self.my_driver.find_element(*bl.LogInLocators.Login_cancel)
        cancel.click()

    def login_name(self, name):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.LogInLocators.Login_username,)))
        login_name = self.my_driver.find_element(*bl.LogInLocators.Login_username)
        login_name.click()
        login_name.send_keys(name)

    def login_pass(self, passwd):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.LogInLocators.Login_password,)))
        login_name = self.my_driver.find_element(*bl.LogInLocators.Login_password)
        login_name.click()
        login_name.send_keys(passwd)


class CartPage(BasePage):

    # No Login and with login are two separate tests because the error message when logged in is different (What?????)
    def add_random_item_no_login(self):
        general = GeneralPage(self.my_driver)
        main = MainPage(self.my_driver)
        self.my_driver.get(general.random_item())
        main.click_add_to_cart()
        alert = general.find_alert()
        assert alert.text == 'Product added'
        alert.accept()

    def add_random_item_with_login(self):
        general = GeneralPage(self.my_driver)
        main = MainPage(self.my_driver)
        self.my_driver.get(general.random_item())
        main.click_add_to_cart()
        alert = general.find_alert()
        assert alert.text == 'Product added.'
        alert.accept()

    def delete_first_item(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.CartPageLocators.delete_first_item,)))
        delete = self.my_driver.find_element(*bl.CartPageLocators.delete_first_item)
        delete.click()

    def click_place_order(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.CartPageLocators.Place_order,)))
        place = self.my_driver.find_element(*bl.CartPageLocators.Place_order)
        place.click()

    def click_cancel_order(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.CartPageLocators.cancel_order,)))
        cancel = self.my_driver.find_element(*bl.CartPageLocators.cancel_order)
        cancel.click()

    def insert_name(self, name):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.CartPageLocators.Name,)))
        names = self.my_driver.find_element(*bl.CartPageLocators.Name)
        names.click()
        names.send_keys(name)

    def insert_country(self, country):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.CartPageLocators.Country,)))
        countries = self.my_driver.find_element(*bl.CartPageLocators.Country)
        countries.click()
        countries.send_keys(country)

    def insert_city(self, city):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.CartPageLocators.City,)))
        cities = self.my_driver.find_element(*bl.CartPageLocators.City)
        cities.click()
        cities.send_keys(city)

    def insert_credit_card(self, credit_card):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.CartPageLocators.Credit_Card,)))
        credit = self.my_driver.find_element(*bl.CartPageLocators.Credit_Card)
        credit.click()
        credit.send_keys(credit_card)

    def insert_month(self, months):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.CartPageLocators.Month,)))
        month = self.my_driver.find_element(*bl.CartPageLocators.Month)
        month.click()
        month.send_keys(months)

    def insert_year(self, years):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.CartPageLocators.Year,)))
        year = self.my_driver.find_element(*bl.CartPageLocators.Year)
        year.click()
        year.send_keys(years)

    def click_place_order_page(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.CartPageLocators.order_page_order,)))
        order = self.my_driver.find_element(*bl.CartPageLocators.order_page_order)
        order.click()

    def order_details(self, name, country, city, credit_card, months, years):
        cart = CartPage(self.my_driver)
        cart.insert_name(name)
        cart.insert_country(country)
        cart.insert_city(city)
        cart.insert_credit_card(credit_card)
        cart.insert_month(months)
        cart.insert_year(years)

    def confirm_page_exit(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.CartPageLocators.confirm_page_exit,)))
        exits = self.my_driver.find_element(*bl.CartPageLocators.confirm_page_exit)
        exits.click()

    def find_amount_of_cart_items(self):
        bu.sleep(1)
        tbody = self.my_driver.find_elements(*bl.CartPageLocators.find_all_items)
        length = len(tbody)
        return length

    def assert_cart_has_items(self):
        cart_has_items = bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located(bl.CartPageLocators.item_exists))
        return cart_has_items

    def assert_order_confirmed(self):
        order_confirmed = bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located(bl.CartPageLocators.order_confirmed))
        return order_confirmed

    def assert_no_cart_items(self):
        no_cart_items = bu.WDW(self.my_driver, 10).until(bu.EC.invisibility_of_element(bl.CartPageLocators.delete_first_item))
        return no_cart_items
