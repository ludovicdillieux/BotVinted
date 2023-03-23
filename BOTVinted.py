from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By #Permet d'accéder aux différents élements de la page web

from webdriver_manager.chrome import ChromeDriverManager

# On crée une instance du web-driver Firefox et on va sur la page de eBay.fr
catalog_id = input("Categorie : ")
size_id = input("Taille article : ")
brand_id = input("Marque : ")
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(f"https://www.vinted.fr/vetements?order=newest_first&catalog[]={catalog_id if size_id else ''}&size_id[]={size_id if size_id else ''}&brand_id[]={brand_id if brand_id else ''}")
 
# En fonction de notre connection et des performance de notre machine il faudra attendre
 
# que la page charge avant de passer à 5*la suite
def retrieve_article(driver): 
    sleep(2)
    offers = driver.find_elements(By.XPATH, "//div[@class='feed-grid__item']")
    nb_offre = 0
    for offer in offers:
        pseudo = offer.find_element(By.CLASS_NAME, "web_ui__Text__text")
        prix = offer.find_element(By.TAG_NAME, "h3")
        voir_annonce = offer.find_element(By.CLASS_NAME, "web_ui__ItemBox__overlay")
        image_div = offer.find_elements(By.CLASS_NAME, "web_ui__Image__ratio")
        marque_div = offer.find_elements(By.CLASS_NAME, "web_ui__ItemBox__details")
        taille_div = offer.find_elements(By.CLASS_NAME, "web_ui__ItemBox__subtitle")
        print(pseudo.text)
        for image in image_div:
            ur_img = image.find_element(By.CLASS_NAME, "web_ui__Image__content").get_attribute("src")
            print(ur_img)
        for marque in marque_div:
            nom_marque = marque.find_element(By.CLASS_NAME, "web_ui__Text__left").text
            print(f"Nom de la marque : {nom_marque}")
        for taille in taille_div:
            taille_article = taille.find_element(By.CLASS_NAME, "web_ui__Text__left").text
            print(f"Taille : {taille_article}")
        
        print(f"Prix : {prix.text}")
        print(f"Voir l'annonce : {voir_annonce.get_attribute('href')}")
        print("-----------")
        if nb_offre <= 3:
            nb_offre += 1
        else:
            break

    print(nb_offre)

def check_new_article():
    pass

retrieve_article(driver)