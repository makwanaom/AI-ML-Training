from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


driver = webdriver.Edge()


driver.get("https://www.instagram.com/")
sleep(5)


emailEle = driver.find_element(By.NAME, "username")
passEle = driver.find_element(By.NAME, "password")
btnEle = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')

emailEle.send_keys("vishnumakwana577@gmail.com")
sleep(3)
passEle.send_keys("555556")
sleep(3)
btnEle.click()
sleep(5)


reelsBtn = driver.find_element(By.XPATH, "//a[contains(@href, '/reels/')]")
reelsBtn.click()
sleep(5)


def get_reel_duration():
    try:
        
        duration_ele = driver.find_element(By.XPATH, '//video[@data-testid="reel_video"]')
        duration = float(duration_ele.get_attribute('duration'))
        return duration
    except Exception as e:
        print(f"Error getting reel duration: {e}")
        return 10



def scroll_to_next_reel():
    try:
        body_element = driver.find_element(By.TAG_NAME, 'body')
        body_element.send_keys(Keys.ARROW_DOWN)
        print("Scrolled to next reel.")
    except Exception as e:
        print(f"Error scrolling to next reel: {e}")



while True:

    reel_duration = get_reel_duration()
    print(f"Reel duration: {reel_duration} seconds")
    
    
    sleep(reel_duration)


    scroll_to_next_reel()

    sleep(2)


