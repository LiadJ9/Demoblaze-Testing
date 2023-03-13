import packages.utilities.blaze_driver as bu
import packages.pages.blaze_pages as bp
import packages.constructors.blaze_locators as bl
import packages.constructors.blaze_locators1 as bl1
max_word_count = '1sihA8ttDrEsi02sZMz3uYrvqxhZG6mIlQ6QWRnFa6Wdf43KzP7IKuSC0609x2rXgJGBbDI9fvaehc4Rg808bStvl4uW4xEu7ptEWdeL8H0oSEh6wdQ04IKEcqhL33s1AccVY3PBKr6lfbcPf1k38LR186fIN3B6l5LhYLzgXkaVm7owjyJljIz7xCU3NEzvzqhmvQlhFqunh5AWfkp3kSqvCXkGRhTULKkd49zyi2rBHrDtCkq5QOJoJgWM217PxQaG'
msg = 'This is the message I want to send to your company, I really dislike your site and I think you should do a better job at ensuring quality'

# TO DO : HOME, LOGIN, SIGNUP, CART


class TestBlazeHome(bu.unittest.TestCase):

    def setUp(self):
        self.my_driver = bu.get_chrome_driver()
        self.my_driver.get('https://www.demoblaze.com/index.html')
        self.my_driver.maximize_window()

    def test_Home_button(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl1.HL.hb,)))
        home = self.my_driver.find_element(*bl1.HL.hb)
        home.click()
        assert self.my_driver.find_element(*bl1.HL.hb)

    def test_BCP(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl1.HL.hb,)))
        home = self.my_driver.find_element(*bl1.HL.hb,)
        home.click()
        change_picture = self.my_driver.find_element(bu.By.XPATH, bl1.MPL.BCP)
        change_picture.click()
        bu.WDW(self.my_driver, 5).until(bu.EC.visibility_of_element_located((bu.By.XPATH, bl1.MPL.second_pic)))
        assert self.my_driver.find_element(bu.By.XPATH, bl1.MPL.second_pic)

    def test_button_next(self):
        bu.WDW(self.my_driver, 5).until(bu.EC.visibility_of_element_located((*bl1.HL.hb,)))
        b_next = self.my_driver.find_element(*bl1.MPL.NB,)
        b_next.click()
        bu.WDW(self.my_driver, 5).until(bu.EC.visibility_of_element_located((*bl1.MPL.mc_img,)))
        assert self.my_driver.find_element(*bl1.MPL.mc_img,)

    def test_button_previous(self):
        bu.WDW(self.my_driver, 5).until(bu.EC.visibility_of_element_located((*bl1.HL.hb,)))
        next_b = self.my_driver.find_element(*bl1.MPL.NB,)
        next_b.click()
        bu.WDW(self.my_driver, 5).until(bu.EC.visibility_of_element_located((*bl1.MPL.mc_img,)))
        previous_b = self.my_driver.find_element(*bl1.MPL.PB,)
        previous_b.click()
        bu.WDW(self.my_driver, 5).until(bu.EC.visibility_of_element_located((*bl1.MPL.FPI,)))
        assert self.my_driver.find_element(*bl1.MPL.FPI,)

    def test_first_button_header_picture(self):
        bu.WDW(self.my_driver, 5).until(bu.EC.visibility_of_element_located((*bl1.HL.hb,)))
        first_button = self.my_driver.find_element(*bl1.HL.FBHP,)
        first_button.click()
        bu.WDW(self.my_driver, 5).until(bu.EC.visibility_of_element_located((*bl1.HL.FI,)))
        assert self.my_driver.find_element(*bl1.HL.FI,)

    def test_second_button_header_picture(self):
        bu.WDW(self.my_driver, 5).until(bu.EC.visibility_of_element_located((*bl1.HL.hb,)))
        second_button = self.my_driver.find_element(*bl1.HL.SBHP,)
        second_button.click()
        bu.WDW(self.my_driver, 5).until(bu.EC.visibility_of_element_located((*bl1.HL.SI,)))
        assert self.my_driver.find_element(*bl1.HL.SI,)

    def test_third_button_header_picture(self):
        bu.WDW(self.my_driver, 5).until(bu.EC.visibility_of_element_located((*bl1.HL.hb,)))
        third_button = self.my_driver.find_element(*bl1.HL.TBHP,)
        third_button.click()
        bu.WDW(self.my_driver, 5).until(bu.EC.visibility_of_element_located((*bl1.HL.TI,)))
        assert self.my_driver.find_element(*bl1.HL.TI,)

    def tearDown(self):
        bu.sleep(1)
        self.my_driver.quit()


