from pydantic import BaseModel, Field
from typing import Annotated

class IrisInput(BaseModel):
    sepal_length: Annotated[float, Field(..., description="Length of the sepal in cm", example=5.1, gt=0, lt=10)]
    sepal_width:  Annotated[float, Field(..., description="Width of the sepal in cm", example=3.5, gt=0, lt=10)]
    petal_length: Annotated[float, Field(..., description="Length of the petal in cm", example=1.4, gt=0, lt=10)]
    petal_width:  Annotated[float, Field(..., description="Width of the petal in cm", example=0.2, gt=0, lt=10)]
