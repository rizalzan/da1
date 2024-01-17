

# ==Class==
# =Class adalah blueprint dari suatu objek yg ingin kita buat
class Students: 
    def __init__(self, name, age, hight):
        self.name = name
        self.age = age
        self.hight = hight

zan = Students (name='Zan', age='18', hight= '170 cm')
# zan disebut objek, name, age, hight adalah parameter
fay = Students (name='Fay', age='11', hight='160 cm') 
print(zan.name, zan.age)
print(fay.name, fay.age, fay.hight)

# ==rumus baku==
# class nama_class:
    # def __init__(self, parameter_1 )
        # self.parameter_1 = parameter_1