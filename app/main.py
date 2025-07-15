from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy import select
from sqlalchemy.orm import Session

from app import models
from app import schemas
from app import utils
from app.database import SessionLocal, engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/shorten', response_model=schemas.URLResponse)
def create_short_url(request: schemas.URLRequest, db: Session = Depends(get_db)):
    # Collision check
    while True:
        short_code = utils.generate_code()
        statement = select(models.URL).where(models.URL.short_code == short_code)
        if db.execute(statement).scalar_one_or_none() is None:
            break

    url = models.URL(original_url=str(request.url), short_code=short_code)
    db.add(url)
    db.commit()

    short_url = f'http://localhost:8000/{short_code}'
    return schemas.URLResponse(short_url=short_url)


@app.get('/{code}')
def redirect_to_url(code: str, db: Session = Depends(get_db)):
    statement = select(models.URL).where(models.URL.short_code == code)
    result = db.execute(statement).scalar_one_or_none()
    if result is None:
        raise HTTPException(status_code=404, detail='URL not found')
    return RedirectResponse(result.original_url)
