from tkinter import *

#variables ventana principal y globales
xsize=1200
ysize=700
color = '#E4ECEF'
Status = 0
Possition = 0
Idioma = 1
tabla = []
tabla2 = []
#variables de ventana Iniciar Sesion
xsize2 = 400
ysize2 = 550
color2 = '#D6EDF3'
#variables de ventana Administrador
xposition=40
yposition= 80
typeletter='Helvetica 12'
xwidth = 25
#variable ventana de las Aplicaciones
xpos = 100
ypos = 100
xposition1=60
yposition1=80

#funcion que convierte el archivo plano compradores.txt a una lista 
buyer = open('DB/comprador.txt', 'r')
usersList = buyer.readlines()
buyer.close()
def splitUsers(a, L):
    if  a == L:
        return ''
    else:
        usersList[a] = usersList[a].replace('\n', '').replace('Other', 'Otro').split(',')
        return splitUsers(a+1, L)
splitUsers(0, len(usersList))
IDComprador = len(usersList)+1

#funcion que convierte el archivo plano idioma.txt a una lista 
idioma = open('DB/idioma.txt', 'r')
idiomaList = idioma.readlines()
idioma.close()
def splitIdioma(a, L):
        if  a == L:
            return ''
        else:
            idiomaList[a] = idiomaList[a].replace('\n', '').split(',')
            return splitIdioma(a+1, L)
splitIdioma(0, len(idiomaList))

#funcion que convierte el archivo plano apps.txt a una lista 
apps = open('DB/apps.txt', 'r')
appsList = apps.readlines()
apps.close()
def splitApps(a, L):
        if  a == L:
            return ''
        else:
            appsList[a] = appsList[a].replace('\n', '').split(';')
            return splitApps(a+1, L)
splitApps(0, len(appsList))
IDApp = len(appsList)+1

#funcion que convierte el archivo plano vendedor.txt a una lista 
seller = open('DB/vendedor.txt', 'r')
sellerList = seller.readlines()
seller.close()
def splitSeller(a, L):
        if  a == L:
            return ''
        else:
            sellerList[a] = sellerList[a].replace('\n', '').split(',')
            return splitSeller(a+1, L)
splitSeller(0, len(sellerList))
IDVendedor = len(sellerList)+1

#Ventana principal y ajustes
main = Tk()
main.title('AStore')
main.minsize(xsize, ysize)
main.resizable(width=NO, height=NO)
main.config(bg='white')

fondo = PhotoImage(file='img/fondo1.gif')
canvasMain = Canvas(main, width=xsize, height = ysize, bg=color)
canvasMain.place(x=0, y=0)
fondoLabel = Label(canvasMain, image = fondo)
fondoLabel.place(x = -5, y = -5)
tittleLabel = Label(canvasMain, text='Astore', font=('Helvetica 25 bold'), bg='#CCFFFF')
tittleLabel.place(x=20, y=15)
searchEntry = Entry(canvasMain, width=30, font=('Helvetica 20'))
searchEntry.place(x=200, y=20)
    
#Ventana Iniciar Sesion y ajustes 
def ventanaUsuario(): #funcion llama la ventana de iniciar sesion
    main.withdraw()
    main2 = Toplevel()
    main2.minsize(xsize2, ysize2)
    main2.resizable(width = NO, height = NO)
    canvasUsuario = Canvas(main2, width=xsize2, height = ysize2, bg=color2)
    canvasUsuario.place(x=0, y=0)
    fondo2Label = Label(canvasUsuario, image = fondo2)
    fondo2Label.place(x = -5, y = -5)

#Interfaz de ventana Iniciar Sesion
    def idioma2():
        main2.title(idiomaList[1][Idioma])
        topLabel = Label(canvasUsuario, text=idiomaList[3][Idioma], font='Helvetica 18 bold', bg=color, width=12)
        topLabel.place(x=110, y=75)
        usuarioLabel = Label(canvasUsuario, text=idiomaList[4][Idioma],width=5)
        usuarioLabel.place(x=70, y=200)
        usuarioEntry = Entry(canvasUsuario, width=30)
        usuarioEntry.place(x=120, y=200)
        usuarioPassword = Entry(canvasUsuario, width=10, font='wingdings')
        usuarioPassword.place(x=120, y=250)
        usuarioLabelPassword = Label(canvasUsuario, text=idiomaList[5][Idioma],width=9)
        usuarioLabelPassword.place(x=45, y=250)
#Boton idioma en ventana Iniciar Sesion
        idiomaButton = Button(canvasUsuario, text=idiomaList[2][Idioma], command=cambiarIdioma, width=7)
        idiomaButton.place(x=320, y=500)
            
#Verifica inicio de sesion
        def revisarVendedores(n, L): #funcion que revisa las ID de vendedores
            if n == L:
                return False
            elif sellerList[n][0] == str(usuarioEntry.get()):
                return sellerList[n][0]
            else:
                return revisarVendedores(n+1, L)
            
        def principal(): #funcion para ingresar a modo administrador o usuario normal
            vendedorID = revisarVendedores(0, len(sellerList))
            if (usuarioEntry.get() == 'admin') and (usuarioPassword.get() == '1234'):
                mainAdmin()
            elif usuarioEntry.get() != '':
                global usersList
                global Status
                global Possition
                L = len(usersList)
                poss = getCorreo(usersList, L, 0)
                if searchEmail(poss, usersList) == True:
                    main.deiconify()
                    main2.destroy()
                    Possition=poss
                    Status=1
                    estado()
                elif str(usuarioEntry.get()) == vendedorID:
                    mainVendedor(vendedorID)
                else:
                    cuadroError = Label(canvasUsuario, text=idiomaList[7][Idioma], width=24)
                    cuadroError.place(x=120, y=280)
            else:
                    cuadroError = Label(canvasUsuario, text=idiomaList[14][Idioma], width=24)
                    cuadroError.place(x=120, y=280)

        def getCorreo(usersList, L, n): #funcion que obtiene el correo en el entry y revisa si existe en la base de datos
            if n == L:
                return False
            elif usersList[n][2] == str(usuarioEntry.get()):
                return n
            else:
                return getCorreo(usersList, L, n+1)

        def searchEmail(poss, usersList):#funcion que compara el correo ingresado con la contraseña adecuada
            if poss >= 0:
                password = usersList[poss][3]
                entry = str(usuarioPassword.get())
                if entry == password:
                    return True
                else:
                    return False

#Ventana modo Vendedor
        def mainVendedor(ID):
            main2.destroy()
            mainVendedor = Toplevel()
            mainVendedor.minsize(950, 500)
            mainVendedor.resizable(width=NO, height=NO)
            
            canvasVendedor = Canvas(mainVendedor, width=950, height=500, bg=color)
            canvasVendedor.place(x=0, y=0)
            canvasApps = Canvas(mainVendedor, width=300, height=500, bg=color)
            canvasApps.place(x=350, y=80)
            
