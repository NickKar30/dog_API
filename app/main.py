# generated by fastapi-codegen:
#   filename:  clinic.yaml
#   timestamp: 2023-11-02T15:56:47+00:00

from __future__ import annotations

from typing import List, Optional, Union

from fastapi import FastAPI

from .models import Dog, DogType, HTTPValidationError, Timestamp

app = FastAPI(
    title='FastAPI',
    version='0.1.0',
)


@app.get('/#-datamodel-code-generator-#-root-#-special-#', response_model=Any)
def root__get() -> Any:
    """
    Root
    """
    pass


@app.get(
    '/dog', response_model=List[Dog], responses={'422': {'model': HTTPValidationError}}
)
def get_dogs_dog_get(
    kind: Optional[DogType] = None,
) -> Union[List[Dog], HTTPValidationError]:
    """
    Get Dogs
    """
    pass


@app.post('/dog', response_model=Dog, responses={'422': {'model': HTTPValidationError}})
def create_dog_dog_post(body: Dog) -> Union[Dog, HTTPValidationError]:
    """
    Create Dog
    """
    pass


@app.get(
    '/dog/{pk}', response_model=Dog, responses={'422': {'model': HTTPValidationError}}
)
def get_dog_by_pk_dog__pk__get(pk: int) -> Union[Dog, HTTPValidationError]:
    """
    Get Dog By Pk
    """
    pass


@app.patch(
    '/dog/{pk}', response_model=Dog, responses={'422': {'model': HTTPValidationError}}
)
def update_dog_dog__pk__patch(
    pk: int, body: Dog = ...
) -> Union[Dog, HTTPValidationError]:
    """
    Update Dog
    """
    pass


@app.post('/post', response_model=Timestamp)
def get_post_post_post() -> Timestamp:
    """
    Get Post
    """
    pass