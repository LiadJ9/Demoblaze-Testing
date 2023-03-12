import packages.constructors.blaze_locators1 as bl1
import packages.utilities.blaze_driver as bu
import HtmlTestRunner
import packages.pages.blaze_pages1 as bp1


class TestBlazeMain(bu.unittest.TestCase):

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

    def test_add_item_to_cart_while_LoggedIn(self):
        bu.WDW(self.my_driver, 5).until(bu.EC.visibility_of_element_located((*bl1.Cart.LHB,)))
        LogIn_B = self.my_driver.find_element(*bl1.Cart.LHB,)
        LogIn_B.click()
        bu.WDW(self.my_driver, 5).until(bu.EC.visibility_of_element_located((*bl1.Cart.UF,)))
        UNF = self.my_driver.find_element(*bl1.Cart.UF,)
        UNF.clear()
        UNF.send_keys('alex12345')
        PF = self.my_driver.find_element(*bl1.Cart.PF,)
        PF.clear()
        PF.send_keys('12345')
        LB = self.my_driver.find_element(*bl1.Cart.LB,)
        LB.click()
        bu.WDW(self.my_driver, 5).until(bu.EC.visibility_of_element_located((*bl1.Cart.RP,)))
        RP = self.my_driver.find_element(*bl1.Cart.RP,)
        RP.click()


    def tearDown(self):
        bu.sleep(3)
        self.my_driver.close()


if __name__ == '__main__':
    bu.unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