#Interfaz de ventana modo Vendedor
            def idioma7():
                mainVendedor.title (sellerList[int(ID)-1][1])
                newLabel2 = Label(canvasVendedor, text= idiomaList[28][Idioma], font='Helvetica 18 bold', fg=color, bg='#253235', width=15)
                newLabel2.place(x=xposition1+5 , y=yposition1-60)
                nameLabel2 = Label(canvasVendedor, text=idiomaList[29][Idioma], fg=color , font=typeletter, bg='#253235')
                nameLabel2.place(x=xposition1-40, y=yposition1)
                sellerLabel2 = Label(canvasVendedor, text=idiomaList[50][Idioma], fg=color, font=typeletter, bg='#253235', width=10)
                sellerLabel2.place(x=xposition1-18, y=yposition1+30)
                descriptionLabel2 = Label(canvasVendedor, text=idiomaList[51][Idioma], fg=color, font=typeletter, bg='#253235', width=10)
                descriptionLabel2.place(x=xposition1-16, y=yposition1+60)
                priceLabel2 = Label(canvasVendedor, text=idiomaList[33][Idioma], fg=color, font=typeletter, bg='#253235', width=8)
                priceLabel2.place(x=xposition1, y=yposition1+90)
                imgLabel2 = Label(canvasVendedor, text=idiomaList[31][Idioma], fg=color, font=typeletter, bg='#253235', width=8)
                imgLabel2.place(x=xposition1, y=yposition1+120)
                img2Label2 = Label(canvasVendedor, text=idiomaList[32][Idioma], fg=color, font=typeletter, bg='#253235', width=8)
                img2Label2.place(x=xposition1, y=yposition1+150)
                categoryLabel = Label(canvasVendedor, text=idiomaList[53][Idioma], fg=color, font=typeletter, bg='#253235', width=8)
                categoryLabel.place(x=xposition1, y=yposition1+180)
                appsIDLabel = Label(canvasVendedor, text='ID', bg=color)
                appsIDLabel.place(x=350, y=50)
                appsNameLabel = Label(canvasVendedor, text=idiomaList[29][Idioma], bg=color)
                appsNameLabel.place(x=380, y=50)
                sellerIDLabel = Label(canvasVendedor, text=idiomaList[61][Idioma], bg=color)
                sellerIDLabel.place(x=480, y=50)
                statusLabel = Label(canvasVendedor, text=idiomaList[59][Idioma], bg=color)
                statusLabel.place(x=520, y=50)
                precioLabel = Label(canvasVendedor, text=idiomaList[60][Idioma], bg=color, width=6)
                precioLabel.place(x=610, y=50)
                downloadsLabel = Label(canvasVendedor, text=idiomaList[62][Idioma], bg=color, width=7)
                downloadsLabel.place(x=720, y=50)
                donwloadsCRLabel = Label(canvasVendedor, text='CR', bg=color)
                donwloadsCRLabel.place(x=775, y=50)
                categoryLabel = Label(canvasVendedor, text=idiomaList[53][Idioma], bg=color)
                categoryLabel.place(x=800, y=50)
                estadoLabel = Label(canvasVendedor, text=idiomaList[66][Idioma], bg=color, font='Helvetica 12 bold', width=12)
                estadoLabel.place(x=400, y=10)
                
                nameEntry2 = Entry(canvasVendedor, width=xwidth)
                nameEntry2.place(x=xposition1+90, y=yposition1)
                sellerEntry2 = Entry(canvasVendedor, width=xwidth, state=DISABLED)
                sellerEntry2.insert(0, ID)
                sellerEntry2.place(x=xposition1+90, y=yposition1+30)
                descriptionEntry2 = Entry(canvasVendedor, width=xwidth)
                descriptionEntry2.place(x=xposition1+90, y=yposition1+60)
                priceEntry2 = Entry(canvasVendedor, width=xwidth)
                priceEntry2.place(x=xposition1+90, y=yposition1+90)
                imgEntry2 = Entry(canvasVendedor, width=xwidth)
                imgEntry2.place(x=xposition1+90, y=yposition1+120)            
                img2Entry2 = Entry(canvasVendedor, width=xwidth)
                img2Entry2.place(x=xposition1+90, y=yposition1+150)
                estadoEntry = Entry(canvasVendedor, width=5)
                estadoEntry.place(x=535,y=12)
                
                category=[idiomaList[54][Idioma],idiomaList[56][Idioma],idiomaList[55][Idioma], 'Multimedia']
                select=StringVar(main)
                select.set(idiomaList[54][Idioma])
                category = OptionMenu(canvasVendedor, select, *category)
                category.config(width=15)
                category.place(x=xposition+110, y=yposition+175)
                
