""" здесь последовательно будет описан код работы со строками начиная с простого примера 
подсчета в тексте букв слов и предложений """
text=input('введите текст:')
words=text.split()# перем подсчета слов
sentences=text.split('.')# перем подсчета предл
# первая фу подсчета букв
def count_letter ():
    print(f'   текст из :{len(text)} символов')
# вторая  фу подсчета слов
def count_words(count):
    print(f'   текст из :{len(count)} слов') 
# третья фу подсчета предл
def count_sentences(count):
     print(f'   текст из:{len(count)-1} предложений ')

print('  ',words)#показывает питон список
if len(words)==1:
   print('вы ввели одно слово')
   count_letter()
elif len(sentences) >1:
   count_sentences(sentences)
   count_words(words)
   count_letter()

else:
   count_words(words)
   count_letter()                                                                                                                                                                                    