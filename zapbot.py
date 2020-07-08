from selenium import webdriver
import time

class WhatsappBot:
    def __init__(self): 
        self.mensagem = "Testando chat bot para whatsapp. Gabriel é lindo"
        self.grupos = ["Nath", "PV calaboca", "Heleno", "Mozão 💕"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def EnviarMensagens(self):
        # class="_3uMse" Mozão 💕
        # <span data-testid="send" data-icon="send" 
        # <span dir="auto" title="🔥FESTA JUNINA BELTRAO🔥" class="_3ko75 _5h6Y_ _3Whw5"><img crossorigin="anonymous" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" alt="🔥" draggable="false" class="b68 emoji wa _3Whw5" style="background-position: -20px -80px;">FESTA JUNINA BELTRAO<img crossorigin="anonymous" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" alt="🔥" draggable="false" class="b68 emoji wa _3Whw5" style="background-position: -20px -80px;"></span>
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(30)
        for grupo in self.grupos:
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(3)
            grupo.click()
            chat_box = self.driver.find_element_by_class_name('_3uMse')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)

bot = WhatsappBot()
bot.EnviarMensagens()
        
