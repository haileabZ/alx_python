def safe_print_division(a, b):
  try:
    result=a/b
    print("Inside result:{}".format(result))
  except ZeroDivisionError:
    print("Inside result:{}".format("None"))
    result="None"
  finally:
    print("{} / {} = {}".format(a, b, result))
