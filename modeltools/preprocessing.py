"""
Este módulo contiene helpers para el preprocesamiento de datos
"""
import numpy as np

def dummy(a, b):
    """
    Sums two numbers

    :param a: number
    :param b: number
    :returns: total sum
    """
    return a + b

def get_numerical_features(df):
    """
    get_numerical_features devuelve una lista con el nomabre de las columnas que contienen datos de tipo numérico
    
    :param df: DataDrame
    :type df: DataFrame
    :returns: A list of column names of number datatypes 
    :rtype: List[str]

    >>> from modeltools.preprocessing import get_numerical_features
    >>> import pandas as pd
    >>> df = pd.DataFrame({"a": [1]})
    >>> get_numerical_features(df)
    ['a']
    """
    return list(df.select_dtypes(include=[np.number]).columns)