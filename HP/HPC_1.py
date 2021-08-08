import requests
from bs4 import BeautifulSoup

file=open('Input_HPC.txt')
all_SN=file.read().split('\n')
list_serial_numbers=[]
for serial_number in all_SN:
    if len(serial_number)==10:
        url='http://partsurfer.hpe.com/Search.aspx?SearchText='+serial_number
        urlcontent=requests.get(url)
        parsed_page=BeautifulSoup(urlcontent.content,'html.parser')
        part_data = parsed_page.findAll(id=True)

        description = ''
        pattern_list=['IC uP','IC, uP','IC,uP']

        pattern_list2=['HPE','HP']
        for part in part_data:
            if 'ctl00_BodyContentPlaceHolder_lblDescription' in part.attrs.get('id'):
                    description=part.text
                    prepared_row = serial_number + ';' + description

            for item in pattern_list:
                if item in part.text and 'ctl00_BodyContentPlaceHolder_gridCOMBOM_' in part.attrs.get('id'):
                    prepared_row += ';' + part.text
                    id = part.attrs.get('id')
                    quantity_id = id.replace('desc', 'qty')
                    quantity =parsed_page.find(id=quantity_id).text
                    prepared_row += ';' + quantity

        for part in part_data:
            if description:
                model=description.split(' ')[2]
                for item in pattern_list2:
                    N_item=(item+' '+ model).lower()
                    if N_item in part.text.lower() and 'ctl00_BodyContentPlaceHolder_gridCOMBOM_' in part.attrs.get('id'):
                        prepared_row += ';' + part.text
                        id = part.attrs.get('id')
                        quantity_id = id.replace('desc', 'qty')
                        quantity = parsed_page.find(id=quantity_id).text
                        prepared_row += ';' + quantity
            else:
                prepared_row=serial_number+';'+'No data on Page'
    else:
        prepared_row=serial_number+';'+'Incorrect SN'

    list_serial_numbers.append(prepared_row)

output=open('output.txt','w')
for SN in list_serial_numbers:
    output.write(SN+'\n')
output.close()
print('Done:) Check file output.txt in your folder.')
