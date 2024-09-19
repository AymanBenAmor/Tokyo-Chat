import tkinter
import threading
import pyttsx3
import speech_recognition

import pygame
import csv
from googletrans import Translator

from tkinter import *

from PIL import ImageTk, Image


################## set up speaker  ####################
translator = Translator()
recognizer = speech_recognition.Recognizer()

def rechercher_mot(chaine, mot):
    mots_chaine = chaine.split()  # Divise la chaîne en une liste de mots
    if mot in mots_chaine:
        return True
    else:
        return False

def list_ref():
    # Ouverture du fichier CSV en mode lecture
    with open('data.csv', 'r') as data:
        lecteur_csv = csv.reader(data)

        my_dict = {}

        # Parcours des lignes du fichier CSV
        for ligne in lecteur_csv:

            cle = str(ligne[0])
            valeur = str(ligne[1])
            my_dict[cle] = valeur

    return my_dict

def sound_play(mp3_file):
    pygame.mixer.music.load(mp3_file)

    # Play the MP3 sound
    pygame.mixer.music.play()

    # Wait for the sound to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # Clean up resources
    pygame.mixer.music.stop()

droid = pyttsx3.init()
#droid.say("bonjour je suis tokyo et je suis à votre disposition aujourdhuit pour vous ecoutez et répondre à vos questions")
#droid.runAndWait()

pygame.init()


stop = False

opening_sound = "sounds/welcome.mp3"



data = list_ref()
#print("data :", data)

############ set the dashboard#############

############ thread "#########
def start_recognition():
    recognition_thread = threading.Thread(target=speak)
    recognition_thread.daemon = True
    recognition_thread.start()

def test_recognition():
    recognition_thread = threading.Thread(target=test)
    recognition_thread.daemon = True
    recognition_thread.start()

