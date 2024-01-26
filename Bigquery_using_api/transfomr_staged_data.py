if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    print('Rows with zero passengers',data['passenger_count'].isin([0]).sum())    

    data = data[data['passenger_count'] > 0 or data['trip_distance'] > 0]
    data.columns = (data.columns
                    .str.repalace(' ','_')
                    .str.lower()
                    )
    
    return data


@test
def test_output(output, *args) -> None:
    
    assert output['VendorID'].isin([1,2]).all(), "VendorID should be one of the existing values."
    assert (output['passenger_count'] > 0).all(), "Passenger count should be greater than 0."
    assert (output['trip_distance'] > 0).all(), "Trip distance should be greater than 0."