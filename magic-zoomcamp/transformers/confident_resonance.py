if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    

    # print('Rows with zero passengers',data['passenger_count'].isin([0]).sum())    

    # data = data[data['passenger_count'] > 0 | data['trip_distance'] > 0]
    # data.columns = (data.columns
    #                 .str.repalace(' ','_')
    #                 .str.lower()
    #                 )
    
    # return data
    data = data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]
    data.columns = (data.columns
                .str.replace(' ','_')
                .str.lower()
                )
    print(data["vendorid"].unique())
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
