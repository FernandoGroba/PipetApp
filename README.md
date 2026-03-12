# PipetApp 🐾 

**PipetApp** es una solución SaaS diseñada para dueños de mascotas que buscan simplificar el seguimiento sanitario de sus compañeros. Este proyecto combina una arquitectura robusta en el backend con una interfaz de usuario optimizada (UX/UI), enfocada en la usabilidad y la gestión eficiente de tratamientos.



## 🚀 Características
- **Dashboard Dinámico:** Visualización clara de mascotas registradas mediante tarjetas informativas.
- **Gestión de Mascotas:** Registro completo que incluye nombre, raza, peso y fechas de tratamiento.
- **Lógica de Notificaciones:** Sistema que calcula los días restantes para la próxima aplicación de pipeta o medicamentos.
- **Autenticación:** Sistema de login seguro con manejo de sesiones personalizadas.
- **Diseño Responsive:** Interfaz construida con Tailwind CSS, optimizada para dispositivos móviles y escritorio.

## 🛠️ Stack Tecnológico

| Tecnología | Uso |
| :--- | :--- |
| **Python / Flask** | Lógica de servidor y rutas |
| **MySQL (MariaDB)** | Almacenamiento de datos relacionales |
| **Jinja2** | Renderizado de plantillas dinámicas |
| **Tailwind CSS** | Estilizado y Layout de alta fidelidad |
| **Figma** | Diseño UX/UI y Prototipado |

## 📐 Arquitectura del Proyecto
El proyecto sigue un patrón de diseño organizado para facilitar la escalabilidad:
- `/models`: Lógica de negocio y consultas SQL encapsuladas.
- `/db`: Configuración y puentes de conexión a la base de datos.
- `/templates`: Vistas HTML interactivas.
- `/static`: Recursos visuales y estilos adicionales.



## ⚙️ Instalación Local

1. Clona este repositorio:
   ```bash
   git clone [https://github.com/tu-usuario/pipetapp.git](https://github.com/tu-usuario/pipetapp.git)
