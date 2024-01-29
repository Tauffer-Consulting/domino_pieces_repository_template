from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
import numpy as np
import plotly.graph_objects as go
from pathlib import Path


class ExampleSineWavePiece(BasePiece):

    def piece_function(self, input_data: InputModel):

        self.logger.info("Generating sine wave.")

        # Generate sine wave
        num_samples = int(input_data.duration * input_data.sample_rate)
        time = np.linspace(0, input_data.duration, num_samples)
        sine_wave = np.sin(2 * np.pi * input_data.frequency * time)

        # Generate wave figure
        time = np.linspace(0, input_data.duration, len(sine_wave))
        fig = go.Figure(data=go.Scatter(x=time, y=sine_wave, mode='lines'))
        fig.update_layout(title='Sine Wave', xaxis_title='Time (s)', yaxis_title='Amplitude')

        # Save figure to piece file system
        fig_path = str(Path(self.results_path) / "sine.json")
        fig.write_json(fig_path)

        # Set wave image to be displayed in the results on UI
        self.display_result = {
            'file_type': 'plotly_json',
            'file_path': fig_path
        }

        # Return success message
        return OutputModel(message="Sine wave generated.")
