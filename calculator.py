# برنامج العمليات الحسابية الأساسية في بايثون

# إدخال الأرقام من المستخدم
num1 = float(input("أدخل الرقم الأول: "))
num2 = float(input("أدخل الرقم الثاني: "))

# 1. الجمع
addition = num1 + num2
print(f"الجمع: {num1} + {num2} = {addition}")

# 2. الطرح
subtraction = num1 - num2
print(f"الطرح: {num1} - {num2} = {subtraction}")

# 3. الضرب
multiplication = num1 * num2
print(f"الضرب: {num1} * {num2} = {multiplication}")

# 4. القسمة
if num2 != 0:
    division = num1 / num2
    print(f"القسمة: {num1} / {num2} = {division}")
else:
    print("القسمة: لا يمكن القسمة على الصفر!")

# 5. القسمة الصحيحة (بدون باقي)
if num2 != 0:
    floor_division = num1 // num2
    print(f"القسمة الصحيحة: {num1} // {num2} = {floor_division}")

# 6. باقي القسمة (Modulus)
if num2 != 0:
    modulus = num1 % num2
    print(f"باقي القسمة: {num1} % {num2} = {modulus}")

# 7. الأسس (Power)
exponentiation = num1 ** num2
print(f"الأسس: {num1} ** {num2} = {exponentiation}")