# 🎵 Descargador de YouTube a MP3

Un script en Python potente y fácil de usar para descargar videos de YouTube y convertirlos a formato MP3 de alta calidad. Optimizado especialmente para videos de larga duración.

## ✨ Características

- 🚀 **Rápido y eficiente**: Utiliza `yt-dlp` (sucesor mejorado de youtube-dl)
- 🎧 **Alta calidad de audio**: Descarga a 192 kbps con frecuencia de 44.1 kHz
- 📁 **Organización automática**: Crea carpetas de destino automáticamente
- 📋 **Soporte para playlists**: Descarga playlists completas
- ⏱️ **Optimizado para videos largos**: Maneja eficientemente contenido de cualquier duración
- 🛡️ **Manejo robusto de errores**: Recuperación automática de errores comunes
- 💻 **Interfaz amigable**: Menú interactivo y confirmaciones de seguridad
- 📊 **Información detallada**: Muestra título, duración y calidad antes de descargar

## 📋 Requisitos

### Software requerido:
- **Python 3.7+**
- **FFmpeg** (para conversión de audio)

### Librerías de Python:
- `yt-dlp`
- `pathlib` (incluida en Python 3.4+)

## 🚀 Instalación

### 1. Clonar o descargar el código
```bash
# Si tienes git instalado
git clone [tu-repositorio]

# O simplemente descarga el archivo descargador_youtube.py
```

### 2. Instalar dependencias de Python
```bash
pip install yt-dlp
```

### 3. Instalar FFmpeg

