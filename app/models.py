from django.db import models
class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")
    def ___str___(self):
        return f"{self.nome}, {self.uf}"
    class Meta: 
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"



class Autor(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Autor")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade do autor")
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

class Editora(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da editora")
    site = models.CharField(max_length=100, verbose_name="Site da editora")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade da editora")
    def __str__(self):
            return self.nome
    class Meta:
        verbose_name = "EDITORA"
        verbose_name_plural = "Editoras"

class Leitor(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Leitor")
    email =models.CharField(max_length=100, verbose_name="Email do Leitor")
    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF do leitor")
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Leitor"
        verbose_name_plural = "Leitores"

class Genero(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Gênero") 
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Gênero"
        verbose_name_plural = "Gêneros" 

class Livro(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do livro")
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE,
verbose_name="Editora do livro")
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE,
verbose_name="Gênero do livro")
    preco = models.IntegerField(verbose_name="Preço do livro")
    data_plub = models.DateField(verbose_name="Data de publicação do livro")
    status = models.BooleanField(verbose_name="Status do livro")

    def __str__(self):
        return f'{self.nome}, {self.editora}, {self.genero}, {self.preco}, {self.data_plub}, {self.status}'
    
    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros" 




 


    

# Create your models here.
