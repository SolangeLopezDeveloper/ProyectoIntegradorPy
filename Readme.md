# 🍰 Quiero Algo Dulce — E-commerce Django

![App Preview](./docs/screenshot.png)
> 📸 *Captura de la aplicación corriendo localmente. Imagen en `/docs/screenshot.png`.*

## 🔗 Demo
**[Ver aplicación en vivo](#)** *(proximamente en Railway)*

---

## 📌 Descripción

**Quiero Algo Dulce (QAD)** es una plataforma e-commerce desarrollada como proyecto integrador de cursada, pensada para conectar emprendedoras y emprendedores de repostería y pastelería con clientes según su ubicación geográfica.

Las áreas finalizadas incluyen:
- Registro de **usuario vendedor** para cargar y ofertar productos
- Registro de **usuario comprador** para adquirir productos
- Gestión de carrito y órdenes de compra

Desde su concepción, QAD está pensada para ser completamente escalable. Próximamente: geolocalización y pasarelas de pago.

---

## 🛠️ Tecnologías

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=flat&logo=bootstrap&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)

- **Python / Django 4.2** — backend y ORM
- **Bootstrap + Bootswatch** — estilos y componentes UI
- **CKEditor** — editor de texto enriquecido
- **Pillow** — manejo de imágenes
- **SQLite** — base de datos de desarrollo

---

## 🗂️ Estructura de apps

| App | Modelos |
|-----|---------|
| myapp | Product, Category, Event, Medida |
| users | User, Address, Cart, CartProduct, Order, OrderProduct |

---

## 🚀 Correr localmente

### Requisitos
- Python 3.12
- pip

```bash
# Clonar el repositorio
git clone https://github.com/SolangeLopezDeveloper/ProyectoIntegradorPy.git
cd ProyectoIntegradorPy

# Crear y activar entorno virtual
python -m venv env

# Windows:
env\Scripts\activate
# Mac/Linux:
source env/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Aplicar migraciones
cd QAD
python manage.py migrate

# Iniciar servidor
python manage.py runserver
```

La aplicación estará disponible en `http://localhost:8000/home/`

---

## 👩‍💻 Desarrollado por

**Solange López** — [GitHub](https://github.com/SolangeLopezDeveloper)

> Proyecto integrador de cursada — 2023
