class Family:
    def parents(self,mather=str(input()),father=str(input())):
        self.mather=mather
        self.father=father
        return "Name of father and mather:{},{}".format(father,mather)
    def years(self,year=int(input("Date of birth:\n")),year1=int(input())):
        self.year=year
        self.year1=year1
        return self.year-self.year1
p=Family()
a=p.parents()
print(a)
s=p.years()
print(s)


    