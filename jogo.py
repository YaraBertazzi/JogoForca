# Hangman Game (Jogo da Forca) 

import random

# Board (tabuleiro)
board = ['''
>>>>>>>>>>Hangman<<<<<<<<<<
+---+
|   |
    |
    |
    |
    |
=========''', '''
+---+
|   |
O   |
    |
    |
    |
=========''', '''
+---+
|   |
O   |
|   |
    |
    |
=========''', '''
 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

	# Método Construtor
	def __init__(self, palavra):
		self.palavra = palavra #palavra
		self.letras_perdidas = [] # letras_perdidas
		self.letras_adivinhadas = [] #letras_adivinhadas
		
	# Método para adivinhar a letra
	def adivinhar(self, letra): #adivinhar   #letters = letra

		#se a letra estiver em (palavra) self.word e a letra não estiver (sido adivinhada) self.letras_adivinhadas:# acrescenta em palavras adininhadas
		if letra in self.palavra and letra not in self.letras_adivinhadas:
			self.letras_adivinhadas.append(letra)

		#ou se letra  não estiver em self.word e letra não estiver em (letras perdidas) self.letras_perdidas: # acrescenta em letras perdidas
		elif letra not in self.palavra and letra not in self.letras_perdidas:
			self.letras_perdidas.append(letra)
		else:
			return False
		return True
		
	# Método para verificar se o jogo terminou
	def carrasco_over(self):
		return self.carrasco_won() or (len(self.letras_perdidas) == 6)
		
	# Método para verificar se o jogador venceu
	def carrasco_won(self):
		# # se '_' não estiver em self.palavra_oculta():
		if '_' not in self.palavra_oculta():
			return True
		return False
		
	# Método para não mostrar a letra no board
	def palavra_oculta(self):
		rtn = ''
		for letra in self.palavra:
			if letra not in self.letras_adivinhadas:
				rtn += '_'
			else:
				rtn += letra
		return rtn
		
	# Método para checar o status do game e imprimir o board na tela
	def print_game_status(self):
		print (board[len(self.letras_perdidas)])
		print ('\nPalavra: ' + self.palavra_oculta())
		print ('\nLetras erradas: ',) 
		for letra in self.letras_perdidas:
			print (letra, )
		print ()
		print ('Letras corretas: ',)
		for letra in self.letras_adivinhadas:
			print (letra, )
		print ()

# Método para ler uma palavra de forma aleatória do banco de palavras
def rand_palavra():
	with open("arquivo.txt", "rt") as f:
		bank = f.readlines()
	return bank[random.randint(0, len(bank))].strip()

# Método Main - Execução do Programa
def main():

	# Objeto
	game = Hangman(rand_palavra())

	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter*
	while not game.carrasco_over():
		game.print_game_status()
		user_input = input('\nDigite uma letra: ')
		game.adivinhar(user_input)

	# Verifica o status do jogo
	game.print_game_status()	

	# De acordo com o status, imprime mensagem na tela para o usuário
	if game.carrasco_won():
		print ('\nParabéns! Você venceu!!')
	else:
		print ('\nGame over! Você perdeu.')
		print ('A palavra era ' + game.palavra)
		
	print ('\nFoi bom jogar com você! Agora vá estudar!\n')



# Executa o programa		
if __name__ == "__main__":
	main()
    
    
    
