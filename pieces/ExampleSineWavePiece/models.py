from pydantic import BaseModel, Field


class InputModel(BaseModel):
    """
    Sleep Piece Input Model
    """

    frequency: int = Field(
        description="Frequency of the sine wave in Hz",
        default=5
    )
    duration: int = Field(
        description="Duration of the sine wave signal in seconds",
        default=1
    )
    sample_rate: int = Field(
        description="Sample rate of the sine wave signal.",
        default=1000
    )

class OutputModel(BaseModel):
    """
    Sleep Piece Output Model
    """
    message: str = Field(
        description="Sleep piece executed"
    )
