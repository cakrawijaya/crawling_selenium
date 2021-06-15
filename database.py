import mysql.connector

class Database():
    def __init__(self):
        self.mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="covid19_case")
        self.mycursor = self.mydb.cursor()

    def inputDataDaerah(self):
        sql1 = "TRUNCATE TABLE covid_case"
        sql2 = "LOAD DATA INFILE 'C:/Users/CakraWijaya/Documents/selenium_covid/data_kasus.csv' INTO TABLE covid_case FIELDS TERMINATED BY ',' LINES TERMINATED BY '\r\n' (kelurahan, suspek_aktif_dirawat, konfirmasi_total, konfirmasi_dirawat, konfirmasi_sembuh, konfirmasi_meninggal)"
        self.mycursor.execute(sql1)
        self.mycursor.execute(sql2)
        self.mydb.commit()

    def inputDataKasus(self):
        sql1 = "TRUNCATE TABLE data_daerah"
        sql2 = "LOAD DATA INFILE 'C:/Users/CakraWijaya/Documents/selenium_covid/data_daerah.csv' INTO TABLE data_daerah FIELDS TERMINATED BY ',' LINES TERMINATED BY '\r\n' (kecamatan, kelurahan)"
        self.mycursor.execute(sql1)
        self.mycursor.execute(sql2)
        self.mydb.commit()
x = Database()
x.inputDataDaerah()
x.inputDataKasus()