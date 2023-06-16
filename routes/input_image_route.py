from fastapi import APIRouter, Body, File, UploadFile, Form
from fastapi.encoders import jsonable_encoder
import fileinput
from utils.gcs_storage import GCStorage
from functions.generate_id import makeId
import os
from models.response import(
    ErrorResponseModel,
    ResponseModel
)

router = APIRouter()

@router.post("/",response_description="post image file")
async def uploadImage(username: str = Form(...), image_1 : UploadFile=File(...), 
                                                 image_2 : UploadFile=File(...),
						 image_3 : UploadFile=File(...),
						 image_4 : UploadFile=File(...),
						 image_5 : UploadFile=File(...)):
    
    unique_filename_1 = makeId() + "-" + image_1.filename
    unique_filename_2 = makeId() + "-" + image_2.filename
    unique_filename_3 = makeId() + "-" + image_3.filename
    unique_filename_4 = makeId() + "-" + image_4.filename
    unique_filename_5 = makeId() + "-" + image_5.filename
    
    
    file_utils_1 = f"utils/{unique_filename_1}"
    with open(file_utils_1, "wb") as file:
        contents = await image_1.read()
        file.write(contents)
    file_utils_2 = f"utils/{unique_filename_2}"
    with open(file_utils_2, "wb") as file:
        contents = await image_2.read()
        file.write(contents)
    file_utils_3 = f"utils/{unique_filename_3}"
    with open(file_utils_3, "wb") as file:
        contents = await image_3.read()
        file.write(contents)
    file_utils_4 = f"utils/{unique_filename_4}"
    with open(file_utils_4, "wb") as file:
        contents = await image_4.read()
        file.write(contents)
    file_utils_5 = f"utils/{unique_filename_5}"
    with open(file_utils_5, "wb") as file:
        contents = await image_5.read()
        file.write(contents)
    
    file_path_1 = GCStorage().upload_file(file_utils_1)
    file_path_2 = GCStorage().upload_file(file_utils_2) 
    file_path_3 = GCStorage().upload_file(file_utils_3) 
    file_path_4 = GCStorage().upload_file(file_utils_4) 
    file_path_5 = GCStorage().upload_file(file_utils_5) 
    os.remove(file_utils_1)
    os.remove(file_utils_2)
    os.remove(file_utils_3)
    os.remove(file_utils_4)
    os.remove(file_utils_5)    
    return{
        "upload file_1":file_path_1, 
        "upload file_2":file_path_2, 
	"upload file_3":file_path_3, 
	"upload file_4":file_path_4, 
	"upload file_5":file_path_5 
    }
