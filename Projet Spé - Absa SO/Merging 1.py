# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 15:55:52 2019

@author: Absa
"""

import tkinter as tk
from PIL import Image, ImageTk
import mysql.connector as db
import datetime as dt

con = db.connect(host="localhost",user="root",password="", database="icaredb")
cursor = con.cursor()


class Accueil (tk.Frame):
    
    def __init__(self,fenetre):
        tk.Frame.__init__(self)
        self.initialiser()
        
    def initialiser(self):
        self.pack(fill=tk.BOTH, expand=1)
        
        def logIn ():
            
          if uservar.get()== "user1" and passwrdvar.get()=="mymdp": 
            self.destroy()
            mainConnect()
                
          else:
              bad_id = tk.Label(self, text ="Veuillez saisir les bon identifiants" )
              bad_id.place(x=280,y=230)
        
        
        logo = Image.open("icarelogo1.png")
        logo1= ImageTk.PhotoImage(logo)
        img = tk.Label(self, image=logo1)
        img.image = logo1
        img.place(x=150)       
        
        
        intro = tk.Label(self, text ="Veuillez vous identifier afin d'accéder à vos données.\n" )
        intro.place(x=280,y=200)
        
        uservar = tk.StringVar() 
        username = tk.Label(self, text ="Nom d'utilisateur" )
        username.place(x=240,y=275)
        entree1 = tk.Entry(self, textvariable=uservar, width=30)
        entree1.place(x=375,y=275)      
       
        passwrdvar = tk.StringVar() 
        password = tk.Label(self, text ="Mot de Passe       ")
        password.place(x=240,y=325)
        entree2 = tk.Entry(self, textvariable=passwrdvar, width=30,show='*')
        entree2.place(x=375,y=325)
       
        se_connecter = tk.Button (self, text="Se connecter", width=20, command=logIn)
        se_connecter.place(x=375,y=400)
        
              
        self.mainloop()
            
       
class Connected (tk.Frame):
    
    def __init__(self):
        
        tk.Frame.__init__(self)
        
        
    def initialiser(self):
        
        self.pack(fill=tk.BOTH,expand=1)
        
        bg = Image.open("bg.png")
        bg1= ImageTk.PhotoImage(bg)
        img = tk.Label(self, image=bg1)
        img.image = bg1
        img.pack()  
                
        logo = Image.open("icar.png")
        logo1= ImageTk.PhotoImage(logo)
        img = tk.Label(self, image=logo1)
        img.config(bg="white")
        img.image = logo1
        img.place(x=20)   
#        self.pack(fill=tk.BOTH)
#        (tk.Label(self, text ="Vous êtes maintenant connecté." )).place(x=355, y=120)
        
        logo_photo = Image.open("logo_photo2.png") #img 100x100 px
        logo_photo1= ImageTk.PhotoImage(logo_photo)
        img = tk.Label(self, image=logo_photo1)
        img.image = logo_photo1
        img.place(x=750, y = 100)   
        change_photo = tk.Button (self, text="Changer la photo", width=15, height=1)#, command=#)
        change_photo.place(x=745,y=210)
        
        cursor.execute("""SELECT * FROM utilisateur""")
        user1 = cursor.fetchall()
        print(user1)
        
        
        welcome = tk.Label(self, text ="Hello {} !".format(user1[0][1]) )
        welcome.config(height=2, width= 25)
        welcome.config(font=('Helvetica',17,'bold'))
        welcome.config(foreground="gray54", bg="white")
        welcome.place(x=90, y = 120)
        
        
        poids = tk.Label(self, text ="Vous pesez {} kilos.".format(user1[0][3]) )
        poids.config(font=('Helvetica',9,''))
        poids.config(foreground="sea green", bg="white")
        poids.place(x=70, y = 200)
        
        
        taille = tk.Label(self, text ="Vous mesurez : {} centimètres.".format(user1[0][4]) )
        taille.config(font=('Helvetica',9,''))
        taille.config(foreground="sea green", bg="white")
        taille.place(x=70, y = 225)
        
        allergies = tk.Label(self, text ="Des allergies à signaler ? {} ".format(user1[0][5]) )
        allergies.config(font=('Helvetica',9,''))
        allergies.config(foreground="sea green", bg="white")
        allergies.place(x=70, y = 250)
        
        def Info_In ():
            self.destroy()
            mainSaisieInfo()
        
        modif_donnees = tk.Button (self, text="Modifier mes informations", width=25, height=1, command=Info_In)
        modif_donnees.place(x=70,y=400)
        
        def Info ():
            self.destroy()
            mainInfos()
        
#        info_perso = tk.Button (self, text="Mes informations personnelles", width=30, height=3, command=Info)
#        info_perso.pack()
#        info_perso.place(x=150,y=200)
        
        def Tension():
            self.destroy()
            mainTension ()
        
        tension = tk.Button (self, text="Tension", width=30, height=2, command=Tension)
        tension.place(x=500,y=200)
        
#        def RDV():
#            self.destroy()
#            mainRDV ()
#            
#        rdv = tk.Button (self, text="Mes rendez-vous", width=25, height=2, command=RDV)
#        rdv.place(x=500,y=250)
        def rdv_In ():
            self.destroy()
            mainSaisieRDV()
                    
        
        rdv_in = tk.Button (self, text="Je souhaite prendre un rendez-vous", width=30, height=2, command=rdv_In)
        rdv_in.place(x=500,y=250)
        
#        medoc = tk.Button (self, text="Mes médicaments", width=25, height=2, command=self.Medoc)
#        medoc.place(x=500,y=200)
#        
#        analyses = tk.Button (self, text="Mes analyses", width=25, height=2, command=self.Analyses)
#        analyses.place(x=500,y=250)
        
        logout = tk.Button (self, text="Déconnexion", width=20, height=1, command=self.Deconnect)
        logout.place(x=750,y=20)
        
       

        
        
#    def RDV(self):
#        
#        self.destroy()
#        
#        myrdv = tk.Frame()
#        myrdv.pack(fill=tk.BOTH,expand=1)
#        logo = Image.open("icar.png")
#        logo1= ImageTk.PhotoImage(logo)
#        img = tk.Label(myrdv, image=logo1)
#        img.image = logo1
#        img.place(x=20)
#        return_accueil = tk.Button (myrdv, text="Accueil", width=15, height=1, command=mainConnect)
#        return_accueil.place(x=250,y=28)
#        
#    def Analyses(self):
#        
#        self.destroy()
#        
#        myanalyse = tk.Frame()
#        myanalyse.pack(fill=tk.BOTH,expand=1)
#        logo = Image.open("icar.png")
#        logo1= ImageTk.PhotoImage(logo)
#        img = tk.Label(myanalyse, image=logo1)
#        img.image = logo1
#        img.place(x=20)
#        return_accueil = tk.Button (myanalyse, text="Accueil", width=15, height=1, command=mainConnect)
#        return_accueil.place(x=250,y=28)
#        
#    def Medoc(self):
#    
#        self.destroy()
#        
#        medoc = tk.Frame()
#        medoc.pack(fill=tk.BOTH,expand=1)
#        logo = Image.open("icar.png")
#        logo1= ImageTk.PhotoImage(logo)
#        img = tk.Label(medoc, image=logo1)
#        img.image = logo1
#        img.place(x=20)
#        return_accueil = tk.Button (medoc, text="Accueil", width=15, height=1, command=mainConnect)
#        return_accueil.place(x=250,y=28)
#        
    def Deconnect(self):
        
        self.destroy()
        main ()
        
    def Retour(self,frame):
        frame.destroy()                
        mainConnect()
              
class MyInfos (tk.Frame):
    
    def __init__(self,fenetre):
        tk.Frame.__init__(self)
        
        
    def initialiser(self):
        
        self.pack(fill=tk.BOTH,expand=1)            
        
        def Info_In ():
            self.destroy()
            mainSaisieInfo()
            
        logo = Image.open("icar.png")
        logo1= ImageTk.PhotoImage(logo)
        img = tk.Label(self, image=logo1)
        img.image = logo1
        img.place(x=20)   
        
#        def change_photo ():
#            filepath = askopenfilename(title="maphoto",filetypes=[('png files','.png'),('all files','.*')])
#            photo = PhotoImage(file=filepath)
        
        logo_photo = Image.open("logo_photo2.png") #img 100x100 px
        logo_photo1= ImageTk.PhotoImage(logo_photo)
        img = tk.Label(self, image=logo_photo1)
        img.image = logo_photo1
        img.place(x=750, y = 100)   
        change_photo = tk.Button (self, text="Changer la photo", width=15, height=1)#, command=#)
        change_photo.place(x=745,y=210)
        
        def accueil ():
            self.destroy()
            mainConnect()
            
        return_accueil = tk.Button (self, text="Accueil", width=15, height=1, command=accueil)
        return_accueil.place(x=250,y=28)
        
        saisie_donnees = tk.Button (self, text="Saisir des informations", width=25, height=1, command=Info_In)
        saisie_donnees.place(x=150,y=100)
        
        modif_donnees = tk.Button (self, text="Modifier mes informations", width=25, height=1, command=Info_In)
        modif_donnees.place(x=430,y=100)
        
        cursor.execute("""SELECT * FROM utilisateur""")
        user1 = cursor.fetchall()
        print(user1)
        
        
        welcome = tk.Label(self, text ="Hello {} !\n Voici un petit récap de vos informations.".format(user1[0][2]) )
        welcome.place(x=150, y = 200)
        nom_complet = tk.Label(self, text ="Nom Complet : {} {}".format(user1[0][2], user1[0][1]) )
        nom_complet.place(x=150, y = 250)
        date_naiss = tk.Label(self, text ="Date de naissance : {}".format(user1[0][3]) )
        date_naiss.place(x=150, y = 275)
        email = tk.Label(self, text ="Votre adresse mail : {} ".format(user1[0][5]) )
        email.place(x=150, y = 300)
        num = tk.Label(self, text ="Votre numéro de téléphone : {}".format(user1[0][6]) )
        num.place(x=150, y = 325)
        welcome = tk.Label(self, text ="Côté santé, voici les données disponibles: " )
        welcome.place(x=150, y = 350)
        poids = tk.Label(self, text ="Vous pesez {} kilos.".format(user1[0][7]) )
        poids.place(x=150, y = 375)
        taille = tk.Label(self, text ="Vous mesurez : {} centimètres.".format(user1[0][8]) )
        taille.place(x=150, y = 400)
        allergies = tk.Label(self, text ="Des allergies à signaler ? {} ".format(user1[0][9]) )
        allergies.place(x=150, y = 425)
        
        
        self.mainloop()
        
class Saisie_Infos (tk.Frame):
    
    def __init__(self,fenetre):
        tk.Frame.__init__(self)
        
        
    def initialiser(self):
        
        self.pack(fill=tk.BOTH,expand=1)
        
        def modifier ():
            
            
            
            prenom_var=prenom.get()
            
            choix_genre_var=choix_genre.get()
            poids_var=poids.get()
            longueur_var=longueur.get()
            allergie_var=allergie.get()
            
#            x=(nom_var,prenom_var,date_naiss_var,choix_genre_var,mail_var,numero_var,poids_var,longueur_var,allergie_var)
#            print(x)
            cursor.execute("""UPDATE utilisateur SET prenom = %s WHERE idutilisateur = 63""", (prenom_var,))
            cursor.execute("""UPDATE utilisateur SET poids = %s WHERE idutilisateur = 63""", (poids_var,))
            cursor.execute("""UPDATE utilisateur SET taille = %s WHERE idutilisateur = 63""", (longueur_var,))
            cursor.execute("""UPDATE utilisateur SET allergie = %s WHERE idutilisateur = 63""", (allergie_var,))
            cursor.execute("""UPDATE utilisateur SET genre = %s WHERE idutilisateur = 63""", (choix_genre_var,))
            
            con.commit ()
            self.destroy()
            mainConnect()
        
            
       
            
#        def valider ():
#            nom_var=nom.get()
#            prenom_var=prenom.get()
#            date_naiss_var=date_naiss.get()
#            choix_genre_var=choix_genre.get()
#            mail_var=mail.get()
#            numero_var=numero.get()
#            poids_var=poids.get()
#            longueur_var=longueur.get()
#            allergie_var=allergie.get()
#            
#            x=(nom_var,prenom_var,date_naiss_var,choix_genre_var,mail_var,numero_var,poids_var,longueur_var,allergie_var)
#            print(x)
#            cursor.execute("""INSERT INTO utilisateur VALUES (NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",x)
#            con.commit ()
#            mainConnect()
            

        
        logo = Image.open("icar.png")
        logo1= ImageTk.PhotoImage(logo)
        img = tk.Label(self, image=logo1)
        img.image = logo1
        img.grid(row=1)   
        def accueil ():
            self.destroy()
            mainConnect()
            
        return_accueil = tk.Button (self, text="Accueil", width=15, height=1, command=accueil)
        return_accueil.grid(row=1, column=1)
            
        
#        nom = tk.StringVar() 
#        surname = tk.Label(self, text ="Nom: " )
#        surname.grid(row=2, sticky=tk.W)
#        surname_in = tk.Entry(self, textvariable=nom, width=40)
#        surname_in.grid(row=2, column=1)
        
        prenom = tk.StringVar() 
        name = tk.Label(self, text ="Prénom: " )
        name.grid(row=3, sticky=tk.W)
        name_in = tk.Entry(self, textvariable=prenom, width=40)
        name_in.grid(row=3, column=1)
        
#        date_naiss = tk.StringVar()
#        birthday = tk.Label(self, text ="Date de Naissance (AAAA-MM-JJ): " )
#        birthday.grid(row=4, sticky=tk.W)
#        birth_in = tk.Entry(self,textvariable=date_naiss,width=40)
#        birth_in.grid(row=4, column=1)
         
        
        genre = tk.Label(self, text ="Genre: " )
        genre.grid(row=5, sticky=tk.W)
        choix_genre = tk.StringVar() 
        M = tk.Radiobutton(self, text="Homme", variable=choix_genre, value="Homme")
        F = tk.Radiobutton(self, text="Femme", variable=choix_genre, value="Femme")
        M.select()
        M.grid(row=5, column=1)
        F.grid(row=5, column=2)
#        
#        mail = tk.StringVar()
#        email = tk.Label(self, text ="Adresse mail: " )
#        email.grid(row=6, sticky=tk.W)
#        email_in = tk.Entry(self, textvariable=mail, width=40)
#        email_in.grid(row=6, column=1)
#        
#        numero = tk.StringVar()
#        telephone = tk.Label(self, text ="Téléphone: " )
#        telephone.grid(row=7, sticky=tk.W)
#        telephone_in = tk.Entry(self, textvariable=numero, width=40)
#        telephone_in.grid(row=7, column=1)
#        
        poids = tk.DoubleVar()
        weight = tk.Label(self, text ="Poids (kg): " )
        weight.grid(row=8, sticky=tk.W)
        weight_in = tk.Entry(self, textvariable=poids ,width=40)
        weight_in.grid(row=8, column=1)
        
        longueur = tk.IntVar()
        taille = tk.Label(self, text ="Taille (cm): " )
        taille.grid(row=9, sticky=tk.W)
        taille_in = tk.Entry(self, textvariable=longueur, width=40)
        taille_in.grid(row=9, column=1)
        
        allergie = tk.StringVar()
        mesallergies = tk.Label(self, text ="Allergies(si vous en avez): " )
        mesallergies.grid(row=10, sticky=tk.W)
        mesallergies_in = tk.Entry(self, textvariable=allergie, width=40)
        mesallergies_in.grid(row=10, column=1)

           
        Enregistrer = tk.Button (self, text="Enregistrer", width=15, height=1, command=modifier)
        Enregistrer.grid(row=11,column=3)
        
class Tension (tk.Frame):
    
    def __init__(self,fenetre):
        tk.Frame.__init__(self)
        
        
    def initialiser(self):
        
        self.pack(fill=tk.BOTH,expand=1)
        
        bg = Image.open("bgTension.png")
        bg1= ImageTk.PhotoImage(bg)
        img = tk.Label(self, image=bg1)
        img.image = bg1
        img.pack()  
         
        logo = Image.open("icar.png")
        logo1= ImageTk.PhotoImage(logo)
        img = tk.Label(self, image=logo1)
        img.config(bg="white")
        img.image = logo1
        img.place(x=20)
        
        def accueil ():
            self.destroy()
            mainConnect()
            
        return_accueil = tk.Button (self, text="Accueil", width=15, height=1, command=accueil)
        return_accueil.place(x=250,y=28)
     
        
            # mettre une image type le saviez vous concernant la tensuon
        
        e1 = tk.StringVar()
        e1.set("Date")
        entree1 = tk.Entry(self, textvariable=e1, width=20, state='readonly', justify='center')
        entree1.place(x= 304, y=100)
        
        e2 = tk.StringVar()
        e2.set("Horaire de prise")
        entree2 = tk.Entry(self, textvariable=e2, width=20, state='readonly', justify='center')
        entree2.place(x= 430, y=100)
        
        e3 = tk.StringVar()
        e3.set("Diastole")
        entree3 = tk.Entry(self, textvariable=e3, width=20, state='readonly', justify='center')
        entree3.place(x= 556, y=100)
        
        e4 = tk.StringVar()
        e4.set("Systole")
        entree4 = tk.Entry(self, textvariable=e4, width=20, state='readonly', justify='center')
        entree4.place(x= 682, y=100)
        
        cursor.execute("""SELECT * FROM tension""")
        tension = cursor.fetchall()
       
        
        for i in range (len(tension)):
            e1 = tk.StringVar()
            e1.set(tension[i][1])
            entree1 = tk.Entry(self, textvariable=e1, width=20, state='readonly', justify='center')
            entree1.place(x= 304, y=((i+1)*20)+100)
            
            e2 = tk.StringVar()
            e2.set(tension[i][2])
            entree2 = tk.Entry(self, textvariable=e2, width=20, state='readonly', justify='center')
            entree2.place(x= 430, y=((i+1)*20)+100)
            
            e3 = tk.StringVar()
            e3.set(tension[i][3])
            entree3 = tk.Entry(self, textvariable=e3, width=20, state='readonly', justify='center')
            entree3.place(x= 556, y=((i+1)*20)+100)
            
            e4 = tk.StringVar()
            e4.set(tension[i][4])
            entree4 = tk.Entry(self, textvariable=e4, width=20, state='readonly', justify='center')
            entree4.place(x= 682, y=((i+1)*20)+100)
                
            
                
            def Tension_In ():
                self.destroy()
                mainSaisieTension()
        
                    
        
        tension_in = tk.Button (self, text="J'ai pris ma tension", width=15, height=1, command=Tension_In)
        tension_in.place(x= 120, y=100)
  
        
        
        self.mainloop()
        
class Saisie_Tension (tk.Frame):
    
    def __init__(self,fenetre):
        tk.Frame.__init__(self)
        
        
    def initialiser(self):
        
        self.pack(fill=tk.BOTH,expand=1)
        
       
            
        def valider ():
            dia = diastole.get()
            sys = systole.get()
            day= d_h[0]
            hour=d_h[1]
            x=(day,hour,dia,sys)
            print(x)
            cursor.execute("""INSERT INTO tension VALUES (NULL,%s,%s,%s,%s)""",x)
            con.commit ()
            
            self.destroy()
            
            mainTension ()
            
        def accueil ():
            self.destroy()
            mainConnect()
            
        return_accueil = tk.Button (self, text="Accueil", width=15, height=1, command=accueil)
        return_accueil.grid(row=1, column=1)
            
        
        logo = Image.open("icar.png")
        logo1= ImageTk.PhotoImage(logo)
        img = tk.Label(self, image=logo1)
        img.image = logo1
        img.grid(row=1)   
          
        
        date_heure = str( dt.datetime.now())
        d_h = date_heure.split()
        date="Date d'aujourd'hui: "+d_h[0]
        heure ="Heure: "+ d_h[1]
        (tk.Label(self, text =date )).grid(row=2, column=1)
        (tk.Label(self, text =heure)).grid(row=3, column=1)
        
        
        diastole = tk.DoubleVar()
        diast = tk.Label(self, text ="Saisir la diastole: " )
        diast.grid(row=4, sticky=tk.W)
        diast_in = tk.Entry(self,textvariable=diastole,width=40)
        diast_in.grid(row=4, column=1)
         
        
        systole = tk.DoubleVar()
        syst = tk.Label(self, text ="Saisir la systole: " )
        syst.grid(row=5, sticky=tk.W)
        syst_in = tk.Entry(self,textvariable=systole,width=40)
        syst_in.grid(row=5, column=1)
                
        Enregistrer = tk.Button (self, text="Enregistrer", width=15, height=1, command=valider)
        Enregistrer.grid(row=11,column=1)
        
class RDV (tk.Frame):
    
    def __init__(self,fenetre):
        tk.Frame.__init__(self)
        
        
    def initialiser(self):
        
        self.pack(fill=tk.BOTH,expand=1)
        
         
        logo = Image.open("icar.png")
        logo1= ImageTk.PhotoImage(logo)
        img = tk.Label(self, image=logo1)
        img.image = logo1
        img.grid(row=1)  
        
        def accueil ():
            self.destroy()
            mainConnect()
            
        return_accueil = tk.Button (self, text="Accueil", width=15, height=1, command=accueil)
        return_accueil.grid(row=1, column=1)
        
#        def accueil ():
#            self.destroy()
#            mainConnect()
#            
#        return_accueil = tk.Button (self, text="Accueil", width=15, height=1, command=accueil)
#        return_accueil.place(x=250,y=28)
     
        
            # mettre une image type le saviez vous concernant la tensuon
        
        e1 = tk.StringVar()
        e1.set("Date")
        entree1 = tk.Entry(self, textvariable=e1, width=20, state='readonly', justify='center')
        entree1.grid(row=2,column=1)
        
        e2 = tk.StringVar()
        e2.set("Heure")
        entree2 = tk.Entry(self, textvariable=e2, width=20, state='readonly', justify='center')
        entree2.grid(row=2,column=2)
        
        e3 = tk.StringVar()
        e3.set("Médecin")
        entree3 = tk.Entry(self, textvariable=e3, width=20, state='readonly', justify='center')
        entree3.grid(row=2,column=3)
        
        e4 = tk.StringVar()
        e4.set("Téléphone")
        entree4 = tk.Entry(self, textvariable=e4, width=20, state='readonly', justify='center')
        entree4.grid(row=2,column=4)
        
        
                
        def rdv_In ():
            self.destroy()
            mainSaisieRDV()
                    
        
        rdv_in = tk.Button (self, text="Je souhaite prendre un rendez-vous", width=30, height=2, command=rdv_In)
        rdv_in.grid(row=5, column=0)
  
        
        
        self.mainloop()
        
class Saisie_rdv (tk.Frame):
    
    def __init__(self,fenetre):
        tk.Frame.__init__(self)
        
        
    def initialiser(self):
        
        self.pack(fill=tk.BOTH,expand=1)
        
       
            
        def valider ():
            self.destroy()
            choix_medecin = type_med.get()
            
            rdv = tk.Frame()
            rdv.pack(fill=tk.BOTH,expand=1)
            logo = Image.open("icar.png")
            logo1= ImageTk.PhotoImage(logo)
            img = tk.Label(rdv, image=logo1)
            img.image = logo1
            img.grid()
#            return_accueil = tk.Button (myrdv, text="Accueil", width=15, height=1, command=mainConnect)
#            return_accueil.place(x=250,y=28)
            
            e1 = tk.StringVar()
            e1.set("Nom")
            entree1 = tk.Entry(rdv, textvariable=e1, width=20, state='readonly', justify='center')
            entree1.grid(row=2,column=1)
            
            e2 = tk.StringVar()
            e2.set("Prénom(s)")
            entree2 = tk.Entry(rdv, textvariable=e2, width=20, state='readonly', justify='center')
            entree2.grid(row=2,column=2)
            
            e3 = tk.StringVar()
            e3.set("Téléphone")
            entree3 = tk.Entry(rdv, textvariable=e3, width=20, state='readonly', justify='center')
            entree3.grid(row=2,column=3)
            
            e4 = tk.StringVar()
            e4.set("Selectionner le médecin")
            entree4 = tk.Entry(rdv, textvariable=e4, width=25, state='readonly', justify='center')
            entree4.grid(row=2,column=4)
                
            cursor.execute("""SELECT idmedecin, nom, prenom, numero FROM medecin WHERE specialite = %s""", (choix_medecin, ))
            medecin = cursor.fetchall()
            print(medecin)
            
            def choix (idm):    
                
                    intro = tk.Label(rdv, text ="Voici les disponibilités du médecin choisi:" )
                    intro.grid(row=8,column=0)                
                    cursor.execute("""SELECT date,heure FROM disponibilite WHERE medecin_idmedecin = %s""", (idm, ))
                    dispo = list(cursor.fetchall())
                    
                    e1 = tk.StringVar()
                    e1.set("Date")
                    entree1 = tk.Entry(rdv, textvariable=e1, width=20, state='readonly', justify='center')
                    entree1.grid(row=30,column=1)
                    
                    e2 = tk.StringVar()
                    e2.set("Heure")
                    entree2 = tk.Entry(rdv, textvariable=e2, width=20, state='readonly', justify='center')
                    entree2.grid(row=30,column=2)
                    
                    if dispo == []:
                      
#                        (tk.Label(rdv, text ="Il n'y a aucune disponibilité. Désolé." )).grid(row=20, column=0)
#                        (tk.Label(rdv, text ="                                 " )).grid(row=21, column=1)
#                        (tk.Label(rdv, text ="                                  ")).grid(row=22, column=1)
                        (tk.Label(rdv, text ="indisponible" )).grid(row=32, column=1)
                        (tk.Label(rdv, text ="indisponible")).grid(row= 32, column=2)
                        
                        
                    else:
                     
                        (tk.Label(rdv, text ="                                                                                                       " )).grid(row=20, column=0)
                        d=str(dispo[0][0]).split("-")
                        
                        date=str(d[2])+"-"+str(d[1])+"-"+str(d[0])
                        hour = dispo[0][1]
                        day = hour.days
                        second = hour.seconds
                        heure = day*24+second//3600
                        seconds = second%60
                        minutes = (second%3600)//60
                        h=str(heure)+":"+str(minutes)+":"+str(seconds)
                        
                    
                        
                        for i in range(1):
                            
                            (tk.Label(rdv, text =date )).grid(row=(i+1)+31, column=1)
                            (tk.Label(rdv, text =h)).grid(row= (i+1)+31, column=2)
                            
                

            for i in range (len(medecin)):
                                
                e1 = tk.StringVar()
                e1.set(medecin[i][1])
                entree1 = tk.Entry(rdv, textvariable=e1, width=20, state='readonly', justify='center')
                entree1.grid(row=i+3,column=1)
                
                e2 = tk.StringVar()
                e2.set(medecin[i][2])
                entree2 = tk.Entry(rdv, textvariable=e2, width=20, state='readonly', justify='center')
                entree2.grid(row=i+3,column=2)
                
                e3 = tk.StringVar()
                e3.set(medecin[i][3])
                entree3 = tk.Entry(rdv, textvariable=e3, width=20, state='readonly', justify='center')
                entree3.grid(row=i+3,column=3)
                
#                select = tk.IntVar() 
#                selected = tk.Radiobutton(rdv, variable=select, value=medecin[i][0])
#                selected.grid(row=i+3,column=4)
                
                Enregistrer = tk.Button (rdv, text="Choisir", width=15, height=1, command=lambda i=i : choix(idm=medecin[i][0]))
                Enregistrer.grid(row=i+3,column=4) 
                
#                
#                
#                
#            def choix ():
#                idmedecin = select.get()
#                print(idmedecin)
#                
#            Enregistrer = tk.Button (rdv, text="Voir les disponibilités", width=15, height=1, command=choix)
#            Enregistrer.grid(row=7,column=2)   
            
                
                
            
        

        
        logo = Image.open("icar.png")
        logo1= ImageTk.PhotoImage(logo)
        img = tk.Label(self, image=logo1)
        img.image = logo1
        img.grid()  
          
    
        
        intro = tk.Label(self, text ="Veuillez choisir le médecin chez qui prendre rendez-vous." )
        intro.grid(row=0,column=1)
        
         
        type_med = tk.StringVar() 
        t1 = tk.Radiobutton(self, text="Cardiologue", variable=type_med, value="Cardiologue")
        t2 = tk.Radiobutton(self, text="Dermatologue", variable=type_med, value="Dermatologue")
        t3 = tk.Radiobutton(self, text="Généraliste", variable=type_med, value="Généraliste")
        t4 = tk.Radiobutton(self, text="Ophtalmologue", variable=type_med, value="Ophtalmologue")
        t5 = tk.Radiobutton(self, text="Urologue", variable=type_med, value="Urologue")
        t6 = tk.Radiobutton(self, text="Dentiste", variable=type_med, value="Dentiste")
        t7 = tk.Radiobutton(self, text="Pédiatre", variable=type_med, value="Pédiatre")
        t8 = tk.Radiobutton(self, text="Endocrinologue", variable=type_med, value="Endocrinologue")
        t9 = tk.Radiobutton(self, text="Orthopédiste", variable=type_med, value="Orthopédiste")
        t10 = tk.Radiobutton(self, text="ORL", variable=type_med, value="ORL")
        t11 = tk.Radiobutton(self, text="Nutritionniste", variable=type_med, value="Nutritionniste")
        t12 = tk.Radiobutton(self, text="Psychologue", variable=type_med, value="Psychologue")
        t1.select()
        
        t1.grid(row=1, column=1, sticky=tk.W)
        t2.grid(row=1, column=2, sticky=tk.W)
        t3.grid(row=2, column=1, sticky=tk.W)
        t4.grid(row=2, column=2, sticky=tk.W)
        t5.grid(row=3, column=1, sticky=tk.W)
        t6.grid(row=3, column=2, sticky=tk.W)
        t7.grid(row=4, column=1, sticky=tk.W)
        t8.grid(row=4, column=2, sticky=tk.W)
        t9.grid(row=5, column=1, sticky=tk.W)
        t10.grid(row=5, column=2, sticky=tk.W)
        t11.grid(row=6, column=1, sticky=tk.W)
        t12.grid(row=6, column=2, sticky=tk.W)
        
#        date_heure = str( dt.datetime.now())
#        d_h = date_heure.split()
#        date="Date d'aujourd'hui: "+d_h[0]
#        heure ="Heure: "+ d_h[1]
#        (tk.Label(self, text =date )).grid(row=2, column=1)
#        (tk.Label(self, text =heure)).grid(row=3, column=1)
#        
        

        Enregistrer = tk.Button (self, text="Choisir un médecin", width=15, height=1, command=valider)
        Enregistrer.grid(row=7,column=2)
              
    
def main():
    root= tk.Tk()
    root.geometry("900x500")
    Accueil(root)
    
def mainConnect ():    
    page=Connected()
    page.initialiser()    
    
def mainInfos():    
    page=MyInfos(tk.Tk)
    page.initialiser()
    
def mainSaisieInfo():    
    page=Saisie_Infos(tk.Tk)
    page.initialiser()     
        
def mainTension():    
    page=Tension(tk.Tk)
    page.initialiser()
    
def mainSaisieTension():    
    page=Saisie_Tension(tk.Tk)
    page.initialiser()     
    
def mainRDV(): 
    page=RDV(tk.Tk)
    page.initialiser()
    
def mainSaisieRDV():    
    page=Saisie_rdv(tk.Tk)
    page.initialiser()     