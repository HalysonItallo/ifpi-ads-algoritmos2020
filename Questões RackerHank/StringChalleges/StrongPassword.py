from auxString import contains

def main():
  n = int(input())
  password = input()
  minimumNumber(n, password)
  
  
def minimumNumber(n, password):
  count_number = 0
  count_lower_case = 0
  count_upper_case = 0
  count_special_characteres = 0

  number  =  "0123456789" 
  lower_case  =  "abcdefghijklmnopqrstuvwxyz" 
  upper_case  =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
  special_characters  =  "! @ # $% ^ & * () - +"
  
  result_strong_password = 0
  
  for i in range(len(password)):
    if contains(number, password[i]):
      count_number +=1
    elif contains(lower_case, password[i]):
      count_lower_case +=1
    elif contains(upper_case, password[i]):
      count_upper_case +=1
    elif contains(special_characters, password[i]):
      count_special_characteres += 1
  
  if count_number < 1:
    result_strong_password += 1
  elif count_lower_case < 1:
    result_strong_password += 1
  elif count_upper_case < 1:
    result_strong_password += 1
  elif count_special_characteres < 1:
    result_strong_password += 1
  
  if n < 6:
    result_strong_password += (6-n) - result_strong_password
  
  print(result_strong_password)


main()