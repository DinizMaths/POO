from modelo import *

def dar_likes(programa, numero_de_likes):
  for i in range(numero_de_likes):
    programa.dar_like()

vingadores = Filme('vingadores - Guerra Infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('Todo mundo em pânico', 1999, 100)
demolidor = Serie('demolidor', 2016, 2)

dar_likes(vingadores, 35)
dar_likes(atlanta, 7)
dar_likes(tmep, 12)
dar_likes(demolidor, 20)


filmes_e_series = [vingadores, atlanta, demolidor]

playlist_fim_de_semana = Playlist('Fim de Semana', filmes_e_series)

playlist_fim_de_semana.append(tmep)

for programa in playlist_fim_de_semana:
  print(programa)

print(f'Tamanho da Playlist "{ playlist_fim_de_semana.nome }": { len(playlist_fim_de_semana) }\n')

print(f'A Série { demolidor.nome } está na Playlist "{ playlist_fim_de_semana.nome }"?', end=' ')
print(f'{ "Sim" if (demolidor in playlist_fim_de_semana) else "Não" }')
