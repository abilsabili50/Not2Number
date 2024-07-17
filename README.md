# Not2Number

Not2Number is a website to transform block notation into number notation that contains in song sheet music. Number notation represent common tone from Do-Si

## Built With

[Label-Studio](https://labelstud.io/) - Data Labeling Platform <br/>
[OpenCV](https://opencv.org/) - Computer Vision Library <br/>
[Tensorflow](https://www.tensorflow.org/hub/tutorials/object_detection) - Tensorflow Object Detection Module <br/>
[Faster R-CNN & ResNet50](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md) - Pretrained Faster R-CNN ResNet50 Model <br/>
[Flask](https://flask.palletsprojects.com/en/3.0.x/api/) - Python Micro-Framework <br/>
[Seputar Musikal](https://www.seputarmusikal.com/) - Dataset Partitur Notasi Balok <br/>

## How to Use

These instructions will get this project up and running on your local machine.

### Prerequisites

You will need to install [Python](https://www.python.org/downloads/) on your local machine.

### Installing

#### First you need to clone the repository. Run the following command :

```bash
git clone https://github.com/abilsabili50/Not2Number
```

> this process may take some times

#### Enter the directory :

```bash
cd Not2Number
```

#### Install dependecies using :

```bash
pip install -r requirements.txt
```

## Usage

### Run The Project

you can run the project by this following command:

```bash
python app.py
```

this will start the development server.

### Access The Web Page

you can access the web page by paste this url into your local browser.

```arduino
http://localhost:5000
```
this [url](http://localhost:5000) will bring you to main page of Not2Number website. The page will look like the one shown in the image below.

![image](https://github.com/user-attachments/assets/9b021962-661b-4031-bc16-3736676ee478) <br/>

From the image above, you can see there is a button with text `Konversi Partitur` that will bring you into the main feature that shown in the image below.

![image](https://github.com/user-attachments/assets/93c85bd3-5598-4521-a81c-5ead5a7d86bb)

### Insert Demo Image

I provide the demo image in [this](https://drive.google.com/drive/folders/1mnohEJMJoFOO4IJgX93XKErzkji_Gu3y) drive that you can use as an input image. You can input it by clicking button that have text `Masukkan Gambar`.

### Perform Transformation

You can transform the input image by clicking `Transform` button that can be seen on the image above while you insert the input image.

> it may take some times while process transformation is running

### Download The Result Image

After the transformation process is complete, the feature page will look like the one shown in the image below.

![image](https://github.com/user-attachments/assets/a0cdeac4-7211-4777-a6bf-e7ae4f15fe62)

### Result Image

Example of result image can be seen in the image below.

![Image](https://github.com/user-attachments/assets/ba621778-271d-4ed3-8d75-be6ea22c0061)

> example of result image is using song sheet music of `Cublak - Cublak Suweng`

## Attention

### Weakness of Not2Number

Not2Number project is far from perfect, that has weakness with an input image that has potrait orientation.

### Special Thanks

Special thanks to:

- Eka Prakarsa Mandyartha, S.T., M.Kom. - `Supervisor 1`
- Agung Mustika Rizki, S.Kom., M.Kom. - `Supervisor 2`
- [Fahrul Firmansyah](https://github.com/aldebarankwsuperrr), S.Kom. - `Advisor`
- [Putra Dwi Wira G.Y.](https://github.com/PutraWiraG), S.Kom. - `Advisor`

- [Seputar Musikal](https://www.seputarmusikal.com/) - `Dataset Supplier`