from textwrap import dedent
def game_instructions():
  script = dedent("""***Welcome to mad libs***
      ***********************************
      ***********************************
      **********************************""")
  print(script)
  return script   
game_instructions()
def pull_template():
  with open("madlib_clin/template.txt") as template:
    x = template.read()
    print(x)
  return x
pull_template()
def pull_keys():
  with open("madlib_clin/template.txt") as template:
    content = template.read()
    key_list = []
    last_spot = 0
    bracket_var = content.count("{")
    for item in range(bracket_var):
      start_spot = content.find("{",last_spot) + 1
      last_spot = content.find("}", start_spot)
      txt_key = content[start_spot : last_spot]
      key_list.append(txt_key)
      print(key_list)
    return key_list
pull_keys()
# def mad_lib_bulk(key_list):
  
#   mad_lib_bulk()
