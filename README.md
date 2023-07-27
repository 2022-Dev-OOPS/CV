![254303205-2c708d0a-7f16-4501-8fc8-0b3f5333c2f4](https://github.com/HyeokHam/2022-Dev-OOPS_CV/assets/90409694/61b93f83-3e22-45ba-a557-6f800a48cfbb)
# Computer Vision

CAM Server에서 받은 영상데이터를 Yolov5 모델로 인체를 인식하여 탐지하여 차수벽 가동을 결정하는 역할을 합니다.

## 기술 스택 및 환경

* Environment : Python 3.10
* Framework : Flask 2.3.2
* Library : Pytorch 1.13.1
* Model : YOLOv5
* Hardware : RaspberryPI 4

## 작동 과정

먼저 **중앙 서버**에서 보낸 차수벽 가동 메시지를 수신받아 CCTV에서 스트리밍 영상을 받아 영상 속에서 실시간으로 주변의 보행자를 감지합니다. 

만약 해당 카메라의 범위에서 약 3초간 보행자가 감지되지 않으면 **중앙 서버**로 보행자가 감지되지 않음을 알립니다.

(아키텍쳐)

## 구성

### 서버

해당 서버는 Flask로 구성되었으며 AWS EC2에서 가동됩니다.

해당 서버를 통해 **중앙 서버**에서 차수벽 가동 메시지를 수신받고, 보행자 감지가 종료되면 보행자가 감지되지 않음을 Central Server로 다시 송신하는 역할을 합니다.

또한 해당 서버를 통해 YOLOv5 모델을 통한 **인체 탐지 시스템**을 가동합니다.



### 인체 탐지 시스템

해당 시스템은 Raspberry PI의 성능에 따라 YOLOv5s 모델을 사용하였습니다.

해당 시스템은 서버를 통해 수신받은 CCTV(CAM) 영상에서 보행자를 식별합니다.

(영상)



## 라이센스

YOLOv5 사용에 따라 **AGPL-3.0 라이센스**를 적용합니다.

**AGPL-3.0 라이센스**에 관한 자세한 내용은 [LICENSE](https://github.com/HyeokHam/2022-Dev-OOPS_CV/blob/feat/CV/LICENSE) 파일을 참조하십시오.