class TestBlazeHeaders(bu.unittest.TestCase):

    def setUp(self):
        self.my_driver = bu.get_chrome_driver()
        self.my_driver.get('https://www.demoblaze.com/index.html')
        self.my_driver.maximize_window()

    def test_home_button_4_1(self):
        header = bp.HeaderPage(self.my_driver)
        header.click_home_button()
        self.assertTrue(self.my_driver.find_element(*bl.MPL.Phone_cat))

    def test_contact_button_4_2(self):
        header = bp.HeaderPage(self.my_driver)
        header.click_contact_button()
        self.assertTrue(self.my_driver.find_element(*bl.CL.Contact_email))

    def test_about_us_button_4_3(self):
        header = bp.HeaderPage(self.my_driver)
        header.click_about_us_button()
        self.assertTrue(self.my_driver.find_element(*bl.AUL.Big_Play_button))

    def test_cart_button_4_4(self):
        header = bp.HeaderPage(self.my_driver)
        header.click_cart_button()
        self.assertTrue(self.my_driver.find_element(*bl.CartPageLocators.Place_order))

    def test_login_button_4_5(self):
        header = bp.HeaderPage(self.my_driver)
        header.click_login_button()
        self.assertTrue(self.my_driver.find_element(*bl.LogInLocators.Login_cancel))

    def test_signup_button_4_6(self):
        header = bp.HeaderPage(self.my_driver)
        header.click_signup_button()
        self.assertTrue(self.my_driver.find_element(*bl.SignUpLocators.Signup_cancel))

    def tearDown(self):
        bu.sleep(1)
        self.my_driver.quit()


