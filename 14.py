x = '%u0421%u043A%u0430%u043D%u0435%u0440 %u043F%u0440%u0438'
y = x.replace('%', '\\').decode('unicode-escape')
print y

#Сканер при
type(y)
<type 'unicode'>