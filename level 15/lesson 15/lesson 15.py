# კაჰუტი რაც გავაკეთეთ ამ კაჰუტზე ივარჯიშეთ, ჩნააწერი ნახეთ ხელახლა,
# ამოიწერეთ ყველა კითხვა და დეტალურად ახსენით კომენტარის სახით პასუხი


# 1.რომელ ბიბლიოთეკას ვიყენებთ პითონში გეომეტრიული ფიგურების ასაგებად?

#        პასუხია turtle რადგანაც ის გამოიყენება გეომეტრიული ფიგურების ასაგებად



#   2. რომელ ფუნქციას ვიყენებთ როდესაც გვინდა რომ ტერმინალში მოვახდინოთ დაბეჭდვა?


#         პასუხია print(...) ფუნქცია რადგან ის გამოიყენება რაიმის ტერმინალში დასაბეჭდად


# 3. პითონის გამოყენებით შეგვიძლია ალგორითმების შექმნა.

#    პასუხია False  რადგან არ შეგვიძლია რომ პითონის გამოყენებით ალგორითმები შევქმნათ


# 4.  ათწილადზე სამუშაოდ რომელ მონაცემთა ტიპს ვიყენებთ?

#     პასუხია float რადგან ის გამოიყენება ათწილადებთან როდესაც გვინდა მუშაობა


# 5.რომელია პითონისთვის სწორი კომენტარი? 

#      პასუხია # 

# 6. რომელ ფუნქციას ვიყენებთ მომხმარებლისგან terminal-იდან ტექსტის მისაღებად?

#       პასუხია Input ფუნქციას რადგან სწორედაც რომ ეს ფუნქცია გამოიყენება ამისთვის


# 7. input-იდან მიღებული ინფორმაცია ინახება სტრინგის სახით.

#       პასუხია True 


# 8.როგორ ვამოწმებთ მონაცემთა ტიპს? 

# პასუხია type(x) აქ ვიყენებთ type ფუნქციას იმისათვის რომ გავიგოთ რომელი ტიპისაა მონაცემი

# 9. რომელი ცვლადი ინახავს ათწილადს?

#  პასუხია x = 10/2 რადგან როგორც ვიცით გაყოფისას terminal-ში ჩვენ ვიღებთ float რიცხვს ანუ იგივე ათწილადის

#  10. რომელ ვარიანტშია პითონის ცვლადი სწორად შექმნილი

#     პასუხია x = 10 რადგან პითონში ცვლადი ასე იქმნება


# 11. რას გამოიტანს კოდი? 

# name = "goal"

# surname = "orientadze"

# age = 100

# print(name + surname + age)

# პასუხია error-ს რადგან როგორც ვიცით string ტიპის მონაცემს არ შეიძლება int ტიპის მოაცემი მივუმატოთ
# ან ჩავატაროთ ნებისმიერი მათემატიკური მოქმედება


# 12. რას გამოიტანს კოდი?

# num1 = 10

# num2 = 20 

# print(str(num1)+ str(num2))


# პასუხია 1020 რადგან როგორც ვიცით string ტიპის მონაცემს თუ მივუმატეთ string ტიპის მონაცემი ისინი უბრალოდ ერთმანეთს მიეწებებიან


# 13. რას გამოიტანს კოდი როდესაც მომხმარებელი შეიტანს 7-ს?


#   num1 = float(input("enter number : "))

#   print(type(num1))



# კოდი გამოიტანს <class 'float'>-ს რადგან როგორც ხედავთ input ფუნქციის წინ წერია float ფუნქცია რომელიც ნებისმიერ რიცხვს ხდის ათწილადს 
# ამიტომაც ნებისმიერი მომხარებლის მიერ შემოტანილი რიცხვი გადაიქცევა ათწილადად შედეგად კი კოდი გამოიტანს <class 'float'>-ს


#  14.პასუხია:


#  x = ((True and False) or (False or False))

#  y = ((False or True)  and (False and True))

#   print((x and y) or True)


#   პასუხი იქნება True რადგან როდესაც მოცემული გვაქვს True ერთ-ერთ მნიშვნელობად და ასევე იქ არის or-იც მაშინ პასუხი სულ True გამოვა
#   ასევე თუ დააკვირდებით ზევითა კოდი სულაც არ გვჭირდება რადგან ვიცით რომ x ან  y შეიძლება ნებისმერი იყოს True-ც  და False-იც
#   მაგრამ ჩვენ შემდეგ მოცემული გვაქვს "or True" მხოლოდ ამ კოდითაც შეგვიძლია რომ დავინახოთ პასუხი, რომელიცაა True

# 15. რას გამოიყვანს კოდი როდესაც მომხმარებელი შეიყვანს 20-ს?

# age = int(input("enter your age:"))

# print(age > 18)


# პასუხია True რადგან ჩვენ ვიცით რომ 20 მეტია 18-ზე ხოლო თუ age ცვლადის მნიშვნელობა იქნება 20 მაშინ დაიპრინტება იგივე 20 > 18 
# შეიძლება ასეც ვთქვათ ამიტომაც პასუხია True