#### Windows:
1. Descargar desde [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
2. Extraer el archivo y agregar la carpeta `bin` al PATH del sistema

#### macOS:
```bash
# Con Homebrew
brew install ffmpeg

# Con MacPorts
sudo port install ffmpeg
```

#### Ubuntu/Debian:
```bash
sudo apt update
sudo apt install ffmpeg
```

#### CentOS/RHEL/Fedora:
```bash
# CentOS/RHEL
sudo yum install ffmpeg

# Fedora
sudo dnf install ffmpeg
```

## 🎯 Uso

### Método 1: Menú interactivo
```bash
python descargador_youtube.py
```

Sigue las instrucciones en pantalla:
1. Selecciona opción (1: video individual, 2: playlist)
2. Ingresa la URL
3. Especifica carpeta de destino (opcional)
4. Confirma la descarga

### Método 2: Uso programático
```python
from descargador_youtube import descarga_rapida, descargar_youtube_mp3, descargar_playlist_mp3

# Descarga rápida (carpeta por defecto)
descarga_rapida("https://www.youtube.com/watch?v=VIDEO_ID")

# Descarga con opciones personalizadas
descargar_youtube_mp3(
    url="https://www.youtube.com/watch?v=VIDEO_ID",
    carpeta_destino="./mi_musica"
)

# Descarga de playlist completa
descargar_playlist_mp3(
    url_playlist="https://www.youtube.com/playlist?list=PLAYLIST_ID",
    carpeta_destino="./playlists"
)
```

### Método 3: Línea de comandos directa
```bash
# Usando yt-dlp directamente
yt-dlp -x --audio-format mp3 --audio-quality 192K "URL_DEL_VIDEO"
```

## 📂 Estructura de archivos

```
proyecto/
│
├── descargador_youtube.py    # Script principal
├── README.md                 # Este archivo
└── descargas/               # Carpeta por defecto (se crea automáticamente)
    ├── Video 1.mp3
    ├── Video 2.mp3
    └── ...
```

## 🔧 Configuración avanzada

### Personalizar calidad de audio
Edita la variable `preferredquality` en el código:
```python
'preferredquality': '320',  # Para máxima calidad (320 kbps)
'preferredquality': '128',  # Para archivos más pequeños (128 kbps)
```

### Cambiar formato de salida
Modifica el `preferredcodec`:
```python
'preferredcodec': 'aac',    # Para formato AAC
'preferredcodec': 'flac',   # Para formato sin pérdida FLAC
'preferredcodec': 'wav',    # Para formato WAV sin comprimir
```

### Personalizar nombres de archivo
Ajusta el `outtmpl`:
```python
'outtmpl': f'{carpeta_destino}/%(uploader)s - %(title)s.%(ext)s',     # Incluir canal
'outtmpl': f'{carpeta_destino}/%(upload_date)s - %(title)s.%(ext)s',  # Incluir fecha
```

## 📝 Ejemplos de uso

### Ejemplo 1: Video individual
```python
# Descargar un podcast largo
descarga_rapida("https://www.youtube.com/watch?v=pB8Rw147Xwg")
```

### Ejemplo 2: Playlist de música
```python
# Descargar álbum completo
descargar_playlist_mp3(
    "https://www.youtube.com/playlist?list=PLrAl6rYGs4IvGFLfQqJakVP5tb85XbFNr",
    "./album_favorito"
)
```

### Ejemplo 3: Organización por carpetas
```python
# Organizar por género o artista
descargar_youtube_mp3(
    "https://www.youtube.com/watch?v=VIDEO_ID",
    "./musica/rock/banda_favorita"
)
```

## ⚠️ Limitaciones y consideraciones

### Limitaciones técnicas:
- **Dependiente de FFmpeg**: Necesario para conversión de audio
- **Velocidad de descarga**: Limitada por la velocidad de internet y servidores de YouTube
- **Formatos disponibles**: Depende de lo que YouTube ofrezca para cada video

### Consideraciones legales:
- ✅ **Uso personal**: Contenido de tu propiedad o con permisos
- ✅ **Contenido libre**: Creative Commons, dominio público
- ❌ **Contenido protegido**: Música comercial sin permisos
- ❌ **Redistribución**: No redistribuir contenido sin autorización

### Mejores prácticas:
- Verificar que tienes derecho a descargar el contenido
- Usar solo para respaldo personal o uso educativo
- Respetar los términos de servicio de YouTube
- No sobrecargar los servidores con descargas masivas

## 🐛 Solución de problemas

### Error: "yt-dlp not found"
```bash
# Reinstalar yt-dlp
pip uninstall yt-dlp
pip install yt-dlp
```

### Error: "FFmpeg not found"
- Verificar que FFmpeg está instalado y en el PATH
- En Windows, reiniciar la terminal después de instalar

### Error: "Unable to download video"
- Verificar que la URL es correcta
- Algunos videos pueden tener restricciones geográficas
- Videos privados o eliminados no se pueden descargar

### Archivos con nombres extraños
```python
# Usar caracteres seguros en nombres de archivo
'outtmpl': f'{carpeta_destino}/%(title).100s.%(ext)s'  # Limitar longitud
```

### Videos muy largos se cortan
- Verificar espacio en disco disponible
- Algunos videos pueden tener limitaciones de duración

## 🔄 Actualizaciones

### Mantener yt-dlp actualizado
```bash
pip install --upgrade yt-dlp
```

### Verificar versión
```bash
yt-dlp --version
```

## 🤝 Contribuciones

Las contribuciones son bienvenidas:

1. Fork del proyecto
2. Crear una rama para tu feature (`git checkout -b feature/nueva-caracteristica`)
3. Commit de tus cambios (`git commit -m 'Agregar nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Abrir un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 🆘 Soporte

Si encuentras problemas:

1. **Revisa la sección de solución de problemas**
2. **Verifica que todas las dependencias están instaladas**
3. **Asegúrate de tener la versión más reciente de yt-dlp**
4. **Crea un issue** con detalles del error y tu sistema operativo

## 📚 Recursos adicionales

- [Documentación de yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [Guía de instalación de FFmpeg](https://ffmpeg.org/download.html)
- [Términos de servicio de YouTube](https://www.youtube.com/static?template=terms)

---

**⭐ Si este proyecto te fue útil, no olvides darle una estrella!**
