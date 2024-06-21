import document


doc = document ("/pardaz/Desktop/SFI/En man som heter Ove av Fredrik Backman.docx")

numbersdone = 0

for para in doc.paragraphs:
  print(para.text)
  newtext = ""
  for char in para.text:
    if char in "1234567890":
      if numbersdone == 0:
        newtext += char
        numbersdone += 1

      else:
        newtext = newtext[:-1*numbersdone] + char + newtext[-1*numbersdone:]
        numbersdone +=1
    else:
      newtext += char
      numbersdone =0
    print (newtext)