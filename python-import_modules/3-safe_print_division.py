def safe_print_division(a, b):
  try:
    result=a/b
  except ZeroDivisionError:
    print("Inside result:{}".format("None"))
  finally:
    print("Inside result:{}".format(result))
    print("{} / {} = {}".format(a, b, result))
