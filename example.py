import UUF
import os

### tree view in dict ###
print(UUF.dicttreeview(os.getcwd()))


### type checking ###
def function(): pass
l = [1, 2, 3, 4, 5]
check_type = UUF.CheckType(
    ["hey", 5, function, l],
    [str, (int, str), (UUF.function, str), (str, int, list)]
)



### pattern checking ###
test_0 = (1, ['hey', 'hey'])
test_1 = [2, 9, 'test', (1, 'test')]
check_pattern = UUF.Pattern(
	[test_0, test_1],
	[(int, [str, str]), [int, int, str, (int, str)]]
)
print('type checking :', check_type, check_pattern)



### unpacking all element from var ###
v = (1, 2, (3, 4, 5), ['t', 2])
print('unpacking all testing :', UUF.Unpack(v))



### error data management testing ###
ED = UUF.ErrorData(
    {TypeError: "Here is a type error",
     ValueError: "some value error",
     UUF.CharError: "custom char error !"}
)
# raise Exception(ED[TypeError])



### custom error message testing ###
try:
	'a' + 2

except Exception as e:
	raise UUF.LenghtError(UUF.BasicErrorMessage(e, __file__))