class TestBlazeContact(bu.unittest.TestCase):
    def setUp(self):
        self.my_driver = bu.get_chrome_driver()
        self.my_driver.get('https://www.demoblaze.com/index.html')
        self.my_driver.maximize_window()

    def test_no_info_added_5_1(self):
        header = bp.HeaderPage(self.my_driver)
        contact = bp.ContactPage(self.my_driver)
        alerts = bp.GeneralPage(self.my_driver)
        header.click_contact_button()
        contact.click_send()
        alert = alerts.find_alert()
        if alert.text == 'invalid email, name and message':
            vals = True
        else:
            vals = False
        self.assertTrue(vals)

    def test_invalid_email_5_2(self):
        header = bp.HeaderPage(self.my_driver)
        contact = bp.ContactPage(self.my_driver)
        alerts = bp.GeneralPage(self.my_driver)
        header.click_contact_button()
        contact.insert_contact_name('Liad Manteka')
        contact.insert_mail('liadgmail.com')
        contact.msg_contents(msg)
        contact.click_send()
        alert = alerts.find_alert()
        if alert.text == 'invalid email':
            vals = True
        else:
            vals = False
        self.assertTrue(vals)

    def test_invalid_message_5_3(self):
        header = bp.HeaderPage(self.my_driver)
        contact = bp.ContactPage(self.my_driver)
        alerts = bp.GeneralPage(self.my_driver)
        header.click_contact_button()
        contact.insert_contact_name('Liad Manteka')
        contact.insert_mail('liad@gmail.com')
        contact.click_send()
        alert = alerts.find_alert()
        if alert.text == 'invalid message':
            vals = True
        else:
            vals = False
        self.assertTrue(vals)

    def test_valid_message_5_4(self):
        header = bp.HeaderPage(self.my_driver)
        contact = bp.ContactPage(self.my_driver)
        alerts = bp.GeneralPage(self.my_driver)
        header.click_contact_button()
        contact.insert_contact_name('Liad Manteka')
        contact.insert_mail('liad@gmail.com')
        contact.msg_contents(msg)
        contact.click_send()
        alert = alerts.find_alert()
        if alert.text == 'Thanks for the message!!':
            vals = True
        else:
            vals = False
        self.assertTrue(vals)

    def test_max_word_count_5_5(self):
        header = bp.HeaderPage(self.my_driver)
        contact = bp.ContactPage(self.my_driver)
        alerts = bp.GeneralPage(self.my_driver)
        header.click_contact_button()
        contact.insert_contact_name('Liad Manteka')
        contact.insert_mail('liad@gmail.com')
        contact.msg_contents(max_word_count)
        contact.click_send()
        alert = alerts.find_alert()
        if alert.text == 'Invalid message.':
            vals = True
        else:
            vals = False
        self.assertTrue(vals)

    def test_invalid_name_5_6(self):
        header = bp.HeaderPage(self.my_driver)
        contact = bp.ContactPage(self.my_driver)
        alerts = bp.GeneralPage(self.my_driver)
        header.click_contact_button()
        contact.insert_mail('liad@gmail.com')
        contact.msg_contents(msg)
        contact.click_send()
        alert = alerts.find_alert()
        if alert.text == 'Invalid name.':
            vals = True
        else:
            vals = False
        self.assertTrue(vals)

    def test_cancel_button_5_7(self):
        header = bp.HeaderPage(self.my_driver)
        contact = bp.ContactPage(self.my_driver)
        header.click_contact_button()
        contact.click_cancel()
        bu.sleep(1)
        self.assertTrue(bu.WDW(self.my_driver, 10).until(bu.EC.invisibility_of_element((*bl.CL.Cancel_button,))))

    def test_submit_button_5_8(self):
        header = bp.HeaderPage(self.my_driver)
        contact = bp.ContactPage(self.my_driver)
        alerts = bp.GeneralPage(self.my_driver)
        header.click_contact_button()
        contact.click_send()
        self.assertTrue(alerts.find_alert())

    def tearDown(self):
        bu.sleep(1)
        self.my_driver.quit()


class TestBlazeAboutUs(bu.unittest.TestCase):
    def setUp(self):
        self.my_driver = bu.get_chrome_driver()
        self.my_driver.get('https://www.demoblaze.com/index.html')
        self.my_driver.maximize_window()

    def test_video_play_6_1(self):
        header = bp.HeaderPage(self.my_driver)
        about = bp.AboutPage(self.my_driver)
        header.click_about_us_button()
        about.click_big_play()
        play_status = self.my_driver.find_element(*bl.AUL.Play_button)
        self.assertTrue(play_status.get_attribute('title') == 'Pause')

    def test_sound_slider_6_2(self):
        header = bp.HeaderPage(self.my_driver)
        about = bp.AboutPage(self.my_driver)
        header.click_about_us_button()
        about.click_big_play()
        about.drag_sound_slider(5)
        sound_result = self.my_driver.find_element(*bl.AUL.total_volume)
        self.assertTrue(sound_result.get_attribute('style') != "width: 100%;")

    def test_volume_on_off_6_3(self):
        header = bp.HeaderPage(self.my_driver)
        about = bp.AboutPage(self.my_driver)
        header.click_about_us_button()
        about.click_big_play()
        about.click_sound_button()
        sound_result = self.my_driver.find_element(*bl.AUL.Sound_OnOff)
        self.assertTrue(sound_result.get_attribute('title') == 'Unmute')
        about.click_sound_button()
        self.assertTrue(sound_result.get_attribute('title') == 'Mute')

    def test_pause_and_play_6_4(self):
        header = bp.HeaderPage(self.my_driver)
        about = bp.AboutPage(self.my_driver)
        header.click_about_us_button()
        about.click_big_play()
        about.click_play_button()
        play_status = self.my_driver.find_element(*bl.AUL.Play_button)
        self.assertTrue(play_status.get_attribute('title') == 'Play')
        about.click_play_button()
        self.assertTrue(play_status.get_attribute('title') == 'Pause')

    def test_fullscreen_6_5(self):
        header = bp.HeaderPage(self.my_driver)
        about = bp.AboutPage(self.my_driver)
        header.click_about_us_button()
        about.click_big_play()
        about.click_fullscreen()
        full_screen_check = self.my_driver.find_element(*bl.AUL.Fullscreen)
        self.assertTrue(full_screen_check.get_attribute('title') == 'Non-Fullscreen')
        about.click_fullscreen()
        self.assertTrue(full_screen_check.get_attribute('title') == 'Fullscreen')

    def test_exit_button_6_6(self):
        header = bp.HeaderPage(self.my_driver)
        about = bp.AboutPage(self.my_driver)
        header.click_about_us_button()
        about.click_big_play()
        about.click_exit_button()
        self.assertTrue(bu.WDW(self.my_driver, 10).until(bu.EC.invisibility_of_element((*bl.AUL.Play_button,))))

    def tearDown(self):
        bu.sleep(1)
        self.my_driver.quit()


