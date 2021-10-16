#uso de la API https://pokapi.co

#Puedes consultar como instalar matplotlib en este blog: http://blog.espol.edu.ec/ccpg1001/descargas/matplotlib-graficas-instalar/
#Librerias a utilizar:
import requests
import matplotlib.pyplot as plt#matplotlib es una libreraía para mostrar graficos
import matplotlib.image as img

#pedimos que el usuario introduzca el nombre del pokemon(debe de estar bien escrito)
pokemon = input("introduce un pokemon: ")
#solicitamos el pokemon desde la api, el contatenado de la variable pokemon 
# ayuda a identificarlo en la api
url= "https://pokeapi.co/api/v2/pokemon/" + pokemon

#obtenemos la url
res = requests.get(url)

#preguntamos si este pokemon no se encuentra en la lista
if res.status_code !=200 :
    print("Pokemon no encontrado")
    exit()

#mostramos el sprite(imagen) del pokemon solicitado
imagen = img.imread(res.json()['sprites']['front_default'])
#añadimos un titulo al grafico.
plt.title(res.json()['name'])
imgplot = plt.imshow(imagen)
plt.show()