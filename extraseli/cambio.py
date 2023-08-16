from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pymongo
client = pymongo.MongoClient("mongi", 27017, username='root',password='rootpassword') 
print(client)
print(client.list_database_names())
mydb = client["Dolarcambio"]

mycol = mydb["cambiodiario"]
#from selenium.webdriver.common.keys import Keys

#from webdriver_manager.chrome import ChromeDriverManager

#driver = webdriver.Chrome(ChromeDriverManager().install())
#opt = webdriver.chrome.options.Options()
#capabilities = opt.to_capabilities()

options = Options()
options.headless = True
capabilities = options.to_capabilities()
driver = webdriver.Remote(command_executor="http://seli:4444/wd/hub", desired_capabilities=capabilities,)
#driver = webdriver.Chrome('C:\chromedriver.exe')
driver.get('https://www.dof.gob.mx/indicadores.php#gsc.tab=0')
dfecha = driver.find_element(By.ID, "dfecha")
dfecha.send_keys("01/08/2023")
driver.implicitly_wait(100)
hfecha = driver.find_element(By.ID, "hfecha")
hfecha.send_keys("13/08/2023")
driver.implicitly_wait(100)
btn_consultar = driver.find_element(By.CSS_SELECTOR, "img[src*='imagesnew/btn_consultar']")
print(btn_consultar)
driver.implicitly_wait(10)
btn_consultar.click()
driver.implicitly_wait(100)
driver.implicitly_wait(100)

ele= driver.find_elements(By.CLASS_NAME,"txt")
print(ele[0].text)
print(ele[1].text)
print("************************")
#print(ele)
e=0
a={}
a["rango_fechas"] =ele[1].text
for i in range(2,len(ele),2):
    a[str(e)]={'fecha':ele[i].text,'cambio':ele[i+1].text}
    print("Fecha: "+ ele[i].text)
    print("Cambio: " + ele[i+1].text)
    e +=1
    print("*******************")
print("------------------------")
print(a)
document= a
mycol.insert_one(document)

