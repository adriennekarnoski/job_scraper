"""Test JobData class and methods attached."""
import pytest
from job_data import JobData
import pandas as pd


def test_initialization_of_test_environment():
    """Test on initialization the environment is set to test."""
    jd = JobData('test')
    assert jd.environment == 'test'


def test_initialization_of_job_data_has_df():
    """Test on initialization the dataframe is created."""
    jd = JobData('test')
    assert isinstance(jd.df, pd.core.frame.DataFrame)
