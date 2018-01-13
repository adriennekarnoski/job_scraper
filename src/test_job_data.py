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


def test_initialization_has_empty_date():
    """Test date property is set to none."""
    jd = JobData('test')
    assert jd.date is None


def test_initialization_has_empty_state_dict():
    """Test state dict property is set to none."""
    jd = JobData('test')
    assert jd.state_dict is None


def test_initialization_has_empty_time_dict():
    """Test time dict property is set to none."""
    jd = JobData('test')
    assert jd.time_dict is None


def test_initialization_has_empty_top_ten():
    """Test top ten dict property is set to none."""
    jd = JobData('test')
    assert jd.top_ten is None


def test_count_states_method_returns_dict():
    """Test the count states method returns a dictionary."""
    jd = JobData('test')
    assert isinstance(jd.count_states(), dict)


def test_count_state_dict_property_is_updated():
    """Test the count states method updates the state dict property."""
    jd = JobData('test')
    states = jd.count_states()
    assert jd.state_dict == states


def test_count_days_method_returns_dict():
    """Test the count days method returns a dictionary."""
    jd = JobData('test')
    assert isinstance(jd.count_days(), dict)


def test_count_days_dict_property_is_updated():
    """Test the count days method updates the time dict property."""
    jd = JobData('test')
    days = jd.count_days()
    assert jd.time_dict == days


def test_days_dict_zero_key_has_values():
    """Test that posts on day of scrape are listed as zero."""
    jd = JobData('test')
    days = jd.count_days()
    assert jd.time_dict['0'] != 0


def test_count_tags_method_returns_dict():
    """Test the count tags method returns a dictionary."""
    jd = JobData('test')
    assert isinstance(jd.count_tags(), dict)


def test_count_tags_dict_property_is_updated():
    """Test the count tags method updates the time dict property."""
    jd = JobData('test')
    tags = jd.count_tags()
    assert jd.top_ten == tags


def test_chart_states_returns_list():
    """Test the chart state function returns list."""
    jd = JobData('test')
    jd.count_states()
    assert isinstance(jd.chart_states(), list)


def test_chart_states_list_lengths():
    """Test chart state function lists are same length."""
    jd = JobData('test')
    jd.count_states()
    one, two = jd.chart_states()[0], jd.chart_states()[1]
    assert len(one) == len(two)


def test_chart_states_raises_error():
    """Test chart state raises error if state dict not available."""
    jd = JobData('test')
    with pytest.raises(ValueError):
        jd.chart_states()


def test_hour_removed_from_time():
    """Test hour is removed from times that have h."""
    jd = JobData('test')
    state_dict = jd.count_states()
    key_list = list(state_dict.values())
    assert 'h' not in key_list


def test_day_removed_from_time():
    """Test day is removed from times that have d."""
    jd = JobData('test')
    state_dict = jd.count_states()
    key_list = list(state_dict.values())
    assert 'd' not in key_list


def test_week_removed_from_time():
    """Test week is removed from times that have w."""
    jd = JobData('test')
    state_dict = jd.count_states()
    key_list = list(state_dict.values())
    assert 'w' not in key_list


def test_chart_days_returns_list():
    """Test the chart days function returns list."""
    jd = JobData('test')
    jd.count_days()
    assert isinstance(jd.chart_days(), list)


def test_chart_days_raises_error():
    """Test chart days raises error if time dict not available."""
    jd = JobData('test')
    with pytest.raises(ValueError):
        jd.chart_days()


def test_chart_tags_returns_list():
    """Test the chart tags function returns list."""
    jd = JobData('test')
    jd.count_tags()
    assert isinstance(jd.chart_tags(), list)


def test_chart_tags_raises_error():
    """Test chart tags raises error if time dict not available."""
    jd = JobData('test')
    with pytest.raises(ValueError):
        jd.chart_tags()