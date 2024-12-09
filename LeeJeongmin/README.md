# Pelvic X-Ray Segmentation

## 프로젝트 개요
이 프로젝트는 딥러닝 기반의 U-Net 모델을 사용하여 골반 엑스레이 이미지를 분할(Segmentation)하는 프로젝트입니다.

## 사용된 라이브러리

- **Python**: 3.8+
- **TensorFlow**: 2.6.0
- **Keras**: TensorFlow Keras 모듈 포함
- **Keras-Unet-Collection**: 0.1.12
- **OpenCV**: 4.5.5
- **NumPy**: 1.19.5
- **SciPy**: 1.7.1
- **Matplotlib**: 3.4.3
- **Scikit-learn**: 0.24.2
- **Pandas**: 1.3.3
- **Numba**: 0.54.1

## 설치 방법

```bash
pip install tensorflow==2.6.0 keras==2.6.0 opencv-python==4.5.5 numpy==1.19.5 scipy==1.7.1 matplotlib==3.4.3 scikit-learn==0.24.2 pandas==1.3.3 numba==0.54.1 keras-unet-collection==0.1.12
```

## 실행 방법

1. Train
- 데이터 준비
img_path 변수에 데이터셋 경로를 설정
ex)img_path = '../../1. 데이터/4. 골반 분할 연구 데이터/

- Train 코드 실행

- 모델 저장
학습이 완료되면, 결과 모델은 .h5 파일 형식으로 저장
ex)6_result/exp_fold{fold_num}/model/

2. Test
- 데이터 준비
테스트 데이터셋 경로를 img_path 변수에 설정
ex)img_path = '../../1. 데이터/4. 골반 분할 연구 데이터/'

- 모델 준비
학습 완료된 모델 파일(last.h5)을 아래 경로에 저장
ex)6_result/exp_fold{fold_num}/model/last.h5

- Test 코드 실행

- 결과 확인
예측된 마스크 이미지 저장 경로
6_result/exp_fold{fold_num}/pred_total/
원본 이미지와 오버레이된 결과 저장 경로
6_result/exp_fold{fold_num}/pred_total_over/


## 주요 기능

- 예측 수행: 학습된 U-Net 모델(last.h5)을 불러와 테스트 데이터에 대해 분할 예측을 수행
- 후처리
fill_hole_cv: 구멍 메우기 알고리즘을 통해 예측 마스크 후처리
Morphology Open: 노이즈 제거 및 세부 조정
- 결과 저장:
후처리된 마스크 이미지 저장
원본 이미지와 예측 결과를 오버레이한 이미지 저장

## 참고 자료
- [Keras Unet Collection GitHub](https://github.com/zhixuhao/unet)
- [TensorFlow 공식 문서](https://www.tensorflow.org/)
