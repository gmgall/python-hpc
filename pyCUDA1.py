#Importa o driver do cuda - Contem as rotinas de manipulacao de memoria e funcoes de comunicacao entre CPU e GPU
import pycuda.driver as cuda

#Autoinicializa a GPU - Quando utilizado desta forma, inicializa apenas a primeira GPU disponivel no sistema
import pycuda.autoinit

#Importa o compilador para a geracao do codigo binario do kernel
from pycuda.compiler import SourceModule

#Importa o modulo numpy
import numpy

#Criacao da matriz a de dimensao 4x4
a = numpy.random.randn(4,4)

#Definicao do tipo de dados do vetor (o default do numpy eh ser double, ou seja, float64)
a = a.astype(numpy.float32)

#Aloca um espaco de memoria de mesmo tamanho da matriz a na memoria da GPU
a_gpu = cuda.mem_alloc(a.nbytes)

#Copia os valores inicializados na matriz a que estah na memoria da CPU  para a matriz a_gpu que estah na memoria da GPU
cuda.memcpy_htod(a_gpu, a)

#Kernel - Funcao que sera executada dentro da GPU
#O kernel é sempre escrito na linguagem CUDA
mod = SourceModule("""
  __global__ void doublify(float *a)
  {
    //Calculo do indice da thread
    int idx = threadIdx.x + threadIdx.y*4;
    //Multiplica o elemento a[idx] por 2 e armazena no mesmo endereco de memoria
    a[idx] *= 2;
  }
  """)

#Define o nome do kernel que sera execuatdo
func = mod.get_function("doublify")

#Chamada do kernel com apenas uma bloco de 4x4 em uma grade de 1x1x1
func(a_gpu, block=(4,4,1))

#Cria uma matriz vazia a_doubled com as mesmas dimensoes de a
a_doubled = numpy.empty_like(a)

#Copia os valores da matriz a_gpu que estah na memoria da GPU para a matriz recem criada a_doubled que estah na memoria da CPU
cuda.memcpy_dtoh(a_doubled, a_gpu)

#Imprime a matriz a_doubled
print(a_doubled)

#Imprime a matriz a
print(a)
