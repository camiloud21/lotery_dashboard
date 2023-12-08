from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = False
options.add_argument("--window-size=1920,1200")

nmayor_list = []

DRIVER_PATH = '/opt/homebrew/bin/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH,options=options,)
driver.get('https://loteriadeboyaca.gov.co/inicio/resultados/')
sleep(1)
iframe = driver.find_element(By.CLASS_NAME, "container > iframe")
driver.switch_to.frame(iframe)
driver.find_element(By.TAG_NAME, "input").click()
sorteos = driver.find_elements(By.TAG_NAME,'li')
sleep(1)

# for sorteo in sorteos:
#     sorteo.click()
sleep(1)
print(driver.find_element(By.CLASS_NAME, "billete-serie").text)
nmayor_list.append(driver.find_element(By.CLASS_NAME, "billete-serie").text)

#nmayor_list.append(nmayor)

print("El listado de premios mayores son " + str(nmayor_list))

driver.switch_to.default_content()


