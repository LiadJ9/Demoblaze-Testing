from packages.utilities.blaze_driver import By

# # # # # LOCATORS - We use these to tidy up our code and save time searching for elements # # # # # #

# HL - HEADER LOCATORS

# CL - CONTACT LOCATORS

# AUL - ABOUT US LOCATORS

# MPL - MAIN PAGE LOCATORS


class HL(object):
    Logo_redirect = (By.ID, 'nava')
    Home = (By.XPATH, '/html/body/nav/div[1]/ul/li[1]/a')
    Contact = (By.XPATH, '/html/body/nav/div[1]/ul/li[2]/a')
    About_us = (By.XPATH, '/html/body/nav/div[1]/ul/li[3]/a')
    Cart = (By.ID, 'cartur')
    Login = (By.XPATH, '//*[@id="login2"]')
    Signup = (By.XPATH, '//*[@id="signin2"]')
    Username = (By.ID, 'nameofuser')
    logout = (By.XPATH, '//*[@id="logout2"]')


class CL(object):
    Cancel_button = (By.XPATH, '/html/body/div[1]/div/div/div[1]/button')
    Contact_email = (By.ID, 'recipient-email')
    Contact_name = (By.ID, 'recipient-name')
    Message_box = (By.ID, 'message-text')
    Send_message = (By.XPATH, '/html/body/div[1]/div/div/div[3]/button[2]')


class AUL(object):
    Close_button = (By.XPATH, '/html/body/div[4]/div/div/div[3]/button')
    Big_Play_button = (By.CLASS_NAME, 'vjs-big-play-button')
    Sound_OnOff = (By.XPATH, '/html/body/div[4]/div/div/div[2]/form/div/div/div[4]/div[1]/button')
    Sound_slider = (By.XPATH, '/html/body/div[4]/div/div/div[2]/form/div/div/div[4]/div[1]/div/div')
    Play_button = (By.CLASS_NAME, 'vjs-play-control')
    Fullscreen = (By.CLASS_NAME, 'vjs-fullscreen-control')
    total_volume = (By.CLASS_NAME, 'vjs-volume-level')


class MPL(object):
    Carousel_previous = (By.CLASS_NAME, 'carousel-control-prev')
    Carousel_next = (By.CLASS_NAME, 'carousel-control-next')
    Carousel_slide1 = (By.XPATH, '/html/body/nav/div[2]/div/ol/li[1]')
    Carousel_slide2 = (By.XPATH, '/html/body/nav/div[2]/div/ol/li[2]')
    Carousel_slide3 = (By.XPATH, '/html/body/nav/div[2]/div/ol/li[3]')
    Phone_cat = (By.CSS_SELECTOR, 'a.list-group-item:nth-child(2)')
    Laptop_cat = (By.CSS_SELECTOR, 'a.list-group-item:nth-child(3)')
    Monitor_cat = (By.CSS_SELECTOR, 'a.list-group-item:nth-child(4)')
    Previous = (By.ID, 'prev2')
    Next = (By.ID, 'next2')
    Add_to_cart = (By.XPATH, '/html/body/div[5]/div/div[2]/div[2]/div/a')

class LogInLocators(object):
    Login_username = (By.ID, 'loginusername')
    Login_password = (By.ID, 'loginpassword')
    Login_submit = (By.XPATH, '/html/body/div[3]/div/div/div[3]/button[2]')
    Login_cancel = (By.XPATH, '/html/body/div[3]/div/div/div[3]/button[1]')


class SignUpLocators(object):
    Signup_username = (By.ID, 'sign-username')
    Signup_password = (By.ID, 'sign-password')
    Signup_submit = (By.XPATH, '/html/body/div[2]/div/div/div[3]/button[2]')
    Signup_cancel = (By.XPATH, '/html/body/div[2]/div/div/div[3]/button[1]')


class CartPageLocators(object):
    Place_order = (By.XPATH, '/html/body/div[6]/div/div[2]/button')
    Name = (By.ID, 'name')
    Country = (By.ID, 'country')
    City = (By.ID, 'city')
    Credit_Card = (By.ID, 'card')
    Month = (By.ID, 'month')
    Year = (By.ID, 'year')
    item_exists = (By.ID, 'tbodyid')
    delete_first_item = (By.XPATH, '/html/body/div[6]/div/div[1]/div/table/tbody/tr[1]/td[4]/a')
    order_page_order = (By.XPATH, '/html/body/div[3]/div/div/div[3]/button[2]')
    order_confirmed = (By.CSS_SELECTOR, '.sweet-alert')
    confirmation_page_info = (By.XPATH, '/html/body/div[10]/p')
    confirm_page_exit = (By.XPATH, '/html/body/div[10]/div[7]/div/button')
    find_all_items = (By.XPATH, '/html/body/div[6]/div/div[1]/div/table/tbody/tr[@class="success"]')
    cancel_order = (By.XPATH, '/html/body/div[3]/div/div/div[3]/button[1]')





