import utilities.blaze_driver as bu
# MainPageLocators = MPL
# HeaderLocators = HL

# first_button_header_picture = FBHP
# second_button_header_picture = SBHP
# third_button_header_picture = TBHP

# first_image = FI
# second_image = SI
# third_image = TI

# button_change_picture = BCP
# NB = next_button
# PB = previous_button
# FPI = first_page_image

# # # # # LOCATORS - We use these to tidy up our code and save time searching for elements # # # # # #


class HL(object):
    home_button = (bu.By.XPATH, '/html/body/nav/div[1]/ul/li[1]/a')
    hb = '/html/body/nav/div[1]/ul/li[1]/a'
    FBHP = '/html/body/nav/div[2]/div/ol/li[1]'
    FI = '/html/body/nav/div[2]/div/ol/li[1]'
    SBHP = '/html/body/nav/div[2]/div/ol/li[2]'
    SI = '/html/body/nav/div[2]/div/div/div[2]/img'
    TBHP = '/html/body/nav/div[2]/div/ol/li[3]'
    TI = '/html/body/nav/div[2]/div/div/div[3]/img'

class MPL(object):
    BCP = '/html/body/nav/div[2]/div/a[2]'
    second_pic = '/html/body/nav/div[2]/div/div/div[2]/img'
    NB = '/html/body/div[5]/div/div[2]/form/ul/li[2]/button'
    mc_img = '/html/body/div[5]/div/div[2]/div/div[1]/div/a/img'
    PB = '/html/body/div[5]/div/div[2]/form/ul/li[1]/button'
    FPI = '/html/body/div[5]/div/div[2]/div/div[1]/div/a/img'



class CartPageLocators(object):
    pass