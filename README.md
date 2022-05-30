
# Thesis-papes

La idea principal es comparar distintos enfoques para construir modelos de recomendación basados en filtros colaborativos e híbridos (es decir,  una combinación entre filtros colaborativos y basados en contenido), explicando ventajas y desventajas de cada enfoque y la arquitectura y funcionamiento de cada modelo.

## Modelos

A continuacion se especifican los modelos a comparar:

 * Memory based CF: Sera el baseline o modelo de referencia, del cual queremos obtener mejores resultados.
     * KNN(User-User/Item-Item/Ensemple) usando distancia coseno y distacia coseno ajustada.
 * Model Based CF: Modelos de filtros colaborativos basados en redes neuronales.
   * Collaborative Filtering
      * Generalized Matrix Factorization (GMF)
        * User/Item embeddings dot product.
        * User/Item embeddings dot product + user/item biases.
      * Neural Network Matrix Factorization: User/Item Embedding + flatten + Full Connected.
      * Deep Factorization Machine.
    * Enfoque Híbrido: Combinando filtros colaborativos(CF) con el enfoque basado en contenido(CB).
        * Enfoque 1: Se genera un embedding de items con los modelos de CF ya definidos y otro embedding de items con alguna varaicion de auto-encoder. Finalmente se genera una lista de recomendaciones para in item promediando las distancias coseno de ambos modelos.
        * Enfoque 2: Item a Enfoque 1, pero se podria usar BERT para generar un embedding a partir del texto de overview y tags de un item/movie.
        * Enfoque 3: Item a Enfoque 1, èrp usando un sequence-to-sequence auto-encoder.
        * Enfoque 4
            * Promedio las distancias coseno, pesado por la cantidad de interacciones actuales del usuario. 
            * De esta forma, los usuario con mas interaciiones recomendaciones mas influenciada por CF que CB y vise versa.
 * Ensample/Staking de modelos.

## Metricas

Para compara todos los modelos se esta utilizando la metrica **Mean Average Precision at k (mAP@k)**. Dada una lista de k items ordenados desc. por ratings predicho para el usuario; esta metrica, permite medir la frecuencia con que la que se encuentram X ratings en las primeras posiciones en una lsita de items recomendados. Por ejemplo: ratings entre 4 y 5.

Otras métricas utilizadas:
* RMSE
* FBetaScore
* Precision@K
* Recall@K
* FBetaScore@K

## Hipótesis

Intentó determinar si modelos basados en deep learning obtienen mejores resultados a modelos que no estan basado en deep learning y cuales son las ventajas y desventajas a la hora de implementar cada enfoque. Los modelos a comparar son distintas implementaciones de filtros colaborativos y modelos hibridos (CB + CF).

## Datos

Para tener los datos necesario para probar los enfoques de filtros colaborativos(CF) y basados en contenido(CB) necesito:
* Calificaciones de los ítems(movies) de los usuarios (CF)
* Features propies de los ítems (CB)

Dado esto, combine los siguientes datasets:

* [MovieLens 25M Dataset](https://grouplens.org/datasets/movielens/25m/): Prácticamente no tiene información de las películas pero si tiene las calificaciones de los usuarios.
* [TMDB Movie Dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset?select=movies_metadata.csv): No tiene calificaciones personalizadas como el dataset anterior pero tiene varios features para las películas que es lo que necesito.


## Referencias

[References](https://github.com/adrianmarino/thesis-paper/tree/master/notebooks/references.ipynb)


## Extras

Dada la demanda de procesamiento que tienen estos modelos estoy implementado todo en [pytorch](https://pytorch.org) para poder usar GPU, ya que [scikit-learn](https://scikit-learn.org/stable/) no lo permite. También estuve trabajando en un modelo de capas para poder pasar como input las variables overview y tags de las películas ([Multi-categorical variable embedding module](https://github.com/adrianmarino/thesis-paper/tree/master/notebooks/weighted_avg_embedding_bag.ipynb)).

## Notebooks

* [Preprocesamiento](https://github.com/adrianmarino/thesis-paper/tree/master/notebooks/data-preprocessing.ipynb)
* [Analisis exploratorio](https://github.com/adrianmarino/thesis-paper/tree/master/notebooks/eda.ipynb)
* Memory based CF
  * [KNN User-User/Item-Item/Ensemple](https://github.com/adrianmarino/thesis-paper/tree/master/notebooks/models_knn.ipynb): Usando distancia coseno y distacia coseno ajustada.
* Model based CF
  * [Generalized Matrix Factorization (GMF)](https://github.com/adrianmarino/thesis-paper/tree/master/notebooks/models_gmf.ipynb): Embedding's + dot product.
  * [Generalized Matrix Factorization (GMF) biased](https://github.com/adrianmarino/thesis-paper/tree/master/notebooks/models_gmf_bias.ipynb): Embedding's + dot product + user/item bias.
  * [Neural Network Matrix Factorization](https://github.com/adrianmarino/thesis-paper/tree/master/notebooks/models_nn_mf.ipynb):  User/Item Embedding + flatten + Full Connected.
  * [Deep Factorization Machine](https://github.com/adrianmarino/thesis-paper/tree/master/notebooks/models_deep_fm.ipynb)
* Enfoque Híbrido
   * Enfoque 1: **Pending**
   * Enfoque 2: **Pending**
   * Enfoque 3: **Pending**
   * Enfoque 4: **Pending**
* [Multi-categorical variable embedding module](https://github.com/adrianmarino/thesis-paper/tree/master/notebooks/weighted_avg_embedding_bag.ipynb)

## Using or based on

* [pytorch-common](https://github.com/adrianmarino/pytorch-common)
* [knn-cf-rec-sys](https://github.com/adrianmarino/knn-cf-rec-sys)
* [deep-fm](https://github.com/adrianmarino/deep-fm)
* [recommendation-system-approaches](https://github.com/adrianmarino/recommendation-system-approaches)

## Requisites

* [anaconda](https://www.anaconda.com/products/individual) / [miniconda](https://docs.conda.io/en/latest/miniconda.html)


## Getting started

**Step 1**: Clone repo.

```bash
$ git clone https://github.com/adrianmarino/thesis-paper.git
$ cd thesis-paper
```

**Step 2**: Create environment.

```bash
$ conda env create -f environment.yml
```

## See notebooks in jupyter lab

**Step 1**: Enable project environment.

```bash
$ conda activate thesis
```

**Step 2**: Under project directory boot jupyter lab.

```bash
$ jupyter lab

Jupyter Notebook 6.1.4 is running at:
http://localhost:8888/?token=45efe99607fa6......
```

**Step 3**: Go to http://localhost:8888.... as indicated in the shell output.

