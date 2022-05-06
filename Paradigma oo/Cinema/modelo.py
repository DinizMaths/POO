class Programa:
  def __init__(self, nome, ano):
    self._nome = nome.title()
    self.ano = ano
    self._likes = 0
  
  def dar_like(self):
    self._likes += 1

  @property
  def likes(self):
    return self._likes

  @property
  def nome(self):
    return self._nome

  @nome.setter
  def nome(self, novo_nome):
    self._nome = novo_nome.title()

  def __str__(self, extra):
    return (f'{ self.nome } ({ self.ano }) \n{ extra } \nLikes: { self.likes }\n')

class Filme(Programa):
  def __init__(self, nome, ano, duracao):
    super().__init__(nome, ano)
    self.duracao = duracao

  def __str__(self):
    return super().__str__(f'Duração: {self.duracao} minutos')

class Serie(Programa):
  def __init__(self, nome, ano, temporadas):
    super().__init__(nome, ano)
    self.temporadas = temporadas

  def __str__(self):
    return super().__str__(f'Temporada(s): {self.temporadas}')

class Playlist:
  def __init__(self, nome, programas):
    self._nome = nome
    self._programas = programas

  def __getitem__(self, item):
    return self._programas[item]

  def __len__(self):
    return len(self._programas)

  @property
  def nome(self):
    return self._nome

  @property
  def listagem(self):
    return self._programas

  @property
  def tamanho(self):
    return len(self._programas)

  @nome.setter
  def nome(self, novo_nome):
    self._nome = novo_nome

  def append(self, item):
    self._programas.append(item)

 