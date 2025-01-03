<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Perfil de GitHub - Actualización Rápida</title>
  <script>
    // Función para actualizar las imágenes en intervalos rápidos
    function actualizarEstadisticas() {
      // Generamos un timestamp para evitar caché
      const timestamp = new Date().getTime();

      // Actualizamos las URLs de las imágenes con el timestamp
      document.getElementById("estadisticas").src = "https://github-readme-stats-eight-theta.vercel.app/api?username=AlexGRDev&show_icons=true&theme=algolia&include_all_commits=true&count_private=true&timestamp=" + timestamp;
      document.getElementById("lenguajes").src = "https://github-readme-stats-eight-theta.vercel.app/api/top-langs/?username=AlexGRDev&layout=compact&langs_count=6&theme=algolia&timestamp=" + timestamp;
      document.getElementById("contribuciones").src = "https://github-readme-streak-stats.herokuapp.com/?user=AlexGRDev&theme=algolia&timestamp=" + timestamp;
    }

    // Establecer la actualización de las imágenes cada 500 milisegundos
    setInterval(actualizarEstadisticas, 500); // Intervalo de 0.5 segundos
  </script>
</head>
<body>
  <div align="center">
    <h1>¡Hola, soy <a href="https://github.com/AlexGRDev" target="_blank">AlexGRDev</a> 👋</h1>
    <p>Técnico de Sistemas Informáticos</p>
  </div>

  [![GitHub followers](https://img.shields.io/github/followers/AlexGRDev?style=social)](https://github.com/AlexGRDev)

  ## 🚀 Sobre mí

  Soy un **Técnico de Sistemas Informáticos** apasionado por la **Ciberseguridad**, con experiencia en la **Administración de Sistemas Informáticos**.

  - 🖥️ **Tecnologías que domino**: C, Shell, Python
  - 🔒 **Especialización**: Técnico en Sistemas Informáticos
  - 📚 **Formación**:
    - **Técnico en Sistemas Microinformáticos y Redes**: Actualmente - 09/2024
    - **Programming Course - 42 Piscine** (26 días, Shell, C): 10/2024 - 11/2024
    - **Técnico Superior en Administración de Sistemas Informáticos y Redes**: 09/2021 - 06/2024

  ### ⚙️ Mis Estadísticas en GitHub

  <div align="center">
    <table>
      <tr>
        <td style="width: 50%; text-align: center;">
          <img id="estadisticas" src="https://github-readme-stats-eight-theta.vercel.app/api?username=AlexGRDev&show_icons=true&theme=algolia&include_all_commits=true&count_private=true&timestamp=<?=time()?>" style="max-width: 100%; height: auto;" alt="Estadísticas GitHub"/>
        </td>
        <td style="width: 50%; text-align: center;">
          <img id="lenguajes" src="https://github-readme-stats-eight-theta.vercel.app/api/top-langs/?username=AlexGRDev&layout=compact&langs_count=6&theme=algolia&timestamp=<?=time()?>" style="max-width: 100%; height: auto;" alt="Lenguajes principales GitHub"/>
        </td>
      </tr>
    </table>
  </div>

  ### 🧑‍💻 Contribuciones en GitHub

  <p align="center">
    <img id="contribuciones" src="https://github-readme-streak-stats.herokuapp.com/?user=AlexGRDev&theme=algolia&timestamp=<?=time()?>" alt="Contribuciones" style="max-width: 100%; height: auto;" />
  </p>

  ---

  ## Proyectos Destacados

  Aquí tienes algunos de los proyectos en los que he trabajado:

  - **[Proyecto 1 - 42 Barcelona Piscine](https://github.com/AlexGRDev/42Barcelona_CPiscine)**: Este proyecto es parte del curso de **42 Barcelona**, en el que desarrollé habilidades en programación con **C** y **Shell**. Durante este proceso, enfrenté desafíos complejos y trabajé en colaboración con otros estudiantes.  
    **Tecnologías utilizadas**: C, Shell, Linux.
      ![Estado del proyecto](https://img.shields.io/github/last-commit/AlexGRDev/42Barcelona_CPiscine?style=flat-square&color=brightgreen)
      ![Estrellas](https://img.shields.io/github/stars/AlexGRDev/42Barcelona_CPiscine?style=social)
      ![Colaboradores](https://img.shields.io/github/contributors/AlexGRDev/42Barcelona_CPiscine?style=flat-square)
    
  - **[Proyecto 2 - PySafeVault](https://github.com/AlexGRDev/PySafeVault)**: Un gestor de contraseñas en Python que almacena credenciales de forma segura utilizando encriptación AES. Incluye funcionalidades para guardar, consultar y borrar contraseñas con una interfaz en consola fácil de usar.  
    **Tecnologías utilizadas**: Python, AES, Consola.
      ![Estado del proyecto](https://img.shields.io/github/last-commit/AlexGRDev/PySafeVault?style=flat-square&color=brightgreen)
      ![Estrellas](https://img.shields.io/github/stars/AlexGRDev/PySafeVault?style=social)
      ![Colaboradores](https://img.shields.io/github/contributors/AlexGRDev/PySafeVault?style=flat-square)

  ¡Puedes ver más proyectos en mi [repositorio](https://github.com/AlexGRDev) de GitHub!

  ---

  ### 📬 Contáctame

  - 📧 **Email**: [alexgaro2015@gmail.com](mailto:alexgaro2015@gmail.com)
  - 🌐 **LinkedIn**: [AlexGRDev](https://www.linkedin.com/in/alex-garcia-rodriguez-564287208/)

  ---

  ¡Gracias por visitar mi perfil! 😄 ¡Estoy siempre abierto a nuevas oportunidades y colaboraciones!
</body>
</html>