#Agregar aplicaciones
                def addApp(): #funcion que revisa que se llenen los espacios requeridos para ingresar una aplicacion
                    global IDApp
                    if (nameEntry2.get() != ''):
                        if (sellerEntry2.get() != ''):
                            if checkSeller(0, len(sellerList))==False:
                                if (priceEntry2.get() != ''):
                                    apps = open('DB/apps.txt', 'a')
                                    apps.write(str(IDApp))
                                    apps.write(';')
                                    apps.write(nameEntry2.get())
                                    apps.write(';')
                                    apps.write(sellerEntry2.get())
                                    apps.write(';')
                                    apps.write('Activo')
                                    apps.write(';')
                                    apps.write('$'+priceEntry2.get())
                                    apps.write(';')
                                    apps.write(imgEntry2.get())
                                    apps.write(';')
                                    apps.write(img2Entry2.get())
                                    apps.write(';')
                                    apps.write(descriptionEntry2.get())
                                    apps.write(';')
                                    apps.write('0')
                                    apps.write(';')
                                    apps.write('0')
                                    apps.write(';')
                                    apps.write(select.get())
                                    apps.write('\n')
                                    cuadro = Label(canvasVendedor, text=idiomaList[34][Idioma], width=xwidth-5)
                                    cuadro.place(x=xposition1+40, y=yposition1+210)
                                    apps.close()
                                    releer3()
                                else:
                                    cuadroError = Label(canvasVendedor, text=idiomaList[35][Idioma], width=xwidth-5)
                                    cuadroError.place(x=xposition1+40, y=yposition1+210)
                            else:
                                cuadroError = Label(canvasVendedor, text=idiomaList[52][Idioma], width=xwidth-5)
                                cuadroError.place(x=xposition1+40, y=yposition1+210)
                        else:
                            cuadroError = Label(canvasVendedor, text=idiomaList[36][Idioma], width=xwidth-5)
                            cuadroError.place(x=xposition1+40, y=yposition1+210)
                    else:
                        cuadroError = Label(canvasVendedor, text=idiomaList[37][Idioma], width=xwidth-5)
                        cuadroError.place(x=xposition1+40, y=yposition1+210)
                def releer3(): #funcion que redefine la lista de apps para que se actualice
                    global appsList
                    global IDApp
                    apps = open('DB/apps.txt', 'r')
                    appsList = apps.readlines()
                    apps.close()
                    splitApps(0, len(appsList))
                    IDApp = len(appsList)+1

                def checkSeller(n, L): #funcion que revisa si el ID ingresado ya esta registrado
                    if n == L:
                        return True
                    elif str(sellerEntry2.get()) == sellerList[n][0]:
                        return False
                    else:
                        return checkSeller(n+1, L)

                def largoTabla(n, L): #funcion que mide cuantos apps por vendedor hay
                    if n == L:
                        return 0
                    elif appsList[n][2] == ID:
                        return 1 + largoTabla(n+1, L)
                    else:
                        return largoTabla(n+1, L)

                def crearTabla(x, y, L, casilla): #funcion que crea la tabla para apps
                        global tabla2
                        cantidad = largoTabla(0, len(appsList))
                        if x == cantidad:
                            return ''
                        elif y == 9:
                            tabla2 += [casilla]
                            return crearTabla(x+1, 0, L, [])
                        else:
                            if y == 0 or y== 2 or y == 5 or y == 6 or y == 7:
                                cuadro = Entry(canvasApps, text='', width=5, justify=CENTER)
                                cuadro.grid(row=x, column=y)
                                return crearTabla(x, y+1, L, casilla+[cuadro])
                            cuadro = Entry(canvasApps, text='', width=15)
                            cuadro.grid(row=x, column=y)
                            return crearTabla(x, y+1, L, casilla+[cuadro])

                def llenarTabla(x, y, L, a, b): #funcion que llena la tabla para apps con el apps.txt
                    global tabla2
                    cantidad = largoTabla(0, len(appsList))
                    if x == cantidad:
                        return
                    elif y == 5:
                        llenarTabla(x, y+1, L, a, b+3)
                    elif appsList[a][2] == ID:
                        if y != 9:
                            tabla2[x][y].insert(0, appsList[a][b])
                            return llenarTabla(x, y+1, L,a, b+1)
                        else:
                            return llenarTabla(x+1, 0, L, a+1, 0)
                    else:
                        return llenarTabla(x, 0, L, a+1, 0)       
                crearTabla(0, 0, len(appsList), [])
                llenarTabla(0, 0, len(appsList), 0, 0)

                def revisarID(n, L): #funcion que compara la ID con el entry
                    if n == L:
                        return False
                    elif appsList[n][0] == estadoEntry.get() and appsList[n][2] == ID:
                        return n
                    else:
                        return revisarID(n+1, L)
                    
                def cambiarEstado(): #funcion que revisa el estado de la aplicacion
                    appID = revisarID(0, len(appsList))
                    if appsList[appID][3] == 'Activo' and appsList[appID][2] == ID:
                        return 'Inactivo'
                    elif appsList[appID][3] == 'Inactivo' and appsList[appID][2] == ID:
                        return 'Activo'

                def actualizarEstado(): #funcion que cambia el estado de la aplicacion
                    appID = revisarID(0, len(appsList))
                    if appID != False:
                        apps = open('DB/apps.txt', 'w')
                        actualizarEstadoAux(0, len(appsList), apps, appID)
                    else:
                        errorLabel = Label(canvasVendedor, text=idiomaList[68][Idioma], width=15)
                        errorLabel.place(x=660, y=12)
                def actualizarEstadoAux(n, L, apps, appID): #funcion auxiliar que cambia el estado de la aplicacion
                    if n == L:
                        apps.close()
                        aceptaLabel = Label(canvasVendedor, text=idiomaList[70][Idioma], width=15, bg=color)
                        aceptaLabel.place(x=660, y=12)
                        releer3()
                    elif n == appID:
                        apps.write(appsList[n][0])
                        apps.write(';')
                        apps.write(appsList[n][1])
                        apps.write(';')
                        apps.write(appsList[n][2])
                        apps.write(';')
                        apps.write(cambiarEstado())
                        apps.write(';')
                        apps.write(appsList[n][4])
                        apps.write(';')
                        apps.write(appsList[n][5])
                        apps.write(';')
                        apps.write(appsList[n][6])
                        apps.write(';')
                        apps.write(appsList[n][7])
                        apps.write(';')
                        apps.write(appsList[n][8])
                        apps.write(';')
                        apps.write(appsList[n][9])
                        apps.write(';')
                        apps.write(appsList[n][10])
                        apps.write('\n')
                        actualizarEstadoAux(n+1, L, apps, appID)
                    else:
                        apps.write(appsList[n][0])
                        apps.write(';')
                        apps.write(appsList[n][1])
                        apps.write(';')
                        apps.write(appsList[n][2])
                        apps.write(';')
                        apps.write(appsList[n][3])
                        apps.write(';')
                        apps.write(appsList[n][4])
                        apps.write(';')
                        apps.write(appsList[n][5])
                        apps.write(';')
                        apps.write(appsList[n][6])
                        apps.write(';')
                        apps.write(appsList[n][7])
                        apps.write(';')
                        apps.write(appsList[n][8])
                        apps.write(';')
                        apps.write(appsList[n][9])
                        apps.write(';')
                        apps.write(appsList[n][10])
                        apps.write('\n')
                        actualizarEstadoAux(n+1, L, apps, appID)

                def returnMain(): #funcion que regresa a ventana principaal destruyendo la vendedores
                    global tabla2
                    releer3()
                    tabla2 = []
                    idioma1()
                    estado()
                    searchAppsList()
                    main.deiconify()
                    mainVendedor.destroy()

#Botones de ventana Vendedores
                estadoButton = Button(canvasVendedor, text=idiomaList[67][Idioma], width=7, command=actualizarEstado)
                estadoButton.place(x=580, y=10)
                addAppButton=Button(canvasVendedor, text=idiomaList[27][Idioma], command=addApp,width=9)
                addAppButton.place(x=130, y=320)
                returnButton = Button(canvasVendedor, image=circle ,command=returnMain)
                returnButton.place(x=5, y=12)
                idiomaButton = Button(canvasVendedor, text=idiomaList[2][Idioma] ,command=cambiarIdioma, width=7)
                idiomaButton.place(x=5, y=yposition+390)
                
            def cambiarIdioma(): #funcion que cambia idioma desde ventana Iniciar Sesion
                global tabla2
                global Idioma
                if Idioma == 1:
                        Idioma = 2
                elif Idioma == 2:
                        Idioma = 1
                tabla2 = []
                idioma7()
            idioma7()

        def mainReturn(): #funcion que retorna a ventana principal desde Inicar Sesion
            main2.destroy()
            main.deiconify()
            estado()
            idioma1()
            
#Botones de ventana Iniciar Sesion            
        returnButton = Button(canvasUsuario, command=mainReturn, image=circle)
        returnButton.place(x=10, y=10)

#Ventana Crear Cuenta y ajustes
        def createAccount(): #funcion que llama la ventana Crear Cuenta
            mainAccount= Toplevel()
            main2.withdraw()
            mainAccount.minsize(300,350)
            mainAccount.resizable(width=NO, height=NO)
            
            canvasAccount = Canvas(mainAccount, bg=color2, height=350, width=300)
            canvasAccount.place(x=0, y=0)
            fondo2Label = Label(canvasAccount, image = fondo2)
            fondo2Label.place(x = -5, y = -5)

