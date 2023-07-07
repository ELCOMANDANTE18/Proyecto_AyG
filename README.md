# Autómatas y Gramática | Proyecto final
![imagen](https://github.com/ELCOMANDANTE18/Proyecto_AyG/assets/96461803/a4735d77-0cd8-441c-933a-21f05ba12234)
Este proyecto buscará en el registro de conexiones filtrando por usuario y rango de fechas. Se podrá visualizar una tabla y exportarla en formato Excel.
## Instalación
### Nota previa
Si desea descargar los datos incluidos con el proyecto, instale [Git LFS](https://git-lfs.com/).
Se creará un entorno virtual con las siguientes dependencias: `pandas regex pyqt5 qdarkstyle openpyxl`
1. Clonar el repositorio:
```bash
git clone https://github.com/ELCOMANDANTE18/Proyecto_AyG
```
2. Cambiar al directorio:
```bash
cd Proyecto_AyG/Proyecto
```
3. Iniciar el programa:
```bash
chmod +x iniciar.sh
./iniciar.sh
```
## Modo de uso
1. Ejecutar `iniciar.sh` desde el directorio del archivo. Si es la primera vez que se ejecuta instalará las dependencias; Si hay alguna actualización la comprobará e instalará automáticamente.
```
./iniciar.sh
```
2. Se abrirá una ventana

![imagen](https://github.com/ELCOMANDANTE18/Proyecto_AyG/assets/96461803/b214daf8-7e59-4aed-851f-62bb73b28969)

3. Al presionar "Importar CSV" se abrirá el explorador de archivos para seleccionar el .csv a filtrar. Se ha incluido el archivo `ByteNet.csv` en `Proyecto/Material`

![imagen](https://github.com/ELCOMANDANTE18/Proyecto_AyG/assets/96461803/a81306e3-89bf-4adf-a6a5-53764ee96328)

4. Se mostrará la lista de usuarios. Puede elegir el que desea buscar o escribirlo manualmente. En los otros recuadros se debe ingresar el rango de fechas deseado en formato AAAA-MM-DD

![imagen](https://github.com/ELCOMANDANTE18/Proyecto_AyG/assets/96461803/4cf3b462-5fea-4089-9e35-71142049f037)

5. Al presionar `Buscar`, se mostrará una vista previa de los datos filtrados

![imagen](https://github.com/ELCOMANDANTE18/Proyecto_AyG/assets/96461803/82dedcec-dfdf-4a33-8c2a-ad69886ac531)

6. El resultado se puede `Exportar a Excel`

![imagen](https://github.com/ELCOMANDANTE18/Proyecto_AyG/assets/96461803/a36010dc-2843-4085-bbdc-eaf5aa553154)

## Notas
El programa filtra automáticamente las filas con valores corruptos, nulos o incorrectos.
## Desarrolladores
<table>
  <tr>
    <td colspan="3">
      <!-- Víctor Benjamín Giménez -->
      <div align="justify">
        <!-- Profile -->
        <p align="center">
          <samp>
            <b>
              <br>
              <img src="https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/90203317?v=latest&h=128&w=128&fit=cover&mask=circle&maxage=7d">
            </b>
            <br>
            <img src="https://readme-typing-svg.herokuapp.com/?font=Iosevka&duration=3000&pause=1000&color=FFFFFF&center=true&background=00000080&width=435&lines=Victor+Benjam%C3%ADn+Gim%C3%A9nez;Legajo%3A+61174;vb.gimenez%40alumno.um.edu.ar">
          </samp>
        </p>
      </div>
    </td>
    <td colspan="3">
      <!-- Adriano Gabriel Tisera Aguilera -->
      <div align="justify">
        <!-- Profile -->
        <p align="center">
          <samp>
            <b>
              <br>
              <img src="https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/96461803?v=latest&h=128&w=128&fit=cover&mask=circle&maxage=1s">
            </b>
            <br>
            <img src="https://readme-typing-svg.herokuapp.com/?font=Iosevka&duration=3000&pause=1000&color=FFFFFF&center=true&background=00000080&width=435&lines=Adriano+Gabriel+Tisera+Aguilera;Legajo%3A+59059;ag.tisera%40alumno.um.edu.ar">
            <br>
            <b>
            </b>
          </samp>
        </p>
      </div>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <!-- Facundo Gabriel Mala Palleres -->
      <div align="justify">
        <!-- Profile -->
        <p align="center">
          <samp>
            <b>
              <br>
              <img src="https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/102122973?v=latest&h=128&w=128&fit=cover&mask=circle&maxage=7d">
            </b>
            <br>
            <img src="https://readme-typing-svg.herokuapp.com/?font=Iosevka&duration=3000&pause=1000&color=FFFFFF&center=true&background=00000080&width=435&lines=Facundo+Gabriel+Mala+Palleres;Legajo%3A+61244;f.mala%40alumno.um.edu.ar">
            <br>
            <b>
            </b>
          </samp>
        </p>
      </div>
    </td>
    <td colspan="2">
      <!-- Matías Agustín Pérez -->
      <div align="justify">
        <!-- Profile -->
        <p align="center">
          <samp>
            <b>
              <br>
              <img src="https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/90203616?v=latest&h=128&w=128&fit=cover&mask=circle&maxage=7d">
            </b>
            <br>
            <img src="https://readme-typing-svg.herokuapp.com/?font=Iosevka&duration=3000&pause=1000&color=FFFFFF&center=true&background=00000080&width=435&lines=Matías+Agustín+Pérez;Legajo%3A+61218;maag.perez%40alumno.um.edu.ar">
            <br>
            <b>
            </b>
          </samp>
        </p>
      </div>
    </td>
    <td colspan="2">
      <!-- Anna Clara Páez Rocha -->
      <div align="justify">
        <!-- Profile -->
        <p align="center">
          <samp>
            <b>
              <br>
              <img src="https://images.weserv.nl/?url=https://avatars.githubusercontent.com/u/102602385?v=latest&h=128&w=128&fit=cover&mask=circle&maxage=7d">
            </b>
            <br>
            <img src="https://readme-typing-svg.herokuapp.com/?font=Iosevka&duration=3000&pause=1000&color=FFFFFF&center=true&background=00000080&width=435&lines=Anna+Clara+Páez+Rocha;Legajo%3A+61164;ac.paez%40alumno.um.edu.ar">
            <br>
            <b>
            </b>
          </samp>
        </p>
      </div>
    </td>
  </tr>
</table>

