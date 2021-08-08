# pro cesky str
import requests
from bs4 import BeautifulSoup

file=open('Input_DELL.txt')
all_SN=file.read().split('\n')
list_serial_numbers=[]
for serial_number in all_SN:
    if len(serial_number)==7:
        prepared_row=''
        url='http://www.dell.com/support/home/cz/cs/czdhs1/product-support/servicetag/'+serial_number+'/configuration'
        urlcontent=requests.get(url)
        parsed_page=BeautifulSoup(urlcontent.content,'html.parser')

        part_data=parsed_page.findAll('h1',class_='')
        for part in part_data:
            if 'Podpora pro produkt' in part.text:
                hw_box=part.text[len('Podpora pro produkt__'):(len(part.text)-len('____Přidat k mým produktům__Změnit produkt_'))].strip('\n\t')
                prepared_row = serial_number + ';' + hw_box

        my_proc=parsed_page.findAll(class_='Troubleshooting-left-offset-20 col-lg-7 col-md-7 col-sm-7')
        for part in my_proc:
            if part.text.startswith('PROCESSOR,') or part.text.startswith('Processor,'):
                prepared_row+=';'+part.text

        my_proc=parsed_page.findAll(id='ConfigContainer')
        for part in my_proc:
            if 'Další díly' in part.text:
                prepared_row+=';'+'Config-section OTHER PARTS!'
        Row=prepared_row

        if len(Row)==0:
            Row=serial_number+';'+'No data on Page'

    else:
        Row=serial_number+';'+'Incorrect SN'

    list_serial_numbers.append(Row)

output=open('output.txt','w')
for SN in list_serial_numbers:
    output.write(SN+'\n')
output.close()
print('Done:) Check file output.txt in your folder.')
