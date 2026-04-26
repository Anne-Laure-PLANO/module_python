
class Essai :
    __test_variable = 2
    _variable = 5




if __name__ == '__main__':
  essai = Essai()
  print(essai._variable)
  print(essai.__test_variable)