#Interfaz de ventana Crear Cuenta
            def idioma3(): #funcion que selecciona el texto segun su posicion en la lista de idiomas 
                newLabel = Label(canvasAccount, text=idiomaList[8][Idioma] , font='Helvetica 18 bold', bg=color, width=11)
                newLabel.place(x=xposition+30 , y=yposition-60)
                nameLabel = Label(canvasAccount, text=idiomaList[9][Idioma], bg=color , font=typeletter, width=7)
                nameLabel.place(x=xposition, y=yposition)
                emailLabel = Label(canvasAccount, text=idiomaList[4][Idioma], bg=color, font=typeletter, width=7)
                emailLabel.place(x=xposition, y=yposition+30)
                pass1Label = Label(canvasAccount, text=idiomaList[12][Idioma], bg=color, font=typeletter, width=9)
                pass1Label.place(x=xposition-20, y=yposition+60)
                pass2Label = Label(canvasAccount, text=idiomaList[10][Idioma], bg=color, font=typeletter, width=8)
                pass2Label.place(x=xposition-10, y=yposition+90)
                countryLabel = Label(canvasAccount, text=idiomaList[11][Idioma], bg=color, font=typeletter, width=7)
                countryLabel.place(x=xposition-1, y=yposition+122)

                nameEntry = Entry(canvasAccount, width=xwidth)
                nameEntry.place(x=xposition+70, y=yposition)
                emailEntry = Entry(canvasAccount, width=xwidth)
                emailEntry.place(x=xposition+70, y=yposition+30)
                pass1Entry = Entry(canvasAccount, width=xwidth-17, font='wingdings')
                pass1Entry.place(x=xposition+70, y=yposition+60)
                pass2Entry = Entry(canvasAccount, width=xwidth-17, font='wingdings')
                pass2Entry.place(x=xposition+70, y=yposition+90)
                country=['Costa Rica', idiomaList[22][Idioma]]
                tittle=StringVar(main)
                tittle.set(idiomaList[23][Idioma])
                country = OptionMenu(canvasAccount, tittle, *country)
                country.config(width=9)
                country.place(x=xposition+70, y=yposition+120)

#Crear un nuevo usuario
                def newUser(): #funcion que revisa que las entrys no esten vacías y guarda los datos en compradores.txt
                    global Status
                    global Possition
                    if (nameEntry.get()!=''):
                        if (emailEntry.get()!=''):
                            if checkUser() == True:
                                if (pass1Entry.get()!=''):
                                    if (pass2Entry.get() == pass1Entry.get()):
                                        if (tittle.get()=='Costa Rica') or (tittle.get()==idiomaList[22][Idioma]):
                                            global IDComprador
                                            global usersList
                                            usuarios = open('DB/comprador.txt', 'a')
                                            usuarios.write(str(IDComprador))
                                            usuarios.write(',')
                                            usuarios.write(nameEntry.get())
                                            usuarios.write(',')
                                            usuarios.write(emailEntry.get())
                                            usuarios.write(',')
                                            usuarios.write(pass1Entry.get())
                                            usuarios.write(',')
                                            usuarios.write(tittle.get())
                                            usuarios.write(',')
                                            usuarios.write('0')
                                            usuarios.write('\n')
                                            usuarios.close()
                                            releer2()
                                            mainAccount.destroy()
                                            main.deiconify()
                                            main2.destroy()
                                            Possition = -1
                                            Status = 1
                                            estado()
                                        else:
                                            cuadroError = Label(canvasAccount, text=idiomaList[24][Idioma], width=xwidth-5)
                                            cuadroError.place(x=xposition+40, y=yposition+160)
                                    else:
                                        cuadroError = Label(canvasAccount, text=idiomaList[25][Idioma], width=xwidth-5)
                                        cuadroError.place(x=xposition+40, y=yposition+160)
                                else:
                                    cuadroError = Label(canvasAccount, text=idiomaList[15][Idioma], width=xwidth-5)
                                    cuadroError.place(x=xposition+40, y=yposition+160)
                            else:
                                cuadroError = Label(canvasAccount, text=idiomaList[46][Idioma], width=xwidth-5)
                                cuadroError.place(x=xposition+40, y=yposition+160)
                        else:
                            cuadroError = Label(canvasAccount, text=idiomaList[14][Idioma], width=xwidth-5)
                            cuadroError.place(x=xposition+40, y=yposition+160)
                    else:
                        cuadroError = Label(canvasAccount, text=idiomaList[13][Idioma], width=xwidth-5)
                        cuadroError.place(x=xposition+40, y=yposition+160)
                def releer2(): #funcion que redefine la lista de usuarios para que se actualice
                    global usersList
                    global IDComprador
                    buyer = open('DB/comprador.txt', 'r')
                    usersList = buyer.readlines()
                    buyer.close()
                    splitUsers(0, len(usersList))
                    IDComprador = len(usersList)+1
                def checkUser(): #funcion que verifica si el correo ya esta en uso
                    global usersList
                    return checkUser_aux(usersList , len(usersList), 0)
                def checkUser_aux(usersList, m, n): #funcion auxiliar de checkUser()
                    if  m == n:
                        return True
                    elif usersList[n][2].lower() == str(emailEntry.get()):
                        return False
                    else:
                        return checkUser_aux(usersList, m, n+1)
                        
                def mainReturn(): #funcion que regresa a la ventana de iniciar sesion
                    mainAccount.destroy()
                    main2.deiconify()
                    
                def cambiarIdioma(): #funcion que cambia idioma desde ventana Crear Cuenta
                    global Idioma
                    if Idioma == 1:
                            Idioma = 2
                    elif Idioma == 2:
                            Idioma = 1
                    idioma3()
                    idioma2()
#Botones de ventana Crear Cuenta                
                createButton = Button(canvasAccount, text=idiomaList[26][Idioma], command=newUser, width=12)
                createButton.place(x=xposition+70, y=yposition+210)
                returnButton = Button(canvasAccount, command=mainReturn, image=circle)
                returnButton.place(x= xposition-35, y=yposition-75)
                idiomaButton = Button(canvasAccount, text=idiomaList[2][Idioma], command=cambiarIdioma, width=7)
                idiomaButton.place(x=xposition+190, y=yposition+230)
            idioma3()
            
#Ventana administrador y ajustes       
        def mainAdmin(): #funcion que llama la ventana Admin
            main.withdraw()
            main2.destroy()
            mainAdmin = Toplevel()
            mainAdmin.title ('Admin')
            mainAdmin.minsize(300, 350)
            mainAdmin.resizable(width=NO, height=NO)
            
            canvasAdmin = Canvas(mainAdmin, width=300, height=350, bg='#253235')
            canvasAdmin.place(x=0, y=0)
            
