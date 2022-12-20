import fastapi
from fastapi import FastAPI, UploadFile, File
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import numpy as np
import trans_img
import generate_wav
import recall_wav

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)

@app.post('/')
def index():
    return "111"



@app.post("/files")
async def create_upload_file(file: UploadFile = File(...)):
    with open(f'web/{file.filename}','wb') as f: 
        f.write(await file.read())
    fname = file.filename
    wavp = fname[:fname.index('.')]
    trans_img.img2wav('web/' + fname, 'web/' + wavp + '.wav')
    generate_wav.generate_wav("back.wav", 'web/' + wavp + '.wav', 'web/' + wavp)

    return wavp

@app.post("/recover")
async def recall(file: UploadFile = File(...)):
    with open(f'web/{file.filename}', 'wb') as f:
        f.write(await file.read())
    fname = file.filename
    img = fname[:fname.index('.')]
    recall_wav.return_wav('web/' + fname, "back.wav", 'web/' + img + '_re.wav')
    trans_img.draw_figure('web/' + img + '_re.wav', 'web/' + img + '.png')

    return img + '.png'

if __name__ == '__main__':
    uvicorn.run(app='web:app', host='127.0.0.1', port=8000, reload=True, debug=True)