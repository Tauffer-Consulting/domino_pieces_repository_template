from domino.testing import piece_dry_run

def test_example_simple_piece():
    input_data = dict(
        sleep_time=5
    )
    output_data = piece_dry_run(
        "ExampleSleepPiece",
        input_data,
    )

    assert output_data["message"] is not None