#Interfaz de ventana Admin
            def idioma4():
                newLabel = Label(canvasAdmin, text=idiomaList[17][Idioma] , font='Helvetica 18 bold', fg=color, bg='#253235', width=13)
                newLabel.place(x=xposition+15 , y=yposition-60)
                nameLabel = Label(canvasAdmin, text=idiomaList[9][Idioma], fg=color , font=typeletter, bg='#253235', width=9)
                nameLabel.place(x=xposition-10, y=yposition-10)
                emailLabel = Label(canvasAdmin, text=idiomaList[4][Idioma], fg=color, font=typeletter, bg='#253235', width=9)
                emailLabel.place(x=xposition-10, y=yposition+20)
                webLabel = Label(canvasAdmin, text=idiomaList[18][Idioma], fg=color, font=typeletter, bg='#253235', width=9)
                webLabel.place(x=xposition-20, y=yposition+50)
                viewLabel = Label(canvasAdmin, text = idiomaList[19][Idioma], font='Helvetica 18 bold', fg=color, bg='#253235', width=15, height=2, wraplength=250)
                viewLabel.place(x=xposition, y=yposition+160)
                
                nameEntry = Entry(canvasAdmin, width=xwidth)
                nameEntry.place(x=xposition+70, y=yposition-10)
                emailEntry = Entry(canvasAdmin, width=xwidth)
                emailEntry.place(x=xposition+70, y=yposition+20)
                webEntry = Entry(canvasAdmin, width=xwidth)
                webEntry.place(x=xposition+70, y=yposition+50)
                
#Agregar vendedor nuevo
                def newVendedor(): #funcion que guarda los datos del vendedor en vendedores.txt
                    global sellerList
                    global IDVendedor
                    if (nameEntry.get() != ''):
                        if (emailEntry.get() != ''):
                            if checkSellers() == True:
                                if (webEntry.get() != ''):
                                    vendedor = open('DB/vendedor.txt', 'a')
                                    vendedor.write(str(IDVendedor))
                                    vendedor.write(',')
                                    vendedor.write(nameEntry.get())
                                    vendedor.write(',')
                                    vendedor.write(emailEntry.get())
                                    vendedor.write(',')
                                    vendedor.write(webEntry.get())
                                    vendedor.write('\n')
                                    vendedor.close()
                                    cuadroError = Label(canvasAdmin, text=idiomaList[49][Idioma], width=xwidth-4)
                                    cuadroError.place(x=xposition+40, y=165)
                                    releer()
                                else:
                                    cuadroError = Label(canvasAdmin, text=idiomaList[48][Idioma], width=xwidth-4)
                                    cuadroError.place(x=xposition+35, y=165)
                            else:
                                cuadroError = Label(canvasAdmin, text=idiomaList[47][Idioma], width=xwidth-4)
                                cuadroError.place(x=xposition+35, y=165)
                        else:
                            cuadroError = Label(canvasAdmin, text=idiomaList[14][Idioma], width=xwidth-4)
                            cuadroError.place(x=xposition+35, y=165)
                    else:
                        cuadroError = Label(canvasAdmin, text=idiomaList[13][Idioma], width=xwidth-4)
                        cuadroError.place(x=xposition+35, y=165)
            
                def checkSellers(): #funcion que verifica si el correo y nambre ya estan en uso
                    global sellerList
                    L = len(sellerList)
                    if (checkSellerEmail(sellerList , L, 0) == True) and (checkSellerName(sellerList , L, 0) == True):
                        return True
                    else:
                        return False
                def checkSellerName(sellerList, m, n): #funcion que verifica si el nombre de vendedor ya esta en uso
                    if  m == n:
                        return True
                    elif sellerList[n][1].lower() == str(emailEntry.get().lower()):
                        return False
                    else:
                        return checkSellerName(sellerList, m, n+1)
                def checkSellerEmail(sellerList, m, n): #funcion que verifica si el correo ya esta en uso
                    if  m == n:
                        return True
                    elif sellerList[n][2].lower() == str(emailEntry.get().lower()):
                        return False
                    else:
                        return checkSellerEmail(sellerList, m, n+1)
                                
                def releer(): #funcion que redefine la lista de vendedores para que se actualice
                    global sellerList
                    global IDVendedor
                    seller = open('DB/vendedor.txt', 'r')
                    sellerList = seller.readlines()
                    seller.close()
                    splitSeller(0, len(sellerList))
                    IDVendedor = len(sellerList)+1

#Ventana verVendedores y Apps ajustes
                def verVendedor():
                    mainVer = Toplevel()
                    mainAdmin.withdraw()
                    mainVer.minsize(1200, 700)
                    mainVer.resizable(height=YES, width=NO)
                    
                    def changeIdiomaSellers(): #funcion que cefine el titulo para la ventana VerVendedores segun Idioma
                        if Idioma == 1:
                            mainVer.title('Vendedores y Apps')
                        elif Idioma == 2:
                            mainVer.title('Seelers and Apps')
                    changeIdiomaSellers()
                    
