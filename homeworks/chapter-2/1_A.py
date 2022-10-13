def greetings(n):
    n=n.split(' ')
    return(f'Доброго времени суток, {n[0]} '+f'"Человек" {n[-1]}'+"!")
print(greetings('Гендо Геннадий'))