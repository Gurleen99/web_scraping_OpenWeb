from csv import writer
#just to create 
with open(r'C:\Users\Lenovo\PycharmProjects\pythonProject\R_ladies_global1_demo.csv', 'w', encoding='utf8', newline='') as f:
    write_data = writer(f)
    header = ['Personal_websites','First Name ', 'Last Name', 'Profession', 'Organization', 'Locality','Region','Country','Social Media']
    write_data.writerow(header)
