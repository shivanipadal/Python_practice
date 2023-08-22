def hi(func):
  def hello():
    print("ONE")
    func()
    print("TWO")
  return hello


@hi
def one_func():
   print("INsode main function")
   
one_func()