#Interfaz de ventana verVendedores                     
                    canvasVer=Canvas(mainVer, width=xsize, height=ysize, bg=color)
                    canvasVer.place(x=0, y=0)
                    canvas = Label(canvasVer,width=xsize, height = ysize, bg=color)
                    canvas.place(x=20,y=100)
                    canvas2 = Label(canvasVer,width=xsize, height = ysize, bg=color)
                    canvas2.place(x=620,y=100)
                    
                    vendedoresIDLabel = Label(canvasVer, text='ID', bg=color)
                    vendedoresIDLabel.place(x=25, y=80)
                    vendedoresNameLabel = Label(canvasVer, text=idiomaList[58][Idioma], bg=color)
                    vendedoresNameLabel.place(x=50, y=80)
                    vendedoresEmailLabel = Label(canvasVer, text=idiomaList[57][Idioma], bg=color)
                    vendedoresEmailLabel.place(x=230, y=80)
                    vendedoresWebLabel = Label(canvasVer, text=idiomaList[18][Idioma], bg=color)
                    vendedoresWebLabel.place(x=415, y=80)
                    
                    appsIDLabel = Label(canvasVer, text='ID', bg=color)
                    appsIDLabel.place(x=630, y=80)
                    appsNameLabel = Label(canvasVer, text=idiomaList[29][Idioma], bg=color)
                    appsNameLabel.place(x=655, y=80)
                    sellerIDLabel = Label(canvasVer, text=idiomaList[61][Idioma], bg=color)
                    sellerIDLabel.place(x=750, y=80)
                    statusLabel = Label(canvasVer, text=idiomaList[59][Idioma], bg=color)
                    statusLabel.place(x=790, y=80)
                    precioLabel = Label(canvasVer, text=idiomaList[60][Idioma], bg=color)
                    precioLabel.place(x=880, y=80)
                    downloadsLabel = Label(canvasVer, text=idiomaList[62][Idioma], bg=color)
                    downloadsLabel.place(x=1000, y=80)
                    donwloadsCRLabel = Label(canvasVer, text='CR', bg=color)
                    donwloadsCRLabel.place(x=1045, y=80)
                    categoryLabel = Label(canvasVer, text=idiomaList[53][Idioma], bg=color)
                    categoryLabel.place(x=1080, y=80)

                    borrarLabel = Label(canvasVer, text=idiomaList[63][Idioma], font='Helvetica 12 bold', bg=color)
                    borrarLabel.place(x=75, y=20)
                    borrarEntry = Entry(canvasVer,width=5)
                    borrarEntry.place(x=270, y=22)

                    def crearTabla(x, y, L, casilla): #funcion que crea la tabla para vendedores
                        global tabla
                        if x == L:
                            return ''
                        elif y == 4:
                            tabla += [casilla]
                            return crearTabla(x+1, 0, L, [])
                        else:
                            if y == 0:
                                cuadro = Entry(canvas, text='', width=3, justify=CENTER)
                                cuadro.grid(row=x, column=y)
                                return crearTabla(x, y+1, L, casilla+[cuadro])
                            cuadro = Entry(canvas, text='', width=30)
                            cuadro.grid(row=x, column=y)
                            return crearTabla(x, y+1, L, casilla+[cuadro])

                    def llenarTabla(x, y, L): #funcion que llena la tabla para vendedores con el vendedores.txt
                        global tabla
                        if x == L:
                            return
                        elif y != 4:
                            tabla[x][y].insert(0, sellerList[x][y])
                            return llenarTabla(x, y+1, L)
                        else:
                            return llenarTabla(x+1, 0, L)

                    def crearTabla2(x, y, L, casilla): #funcion que crea la tabla para apps
                        global tabla2
                        if x == L:
                            return ''
                        elif y == 9:
                            tabla2 += [casilla]
                            return crearTabla2(x+1, 0, L, [])
                        else:
                            if y == 0 or y== 2 or y == 5 or y == 6 or y == 7:
                                cuadro = Entry(canvas2, text='', width=5, justify=CENTER)
                                cuadro.grid(row=x, column=y)
                                return crearTabla2(x, y+1, L, casilla+[cuadro])
                            cuadro = Entry(canvas2, text='', width=15)
                            cuadro.grid(row=x, column=y)
                            return crearTabla2(x, y+1, L, casilla+[cuadro])

                    def llenarTabla2(x, y, L, a, b): #funcion que llena la tabla para apps con el apps.txt
                        global tabla2
                        if x == L:
                            return
                        elif y == 5:
                            llenarTabla2(x, y+1, L, a, b+3)
                        elif y != 9:
                            tabla2[x][y].insert(0, appsList[a][b])
                            return llenarTabla2(x, y+1, L,a, b+1)
                        else:
                            return llenarTabla2(x+1, 0, L, a+1, 0)
                        
                    def abrirTabla(): #funcion que abre las tablas al abrir la ventana
                        crearTabla(0, 0, len(sellerList),[])
                        llenarTabla(0, 0, len(sellerList))
                        crearTabla2(0, 0, len(appsList),[])
                        llenarTabla2(0, 0, len(appsList),0 , 0)
                    abrirTabla()
                    
                    def buscarVendedor(n, L): #funcion que revisa si la ID ingresada para borrar existe
                        if n == L:
                            errorLabel = Label(canvasVer, text=idiomaList[65][Idioma], width=30, bg=color)
                            errorLabel.place(x=380, y=20)
                        elif str(borrarEntry.get()) == sellerList[n][0]:
                            return n
                        else:
                            return buscarVendedor(n+1, L)

                    def buscarEstado(n, L): #funcion que revisa si el vendedor tiene apps registradas
                        if n == L:
                            return True
                        elif appsList[n][2] == str(borrarEntry.get()) and appsList[n][3] == 'Activo':
                            return False
                        else:
                            return buscarEstado(n+1, L)

                    def borrarVendedor(): #funcion principal para borrar vendedor
                        if buscarEstado(0, len(appsList)) == True:
                            L = len(sellerList)
                            poss = buscarVendedor(0, L)
                            seller = open('DB/vendedor.txt', 'w')
                            borrarVendedorAux(0, L, seller, poss)
                        else:
                            errorLabel = Label(canvasVer, text=idiomaList[69][Idioma], width=30, bg=color)
                            errorLabel.place(x=380, y=20)

                    def borrarVendedorAux(n, L, seller, poss): #funcion que reescribe el vendedores.txt 
                        if n == L:
                            seller.close()
                            aceptLabel = Label(canvasVer, text=idiomaList[71][Idioma], width=30, bg=color)
                            aceptLabel.place(x=380, y=20)
                        elif n == poss:
                            seller.write('')
                            seller.write(',')
                            seller.write('')
                            seller.write(',')
                            seller.write('')
                            seller.write(',')
                            seller.write('')
                            seller.write('\n')
                            borrarVendedorAux(n+1, L, seller, poss)
                        else:
                            seller.write(sellerList[n][0])
                            seller.write(',')
                            seller.write(sellerList[n][1])
                            seller.write(',')
                            seller.write(sellerList[n][2])
                            seller.write(',')
                            seller.write(sellerList[n][3])
                            seller.write('\n')
                            borrarVendedorAux(n+1, L, seller, poss)

                    def releer(): #funcion que actualiza los datos de la tabla
                        global sellerList
                        seller = open('DB/vendedor.txt', 'r')
                        sellerList = seller.readlines()
                        seller.close()
                        splitSeller(0, len(sellerList))
                         
                    def returnAdmin(): #funcion regresar a ventana principal
                        global tabla
                        global tabla2
                        tabla = []
                        tabla2 = []
                        releer()
                        canvas.destroy()
                        mainVer.destroy()
                        mainAdmin.deiconify()
#Botones de ventana verVendedores
                    borrarButton = Button(canvasVer, text=idiomaList[64][Idioma], command=borrarVendedor)
                    borrarButton.place(x=310, y=18)
                    returnButton = Button(canvasVer, command=returnAdmin, image=circle)
                    returnButton.place(x=10, y=10)
                    
                def returnMain(): #funcion que regresa a ventana principaal destruyendo la admin
                    idioma1()
                    estado()
                    main.deiconify()
                    mainAdmin.destroy()            
#Botones de ventana Admin
                newSellerButton = Button(canvasAdmin, text=idiomaList[6][Idioma], command=newVendedor, width=8)
                newSellerButton.place(x= xposition+75, y=yposition+115)
                viewButton = Button(canvasAdmin, text=idiomaList[20][Idioma], command=verVendedor, width=4)
                viewButton.place(x= xposition+90, y=yposition+230)
                returnButton = Button(canvasAdmin, image=circle ,command=returnMain)
                returnButton.place(x=5, y=12)
                idiomaButton = Button(canvasAdmin, text=idiomaList[2][Idioma] ,command=cambiarIdioma, width=7)
                idiomaButton.place(x=xposition+200, y=yposition+240)
                
            def cambiarIdioma(): #funcion que cambia idioma desde ventana Iniciar Sesion
                global Idioma
                if Idioma == 1:
                        Idioma = 2
                elif Idioma == 2:
                        Idioma = 1
                idioma4()
            idioma4()

#Botones ventana Iniciar Sesion
        usuarioButton = Button(canvasUsuario, text=idiomaList[1][Idioma], command=principal, width=10)
        usuarioButton.place(x=170, y=350)
        usuarioButton2 = Button(canvasUsuario, text=idiomaList[6][Idioma], command=createAccount, width=8)
        usuarioButton2.place(x=176, y=400)

    def cambiarIdioma(): #funcion que cambia idioma desde ventana Iniciar Sesion
        global Idioma
        if Idioma == 1:
                Idioma = 2
        elif Idioma == 2:
                Idioma = 1
        idioma2()
    idioma2()
    
