#!/usr/bin/env python
# coding: utf-8

# # Welcome to Jupyter!

# In[1]:


import random
kelimeler=["mühendis","avukat","mimar","polis","hemşire","grafiker",
           "doktor","öğretmen","memur","sekreter","taksici","dişçi","garson",
           "itfaiyeci","şoför","kasiyer","yazılımcı","tesisatçı"]
kelime=random.choice(kelimeler)
harfler=[]
tahminSayacı=11
kelimeUzunluğu=len(kelime)
kelimeUzunluğuGöstergesi=list('_' * kelimeUzunluğu)
print("OYUNUMUZA HOŞGELDİNİZ..KONUMUZ MESLEKLER ! BAKALIM SİZİN İÇİN SEÇTİĞİMİZ",
      "MESLEĞİ TAHMİN EDEBİLECEK MİSİNİZ ? TAHMİN HAKKINIZ 11...BAŞARILARRRR...")
print(' '.join(kelimeUzunluğuGöstergesi), end='\n')

while tahminSayacı>0 :
  girilenHarf=input("Harf Giriniz: ",)
  if girilenHarf in harfler :
    print("Zaten girilmiş harf")
    continue
  elif len(girilenHarf)>1 :
    print("En fazla bir harf girilebilir.")
    continue
  elif girilenHarf not in kelime :
    tahminSayacı -=1
    print("Üzgünüm, yanlış tahmin ... Kalan tahmin hakkınız {}".format(tahminSayacı))
  else :
    for i in range(len(kelime)) :
      if girilenHarf == kelime[i] :
        print("Tebrikler ! Doğru tahmin..")
        kelimeUzunluğuGöstergesi[i]=girilenHarf
        harfler.append(girilenHarf)

    print(' '.join(kelimeUzunluğuGöstergesi), end='\n')

  print("Kelimenin tamamını tahmin etmek ister misiniz ? (evet/hayır)")
  cevap=input("Cevap: ",)
  if cevap == "evet" :
    print("Tahmin ettiğiniz kelimeyi giriniz..")
    tahmin=input("Tahmin edilen kelime: ",)
    if tahmin==kelime :
      print("TEBRİKLER KELİMEYİ DOĞRU TAHMİN ETTİNİZ !!")
      break
    else :
      tahminSayacı -=1
      print("ÜZGÜNÜM YANLIŞ TAHMİN.. Kalan tahmin hakkınız {}".format(tahminSayacı))
  while (cevap !="evet" and cevap!="hayır") :
    print("UYARI ! *evet* veya *hayır* girmelisiniz..")
    print("Kelimenin tamamını tahmin etmek ister misiniz ? (evet/hayır)")
    cevap=input("Cevap: ",)
    if cevap == "evet" :
      print("Tahmin ettiğiniz kelimeyi giriniz..")
      tahmin=input("Tahmin edilen kelime: ",)
      if tahmin==kelime :
        print("TEBRİKLER KELİMEYİ DOĞRU TAHMİN ETTİNİZ !!")
        break
      else :
        tahminSayacı -=1
        if tahminSayacı==0 :
          continue
        print("ÜZGÜNÜM YANLIŞ TAHMİN.. Kalan tahmin hakkınız {}".format(tahminSayacı))     
  if tahminSayacı==0 :
    print("ÜZGÜNÜM TAHMİN HAKKIN KALMADI..OYUNU KAYBETTİNİZ..DOĞRU CEVAP: {}".format(kelime))
    break 


# This repo contains an introduction to [Jupyter](https://jupyter.org) and [IPython](https://ipython.org).
# 
# Outline of some basics:
# 
# * [Notebook Basics](../examples/Notebook/Notebook%20Basics.ipynb)
# * [IPython - beyond plain python](../examples/IPython%20Kernel/Beyond%20Plain%20Python.ipynb)
# * [Markdown Cells](../examples/Notebook/Working%20With%20Markdown%20Cells.ipynb)
# * [Rich Display System](../examples/IPython%20Kernel/Rich%20Output.ipynb)
# * [Custom Display logic](../examples/IPython%20Kernel/Custom%20Display%20Logic.ipynb)
# * [Running a Secure Public Notebook Server](../examples/Notebook/Running%20the%20Notebook%20Server.ipynb#Securing-the-notebook-server)
# * [How Jupyter works](../examples/Notebook/Multiple%20Languages%2C%20Frontends.ipynb) to run code in different languages.

# You can also get this tutorial and run it on your laptop:
# 
#     git clone https://github.com/ipython/ipython-in-depth
# 
# Install IPython and Jupyter:
# 
# with [conda](https://www.anaconda.com/download):
# 
#     conda install ipython jupyter
# 
# with pip:
# 
#     # first, always upgrade pip!
#     pip install --upgrade pip
#     pip install --upgrade ipython jupyter
# 
# Start the notebook in the tutorial directory:
# 
#     cd ipython-in-depth
#     jupyter notebook
