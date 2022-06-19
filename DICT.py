thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "bhp": 650,
  "cc": 3999
  "colors": ["red", "blue", "white"]
}

print(thisdict)
print(type(thisdict))
print(len(thisdict))

#fetch dictionary key
print(thisdict.keys())

#fetch dictionary only value
print(thisdict.value())

#fetch using key
print(thisdict[model])
