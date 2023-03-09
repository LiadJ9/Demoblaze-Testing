import packages.utilities.blaze_driver as bu
import packages.pages.blaze_pages as bp


class TestBlazeHome(bu.unittest.TestCase):

    def setUp(self):
        self.my_driver = bu.get_firefox_driver()
        self.my_driver.get('https://www.demoblaze.com/index.html')
        self.my_driver.maximize_window()
        header = bp.HeaderPage(self.my_driver)
        contact = bp.ContactPage(self.my_driver)
        alerts = bp.GeneralPage(self.my_driver)

    def test_Home_button(self):
        cmd = bp.HeaderPage(self.my_driver)
        cmd.click_home_button()

    def tearDown(self):
        bu.sleep(3)
        self.my_driver.quit()


class TestBlazeHeaders(bu.unittest.TestCase):

    def setUp(self):
        self.my_driver = bu.get_firefox_driver()
        self.my_driver.get('https://www.demoblaze.com/index.html')
        self.my_driver.maximize_window()

    def tearDown(self):
        bu.sleep(3)
        self.my_driver.quit()


class TestBlazeContact(bu.unittest.TestCase):
    def setUp(self):
        self.my_driver = bu.get_firefox_driver()
        self.my_driver.get('https://www.demoblaze.com/index.html')
        self.my_driver.maximize_window()

    def test_invalid_email_name_and_msg_OK(self):
        header = bp.HeaderPage(self.my_driver)
        contact = bp.ContactPage(self.my_driver)
        alerts = bp.GeneralPage(self.my_driver)
        header.click_contact_button()
        contact.insert_contact_name('Liad')
        contact.insert_mail('liadgmail.com')
        contact.msg_contents('this is the message i"m sending')
        contact.click_send()
        alert = alerts.find_alert()
        assert alert.text == 'Thanks for the message!!'

    def tearDown(self):
        bu.sleep(3)
        self.my_driver.quit()


class TestBlazeAboutUs(bu.unittest.TestCase):
    def setUp(self):
        self.my_driver = bu.get_firefox_driver()
        self.my_driver.get('https://www.demoblaze.com/index.html')
        self.my_driver.maximize_window()

    def tearDown(self):
        bu.sleep(3)
        self.my_driver.quit()


class TestBlazeLogInSignUp(bu.unittest.TestCase):

    def setUp(self):
        self.my_driver = bu.get_firefox_driver()
        self.my_driver.get('https://www.demoblaze.com/index.html')
        self.my_driver.maximize_window()

    def tearDown(self):
        bu.sleep(3)
        self.my_driver.quit()


class TestBlazeCart(bu.unittest.TestCase):

    def setUp(self):
        self.my_driver = bu.get_firefox_driver()
        self.my_driver.get('https://www.demoblaze.com/index.html')
        self.my_driver.maximize_window()

    def tearDown(self):
        bu.sleep(3)
        self.my_driver.quit()


if __name__ == '__main__':
    bu.unittest.main(testRunner=bu.HtmlTestRunner.HTMLTestRunner(output='reports'))
