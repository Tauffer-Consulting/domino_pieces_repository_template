from domino.base_piece import BasePiece
from .models import InputModel, OutputModel, SecretsModel
import os


class ExampleComplexPiece(BasePiece):
    """
    This Piece serves as a more complex example, using Dockerfile as dependency, from where you can start writing your own Piece.
    Remember to also change all other required files accordingly:
    - piece.py (this file)
    - models.py
    - metadata.json
    - requirements.txt or Dockerfile if needed
    """
    
    def piece_function(self, input_data: InputModel, secrets_data: SecretsModel):

        # Input arguments are retrieved from the Input model object
        arg1 = input_data.arg1

        # If this Piece needs to use a Secret value, it can retrieve it from Secrets Model object using secrets_data argument
        piece_secret = secrets_data.EXAMPLE_OPERATOR_SECRET_2

        # Basic logging is already implemented in the BasePiece class
        self.logger.info("Starting piece process...")

        # Here we add the Piece function logic
        message = ""
        result = ""

        # Finally, results should return as an Output model
        return OutputModel(
            message=message,
            result=result
        )