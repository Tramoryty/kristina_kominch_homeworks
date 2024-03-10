# 5) Замените “#” на “/” в 'www.my_site.com#about '

web_site = 'www.my_site.com#about '

print(f'Адрес страницы с ошибкой: {web_site}')
print(f'Верный адрес страницы: {web_site.replace('#', '/')}')
