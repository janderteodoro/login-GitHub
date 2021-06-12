from selenium import webdriver
from time import sleep


class ChromeAuto:
    def __init__(self):
        self.driver_path = 'chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('user-data-dir-Perfil')
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )

    def acess(self, url):
        self.chrome.get(url)

    def close(self):
        self.chrome.quit()

    def clica_sign_in(self):
        try:
            btn_sign_in = self.chrome.find_element_by_link_text('Sign in')
            btn_sign_in.click()
        except Exception as e:
            print('Erro ao clicar em Sign in', e)

    def to_do_login(self, login, password):
        try:
            user_input = self.chrome.find_element_by_id('login_field')
            password_input = self.chrome.find_element_by_id('password')
            btn_sign = self.chrome.find_element_by_xpath('//*[@id="login"]/div[4]/form/div/input[12]')
            user_input.send_keys(login)
            password_input.send_keys(password)
            sleep(3)
            btn_sign.click()
        except Exception as e:
            print('Erro ao realizar login', e)

    @classmethod
    def read_login(cls):
        try:
            email = input('Digite seu email do github: ')
            password = input('Digite a sua senha: ')
        except Exception as e:
            print('Valores inválidos', e)
        else:
            return email, password


if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acess('https://github.com/')
    sleep(5)
    chrome.clica_sign_in()
    sleep(5)
    login = chrome.read_login()
    chrome.to_do_login(login[0], login[1])
    sleep(10)
    chrome.close()