class TestBlazeLogIn(bu.unittest.TestCase):

    def setUp(self):
        self.my_driver = bu.get_chrome_driver()
        self.my_driver.get('https://www.demoblaze.com/index.html')
        self.my_driver.maximize_window()

    def test_log_in_true_7_1(self):
        header = bp.HeaderPage(self.my_driver)
        login = bp.LoginPage(self.my_driver)
        general = bp.GeneralPage(self.my_driver)
        temp_username, temp_password = general.create_existing_account()
        header.click_login_button()
        login.login_pass(temp_password)
        login.login_name(temp_username)
        login.click_login_submit()
        self.assertTrue(bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((*bl.HL.Username,))))

    def test_log_in_wrong_password_7_2(self):
        header = bp.HeaderPage(self.my_driver)
        login = bp.LoginPage(self.my_driver)
        general = bp.GeneralPage(self.my_driver)
        temp_username, temp_password = general.create_existing_account()
        header.click_login_button()
        login.login_pass(temp_password+'blahga')
        login.login_name(temp_username)
        login.click_login_submit()
        alert = general.find_alert()
        if alert.text == 'Wrong password.':
            vals = True
        else:
            vals = False
        self.assertTrue(vals)

    def test_log_in_wrong_username_7_3(self):
        header = bp.HeaderPage(self.my_driver)
        login = bp.LoginPage(self.my_driver)
        general = bp.GeneralPage(self.my_driver)
        temp_username, temp_password = general.create_existing_account()
        header.click_login_button()
        login.login_pass(temp_password)
        login.login_name(temp_username+'shadow')
        login.click_login_submit()
        alert = general.find_alert()
        if alert.text == 'User does not exist.':
            vals = True
        else:
            vals = False
        self.assertTrue(vals)

    def test_log_in_wrong_name_and_pass_7_4(self):
        header = bp.HeaderPage(self.my_driver)
        login = bp.LoginPage(self.my_driver)
        general = bp.GeneralPage(self.my_driver)
        temp_username, temp_password = general.create_existing_account()
        header.click_login_button()
        login.login_pass(temp_password+'clone')
        login.login_name(temp_username+'shadow')
        login.click_login_submit()
        alert = general.find_alert()
        if alert.text == 'User does not exist.':
            vals = True
        else:
            vals = False
        self.assertTrue(vals)

    def test_no_password_7_5(self):
        header = bp.HeaderPage(self.my_driver)
        login = bp.LoginPage(self.my_driver)
        general = bp.GeneralPage(self.my_driver)
        temp_username, temp_password = general.create_existing_account()
        header.click_login_button()
        login.login_name(temp_username+'shadow')
        login.click_login_submit()
        alert = general.find_alert()
        if alert.text == 'Wrong password.':
            vals = True
        else:
            vals = False
        self.assertTrue(vals)
        header.click_logout_button()

    def test_auto_sign_out_7_6(self):
        header = bp.HeaderPage(self.my_driver)
        login = bp.LoginPage(self.my_driver)
        general = bp.GeneralPage(self.my_driver)
        temp_username, temp_password = general.create_existing_account()
        bu.sleep(3)
        header.click_login_button()
        login.login_name(temp_username)
        login.login_pass(temp_password)
        login.click_login_submit()
        self.my_driver.close()
        self.my_driver = bu.get_chrome_driver()
        self.my_driver.get('https://www.demoblaze.com/index.html')
        self.my_driver.maximize_window()
        self.assertTrue(bu.WDW(self.my_driver, 10).until(bu.EC.invisibility_of_element(bl.HL.Username)))

    def tearDown(self):
        bu.sleep(1)
        self.my_driver.quit()


