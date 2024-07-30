- 교재 예제 : https://www.gilbut.co.kr/book/view?bookcode=BN003345#bookData

1. 컴퓨터 정리
- 기존 파이썬 및 아나콘다 관련 프로그램 모두 삭제
	- 1. 윈도우키  + X => 단축매뉴
		- "앱 및 기능" > "python" 검색 후 관련된 프로그램 다 삭제
	- 2. 삭제 후에 단축메뉴의 "Window PowerShell or CMD"
		- "python" 입력 후 실행이 안되거나 MS Store 실행
	- 3(a). 기존에 아나콘다를 설치한 경우
		- .conda, .ipython, .matplotlib 등 기존 파이썬 관련 다 삭제
	- 3(b). 단축매뉴 > 시스템 > 고급 시스템 설정 > 시스템 속성 > 환경 변수
		- user, system의 "PATH"에 python 관련 경로 삭제

2. 아나콘다 설치
	- cache 삭제 부분만 설정 후 설치

3. 아나콘다 사용법 => 반드시 "Conda Prompt"를 사용 `(base) C:\...`
	- conda env list
	- conda create -n torch-book python=3.12
	- conda activate torch-book
	- conda deactivate
	- conda remove -n torch-book 

4. 필요 라이브러리 설치
	- conda install pytorch torchvision torchaudio cpuonly -c pytorch
	- conda install -c conda-forge jupyterlab

5. 경로 변경(프로젝트 경로 : C:\practice-torch)
	- cd C:\practice-torch
	- jupyter-lab