import packages.utilities.blaze_driver as bu
import packages.constructors.blaze_locators1 as bl1

class BasePage(object):
    def __init__(self, my_driver):
        self.my_driver = my_driver
class HP(BasePage):
    def log_in_site(self):
        bu.WDW(self.my_driver, 5).until(bu.EC.visibility_of_element_located((*bl1.Cart.LHB,)))
        LogIn_B = self.my_driver.find_element(*bl1.Cart.LHB, )
        LogIn_B.click()
        bu.WDW(self.my_driver, 5).until(bu.EC.visibility_of_element_located((*bl1.Cart.UF,)))
        UNF = self.my_driver.find_element(*bl1.Cart.UF, )
        UNF.clear()
        UNF.send_keys('alex12345')
        PF = self.my_driver.find_element(*bl1.Cart.PF, )
        PF.clear()
        PF.send_keys('12345')
        LB = self.my_driver.find_element(*bl1.Cart.LB, )
        LB.click()