class TestBlazeSignUp(bu.unittest.TestCase):

    def setUp(self):
        self.my_driver = bu.get_chrome_driver()
        self.my_driver.get('https://www.demoblaze.com/index.html')
        self.my_driver.maximize_window()

    def test_sign_up_true_2_1(self):
        header = bp.HeaderPage(self.my_driver)
        signup = bp.SignupPage(self.my_driver)
        general = bp.GeneralPage(self.my_driver)
        header.click_signup_button()
        signup.signup_name(general.randomusrpswd())
        signup.signup_password(general.randomusrpswd())
        signup.click_signup_submit()
        alert = general.find_alert()
        if alert.text == 'Sign up successful.':
            vals = True
        else:
            vals = False
        self.assertTrue(vals)
        alert.accept()
        header.click_logout_button()

    def test_sign_up_existing_usr_2_2(self):
        header = bp.HeaderPage(self.my_driver)
        signup = bp.SignupPage(self.my_driver)
        general = bp.GeneralPage(self.my_driver)
        temp_username, temp_password = general.create_existing_account()
        bu.sleep(1)
        header.click_signup_button()
        signup.signup_pass_clear()
        signup.signup_name_clear()
        signup.signup_name(temp_username)
        signup.signup_password(temp_password)
        signup.click_signup_submit()
        alert = general.find_alert()
        if alert.text == 'This user already exist.':
            vals = True
        else:
            vals = False
        self.assertTrue(vals)

    def test_sign_up_bad_usrname_2_3(self):
        header = bp.HeaderPage(self.my_driver)
        signup = bp.SignupPage(self.my_driver)
        general = bp.GeneralPage(self.my_driver)
        header.click_signup_button()
        signup.signup_name(general.randomusrpswd()+"/@")
        signup.signup_password(general.randomusrpswd())
        signup.click_signup_submit()
        alert = general.find_alert()
        if alert.text == 'Invalid username.':
            vals = True
        else:
            vals = False
        self.assertTrue(vals)

    def test_sign_up_no_details_2_4(self):
        header = bp.HeaderPage(self.my_driver)
        signup = bp.SignupPage(self.my_driver)
        general = bp.GeneralPage(self.my_driver)
        header.click_signup_button()
        signup.click_signup_submit()
        alert = general.find_alert()
        if alert.text == 'Please fill out Username and Password.':
            vals = True
        else:
            vals = False
        self.assertTrue(vals)

    def test_sign_up_max_wordcount_2_5(self):
        header = bp.HeaderPage(self.my_driver)
        signup = bp.SignupPage(self.my_driver)
        general = bp.GeneralPage(self.my_driver)
        header.click_signup_button()
        signup.signup_name(general.randomusrpswd()+'gj29fjdds')
        signup.signup_password(general.randomusrpswd()+'genmah3419')
        signup.click_signup_submit()
        alert = general.find_alert()
        if alert.text == 'Invalid username and password.':
            vals = True
        else:
            vals = False
        self.assertTrue(vals)

    def test_sign_up_only_username_2_6(self):
        header = bp.HeaderPage(self.my_driver)
        signup = bp.SignupPage(self.my_driver)
        general = bp.GeneralPage(self.my_driver)
        header.click_signup_button()
        signup.signup_name(general.randomusrpswd())
        signup.click_signup_submit()
        alert = general.find_alert()
        if alert.text == 'Please fill out Username and Password.':
            vals = True
        else:
            vals = False
        self.assertTrue(vals)

    def test_sign_up_only_password_2_7(self):
        header = bp.HeaderPage(self.my_driver)
        signup = bp.SignupPage(self.my_driver)
        general = bp.GeneralPage(self.my_driver)
        header.click_signup_button()
        signup.signup_password(general.randomusrpswd())
        signup.click_signup_submit()
        alert = general.find_alert()
        if alert.text == 'Please fill out Username and Password.':
            vals = True
        else:
            vals = False
        self.assertTrue(vals)

    def test_sign_up_special_maxchars_2_8(self):
        header = bp.HeaderPage(self.my_driver)
        signup = bp.SignupPage(self.my_driver)
        general = bp.GeneralPage(self.my_driver)
        header.click_signup_button()
        signup.signup_password(general.randomusrpswd()+'#^&$*#blarg')
        signup.signup_password(general.randomusrpswd()+'#@%#*&(!')
        signup.click_signup_submit()
        alert = general.find_alert()
        if alert.text == 'Invalid username and password.':
            vals = True
        else:
            vals = False
        self.assertTrue(vals)

    def test_sign_up_info_clears_2_9(self):
        header = bp.HeaderPage(self.my_driver)
        general = bp.GeneralPage(self.my_driver)
        general.create_existing_account()
        header.click_signup_button()
        isempty = self.my_driver.find_element(*bl.SignUpLocators.Signup_password)
        val = isempty.get_attribute('value')
        if val.isascii():
            print('Info in info box still exists')
            ans = False
        else:
            ans = True
        self.assertTrue(ans)

    def tearDown(self):
        bu.sleep(1)
        self.my_driver.quit()


