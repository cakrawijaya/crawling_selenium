import csv
class CleanFile():
    def cleanDaftarKasus(self):
            bad_words = ['Total']
            with open('datakasus_temporary.csv') as oldfile, open('data_kasus.csv', 'w') as newfile:
                non_blank = (line for line in oldfile if line.strip())
                for line in non_blank:
                    if not any(bad_word in line for bad_word in bad_words):
                        newfile.write(line)
            return bad_words

    def cleanDaftarDaerah(self):
        bad_words = ['Total']
        with open('datadaerah_temporary.csv') as oldfile, open('data_daerah.csv', 'w') as newfile:
            non_blank = (line for line in oldfile if line.strip())
            for line in non_blank:
                if not any(bad_word in line for bad_word in bad_words):
                    newfile.write(line)
        return bad_words

x = CleanFile()
x.cleanDaftarKasus()
x.cleanDaftarDaerah()