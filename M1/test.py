users_prompt = "Please give me your first and last name, as well as your age"
users_dict ={} # Dictionary of names to return at the end 
max_iter = 4

# While loop to collect inputs from several users as controlled by max_iter parameter
while len(users_dict) < max_iter:

  try:
    input_str = input(users_prompt) # Prompt user for: First name, Last name, and Age.
    input_list = input_str.split()
    age_num = int(input_list[-1])
  except ValueError:
       print ("Age must be an integer, please")
       continue
  
  else:
    try:
      firstlast = input_list[0]+"-"+input_list[1] # Concatenate the First name and the Last name into a single string so it looks like “Last-First”
      users_dict[firstlast] = age_num 
    except:
      print("Whew!, something else occurred. Please try again")
      continue 

with open("myOutput.txt", 'w') as f: 
    for key, value in users_dict.items(): 
        f.write('%s:%s\n' % (key, value))