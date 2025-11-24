"""Tests for data validation functions."""

import pytest
import numpy as np
import pandas as pd
from data_validation_check.validator import check_missing_values


class TestCheckMissingValues:
    """Tests for check_missing_values function."""
    
    def test_no_missing_values(self):
        """Test data with no missing values."""
        data = np.array([1, 2, 3, 4, 5])
        result = check_missing_values(data)
        assert result['has_missing'] is False
        assert result['missing_fraction'] == 0.0
        assert result['exceeds_threshold'] is False
    
    def test_with_missing_values(self):
        """Test data with missing values."""
        data = np.array([1, 2, np.nan, 4, 5])
        result = check_missing_values(data, threshold=0.1)
        assert result['has_missing'] is True
        assert result['missing_fraction'] == 0.2
        assert result['exceeds_threshold'] is True
    
    def test_dataframe_input(self):
        """Test with pandas DataFrame input."""
        df = pd.DataFrame({'a': [1, 2, np.nan], 'b': [4, 5, 6]})
        result = check_missing_values(df)
        assert result['has_missing'] is True
        assert result['missing_fraction'] == pytest.approx(1/6)