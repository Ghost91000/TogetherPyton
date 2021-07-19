# Калькулятор
***
> Программа задумана для обработки целой строки ввода и последовательного выполнения арифметических операций.


Ключевые слова:

False - показатель ложности для булева типа;
True - показатель истинности для булева типа;
None - "пустой" объект;
and - логический оператор И;
with/as - менеджер контекста;
assert - условие, вызывающее исключение, если условие ложно;
break - оператор выхода из цикла;
class - тип, состоящий из методов и атрибутов;
continue - оператор перехода на следующую итерацию цикла;
def - обозначение функции;
del - определение функции;
elif - условный оператор в противном случае-если;
else - условный оператор в противном случае;
except - оператор перехвата исключения;
finally - выполняет инструкцию вне зависимости от исключения;
for - оператор цикла for;                
from - оператор импорта из модуля;
global - оператор создания доступности обращения к переменной за пределами функции;
if - условный оператор если;
import - оператор импорта модуля;
in - оператор проверки на вхождение;
is - оператор проверки ссылаются ли 2 объекта на одно место в памяти;
lambda - определение анонимной функции;
nonlocal - оператор создание доступности обращения к переменной в объемлющей инструкции;
not - логический оператор не;
or - логический оператор или;
pass - ничего не выполняющий оператор;
raise - оператор вызова исключения;
return - оператор возвращения результата;
try - выполнить инструкции, перехватив исключения;
while - условно-циклический оператор до тех пор;
yield - определение функции-генератора.
Помимо ключевых слов, в Python 3 присутствуют встроенные функции:

bool(x) - преобразование к типу bool, использующая стандартную процедуру проверки истинности. Если х является ложным или опущен, возвращает значение False, в противном случае она возвращает True.
bytearray([источник [, кодировка [ошибки]]]) - преобразование к bytearray. Bytearray - изменяемая последовательность целых чисел в диапазоне 0≤X<256. Вызванная без аргументов, возвращает пустой массив байт.
bytes([источник [, кодировка [ошибки]]]) - возвращает объект типа bytes, который является неизменяемой последовательностью целых чисел в диапазоне 0≤X<256. Аргументы конструктора интерпретируются как для bytearray().
complex([real[, imag]]) - преобразование к комплексному числу.
dict([object]) - преобразование к словарю.
float([X]) - преобразование к числу с плавающей точкой. Если аргумент не указан, возвращается 0.0.
frozenset([последовательность]) - возвращает неизменяемое множество.
int([object], [основание системы счисления]) - преобразование к целому числу.
list([object]) - создает список.
memoryview([object]) - создает объект memoryview.
object() - возвращает безликий объект, являющийся базовым для всех объектов.
range([start=0], stop, [step=1]) - арифметическая прогрессия от start до stop с шагом step.
set([object]) - создает множество.
slice([start=0], stop, [step=1]) - объект среза от start до stop с шагом step.
str([object], [кодировка], [ошибки]) - строковое представление объекта. Использует метод __str__.
tuple(obj) - преобразование к кортежу.
abs(x) - возвращает абсолютную величину (модуль числа).
all(последовательность) - возвращает True, если все элементы истинные (или, если последовательность пуста).
any(последовательность) - возвращает True, если хотя бы один элемент - истина. Для пустой последовательности возвращает False.
ascii(object) - как repr(), возвращает строку, содержащую представление объекта, но заменяет не-ASCII символы на экранированные последовательности.
bin(x) - преобразование целого числа в двоичную строку.
callable(x) - возвращает True для объекта, поддерживающего вызов (как функции).
chr(x) - возвращает односимвольную строку, код символа которой равен x.
classmethod(x) - представляет указанную функцию методом класса.
compile(source, lename, mode, ags=0, dont_inherit=False) - компиляция в программный код, который впоследствии может выполниться функцией eval или exec. Строка не должна содержать символов возврата каретки или нулевые байты.
delattr(object, name) - удаляет атрибут с именем 'name'.
dir([object]) - список имен объекта, а если объект не указан, список имен в текущей локальной области видимости.
divmod(a, b) - возвращает частное и остаток от деления a на b.
enumerate(iterable, start=0) - возвращает итератор, при каждом проходе предоставляющем кортеж из номера и соответствующего члена последовательности.
eval(expression, globals=None, locals=None) - выполняет строку программного кода.
exec(object[, globals[, locals]]) - выполняет программный код на Python.
filter(function, iterable) - возвращает итератор из тех элементов, для которых function возвращает истину.
format(value[,format_spec]) - форматирование (обычно форматирование строки).
getattr(object, name ,[default]) - извлекает атрибут объекта или default.
globals() - словарь глобальных имен.
hasattr(object, name) - имеет ли объект атрибут с именем 'name'.
hash(x) - возвращает хеш указанного объекта.
help([object]) - вызов встроенной справочной системы.
hex(х) - преобразование целого числа в шестнадцатеричную строку.
id(object) - возвращает "адрес" объекта. Это целое число, которое гарантированно будет уникальным и постоянным для данного объекта в течение срока его существования.
input([prompt]) - возвращает введенную пользователем строку. Prompt - подсказка пользователю.
isinstance(object, ClassInfo) - истина, если объект является экземпляром ClassInfo или его подклассом. Если объект не является объектом данного типа, функция всегда возвращает ложь.
issubclass(класс, ClassInfo) - истина, если класс является подклассом ClassInfo. Класс считается подклассом себя.
iter(x) - возвращает объект итератора.
len(x) - возвращает число элементов в указанном объекте.
locals() - словарь локальных имен.
map(function, iterator) - итератор, получившийся после применения к каждому элементу последовательности функции function.
max(iter, [args ...] * [, key]) - максимальный элемент последовательности.
min(iter, [args ...] * [, key]) - минимальный элемент последовательности. next(x) - возвращает следующий элемент итератора.
oct(х) - преобразование целого числа в восьмеричную строку.
open(le, mode='r', buering=None, encoding=None, errors=None, newline=None, closefd=True) - открывает файл и возвращает соответствующий поток.
ord(с) - код символа.
pow(x, y[, r]) - идентично выражению ( x ** y ) % r.
reversed(object) - итератор из развернутого объекта.
repr(obj) - представление объекта.
print([object, ...], *, sep=" ", end='\n', le=sys.stdout) - вывод результата на экран.
property(fget=None, fset=None, fdel=None, doc=None) - возвращает специальный объект дескриптора.
round(X [, N]) - округление до N знаков после запятой.
setattr(объект, имя, значение) - устанавливает атрибут объекта.
sorted(iterable[, key][, reverse]) - отсортированный список.
staticmethod(function) - статический метод для функции.
sum(iter, start=0) - сумма членов последовательности.
super([тип [, объект или тип]]) - доступ к родительскому классу.
type(object) - возвращает тип объекта.
type(name, bases, dict) - возвращает новый экземпляр класса name.
vars([object]) - словарь из атрибутов объекта. По умолчанию - словарь локальных имен.
zip(*iters) - итератор, возвращающий кортежи, состоящие из соответствующих элементов аргументов-последовательностей.