 # ¡Bienvenidos a Quiero Algo Dulce! 

<em> Quiero algo dulce es una aplicación pensada para conectar a emprendedoras y emprendedores de Repostería y Pastelería con clientes que deseen contratar sus servicios, de acuerdo a su ubicación geográfica.

Actualmente QAD está en la etapa de desarrollo, las áreas finalizadas de la aplicación son la posibilidad de registrar a un usuario vendedor que accede a cargar sus productos para ofertarlos y la posibilidad de registrar a un usuario comprador para adquirir los mismos. Proximamente se agregarán ubicación geográfica y pasarelas con medios de pago.

Las herramientas utilizadas en el desarrollo son:
##### Estilos y Funcionalidad
- CSS
- Bootstrap https://getbootstrap.com/
- Bootswatch https://bootswatch.com/
- Classy Class-Based Views https://ccbv.co.uk/
- CK Editor https://ckeditor.com/

El proyecto está compuesto por las aplicaciones "My App", que cuenta con los modelos Product, Category, Event y Medida; y "Users", que a su vez tiene sus modelos User, Address, Cart, CartProduct, Order y OrderProduct.

Desde su creación QAD está pensada para ser completamente escalable.

##### Para inicializar el proyecto:
 
- env\Scripts\activate (ingresa al entorno virtual)
- cd QAD
- python manage.py runserver

###### Para ingresar como superusuario:
-Usuario: superuser
-email: super@user.com
-pass: superuser123

###### Para ingresar como usuario visitante:
-Usuario: User1
-pass: prueba1@23

</em>

###### Dependencias requeridas:
asgiref==3.7.2
certifi==2023.7.22
charset-normalizer==3.3.0
Django==4.2.6
django-ckeditor==6.7.0
django-js-asset==2.1.0
idna==3.4
Pillow==10.1.0
requests==2.31.0
sqlparse==0.4.4
tzdata==2023.3
urllib3==2.0.7

### Desarrollado por Solange López



