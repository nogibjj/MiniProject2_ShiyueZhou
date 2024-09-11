from main import generate_descriptive_statistics, generate_summary_statistics
import pandas as pd


def test_generate_descriptive_statistics():
    """testing out generate_descriptive_statistics function"""
    test_data = pd.DataFrame(
        {
            "column1": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "column2": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        }
    )
    des_stat = generate_descriptive_statistics(test_data)
    # Check if the counts are correct
    assert des_stat["column1"]["count"] == 10
    assert des_stat["column2"]["count"] == 10

    # Check if the mean of columns is correct
    assert des_stat["column1"]["mean"] == 5.5
    assert des_stat["column2"]["mean"] == 55

    # Check if the min is correct
    assert des_stat["column1"]["min"] == 1
    assert des_stat["column2"]["min"] == 10


def test_generate_summary_statistics():
    """testing out generate_summary_statistics function"""
    test_data = pd.DataFrame(
        {
            "column1": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "column2": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        }
    )
    summary_stat = generate_summary_statistics(test_data)
    # Check if the mean of column1 and column2 are correct
    assert summary_stat["mean"]["column1"] == 5.5
    assert summary_stat["mean"]["column2"] == 55.0

    # Check if the median is correct
    assert summary_stat["median"]["column1"] == 5.5
    assert summary_stat["median"]["column2"] == 55.0

    # Check if the standard deviation is correct
    assert summary_stat["std"]["column1"] == test_data["column1"].std()
    assert summary_stat["std"]["column2"] == test_data["column2"].std()


if __name__ == "__main__":
    test_generate_descriptive_statistics()
    test_generate_summary_statistics()
