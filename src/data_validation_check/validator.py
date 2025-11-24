"""Test validation functions for data."""

import numpy as np
import pandas as pd
from typing import Union, List


def check_missing_values(data: Union[np.ndarray, pd.DataFrame], 
                        threshold: float = 0.1) -> dict:
    """
    Check for missing values in scientific data.
    
    Parameters
    ----------
    data : numpy.ndarray or pandas.DataFrame
        The data to check for missing values
    threshold : float, optional
        Maximum allowed fraction of missing values (default: 0.1)
        
    Returns
    -------
    dict
        Dictionary containing:
        - 'has_missing': bool indicating if missing values exist
        - 'missing_fraction': fraction of missing values
        - 'exceeds_threshold': bool indicating if threshold is exceeded
        
    Examples
    --------
    >>> import numpy as np
    >>> data = np.array([1, 2, np.nan, 4, 5])
    >>> result = check_missing_values(data, threshold=0.2)
    >>> result['has_missing']
    True
    """
    if isinstance(data, pd.DataFrame):
        total_values = data.size
        missing_count = data.isna().sum().sum()
    elif isinstance(data, np.ndarray):
        total_values = data.size
        missing_count = np.isnan(data).sum()
    else:
        raise TypeError("Data must be numpy array or pandas DataFrame")
    
    missing_fraction = missing_count / total_values if total_values > 0 else 0
    
    return {
        'has_missing': bool(missing_count > 0),
        'missing_fraction': float(missing_fraction),
        'exceeds_threshold': bool(missing_fraction > threshold)
    }


