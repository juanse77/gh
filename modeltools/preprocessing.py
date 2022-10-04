"""
Este módulo contiene helpers para el preprocesamiento de datos
"""
import numpy as np


def get_numerical_features(df):
    """
    get_numerical_features devuelve una lista con el nomabre de las columnas que contienen datos de tipo numérico
    
    Parameters
    ----------
    df: dataframe

    Examples
    --------

    >>> from modeltools.preprocessing import get_numerical_features
    >>> import pandas as pd
    >>> df = pd.DataFrame({"a": [1]})
    >>> get_numerical_features(df)
    ['a']

    """
    return list(df.select_dtypes(include=[np.number]).columns)