class TestBlazeCart(bu.unittest.TestCase):

    def setUp(self):
        self.my_driver = bu.get_chrome_driver()
        self.my_driver.get('https://www.demoblaze.com/index.html')
        self.my_driver.maximize_window()

    def test_add_product_to_cart_3_1(self):
        header = bp.HeaderPage(self.my_driver)
        general = bp.GeneralPage(self.my_driver)
        cart = bp.CartPage(self.my_driver)
        temp_username, temp_password = general.create_existing_account()
        general.log_in_existing_account(temp_username, temp_password)
        bu.sleep(2)
        cart.add_random_item_with_login()
        header.click_cart_button()
        cart_has_items = cart.assert_cart_has_items()
        self.assertTrue(cart_has_items)
        header.click_logout_button()

    def test_delete_product_from_cart_3_2(self):
        header = bp.HeaderPage(self.my_driver)
        general = bp.GeneralPage(self.my_driver)
        cart = bp.CartPage(self.my_driver)
        temp_username, temp_password = general.create_existing_account()
        general.log_in_existing_account(temp_username, temp_password)
        bu.sleep(2)
        cart.add_random_item_with_login()
        header.click_cart_button()
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located(bl.CartPageLocators.item_exists))
        cart.delete_first_item()
        self.assertTrue(bu.WDW(self.my_driver, 10).until(bu.EC.invisibility_of_element_located(bl.CartPageLocators.delete_first_item)))
        header.click_logout_button()

    def test_no_login_valid_details_3_3(self):
        header = bp.HeaderPage(self.my_driver)
        cart = bp.CartPage(self.my_driver)
        cart.add_random_item_no_login()
        header.click_cart_button()
        self.assertTrue(bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located(bl.CartPageLocators.item_exists)))
        cart.click_place_order()
        cart.order_details('bongo longo', 'petach tikva', 'tel aviv', '41395029158321', '12', '2012')
        cart.click_place_order_page()
        order_confirmed = cart.assert_order_confirmed()
        self.assertTrue(order_confirmed)

    def test_no_login_invalid_details_3_4(self):
        header = bp.HeaderPage(self.my_driver)
        cart = bp.CartPage(self.my_driver)
        cart.add_random_item_no_login()
        header.click_cart_button()
        assert bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located(bl.CartPageLocators.item_exists))
        cart.click_place_order()
        cart.order_details('$38@3&*', 'gdjska', '$#)*@&)*!', '@)$#%#@*)!', '$#*&@', '%&#*@)')
        cart.click_place_order_page()
        order_confirmed = cart.assert_order_confirmed()
        self.assertTrue(order_confirmed)

    def test_order_confirmation_name_is_user_name_3_12(self):
        header = bp.HeaderPage(self.my_driver)
        general = bp.GeneralPage(self.my_driver)
        cart = bp.CartPage(self.my_driver)
        temp_username, temp_password = general.create_existing_account()
        general.log_in_existing_account(temp_username, temp_password)
        bu.sleep(2)
        cart.add_random_item_with_login()
        header.click_cart_button()
        self.assertTrue(bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located(bl.CartPageLocators.item_exists)))
        bu.sleep(2)
        cart.click_place_order()
        cart.order_details('mango man', 'texas', 'city', '7819492309', 'years', 'months')
        cart.click_place_order_page()
        self.assertTrue(bu.WDW(self.my_driver, 10).until(bu.EC.text_to_be_present_in_element((bu.By.XPATH, '/html/body/div[10]/p'), temp_username)))
        cart.confirm_page_exit()
        cart.click_cancel_order()
        header.click_logout_button()

    def test_minimum_details_3_6(self):
        header = bp.HeaderPage(self.my_driver)
        cart = bp.CartPage(self.my_driver)
        cart.add_random_item_no_login()
        header.click_cart_button()
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located(bl.CartPageLocators.item_exists))
        cart.click_place_order()
        cart.insert_name('bling bling')
        cart.insert_credit_card("345428971901")
        cart.click_place_order_page()
        order_confirmed = cart.assert_order_confirmed()
        self.assertTrue(order_confirmed)

    def test_random_item_added_to_cart_no_login_3_7(self):
        header = bp.HeaderPage(self.my_driver)
        cart = bp.CartPage(self.my_driver)
        cart.add_random_item_no_login()
        header.click_cart_button()
        cart_has_items = cart.assert_cart_has_items()
        self.assertTrue(cart_has_items)

    def test_add_4_different_items_to_cart_3_8(self):
        header = bp.HeaderPage(self.my_driver)
        cart = bp.CartPage(self.my_driver)
        pop = 'abcd'
        for _ in pop:
            cart.add_random_item_no_login()
        header.click_cart_button()
        length = cart.find_amount_of_cart_items()
        if length == 4:
            vals = True
        else:
            vals = False
        self.assertTrue(vals)

    def test_empty_cart_purchase_3_9(self):
        header = bp.HeaderPage(self.my_driver)
        general = bp.GeneralPage(self.my_driver)
        cart = bp.CartPage(self.my_driver)
        header.click_cart_button()
        cart.click_place_order()
        cart.order_details('mango man', 'texas', 'city', '7819492309', 'years', 'months')
        cart.click_place_order_page()
        self.assertTrue(general.find_alert())

    def test_confirmation_details_same_as_given_3_5(self):
        header = bp.HeaderPage(self.my_driver)
        cart = bp.CartPage(self.my_driver)
        cart.add_random_item_no_login()
        header.click_cart_button()
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located(bl.CartPageLocators.item_exists))
        bu.sleep(1)
        cart.click_place_order()
        cart.order_details('mango man', 'texas', 'city', '7819492309', 'years', 'months')
        cart.click_place_order_page()
        self.assertTrue(bu.WDW(self.my_driver, 10).until(bu.EC.text_to_be_present_in_element(bl.CartPageLocators.confirmation_page_info, 'mango man')))
        self.assertTrue(bu.WDW(self.my_driver, 10).until(bu.EC.text_to_be_present_in_element(bl.CartPageLocators.confirmation_page_info, '7819492309')))

    def test_remove_item_from_list_3_10(self):
        header = bp.HeaderPage(self.my_driver)
        cart = bp.CartPage(self.my_driver)
        cart.add_random_item_no_login()
        cart.add_random_item_no_login()
        header.click_cart_button()
        cart.delete_first_item()
        bu.sleep(3)
        length = cart.find_amount_of_cart_items()
        if length == 1:
            vals = True
        else:
            vals = False
        self.assertTrue(vals)

    def test_log_out_and_log_in_after_adding_item_to_cart_3_11(self):
        header = bp.HeaderPage(self.my_driver)
        cart = bp.CartPage(self.my_driver)
        general = bp.GeneralPage(self.my_driver)
        temp_username, temp_password = general.create_existing_account()
        general.log_in_existing_account(temp_username, temp_password)
        bu.sleep(1)
        cart.add_random_item_with_login()
        header.click_logout_button()
        general.log_in_existing_account(temp_username, temp_password)
        bu.sleep(1)
        header.click_cart_button()
        cart_has_items = cart.assert_cart_has_items()
        self.assertTrue(cart_has_items)

    def test_valid_order_with_login_3_13(self):
        cart = bp.CartPage(self.my_driver)
        general = bp.GeneralPage(self.my_driver)
        header = bp.HeaderPage(self.my_driver)
        temp_username, temp_password = general.create_existing_account()
        general.log_in_existing_account(temp_username, temp_password)
        bu.sleep(1)
        cart.add_random_item_with_login()
        header.click_cart_button()
        cart.click_place_order()
        cart.order_details('bongo longo', 'petach tikva', 'tel aviv', '41395029158321', '12', '2012')
        cart.click_place_order_page()
        cart_has_items = cart.assert_cart_has_items()
        self.assertTrue(cart_has_items)

    def test_invalid_order_with_login_3_14(self):
        cart = bp.CartPage(self.my_driver)
        general = bp.GeneralPage(self.my_driver)
        header = bp.HeaderPage(self.my_driver)
        temp_username, temp_password = general.create_existing_account()
        general.log_in_existing_account(temp_username, temp_password)
        bu.sleep(1)
        cart.add_random_item_with_login()
        header.click_cart_button()
        cart.click_place_order()
        cart.order_details('09799876', 'petach tikva', 'tel aviv', '7989867', '12', '2012')
        cart.click_place_order_page()
        order_confirmed = cart.assert_order_confirmed()
        self.assertTrue(order_confirmed)

    def test_cart_after_order_is_empty_3_15(self):
        header = bp.HeaderPage(self.my_driver)
        cart = bp.CartPage(self.my_driver)
        general = bp.GeneralPage(self.my_driver)
        temp_username, temp_password = general.create_existing_account()
        general.log_in_existing_account(temp_username, temp_password)
        bu.sleep(1)
        cart.add_random_item_with_login()
        header.click_cart_button()
        cart.click_place_order()
        cart.order_details('09799876', 'petach tikva', 'tel aviv', '7989867', '12', '2012')
        cart.click_place_order_page()
        order_confirmed = cart.assert_order_confirmed()
        self.assertTrue(order_confirmed)
        cart.confirm_page_exit()
        cart.click_cancel_order()
        self.my_driver.get('https://www.demoblaze.com/index.html')
        header.click_cart_button()
        no_cart_items = cart.assert_no_cart_items()
        self.assertTrue(no_cart_items)

    def tearDown(self):
        bu.sleep(1)
        self.my_driver.quit()


if __name__ == '__main__':
    test_runner = bu.unittest.main(testRunner=bu.HtmlTestRunner.HTMLTestRunner(output='reports'))
    test_runner.runTests()
