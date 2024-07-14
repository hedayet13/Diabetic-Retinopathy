# Image Processing of Fundus Images of DR Patients

Diabetic retinopathy (DR) is primarily caused by damage to the blood vessels in the retina of diabetic patients. Our project aimed to develop a cost-effective platform to recognize the stages of DR in patients, making early detection more accessible.

## A Sample Retinal Image of DR Patients

To create an automated system for classifying the stages of diabetic retinopathy, we needed to identify specific features within retinal images, known as fundus images. Our system can determine if a patient has mild or severe non-proliferative diabetic retinopathy (NPDR) or other stages. My role focused on the image processing aspects of this project. Below is an example of a retinal image from a DR patient. By counting lesions such as microaneurysms and hemorrhages, we developed a classification algorithm. This process involved removing the macula, optic disc, and blood vessels to isolate the relevant features.

<img src="/media/fundusImages.jpg" alt="Retinal Image of a DR Patient" width="400"/>

## Normal Feature Detection of Fundus Image

Detecting normal features such as blood vessels, the optic disc, and the macula was the first step in our process. Here’s how we approached each:

1. **Blood vessel detection**: 
   - Fundus image -> Extracted green channel -> CLAHE -> Blur -> Background subtraction -> Binary conversion -> Removing small pixels (noise)
   
2. **Optic disc detection**: 
   - Fundus image -> Applying CLAHE on HSV format -> Gray image after blurring -> Draw the contour -> Fill
   
3. **Macula detection**: 
   - Fundus image -> Remove black background -> Apply CLAHE -> Gray image applying filter -> Binary -> Final image after removing noise

<img src="/media/normalFeature.jpg" alt="Normal Feature Detection" width="800"/>

## Abnormal Feature Detection of Fundus Image

Detecting abnormal features such as microaneurysms and hemorrhages posed a greater challenge due to their small size. We divided the fundus image into multiple patches: 15x15 for microaneurysms and 25x25 for hemorrhages. By processing these patches with image algorithms, we could count the microaneurysms and hemorrhages to classify the stages of NPDR. Additionally, for detecting neovascularization, we utilized transfer learning with the InceptionV3 algorithm, leveraging its deep learning capabilities to improve accuracy.

<img src="/media/abnormalFeature.jpg" alt="Abnormal Feature Detection" width="800"/>


## Published Article

An article based on this research is published in Heliyon:

```
@article{mahmood2023hybrid,
  title={A hybrid approach for diagnosing diabetic retinopathy from fundus image exploiting deep features},
  author={Mahmood, Mohammed Arif Iftakher and Aktar, Nasrin and Kader, Md Fazlul},
  journal={Heliyon},
  volume={9},
  number={9},
  year={2023},
  publisher={Elsevier}
}
```


This project not only advances our understanding of diabetic retinopathy but also paves the way for more accessible and affordable diagnostic tools, potentially improving patient outcomes significantly.

