import time
from selenium.webdriver.common.by import By
import pytest
import selenium
from selenium import webdriver
from selenium import webdriver

e_mail = 'denzher54@yandex.ru'
passw = '123456789963ll'

#первая часть#

@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('C:\chromedriver_win32//chromedriver.exe')
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends.skillfactory.ru/login')

   yield

   pytest.driver.quit()


def test_show_my_pets():
   # Вводим email
   pytest.driver.find_element(By.ID, "email").send_keys('denzher54@yandex.ru')
   # Вводим пароль
   pytest.driver.find_element(By.ID, "pass").send_keys('123456789963ll')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
   # Нажимаем на кнопку "Мои Питомцы"
   pytest.driver.find_element(By.XPATH, '//a[contains(text(), "Мои питомцы")]').click()
   time.sleep(5)



   images = pytest.driver.find_element(By.CSS_SELECTOR, '.card-deck .card-img-top')
   names = pytest.driver.find_element(By.CSS_SELECTOR, '.card-deck .card-title')
   descriptions = pytest.driver.find_element(By.CSS_SELECTOR, '.card-deck .card-text')
   all_my_pets_number = pytest.driver.find_element(By.XPATH, '//div[contains(@class, ".col-sm-4 left")]/text()[2]')

   for i in range(len(names)):
    assert images[i].get_attribute('src') != ''
    assert names[i].text != ''
    assert descriptions[i].text != ''
    assert ', ' in descriptions[i]
    parts = descriptions[i].text.split(", ")
    assert len(parts[0]) > 0
    assert len(parts[1]) > 0

    pets_numb = int(pytest.driver.find_element(By.XPATH, '//div[@class=".col-sm-4 left"]').text.split('\n')[1].split(":")[1])
    print('Количество питомцев:', pets_numb)

    all_pets = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr')
    print(len(all_pets))

    all_pets = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr')
    pet_names = []
    for pet in all_pets:
            pet_names.append(pet.text.split(' ')[0])
            print(pet_names)

    all_pets = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr')
    pet_types = []
    for pet in all_pets:
        pet_types.append(pet.text.split(' ')[1])
    print(pet_types)