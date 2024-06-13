class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True

    def __str__(self):
        return f'{self.titulo} por {self.autor} ({self.ano})'
    
class Membro:
    def __init__(self, nome, numero_membro):
        self.nome = nome
        self.numero_membro = numero_membro
        self.livros_emprestados = []

    def emprestar_livro(self, livro):
        if livro.disponivel:
            livro.disponivel = False
            self.livros_emprestados.append(livro)
            print(f'{livro.titulo} emprestado para {self.nome}.')
        else:
            print(f'{livro.titulo} não está disponível.')
    
    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            livro.disponivel = True
            self.livros_emprestados.remove(livro)
            print(f'{livro.titulo} devolvido por {self.nome}.')
        else:
            print(f'{self.nome} não tem o livro {livro.titulo}')

    def __str__(self):
        return f'Membro: {self.nome}, Número: {self.numero_membro}'
    
class Biblioteca:
    def __init__(self):
        self.livros = []
        self.membros = []

    def adicionar_livros(self, livro):
        self.livros.append(livro)
        print(f'Livro {livro.titulo} adicionado à biblioteca.')
    
    def remover_livro(self, livro):
        if livro in self.livros:
            self.livros.remove(livro)
            print(f'O livro {livro.titulo} removido da biblioteca')
        else:
            print(f'O livro {livro.titulo} não está na biblioteca')

    def registrar_membro(self, membro):
        self.membros.append(membro)
        print(f'Membro {membro.nome} registrado.')

    def listar_livros(self):
        print('Livros na biblioteca:')
        for livro in self.livros:
            status = 'Disponível' if livro.disponivel else 'Emprestado'
            print(f'{livro} - {status}')

    def listar_membros(self):
        print('Membros registrados:')
        for membro in self.membros:
            print(membro)

# Exemplo de uso
biblioteca = Biblioteca()

# Adicionando livros
livro1 = Livro('1984', 'George Orwell', 1949)
livro2 = Livro('O Senhor dos Anéis', 'J.R.R. Tolkien', 1954)
biblioteca.adicionar_livros(livro1)
biblioteca.adicionar_livros(livro2)

# Registrando membros
membro1 = Membro('Alice', 1)
membro2 = Membro('Bob', 2)
biblioteca.registrar_membro(membro1)
biblioteca.registrar_membro(membro2)

# Emprestando e devolvendo livros
membro1.emprestar_livro(livro1)
membro1.devolver_livro(livro1)
membro2.emprestar_livro(livro2)

# Listando livros e membros
biblioteca.listar_livros()
biblioteca.listar_membros()