def ajouter():
    nom = entr_nom_article.get()
    if (nom != ""):
        line = [nom, "Articles/" + nom + ".mp3", "  "]

        with open('data.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(line)

        entr_nom_article.delete(0, 'end')
        #print(line)




def supprimer():
    nom_supp = entr_nom_article_suppr.get()

    if (nom_supp != ""):
        with open('data.csv', 'r') as file:
            reader = csv.reader(file)
            lines = list(reader)

        updated_lines = []
        for line in lines:
            if nom_supp != line[0]:  # Exclude the line with the matching value
                updated_lines.append(line)

        with open('data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(updated_lines)
        #print("l'article", nom_supp, "est supprimé")
        entr_nom_article_suppr.delete(0, 'end')



def test():

    translator = Translator()
    recognizer = speech_recognition.Recognizer()
    try:
        with speech_recognition.Microphone() as mic:

            recognizer.adjust_for_ambient_noise(mic, duration=0.2)

            audio = recognizer.listen(mic,phrase_time_limit=5)

            text = recognizer.recognize_google(audio,language="ar-AR")

            text = text.lower()

            translated_text = translator.translate(text, dest='fr')
            frensh_text = translated_text.text.lower()

            lbltest.config(text=frensh_text, background=fen.cget("background"))
    except speech_recognition.UnknownValueError:

        recognizer = speech_recognition.Recognizer()
def clean():
    lbltest.config(text="")

def afficher():
    #show_article_area.insert("Les articles existants sont : \n")
    show_article_area.delete("1.0","end")
    data = list_ref()
    for key in data:
        show_article_area.insert(tkinter.END,key+"\n")

def clear_article():
    show_article_area.delete("1.0", "end")

def stop_discussion():
    text_area.delete("1.0","end")
    global stop
    stop = True

def speak():


    translator = Translator()
    recognizer = speech_recognition.Recognizer()

    sound_play(opening_sound)
    old_son = opening_sound
    while not stop:

        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)

                audio = recognizer.listen(mic, phrase_time_limit=8)

                text = recognizer.recognize_google(audio, language="ar-AR")

                text = text.lower()

                #print("Ayman say : ")
                text_area.insert(tkinter.END, "*Client: ")
                #print(text)
                text_area.insert(tkinter.END, text + "\n")
                translated_text = translator.translate(text, dest='fr')
                frensh_text = translated_text.text.lower()
                #print(f"*traduction: {frensh_text}")
                text_area.insert(tkinter.END, f"*Traduction : {frensh_text}" + "\n\n")

                exist = False

                ####### repeter #######
                if (rechercher_mot(text, "عود") or rechercher_mot(text, "عاود") or rechercher_mot(text,
                                                                                                  "سمعتش") or rechercher_mot(
                    text, "سمعتكش")):
                    sound_play(old_son)
                    exist = True

                ##### ahla ####
                elif (rechercher_mot(text, "السلامه") or rechercher_mot(text, "اهلا") or rechercher_mot(text,
                                                                                                        "احلى") or rechercher_mot(
                    text, "مرحبا")):
                    hello = "sounds/hello.mp3"
                    sound_play(hello)
                    old_son = hello
                    exist = True
                #### chesmek ####
                elif (rechercher_mot(text, "اسمك")):
                    name = "sounds/i am tokyo.mp3"
                    sound_play(name)
                    old_son = name
                    exist = True

                ###### nice to meet you
                elif (rechercher_mot(text, "اسمي")):
                    nice_name ="sounds/nice_name.mp3"
                    sound_play(nice_name)
                    old_son = nice_name
                    exist = True

                ###### goood bye ########
                elif (rechercher_mot(text, "بسلامه") or (rechercher_mot(text, "خير") and rechercher_mot(text, "على"))):
                    good_bye = "sounds/good_bye.mp3"
                    sound_play(good_bye)
                    old_son = good_bye
                    exist = True

                ####### ch7alek #########
                elif (rechercher_mot(text, "حالك") or rechercher_mot(text, "احوالك") or rechercher_mot(text,"باس") or rechercher_mot(text, "شحالك")):
                    fine = "sounds/fine.mp3"
                    sound_play(fine)
                    old_son = fine
                    exist = True

                #############" merci ############
                elif (rechercher_mot(text, "عيشك") or rechercher_mot(text, "عايشك") or rechercher_mot(text,
                                                                                                      "ميرسي") or (
                              rechercher_mot(text, "بارك") and rechercher_mot(text, "الله") and rechercher_mot(text,
                                                                                                               "فيك"))):
                    de_rien = "sounds/de rien.mp3"
                    sound_play(de_rien)
                    old_son = de_rien
                    exist = True


                ##### parcourir les articles ###
                data = list_ref()
                for key in data:

                    if key in frensh_text:
                        sound_play(data[key])

                        old_son = data[key]

                        exist = True
                        """son = pygame.mixer.Sound(data[key])
                        son.play()
                        pygame.time.wait(int(son.get_length() * 1000))
                        old_son=son"""

                if (exist == False):
                    sound_play("sounds/pas compris.mp3")
                    old_son = "sounds/pas compris.mp3"





        except speech_recognition.UnknownValueError:

            recognizer = speech_recognition.Recognizer()
            continue


################## set window #######################

fen = Tk()
fen.title("TOKYO STORE")

fen.config(background="#cea604")

fen.geometry('800x500')
background_image = PhotoImage(file='images/background.png')

icon_image = Image.open("images/icon.jpg")
tk_icon_image = ImageTk.PhotoImage(icon_image)
fen.iconphoto(True, tk_icon_image)

# Create a Label widget to display the image
background_label = Label(fen, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)




################## ajouter article ##################
lblnombre1 = Label(fen, text = "Nouveau article")
lblnombre1.place(x=30 , y=50)
entr_nom_article = Entry(fen)
entr_nom_article.place(x=150 , y=50)


set_data = Button(fen , text = "Ajouter l'article" , command=ajouter)
set_data.place(x=300 , y=50)

################## supprimer ##############
lblsuppr = Label(fen, text = "Article à supprimer")
lblsuppr.place(x=30 , y=110)
entr_nom_article_suppr = Entry(fen)
entr_nom_article_suppr.place(x=150 , y=110)

del_data = Button(fen , text = "Supprimer l'article" , command=supprimer)
del_data.place(x=300 , y=110)


############# connaitre le nom de l'article ###############
lbltest = Label(fen, text = "",background=fen.cget("background"))
lbltest.place(x=220 , y=170)

test_button = Button(fen , text = "connaitre le nom de l'article" , command=test_recognition)
test_button.place(x=30 , y=170)

# clear
test_button = Button(fen , text = "Supprimer" , command=clean)
test_button.place(x=380 , y=170)

######### afficher les articles ##########

show_article_button = Button(fen, text="afficher tout les articles ",command=afficher)
show_article_button.place(x=30 , y=240)

clear_article_button = Button(fen, text="Vider le champs",command=clear_article)
clear_article_button.place(x=30 , y=270)

show_article_area = Text(fen, width=20,height=13)
show_article_area.place(x=200 , y=240)


########## discussion ############
start_discussion_button = Button(fen, text="Commencer la discussion !",command=start_recognition)
start_discussion_button.place(x=500 , y=50)
text_area = Text(fen, width=35,height=23)
text_area.place(x=480, y=100)

stop_discussion_button = Button(fen,text="STOP !",command=stop_discussion)
stop_discussion_button.place(x=700 , y=50)



fen.mainloop()

"""   make the code executable without console and with icon
pyinstaller dashboard.py --onefile --noconsole --icon=TOKYO_ICON.ico   """
