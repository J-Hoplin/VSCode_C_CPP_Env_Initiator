# Visual Studio Code C / C++ Environment Initiator

Latest Version : v 1.0.2(2021/11/26)

- Windows 실행파일은 이 프로그램 [Repository의 Release](https://github.com/J-hoplin1/VSCode_C_CPP_Env_Initiator/releases)에서 다운로드 하실 수 있습니다.

About : Visual Studio Code에서 C/C++환경을 MinGW GCC/G++를 활용해서 프로젝트 생성 / 삭제 / 환경변수 등록을 해주는 프로그램입니다. 처음에는 TypeScript로 구현을 하고 싶었으나, 제 TypeScript숙련도에 문제가 있는상태라 우선 python3와 Windows Batch를 이용해서 만들었습니다. **실행파일은 압축해제후 dist -> initiator -> initiator(톱니바퀴모양).exe를 실행해주시면 됩니다. 우클릭해서 바로가기를 만들어 사용하시는게 편합니다. 압축해제 후 있는 바로가기는 사용할 수 없는점 참고바랍니다.**. 추후 TypeScript로 포팅할 예정이니 기대해주시면 감사하겠습니다.

**이 프로그램을 사용하기 위해서는 VSCode가 add to path가 체크된 상태에서 설치가 되어있어야합니다. 또한 VS Code를 설치하시고 최초 실행 후 컴퓨터를 껏다가 켜신 다음 사용하시기 바랍니다.**

Python : ver 3.7.6

**CLone을 하시게 되면 Mingw64가 없기때문에 실행되지 않을 가능성이 높습니다. clone해서 사용하고 싶으신 분은 [이 링크](https://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win64/Personal%20Builds/mingw-builds/8.1.0/threads-posix/seh/x86_64-8.1.0-release-posix-seh-rt_v6-rev0.7z/download)를 들어가 다운로드 후 7zip파일을 압축 해제후 zip파일로 다시 압축하고, 아래 사진과 같이 mingw/mingw64.zip 을 추가해주신후 사용해 주시기 바랍니다.** 

**만약 소프트웨어 사용중 오류가 나거나, 개선 방안, 새로운 기능에 대한 제안이 있으신 분은 [issue](https://github.com/J-hoplin1/VSCode_C_CPP_Env_Initiator/issues)를 남겨주시면 감사하겠습니다**

![image](https://user-images.githubusercontent.com/45956041/140670957-686fe01c-273f-4930-b9c8-090d1888d2b5.png)

---
### Patch Note

- v 1.0.2

  - Release Date : 2021 / 11 / 26
  - Note : 소스코드 내부 보안을 위해 eval()함수로 처리하던 메소드 실행을 내부적인 메소드 처리로 변경하였습니다. eval()함수의 취약점은 이 [링크](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/eval#eval%EC%9D%84_%EC%A0%88%EB%8C%80_%EC%82%AC%EC%9A%A9%ED%95%98%EC%A7%80_%EB%A7%90_%EA%B2%83!)를 참조해 보시기 바랍니다.
---

### 사용방법

* 해당 소프트웨어에서 모든 옵션을 선택할때는 각 옵션들 좌측에 있는 숫자를 입력해서 선택해주시기 바랍니다. 



1. 실행하기

실행하게 되면 아래와 같은 창이 나오게 됩니다

![image](https://user-images.githubusercontent.com/45956041/140671252-4ec54a91-0384-4270-b6a0-e844518b4a4a.png)

이 프로그램을 종료하기 위해서는 Ctrl + C가 아닌 /exit을 사용해 종료해 주시기 바랍니다. Ctrl + C로 강제종료를 하게 되면 경고창이 뜨게 됩니다

![image](https://user-images.githubusercontent.com/45956041/140671399-6015d74c-6750-4c0e-81b4-ce97b4ab829c.png)

2. help

1번 옵션인 help를 선택하게 되면 이 소프트웨어의 기본적인 Document가 나오게 됩니다. 만약 윗부분이 짤린다면 창을 확대해 주시기 바랍니다.

![image](https://user-images.githubusercontent.com/45956041/140671515-a22d2407-d861-4725-b6d5-1aaf5c1e2069.png)

엔터키를 누르시면 다시 메인으로 가실수 있습니다

3. Install_MinGW_64bit_and_build_basic_ENV

이 옵션은 아래 기능들을 순차적으로 수행합니다

  - MingW설치 : 이 소프트웨어에서 설치하는 MingW위치를 임의로 변경하지 말아주시기 바랍니다. 변경시 소프트웨어 기능을 정상적으로 사용할 수 없게됩니다.

  - MingW Windows 환경변수 자동등록 
  
  - Visual Studio Code Microsoft 권장 C/C++ Extension 모두 설치 : 각 Extension은 실행시점 최신버전으로 설치됩니다. 하지만 추후 extension이 있을시 업데이트는 사용자가 직접 해야합니다

![image](https://user-images.githubusercontent.com/45956041/140671866-3c87d282-3c73-48d1-b365-6403a4ae8735.png)

현재 위 사진과 같이 GCC가 설치가 안되어있는것을 볼 수 있습니다.

![image](https://user-images.githubusercontent.com/45956041/140671895-a9a42680-19c6-478a-9170-bd2374e113f6.png)

실행을 하게되면 처음에 위 사진과 같이 검은 화면에 커서만 깜빡이게 됩니다. 이 과정이 MinGW를 설치하고 있는 과정입니다. 그러다 **CMD에 관리자 권한을 부여하는지 물어보게 되는데, 그때 꼭 '예'를 눌러주시기 바랍니다. 이 부분이 MinGW를 환경변수에 등록하는 과정입니다.** 예를 누르지 않을 경우, [수동으로 환경변수에 등록](https://velog.io/@andrewyoon10/VSCode%EC%97%90%EC%84%9C-CC-%EC%BB%B4%ED%8C%8C%EC%9D%BC-%EB%B0%8F-%EB%94%94%EB%B2%84%EA%B9%85-%ED%99%98%EA%B2%BD-%EB%A7%8C%EB%93%A4%EA%B8%B0)해주어야될 수 도 있습니다. 그 후 C/C++ Extension까지 설치를 정상적으로 완료하게 되면 아래와 같은 화면이 나오게 됩니다. 

![image](https://user-images.githubusercontent.com/45956041/140672155-c34aa602-fe58-4b46-9634-2b2f36f58b7a.png)

이제 다시 GCC 설치 / 환경변수 등록 여부를 확인합시다.

![image](https://user-images.githubusercontent.com/45956041/140672221-7c838c5c-c165-412f-9363-44d18fbb2dbf.png)

아까까지 실행되지 않던 GCC명령어가 환경변수에 잘 등록되어 적용된것을 볼 수 있습니다.

만약 기존에 MinGW가 설치되어있는 상태라면 충돌을 방지하기 위해 아래와 같은 오류창을 출력합니다
![image](https://user-images.githubusercontent.com/45956041/140674239-93804c46-463d-4c22-a974-c0c1e66ec986.png)


4. Settings

![image](https://user-images.githubusercontent.com/45956041/140672498-732eaa66-e056-4b6b-8df3-1d27a61739af.png)

다른 옵션을 보기 전 먼저 View Settings를 먼저 보겠습니다. 이 옵션에서는 기본적인 이 소프트웨어의 정보를 볼 수 있습니다. 여기서 가장 중요한건 이 소프트웨어에 지정되어있는 프로젝트 경로입니다. 프로젝트 경로는 사용자가 만들 프로젝트들이 저장되는 기본 디렉토리를 의미합니다. 이 프로그램에서는 제가 기본적으로 'C:\CProjectDir'라는 임의의 디렉토리를 지정하였습니다. 이 디렉토리가 없다고요? 걱정하지 마세요. 프로그램에서 최초 실행시 디렉토리 존재하지 않을 경우 알아서 생성합니다.

만약 이 프로젝트 디렉토리를 바꾸고 싶다면 프로젝트 경로로 지정하고 싶은 경로를 6번 옵션에 입력해 주면 됩니다. 파일 경로는 아래 사진과 같이 하이라이트 친 부분을 클릭하면 나오는 경로를 복사 붙여넣기해주시면 됩니다. 복사 붙여넣기 방법이 아닌 그냥 경로를 입력해 지정하고 싶은 경우 입력해주시면 알아서 디렉토리를 생성하고, 프로젝트 디렉토리로 지정합니다. 디렉토리를 변경하고 다시 settings를 가면 프로젝트 디렉토리가 변경되어있는것을 볼 수 있습니다. 이 변경된 디렉토리는 바꾼 즉시부터 적용되며, 프로그램을 다시 시작해도 최근 지정한 프로젝트 디렉토리로 고정됩니다.

![image](https://user-images.githubusercontent.com/45956041/140672828-e9050f2b-8d06-4074-9c33-7075d2315284.png)


![image](https://user-images.githubusercontent.com/45956041/140672804-6eac71d1-ce88-4818-84c0-1236e89f4914.png)


![image](https://user-images.githubusercontent.com/45956041/140673064-419a6daa-2633-4f1d-a1dc-679f47c2054e.png)


만약 경로를 그냥 입력하는 방법에서 잘못된 디렉토리나 만들수 없는 디렉토리를 입력한 경우 아래와 같이 오류 창이 나오게되며 프로그램을 종료합니다. 프로그램을 바로 종료하는것은 내부 데이터 꼬임 방지를 위한 것이며, 이는 v. 2.0.0에서 최적화작업을 통해 개선할 예정입니다.

![image](https://user-images.githubusercontent.com/45956041/140673000-e235a477-f9f8-487a-a2c2-5c0159fa47f6.png)

5. Initiate_new_C_C++_Project

이제 새로운 프로젝트를 생성해봅시다. 5번 옵션을 들어가면 아래와 같은 창이 나옵니다. 그럼 새로 생성하고싶은 프로젝트의 이름을 입력하면 프로젝트 환경을 자동으로 초기화 하고, 해당 프로젝트에서 VSCode를 실행하게됩니다.

![image](https://user-images.githubusercontent.com/45956041/140673299-c293d47d-b429-4922-a848-0d9d33eb83e8.png)

그리고 지정한 프로젝트 디렉토리에 직접 들어가봐도 프로젝트가 생성된것을 볼 수 있습니다.

![image](https://user-images.githubusercontent.com/45956041/140673349-b1b9b18d-50d7-4c31-b5c5-84a079e55667.png)

그렇다면 실험으로 C파일 하나를 만들어 디버깅과정을 해보겠습니다. 임의의 코드를 작성하고 중단점 설정후 F5를 눌러 디버깅을 하니 아무 문제 없이 잘 되는모습을 볼 수 있습니다. 중단점 없이 그냥 F5를 누르면 터미널에서 일반 실행을 합니다

![image](https://user-images.githubusercontent.com/45956041/140673549-d62fe0a0-7f2d-423d-9cdb-018fba66c458.png)

6. Open Existing Project

이 옵션과 다음 옵션 설명을 위해 테스트 프로젝트 2개를 더 생성했습니다.
![image](https://user-images.githubusercontent.com/45956041/140673809-cf0a0117-338d-47ad-98f6-9afb7542ff79.png)


이 옵션은 지정한 프로젝트 내에 있는 기존에 생성한 프로젝트를 선택해 Visual Studio Code로 여는것을 수행합니다. 예를 들어 저는 week2라는 프로젝트를 열고싶다고 가정합니다.
![image](https://user-images.githubusercontent.com/45956041/140673711-30c2558b-5cee-4f2e-adb6-fe0b5f1e5750.png)

그럼 아래 사진과 같이 바로 프로젝트가 열리는것을 볼 수 있습니다. 만약 선택한 프로젝트가 이미 열려있다면 해당 열린 창을 다시 엽니다.
![image](https://user-images.githubusercontent.com/45956041/140673772-0da10ada-e12a-41e9-b4f1-ec659c4a9e4a.png)

7. Delete Existing Project

이 4번 옵션은 기존 생성한 프로젝트를 삭제하는 옵션입니다. 만약 week3를 삭제하고 싶다면 해당 번호를 선택합니다. 그러면 정말 선택할 것인지 yes혹은 no를 입력하는 창이 나오게 됩니다. no를 입력하면 다시 메인으로, yes를 클릭하면 삭제를 합니다. **이과정에서 삭제하면 복구가 불가능하니 신중하시기 바랍니다**
![image](https://user-images.githubusercontent.com/45956041/140673960-f75e45aa-5b1b-4098-b502-a28f73f06e94.png)

그리고 만약 현재 작업중인 week1디렉토리를 삭제하고 싶다고 합시다. 만약 현재 프로세스가 가동중이거나 열려있는 상태의 프로젝트를 삭제하려고 하는 경우에는 아래 사진과 같이 윈도우 권한 오류가 뜨게 됩니다. 만약 이 오류창이 뜬다면 해당 프로젝트의 특정 프로세스가 가동중이라는 뜻이니 삭제전 확인해 주시기 바랍니다.
![image](https://user-images.githubusercontent.com/45956041/140674035-beb8113f-4214-499f-bc5f-970662637396.png)

8. command

이 소프트웨어에서는 /exit, /back두개의 커맨드를 지원합니다. 어떤 상황에서 각 명령어를 실행할 수 있는지 알려드리겠습니다.

- exit : 프로그램 종료

  ![image](https://user-images.githubusercontent.com/45956041/140674170-bc31a916-019b-40fb-ada7-f00e8b06610a.png)
  
- /back : 이전단계로(help,Install_MinGW_64bit_and_build_basic_ENV,view settings를 제외한 옵션에서 모두 사용가능)

  ![image](https://user-images.githubusercontent.com/45956041/140674295-3f1b4af9-d215-4a86-8268-27e9ffe7e27b.png)

  ![image](https://user-images.githubusercontent.com/45956041/140674321-45b350bd-7648-4117-8704-ba6eaa21e69a.png)
  
  ![image](https://user-images.githubusercontent.com/45956041/140674360-b503b469-4047-44cc-828a-d596112aa77f.png)
  
  ![image](https://user-images.githubusercontent.com/45956041/140674387-a3fbbc29-3583-4240-9215-41c3639e6f15.png)

이것으로 소프트웨어 사용 방법에대한 설명을 마치겠습니다. 
