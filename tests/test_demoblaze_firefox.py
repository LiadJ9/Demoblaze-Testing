import constructors.blaze_locators as bl
import utilities.blaze_driver as bu


class TestBlazeMain(bu.unittest.TestCase):

    def setUp(self):
        self.my_driver =  bu.get_firefox_driver()
        self.my_driver.get('https://www.demoblaze.com/index.html')
        self.my_driver.maximize_window()

    def test_Home_button(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located(bl.HL.home_button))
        home = self.my_driver.find_element(bl.HL.home_button)
        home.click()


    def tearDown(self):
        bu.sleep(3)
        self.my_driver.close()

