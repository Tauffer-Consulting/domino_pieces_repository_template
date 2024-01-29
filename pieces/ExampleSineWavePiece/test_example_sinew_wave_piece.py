from domino.testing import piece_dry_run

def test_example_sine_wave_piece():
    input_data = dict(
        frequency=5,
        duration=2,
        sample_rate=1000
    )
    output_data = piece_dry_run(
        "ExampleSineWavePiece",
        input_data,
    )

    assert output_data["message"] is not None