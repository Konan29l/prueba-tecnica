from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# a. Abrir una sesión de Selenium y un navegador desde el código
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

try:
    # b. Abrir un video de Youtube
    url = "https://www.youtube.com/watch?v=fyLkvjQVgQ0"
    driver.get(url)
    
    # c. Esperar unos segundos para que cargue el contenido dinámico
    time.sleep(2)


    # c. Extraer la cantidad de "Likes" presente en ese video
    try:
        like_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[contains(@aria-label, "Me gusta")]')
            )
        )
        likes = like_button.get_attribute('aria-label')
        print("Likes:", likes)
    except Exception as e:
        print("No encontró la cantidad de likes..")
        print("Error:", str(e))

    # d. Extraer la URL de ese video
    video_url = driver.current_url
    print("URL del video:", video_url)

finally:
    # e. Cerrar el navegador y cerrar la sesión de Selenium
    time.sleep(2)
    driver.quit()
