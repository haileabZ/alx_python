def safe_print_division(a, b):
  try:
    result=a/b
  except (TypeError, ZeroDivisionError):
    result="None"
  finally:
    print("Inside result: {}".format(result))
    print("{} / {} = {}".format(a, b, result))
   
