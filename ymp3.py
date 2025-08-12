import yt_dlp
import os
import sys
from pathlib import Path

def descargar_youtube_mp3(url, carpeta_destino="./descargas"):
    """
    Descarga un video de YouTube y lo convierte a MP3
    
    Args:
        url (str): URL del video de YouTube
        carpeta_destino (str): Carpeta donde guardar el archivo MP3
    """
    
    # Crear carpeta de destino si no existe
    Path(carpeta_destino).mkdir(exist_ok=True)
    
    # Configuración para yt-dlp
    ydl_opts = {
        'format': 'bestaudio/best',  # Mejor calidad de audio disponible
        'outtmpl': f'{carpeta_destino}/%(title)s.%(ext)s',  # Plantilla del nombre
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # Extraer solo el audio
            'preferredcodec': 'mp3',      # Convertir a MP3
            'preferredquality': '192',    # Calidad del MP3 (192 kbps)
        }],
        'postprocessor_args': [
            '-ar', '44100',  # Frecuencia de muestreo
        ],
        'prefer_ffmpeg': True,
        'keepvideo': False,  # No mantener el video original
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Obtener información del video
            print("Obteniendo información del video...")
            info = ydl.extract_info(url, download=False)
            titulo = info.get('title', 'Sin título')
            duracion = info.get('duration', 0)
            
            # Mostrar información
            print(f"Título: {titulo}")
            print(f"Duración: {duracion // 60}:{duracion % 60:02d}")
            print(f"Calidad de audio: {info.get('abr', 'N/A')} kbps")
            
            # Confirmar descarga
            confirmacion = input("\n¿Desea continuar con la descarga? (s/n): ")
            if confirmacion.lower() not in ['s', 'si', 'sí', 'y', 'yes']:
                print("Descarga cancelada.")
                return False
            
            # Descargar y convertir
            print("\nIniciando descarga y conversión...")
            ydl.download([url])
            print(f"✅ Descarga completada: {titulo}")
            return True
            
    except Exception as e:
        print(f"❌ Error durante la descarga: {str(e)}")
        return False

def descargar_playlist_mp3(url_playlist, carpeta_destino="./descargas"):
    """
    Descarga una playlist completa de YouTube a MP3
    
    Args:
        url_playlist (str): URL de la playlist de YouTube
        carpeta_destino (str): Carpeta donde guardar los archivos MP3
    """
    
    Path(carpeta_destino).mkdir(exist_ok=True)
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{carpeta_destino}/%(playlist_index)s - %(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'prefer_ffmpeg': True,
        'keepvideo': False,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Obteniendo información de la playlist...")
            info = ydl.extract_info(url_playlist, download=False)
            
            playlist_title = info.get('title', 'Playlist sin nombre')
            num_videos = len(info.get('entries', []))
            
            print(f"Playlist: {playlist_title}")
            print(f"Número de videos: {num_videos}")
            
            confirmacion = input("\n¿Desea descargar toda la playlist? (s/n): ")
            if confirmacion.lower() not in ['s', 'si', 'sí', 'y', 'yes']:
                print("Descarga cancelada.")
                return False
            
            print("\nDescargando playlist...")
            ydl.download([url_playlist])
            print(f"✅ Playlist completada: {playlist_title}")
            return True
            
    except Exception as e:
        print(f"❌ Error durante la descarga: {str(e)}")
        return False

def main():
    """Función principal con menú interactivo"""
    
    print("🎵 Descargador de YouTube a MP3")
    print("=" * 40)
    
    while True:
        print("\nOpciones:")
        print("1. Descargar un video")
        print("2. Descargar una playlist")
        print("3. Salir")
        
        opcion = input("\nSeleccione una opción (1-3): ").strip()
        
        if opcion == "1":
            url = input("\nIngrese la URL del video de YouTube: ").strip()
            if url:
                carpeta = input("Carpeta de destino (Enter para './descargas'): ").strip()
                carpeta = carpeta if carpeta else "./descargas"
                descargar_youtube_mp3(url, carpeta)
            else:
                print("URL no válida.")
                
        elif opcion == "2":
            url = input("\nIngrese la URL de la playlist de YouTube: ").strip()
            if url:
                carpeta = input("Carpeta de destino (Enter para './descargas'): ").strip()
                carpeta = carpeta if carpeta else "./descargas"
                descargar_playlist_mp3(url, carpeta)
            else:
                print("URL no válida.")
                
        elif opcion == "3":
            print("¡Hasta luego! 👋")
            break
            
        else:
            print("Opción no válida. Seleccione 1, 2 o 3.")

# Función para uso directo
def descarga_rapida(url, carpeta="./descargas"):
    """
    Función simplificada para descarga rápida
    
    Uso:
    descarga_rapida("https://www.youtube.com/watch?v=VIDEO_ID")
    """
    return descargar_youtube_mp3(url, carpeta)

if __name__ == "__main__":
    # Verificar dependencias
    try:
        import yt_dlp
        print("✅ yt-dlp encontrado")
    except ImportError:
        print("❌ Error: yt-dlp no está instalado")
        print("Instálalo con: pip install yt-dlp")
        sys.exit(1)
    
    # Verificar FFmpeg
    import subprocess
    try:
        subprocess.run(['ffmpeg', '-version'], 
                      stdout=subprocess.DEVNULL, 
                      stderr=subprocess.DEVNULL, 
                      check=True)
        print("✅ FFmpeg encontrado")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("⚠️  Advertencia: FFmpeg no encontrado")
        print("   Instálalo desde: https://ffmpeg.org/download.html")
        print("   El programa funcionará pero sin conversión a MP3")
    
    main()
