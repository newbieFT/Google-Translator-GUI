from googletrans import Translator

t = Translator()

word = t.translate("Em dep qua", src='vi', dest='en')
b = word.text
print(b)