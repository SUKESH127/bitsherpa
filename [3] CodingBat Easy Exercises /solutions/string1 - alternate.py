def hello_name(name):
  return 'Hello ' + name + '!'

def make_abba(a, b):
  return a + b + b + a

def make_tags(tag, word):
  return '<' + tag + '>' + word + '</' + tag + '>'

def make_out_word(out, word):
  mid = int(len(out) / 2)
  # note that the 0 is optional
  # So this would also work:
  # return out[:mid] + word + out[mid:]
  return out[0:mid] + word + out[mid:]

def extra_end(str):
  return str[-2:] + str[-2:] + str[-2:]

def first_two(str):
  if len(str) == 0:
    return ""
  elif len(str) < 2:
    return str
  else:
    return str[0:2]

def first_half(str):
  mid = int(len(str)/2)
  return str[:mid]

def without_end(str):
  return str[1:-1]


