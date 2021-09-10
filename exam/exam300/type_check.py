string = 'string value'
integer = 10
float_value = 3.4
bool = True
# 기본 자료형의 타입 비교
print(type(string), type(integer), type(float_value), type(bool))

print(type(string) == type(''))

print(type(integer) == type(0))

print(type(float_value) == type(0.1))

print(type(bool) == type(True))

print(isinstance(string, str))

print(isinstance(integer, int))

print(isinstance(float_value, float))

def test():
    pass
import types
print(type(test) == types.FunctionType)


