from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
from time import sleep


class ExampleSleepPiece(BasePiece):

    def piece_function(self, input_data: InputModel):

        self.logger.info(f"Sleeping for {input_data.sleep_time} seconds")
        sleep(input_data.sleep_time)
        message = f"Sleep piece executed successfully for {input_data.sleep_time} seconds"
        self.logger.info(message)

        # Return output
        return OutputModel(
            message=message,
        )
