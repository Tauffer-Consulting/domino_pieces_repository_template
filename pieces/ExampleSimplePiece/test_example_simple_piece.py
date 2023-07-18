from domino.testing import piece_dry_run

def test_example_simple_piece():
    input_data = dict(
        distribution_name="gaussian",
        distribution_mean=0.,
        distribution_sd=1.
    )
    output_data = piece_dry_run(
        "ExampleSimplePiece",
        input_data
    )

    assert output_data["message"] is not None
    assert output_data["sample_result"] is not None