#Botones ventana principal
def idioma1(): #funcion actualiza el estado del Idioma en ventana principal
    searchButton = Button(canvasMain, text=idiomaList[0][Idioma], command=searchAppsList)
    searchButton.place(x=680, y=25)
    idiomaButton = Button(canvasMain, text=idiomaList[2][Idioma], command=cambiarIdioma, width=7)
    idiomaButton.place(x=1120, y=20)

def logout(): #funcion que actualiza el Status para indicar si se esta logueado o no
    global Status
    Status = 0
    estado()
def estado(): #funcion que cambia los botones en caso de estar la sesion abierta o cerrada
    global Status
    global Possition
    if Status == 0:
        loginButton = Button(canvasMain, text=idiomaList[1][Idioma], command=ventanaUsuario,width=10)
        loginButton.place(x=1020, y=20)
        userLogued = Label(canvasMain, text = '', justify=RIGHT, width=17, font=typeletter, bg='#CCFFFF')
        userLogued.place(x=850, y=21)
    if Status == 1:
        logoutButton = Button(canvasMain, text = idiomaList[21][Idioma], command=logout, width=10)
        logoutButton.place(x=1020, y=20)
        userLogued = Label(canvasMain, text = str(usersList[Possition][1]), justify=RIGHT, width=17, font=typeletter, bg='#CCFFFF')
        userLogued.place(x=850, y=21)
estado()

#Ventana de la Aplicacion y ajustes
def goApp(n, app1Screen, app2Screen): #funcion que llama la ventana apps
    main.withdraw()
    mainApp = Toplevel()
    mainApp.minsize(xsize-300, ysize)
    mainApp.resizable(width=NO, height=NO)
    mainApp.config(bg='white')
    
    canvasMain = Canvas(mainApp, width=xsize, height = ysize, bg=color)
    canvasMain.place(x=0, y=0)
    fondoLabel = Label(canvasMain, image = fondo)
    fondoLabel.place(x = -5, y = -5)

#Interfaz ventana Apps
    def idioma6():
        IDseller = int(appsList[n][2])-1
        nombreLabel= Label(canvasMain, text=appsList[n][1], bg='#CCFFFF', font='Helvetica 20 bold')
        nombreLabel.place(x=xpos, y=ypos-80)
        vendedorLabel= Label(canvasMain, text=sellerList[IDseller][1], bg='#002B66', fg='white')
        vendedorLabel.place(x=xpos, y=ypos+550)
        webLabel= Label(canvasMain, text=sellerList[IDseller][2], bg='#002B66', fg='white')
        webLabel.place(x=xpos+200, y=ypos+550)
        imagenLabel=Label(canvasMain, image=app1Screen,bd=0)
        imagenLabel.place(x=xpos+20, y=ypos)
        imagen2Label=Label(canvasMain, image=app2Screen, bd=0)
        imagen2Label.place(x=xpos+350, y=ypos)
        descargas1Label=Label(canvasMain, text=idiomaList[38][Idioma], font='Helvetica 10', bg='#CCFFFF')
        descargas1Label.place(x=xpos, y=ypos+300)
        descargas1Ll=Label(canvasMain, text=appsList[n][9], font='Helvetica 10', bg='#CCFFFF')
        descargas1Ll.place(x=xpos+200, y=ypos+300)
        descargas2Label=Label(canvasMain, text=idiomaList[39][Idioma], font='Helvetica 10', width=21, bg='#CCFFFF')
        descargas2Label.place(x=xpos, y=ypos+330)
        descargas2Ll=Label(canvasMain, text=appsList[n][8], font='Helvetica 10', bg='#CCFFFF')
        descargas2Ll.place(x=xpos+200, y=ypos+330)
        descriptionLabel=Label(canvasMain, text=appsList[n][7], font='Helvetica 12', justify=LEFT,wraplength = 400, bg='#005599', fg='white')
        descriptionLabel.place(x=xpos, y=ypos+370)
        comprarLabel= Label(canvasMain, text=appsList[n][4], bg='#CCFFFF',font='Helvetica 16')
        comprarLabel.place(x=xpos+100, y=ypos+200)
        categoryLabel1=Label(canvasMain, text=appsList[n][10], font='Helvetica 12', bg='#CCFFFF')
        categoryLabel1.place(x=xpos+520, y=ypos+205)
        categoryLabel2=Label(canvasMain, text=idiomaList[53][Idioma], font='Helvetica 15', bg='#CCFFFF', width=8)
        categoryLabel2.place(x=xpos+420, y=ypos+200)
        
        def downloadApp(): #funcion que revisa si el usuario esta logueado para poder descargar un app
            if Status == 1:
                sobreescribirUsuario()
                sobreescribirApp(n)
                def uninstallApp(): #funcion para desinstalar un app
                    uninstallButton.destroy()
                    installedButton.destroy()
                    updateLabel.destroy()
                def updateApp(): # funcion que llama un cuadro de texto
                    updateLabel.place(x=xpos, y=ypos+235)                  
#Botones de ventana Apps            
                uninstallButton= Button(canvasMain, text=idiomaList[40][Idioma], bg='white', fg='#FF0000', font=typeletter, command=uninstallApp, width=9)
                uninstallButton.place(x=xpos+100, y=ypos+200)
                installedButton= Button(canvasMain, text=idiomaList[41][Idioma], font=typeletter, bg='white', fg='#4FCD51',width=9, height=1, command=updateApp)
                installedButton.place(x=xpos, y=ypos+200)
                updateLabel= Label(canvasMain, text=idiomaList[42][Idioma], bg='#CCFFFF', width=26)
            elif Status == 0:
                mustLog = Label(canvasMain, text=idiomaList[43][Idioma], bg='#E10000',fg='white', font='bold', width=15)
                mustLog.place(x=xpos, y=ypos+235)
                            
        def sobreescribirUsuario(): #funcion que agreaga las descargas al usuario y sobreescribe el archivo txt
                global Possition
                usersList[Possition][5]=str(int(usersList[Possition][5])+1)
                buyer = open('DB/comprador.txt', 'w')
                sobreescribirUsuarioAux(0, len(usersList),buyer)
        def sobreescribirUsuarioAux(n,L,buyer): #auxiliar de la funcion sobreescribirUsuario()
                if n==L:
                        buyer.close()
                else:
                        buyer.write(usersList[n][0])
                        buyer.write(',')
                        buyer.write(usersList[n][1])
                        buyer.write(',')
                        buyer.write(usersList[n][2])
                        buyer.write(',')
                        buyer.write(usersList[n][3])
                        buyer.write(',')
                        buyer.write(usersList[n][4])
                        buyer.write(',')
                        buyer.write(usersList[n][5])
                        buyer.write('\n')
                        sobreescribirUsuarioAux(n+1,L,buyer)

        def sobreescribirApp(n): #funcion que agreaga las descargas al usuario y sobreescribe el archivo txt
            global Possition
            apps = open('DB/apps.txt', 'w')
            if usersList[Possition][4] == 'Costa Rica':
                appsList[n][9]=str(int(appsList[n][9])+1)
            appsList[n][8]=str(int(appsList[n][8])+1)
            sobreescribirAppAux(0, len(appsList),apps)
            
        def sobreescribirAppAux(n,L,apps): #auxiliar de la funcion sobreescribirApp()
                if n==L:
                        apps.close()
                else:
                        apps.write(appsList[n][0])
                        apps.write(';')
                        apps.write(appsList[n][1])
                        apps.write(';')
                        apps.write(appsList[n][2])
                        apps.write(';')
                        apps.write(appsList[n][3])
                        apps.write(';')
                        apps.write(appsList[n][4])
                        apps.write(';')
                        apps.write(appsList[n][5])
                        apps.write(';')
                        apps.write(appsList[n][6])
                        apps.write(';')
                        apps.write(appsList[n][7])
                        apps.write(';')
                        apps.write(appsList[n][8])
                        apps.write(';')
                        apps.write(appsList[n][9])
                        apps.write(';')
                        apps.write(appsList[n][10])
                        apps.write('\n')
                        sobreescribirAppAux(n+1,L,apps)
