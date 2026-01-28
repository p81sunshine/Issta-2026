def find_substring(str1, sub_str):
   return any(sub_str in str1 for s in str1)