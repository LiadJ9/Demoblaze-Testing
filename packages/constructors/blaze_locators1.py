import packages.utilities.blaze_driver as bu
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

# CB = Cart Button
# LHB = LogIn header Button
# UF = Username Field
# PF = Password Field
# LB = Login Button
# RP = Random Product

# # # # # LOCATORS - We use these to tidy up our code and save time searching for elements # # # # # #


class HL(object):
    hb = (bu.By.XPATH, '/html/body/nav/div[1]/ul/li[1]/a')
    FBHP = (bu.By.XPATH, '/html/body/nav/div[2]/div/ol/li[1]')
    FI = (bu.By.XPATH, '/html/body/nav/div[2]/div/ol/li[1]')
    SBHP = (bu.By.XPATH, '/html/body/nav/div[2]/div/ol/li[2]')
    SI = (bu.By.XPATH, '/html/body/nav/div[2]/div/div/div[2]/img')
    TBHP = (bu.By.XPATH, '/html/body/nav/div[2]/div/ol/li[3]')
    TI = (bu.By.XPATH, '/html/body/nav/div[2]/div/div/div[3]/img')

class MPL(object):
    BCP = (bu.By.XPATH, '/html/body/nav/div[2]/div/a[2]')
    second_pic = (bu.By.XPATH, '/html/body/nav/div[2]/div/div/div[2]/img')
    NB = (bu.By.XPATH, '/html/body/div[5]/div/div[2]/form/ul/li[2]/button')
    mc_img = (bu.By.XPATH, '/html/body/div[5]/div/div[2]/div/div[1]/div/a/img')
    PB = (bu.By.XPATH, '/html/body/div[5]/div/div[2]/form/ul/li[1]/button')
    FPI = (bu.By.XPATH, '/html/body/div[5]/div/div[2]/div/div[1]/div/a/img')



class Cart(object):
    CB = (bu.By.XPATH, '/html/body/nav/div[1]/ul/li[5]/a')
    LHB = (bu.By.XPATH, '/html/body/nav/div[1]/ul/li[5]/a')
    UF = (bu.By.ID, 'loginusername')
    PF = (bu.By.ID, 'loginpassword')
    LB = (bu.By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
    RP = (bu.By.XPATH, '//*[@id="tbodyid"]/div[1]/div/div/h4/a')