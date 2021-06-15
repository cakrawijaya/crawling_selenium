import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import mysql.connector
from database import Database
from clean_file import CleanFile

class CovidCase():
    def __init__(self):
        self.path = r'C:\Users\CakraWijaya\Documents\selenium_covid\chromedriver'
        self.driver = webdriver.Chrome(self.path)
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("start-maximized")
        self.driver.get("https://covid19.tangerangkota.go.id/")
        self.database = Database()
        self.clean_file = CleanFile()

    def daftarKasus(self):
        table = self.driver.find_element_by_xpath('//*[@id="data"]/div/div[13]')
        with open('datakasus_temporary.csv', 'w', newline='') as csvfile:
            wr = csv.writer(csvfile)
            for row in table.find_elements_by_css_selector('tr'):
                wr.writerow([d.text for d in row.find_elements_by_css_selector('td')])
        return table
    
    def daftarDaerah(self):
        with open('datadaerah_temporary.csv', 'w', newline='') as csvfile:
            wr = csv.writer(csvfile)
            x = '//*[@id="data"]/div/div[13]/div/div['
            y = 1
            z = ']'
            for i in x:
                if y <=13:
                    daftar_table = x+str(y)+z
                    table = self.driver.find_element_by_xpath(daftar_table)
                    for kecamatan in table.find_elements_by_css_selector('th'):
                        for kelurahan in table.find_elements_by_css_selector('td:nth-child(1)'):
                            print(kecamatan.text, kelurahan.text)
                            wr.writerow([kecamatan.text,kelurahan.text])
                        y += 1
        self.driver.close()
        return x
    
    def cleanInputData(self):
        self.clean_file.cleanDaftarDaerah()
        self.clean_file.cleanDaftarKasus()
        self.database.inputDataDaerah()
        self.database.inputDataKasus()

x = CovidCase()
x.daftarKasus()
x.daftarDaerah()
x.cleanInputData()