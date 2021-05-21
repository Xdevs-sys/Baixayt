import pytube import youtube
import moviepy.editor as mp
import re
import os

# Digite o Link do Video  e o Local Que Deseja Salvar o MP3 #
link = input("Digite o Link do Video  Deseja Baixar:	")
path = input("Digite o Diretório Que Deseja Salvar o Video:	")
yt = youtube(link)

# Começa o Download #
print("Baixando . . . ")
ys = yt.streams.filter(only_audio=true).first().download(path)
print("Download Complete!")

# Converte MP4 para MP3 #
print("Convertendo arquivo. . .")
for file in os.listdir(path):
	if re.search('mp4', file):
		mp4_path = os.path.join(path, file)
		mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3')
		new_file = mp.AudioFileClip(mp4, path)
		new_file.write_audiofile(mp3_path)
		os.remove(mp4_path)
print("Convertido com Sucesso!")


# Baixar MP3 do YouTube #
# Desenvolvido Pela Enormity Hacking #
