from http import HTTPStatus

from fastapi import APIRouter, HTTPException, Depends
from fastapi_jwt_auth import AuthJWT

from core.config import logger, jwt_settings
from models_backend.models import (
    Bookmark,
    Movie,
    InsertedSuccessModel,
    DeletedCountSuccessModel,
    ObjectsListSuccessModel,
)
from services.bookmarks import Bookmarks
from starlette.requests import Request

from .common import check_auth

COLLECTION_NAME = "bookmarks"
router_bookmarks = APIRouter(prefix=f"/{COLLECTION_NAME}")


@AuthJWT.load_config
def get_config():
    return jwt_settings


@router_bookmarks.post("/add")
async def add_bookmark(bookmark: Bookmark, request: Request, authorize: AuthJWT = Depends()):
    """
    An example request JSON:
    {
    "movie": "803c794c-ddf0-482d-b2c2-6fa92da4c5e2",
    }
    We assume that request headers contain used_uuid, after processing with authentication and middleware.
    Headers:
        ...
        user_uuid: d16b19e7-e116-43b1-a95d-cd5a11e8f1b4
        ...
    """
    user_uuid = (await check_auth(request, authorize)).user_uuid
    try:
        result = await Bookmarks.add(user_uuid, bookmark)
        logger.info("Successfully added %s, user=%s, %s=%s", COLLECTION_NAME, user_uuid, COLLECTION_NAME, bookmark)
        return InsertedSuccessModel(success=True, inserted_id=str(result.inserted_id))
    except Exception as e:
        logger.error(
            "Error adding %s, user=%s, %s=%s, error=%s", COLLECTION_NAME, user_uuid, COLLECTION_NAME, bookmark, e
        )
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail=str(e))


@router_bookmarks.delete("/remove")
async def remove_bookmark(bookmark: Bookmark, request: Request, authorize: AuthJWT = Depends()):
    """
    An example request JSON:
    {
    "movie": "803c794c-ddf0-482d-b2c2-6fa92da4c5e2",
    }
    We assume that request headers contain used_uuid, after processing with authentication and middleware.
    Headers:
        ...
        user_uuid: d16b19e7-e116-43b1-a95d-cd5a11e8f1b4
        ...
    """
    user_uuid = (await check_auth(request, authorize)).user_uuid
    try:
        result = await Bookmarks.remove(user_uuid, bookmark)
        logger.info("Successfully removed %s, user=%s, %s=%s", COLLECTION_NAME, user_uuid, COLLECTION_NAME, bookmark)
        return DeletedCountSuccessModel(success=True, deleted_count=result.deleted_count)
    except Exception as e:
        logger.error(
            "Error removing %s, user=%s, %s=%s, error=%s", COLLECTION_NAME, user_uuid, COLLECTION_NAME, bookmark, e
        )
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail=str(e))


@router_bookmarks.get("/list")
async def list_bookmarks(movie: Movie, request: Request, authorize: AuthJWT = Depends()):
    """
    An example request JSON:
    {
    "id": "803c794c-ddf0-482d-b2c2-6fa92da4c5e2",
    }
    We assume that request headers contain used_uuid, after processing with authentication and middleware.
    Headers:
        ...
        user_uuid: d16b19e7-e116-43b1-a95d-cd5a11e8f1b4
        ...
    + Optional request parameter
        sort: likes_count | average_rate
    """
    user_uuid = (await check_auth(request, authorize)).user_uuid
    try:
        objects_list = await Bookmarks.list(movie, user_uuid)
        logger.info("Successfully listed %s, user=%s, movie=%s", COLLECTION_NAME, user_uuid, movie)
        return ObjectsListSuccessModel(success=True, objects_list=objects_list)
    except HTTPException:
        raise
    except Exception as e:
        logger.error("Error listing %s, user=%s, movie=%s, error=%s", COLLECTION_NAME, user_uuid, movie, e)
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail=str(e))
