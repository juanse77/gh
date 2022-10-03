import pandas as pd
from modeltools.preprocessing import get_numerical_features

def test_get_numerical_features_simple():
    """
    En este test vamos a probar que distingue los campos numéricos entre cadenas de texto y campos de otro tipo
    """

    df = pd.DataFrame({
        "numerica": [5],
        "categorica": ["rojo"]
    })

    # assert es "como un if" que nos falla si la condición es falsa
    assert get_numerical_features(df) == ["numerica"]

def test_get_numerical_features_empty():
    """Este test comprueba que se devuelve una lista vacía si no hay ninguna variable num"""
    df = pd.DataFrame({
        "categorica1": ["azul"],
        "categorica2": ["rojo"]
    })

    assert get_numerical_features(df) == []


def test_get_numerical_features_zero_columns():
    """Este test comprueba que se devuelve una lista vacía si el dataframe no tiene ninguna columna."""

    assert get_numerical_features(pd.DataFrame()) == []


def test_get_numerical_features_zero_rows():
    """Este test comprueba que se devuelve una con una variable si el DF
    tiene una variable numérica pero NINGUNA FILA."""

    assert get_numerical_features(pd.DataFrame({'numerica': pd.Series(dtype=int)}) ) == ["numerica"]


def test_get_numerical_features_complex():
    """
    Este test comprueba que funciona correctamente con números decimales
    """
    
    df = pd.DataFrame({
        "numerica": [5],
        "numerica2": [5.2]
    })

    # assert es "como un if" que nos falla si la condición es falsa
    assert get_numerical_features(df) == ["numerica", "numerica2"]

def test_get_numerical_features_columns_withoutname():
    """
    Este test comprueba que funciona correctamente cuando hay columnas numéricas sin nombre (Columnas con números/posiciones)
    """
    df = pd.DataFrame([
        [1, "a"]
    ])

    assert get_numerical_features(df) == [0]


def test_get_numerical_features_complex():
    """
    Este test comprueba que se devuelve una lista con los valores de campos complejos
    """
    df = pd.DataFrame({
        "complejo": [complex(3, 5)]
    })

    assert get_numerical_features(df) == ["complejo"]