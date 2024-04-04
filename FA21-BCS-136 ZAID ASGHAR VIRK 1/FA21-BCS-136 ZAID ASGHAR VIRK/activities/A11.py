directory = {}

def add_entry(full_name, contact_number):
  directory[full_name] = contact_number

def find_entry(full_name):
  if full_name in directory:
    return directory[full_name]
  else:
    return None

add_entry(("John", "Doe"), "123-4567")
add_entry(("Jane", "Doe"), "234-5678")

search_full_name = ("John", "Doe")
contact_number = find_entry(search_full_name)

if contact_number:
  print(f"{search_full_name[0]} {search_full_name[1]}'s contact number is {contact_number}")
else:
  print(f"{search_full_name[0]} {search_full_name[1]} is not in the directory")