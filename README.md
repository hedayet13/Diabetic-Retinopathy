# Image processing of Fundus Images of DR patients
The main goal was to develop a cost-effective platform for recognizing the stages of DR patients.
## A sample retinal Image of DR patients

## Normal Feture Detection of Fundus Image

## Abnormal Feature Detection of Fundus image
The tough part was detecting microaneurysms and hemorrhages due to their tiny size. We divided the fundus image into multiple patches: 15x15 patches for microaneurysms and 25x25 patches for hemorrhages. We then processed these patches using image algorithms. By counting these microaneurysms and hemorrhages, we classified the stages of NPDR. For neovascularization detection, we used transfer learning with InceptionV3 algorithms.



## A Journal is also published according to this research in Heliyon:
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
