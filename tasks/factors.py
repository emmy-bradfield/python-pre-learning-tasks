def factors(number):
    # ==============
    # Your code here
   print("The factors of",number,"are:")
   for i in range(1, number + 1):
       if number % i == 0:
           print(i)
    # ==============

print(factors(15)) # Should print [3, 5] to the console
print(factors(12)) # Should print [2, 3, 4, 6] to the console
<<<<<<< HEAD
print(factors(13)) # Should print “[]” (an empty list) to the console
=======
print(factors(13)) # Should print “[]” (an empty list) to the console
git add .
git commit -m "push to validate"
git push master origin
>>>>>>> b3f453d8c007dec7c25f5e395151c5524bb67430
