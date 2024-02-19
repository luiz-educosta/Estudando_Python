class Livro(object):

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self):
        return f'O livro {self.titulo} do autor {self.autor} tem {self.paginas}'

    def __str__(self):
        return self.titulo

    def __len__(self):
        return self.paginas


livro1 = Livro('Demian', 'Hermann Hesse', 161)

print(livro1)
print(len(livro1))