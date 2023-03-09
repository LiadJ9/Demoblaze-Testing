import constructors.blaze_locators as bl
import utilities.blaze_driver as bu
import HtmlTestRunner


class TestBlazeMain(bu.unittest.TestCase):

    def setUp(self):
        self.my_driver = bu.get_chrome_driver()
        self.my_driver.get('https://www.demoblaze.com/index.html')
        self.my_driver.maximize_window()

    def test_Home_button(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((bu.By.XPATH, bl.HL.hb)))
        home = self.my_driver.find_element(bu.By.XPATH, bl.HL.hb)
        home.click()
        assert self.my_driver.find_element(bu.By.XPATH, bl.HL.hb)

    def test_BCP(self):
        bu.WDW(self.my_driver, 10).until(bu.EC.visibility_of_element_located((bu.By.XPATH, bl.HL.hb)))
        home = self.my_driver.find_element(bu.By.XPATH, bl.HL.hb)
        home.click()
        change_picture = self.my_driver.find_element(bu.By.XPATH, bl.MPL.BCP)
        change_picture.click()
        bu.WDW(self.my_driver, 5).until(bu.EC.visibility_of_element_located((bu.By.XPATH, bl.MPL.second_pic)))
        assert self.my_driver.find_element(bu.By.XPATH, bl.MPL.second_pic)

    def test_button_next(self):
        bu.WDW(self.my_driver, 5).until(bu.EC.visibility_of_element_located((bu.By.XPATH, bl.HL.hb)))
        b_next = self.my_driver.find_element(bu.By.XPATH, bl.MPL.NB)
        b_next.click()
        bu.WDW(self.my_driver, 5).until(bu.EC.visibility_of_element_located((bu.By.XPATH, bl.MPL.mc_img)))
        assert self.my_driver.find_element(bu.By.XPATH, bl.MPL.mc_img)

    def test_button_previous(self):
        bu.WDW(self.my_driver, 5).until(bu.EC.visibility_of_element_located((bu.By.XPATH, bl.HL.hb)))
        next_b = self.my_driver.find_element(bu.By.XPATH, bl.MPL.NB)
        next_b.click()
        bu.WDW(self.my_driver, 5).until(bu.EC.visibility_of_element_located((bu.By.XPATH, bl.MPL.mc_img)))
        previous_b = self.my_driver.find_element(bu.By.XPATH, bl.MPL.PB)
        previous_b.click()
        bu.WDW(self.my_driver, 5).until(bu.EC.visibility_of_element_located((bu.By.XPATH, bl.MPL.FPI)))
        assert self.my_driver.find_element(bu.By.XPATH, bl.MPL.FPI)

    def test_first_button_header_picture(self):
        bu.WDW(self.my_driver, 5).until(bu.EC.visibility_of_element_located((bu.By.XPATH, bl.HL.hb)))
        first_button = self.my_driver.find_element(bu.By.XPATH, bl.HL.FBHP)
        first_button.click()
        bu.WDW(self.my_driver, 5).until(bu.EC.visibility_of_element_located((bu.By.XPATH, bl.HL.FI)))
        assert self.my_driver.find_element(bu.By.XPATH, bl.HL.FI)

    def test_second_button_header_picture(self):
        bu.WDW(self.my_driver, 5).until(bu.EC.visibility_of_element_located((bu.By.XPATH, bl.HL.hb)))
        second_button = self.my_driver.find_element(bu.By.XPATH, bl.HL.SBHP)
        second_button.click()
        bu.WDW(self.my_driver, 5).until(bu.EC.visibility_of_element_located((bu.By.XPATH, bl.HL.SI)))
        assert self.my_driver.find_element(bu.By.XPATH, bl.HL.SI)

    def test_third_button_header_picture(self):
        bu.WDW(self.my_driver, 5).until(bu.EC.visibility_of_element_located((bu.By.XPATH, bl.HL.hb)))
        third_button = self.my_driver.find_element(bu.By.XPATH, bl.HL.TBHP)
        third_button.click()
        bu.WDW(self.my_driver, 5).until(bu.EC.visibility_of_element_located((bu.By.XPATH, bl.HL.TI)))
        assert self.my_driver.find_element(bu.By.XPATH, bl.HL.TI)

    def tearDown(self):
        bu.sleep(3)
        self.my_driver.close()


if __name__ == '__main__':
    bu.unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
