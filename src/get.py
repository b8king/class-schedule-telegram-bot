from openpyxl import load_workbook
import pyexcel as p
from bs4 import BeautifulSoup
import urllib.request
from urllib.request import urlopen
from socket import timeout
def download():
    try:
        html_page = urllib.request.urlopen("https://college-ural.ru/studentam/studentam-ochnogo-otdeleniya/raspisanie-zanyatiy.php")
        soup = BeautifulSoup(html_page, "html.parser")
        for link in soup.findAll('a', class_='link_underline'):
            url_file=link.get('href')
            break
        urllib.request.urlretrieve('https://college-ural.ru'+url_file, "data/document/xls.xls")

    except ConnectionResetError:
        print("==> ConnectionResetError")
        pass
    except timeout: 
        print("==> Timeout")
        pass
    p.save_book_as(file_name='data/document/xls.xls',
                dest_file_name='data/document/xlsx.xlsx')
