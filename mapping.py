class Mapping:
    def __init__(self, iterable):
        self.items_list=[]
        self.__update(iterable)
        
    def update(self, iterable):
        import ipdb; ipdb.set_trace()
        for item in iterable:
            self.items_list.append(item);
            
    __update = update

class MappingSubclass(Mapping):
    def update(self, keys, values):
        for item in zip(keys, values):
            self.items_list.append(item)
            
class Parrot(object):
    def __init__(self):
            self._voltage=100000
            self._voltage1=50000
    def voltage(self):
            print 'A'
            return self._voltage
    def voltage(self, v):
            print 'A'
            self._voltage = v
    def voltage1(self):
            print 'B'
            return self._voltage1
    #voltage = property(voltage, voltagex);
            
class C(object):
    def __init__(self):
            self._x = 12;
    
    @property
    def x(self):
        return self._x;
        
    @x.setter
    def x(self, value):
        self._x = value;
        
    @x.deleter
    def x(self):
        del self._x;          
           
a = Mapping([x for x in range(0, 10)])
print a.items_list
a.update(['a', 'b'])
print a.items_list

b = MappingSubclass(a.items_list)
print b.items_list
b.update([1, 2, 3], [3, 2, 1])
print b.items_list

c = []
c.append('b')
print c

print "--------------"

a = Parrot()
print a.voltage
print a._voltage1
a.voltage=100
a._voltage1=50
print a.voltage
print a._voltage1