#Botones de ventana Apps          
        downloadButton= Button(canvasMain, text=idiomaList[44][Idioma], font=typeletter, bg='#20EE23', fg='white', command=downloadApp)
        downloadButton.place(x=xpos, y=ypos+200)
        idiomaButton = Button(canvasMain, text=idiomaList[2][Idioma] ,command=cambiarIdioma, width=7)
        idiomaButton.place(x=800, y=650)
    
    def cambiarIdioma(): #funcion que cambia la global Idioma y actualiza la ventana Apps
        global Idioma
        if Idioma == 1:
                Idioma = 2
        elif Idioma == 2:
                Idioma = 1
        idioma6()
    idioma6()
    
#Funcion que retorna a ventana principal desde Apps
    def returnMain():
        mainApp.destroy()
        main.deiconify()
        idioma1()
        estado()
    returnMain = Button(mainApp, image=circle, command=returnMain)
    returnMain.place(x=10, y=10)

#Motor del buscador
xside = 90 
yside = 50
width=300
height=150
circle = PhotoImage(file='img/button.gif')
fondo2= PhotoImage(file='img/fondo2.gif')

def searchAppsNames(n,L): #funcion que compara lo ingresado en la barra de busqueda con las aplicaciones registradas
        if n == L:
                return []
        elif appsList[n][1].lower().startswith(searchEntry.get().lower()) == True or appsList[n][10].lower().startswith(searchEntry.get().lower()) == True:
                if appsList[n][3] == 'Activo':
                    return [n] + searchAppsNames(n+1,L)
                else:
                    return searchAppsNames(n+1,L)
        else:
                return searchAppsNames(n+1,L)
        
def searchAppsList(): #funcion que coloca los botones de los resulatados encontrados
        canvas = Label(canvasMain, width=1200, height=700, image=fondo)
        canvas.place(x=0, y=90)
        lista = searchAppsNames(0, len(appsList))
        cantidad = len(lista)
        def crear1():
                goApp(lista[0], app1, app1ss)
        def crear2():
                goApp(lista[1], app2, app2ss)
        def crear3():
                goApp(lista[2], app3, app3ss)
        def crear4():
                goApp(lista[3], app4, app4ss)
        def crear5():
                goApp(lista[4], app5, app5ss)
        def crear6():
                goApp(lista[5], app6, app6ss)
        def crear7():
                goApp(lista[6], app7, app7ss)
        def crear8():
                goApp(lista[7], app8, app8ss)
        def crear9():
                goApp(lista[8], app9, app9ss)     
        if cantidad >  0:
                app1 = PhotoImage(file=appsList[lista[0]][5])
                app1ss = PhotoImage(file=appsList[lista[0]][6])
                appButton1 = Button(canvas, image=app1, width=width, height=height, command=crear1,bd=0)
                appButton1.place(x=xside, y=yside)
                if cantidad > 1:
                        app2 = PhotoImage(file=appsList[lista[1]][5])
                        app2ss = PhotoImage(file=appsList[lista[1]][6])
                        appButton2 = Button(canvas, image=app2, width=width, height=height, command=crear2,bd=0)
                        appButton2.place(x=xside, y=yside+175)
                        appButton2.forget()
                        if cantidad > 2:
                                app3 = PhotoImage(file=appsList[lista[2]][5])
                                app3ss = PhotoImage(file=appsList[lista[2]][6])
                                appButton3 = Button(canvas, image=app3, width=width, height=height, command=crear3,bd=0)
                                appButton3.place(x=xside, y=yside+350)
                                if cantidad > 3:
                                        app4 = PhotoImage(file=appsList[lista[3]][5])
                                        app4ss = PhotoImage(file=appsList[lista[3]][6])
                                        appButton4 = Button(canvas, image=app4, width=width, height=height, command=crear4,bd=0)
                                        appButton4.place(x=xside+350, y=yside)
                                        if cantidad > 4:
                                                app5 = PhotoImage(file=appsList[lista[4]][5])
                                                app5ss = PhotoImage(file=appsList[lista[4]][6])
                                                appButton5 = Button(canvas, image=app5, width=width, height=height, command=crear5,bd=0)
                                                appButton5.place(x=xside+350, y=yside+175)
                                                if cantidad > 5:
                                                        app6 = PhotoImage(file=appsList[lista[5]][5])
                                                        app6ss = PhotoImage(file=appsList[lista[5]][6])
                                                        appButton6 = Button(canvas, image=app6, width=width, height=height, command=crear6,bd=0)
                                                        appButton6.place(x=xside+350, y=yside+350)
                                                        if cantidad > 6:
                                                                app7 = PhotoImage(file=appsList[lista[6]][5])
                                                                app7ss = PhotoImage(file=appsList[lista[6]][6])
                                                                appButton7 = Button(canvas, image=app7, width=width, height=height, command=crear7,bd=0)
                                                                appButton7.place(x=xside+700, y=yside)
                                                                if cantidad > 7:
                                                                        app8 = PhotoImage(file=appsList[lista[7]][5])
                                                                        app8ss = PhotoImage(file=appsList[lista[7]][6])
                                                                        appButton8= Button(canvas, image=app8, width=width, height=height, command=crear8,bd=0)
                                                                        appButton8.place(x=xside+700, y=yside+175)
                                                                        if cantidad > 8:
                                                                                app9 = PhotoImage(file=appsList[lista[8]][5])
                                                                                app9ss = PhotoImage(file=appsList[lista[8]][6])
                                                                                appButton9 = Button(canvas, image=app9, width=width, height=height, command=crear9,bd=0)
                                                                                appButton9.place(x=xside+700, y=yside+350)
                                                                                appButton2.forget()
                                                                                appButton9.forget()
                                                                                
searchAppsList()

def cambiarIdioma(): #funcion que cambia la global Idioma y actualiza la ventana
        global Idioma
        if Idioma == 1:
                Idioma = 2
        elif Idioma == 2:
                Idioma = 1
        idioma1()
        estado()
idioma1()



main.mainloop()
