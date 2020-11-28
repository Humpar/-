class ALF():
    Tc=0
    Cc=0
    
    def __init__(self,T,C,dit,boxian,*sugar):
        self.T=T
        self.C=C
        self.dit=dit
        self.sugar=sugar
        self.Tc = 0
        self.Cc = 0
        self.line = 0
        self.spary = 0
        
        print(T,C,dit)
    def data(self):
        #global self.Tc,self.Cc,self.line
        self.Tc = int(input('T荧光的浓度'))
        self.Cc = int(input('C荧光的浓度'))
        self.line = int(input('荧光行数'))
        self.spary = int(input('喷量'))

    def compute(self):
        
        Vl=self.line*30*self.spary
        V = Vl+(self.line*10)
        
        print ('最少需要溶液量为{}ul，推荐配液量为{}ul'.format(Vl,V))
        s = input('请选择是否使用推荐配液量，是请输1，否请输0,也可以输入你选择的配液量')
        if s == '1':
            VT = V/self.Tc
            VC = V/self.Cc
            Vdit = V-VT-VC
            print ('T的配液量为{}ul,C的配液量为{}ul,buffer的量为{}ul'.format(VT,VC,Vdit))

        elif s == '0':
            VT = Vl/self.Tc
            VC = Vl/self.Cc
            Vdit = Vl-VT-VC
            print ('T的配液量为{}ul,C的配液量为{}ul,buffer的量为{}ul'.format(VT,VC,Vdit))

        else :
            s = int(s)
            VT = s/self.Tc
            VC = s/self.Cc
            Vdit = s-VT-VC
            print ('T的配液量为{}ul,C的配液量为{}ul,buffer的量为{}ul'.format(VT,VC,Vdit))


        
        
    
ji=ALF(3900,4000,9818,4300)
ji.data()
ji.compute()
