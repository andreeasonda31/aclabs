#heiii
'''

 some code
'''

#import six.moves -rezolva compatibilitatea intr python2 si python3

# my_string = 'test'
# my_string = "test2"
# c=int(raw_input('Number: '))
# print('Your number %s' % c)
##my_dict={'test':10,
		# 'abc' : [1,2,'test','test3'],
		# 'c' : dict(a=10),
		# 'cd': {'a':10}
 		# }
# print my_dict
# print my_dict['abc']
# my_dict['c'] ='a'
# #print dir(my_dict)
# a=range(10)
# print a[2:-1:2]
 

 

# def my_func(a,b,c,d=10):
# 	print locals()


# my_func(1,2,c='test')

def my_function(a,*args,**kwargs):
	print locals()

my_function(1,2,3,kw='test')