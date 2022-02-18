# Windows 개발환경

## 1 SET UP

### 1.0 Essential Software

- Windows 10(2004버전 이상 최신 윈도우)
- Chrome - 개발자 도구가 좋음.
- Visual Studio Code
  - 폴더에서 code열기 체크
- Git - <https://git-scm.com/>

### 1.1 Customizing VSCode

- Extension
  - Python
  - ESLint
  - Prettier
  - Material Theme 또는 Github Theme
  - Material Icon Theme - Activate icon theme
  - Remote - WSL

## 1.2 Chocolatey <https://chocolatey.org/>

- Windows에 개발환경을 설치해주는 프로그램

  - Windows 버전 apt-get, homebrew

- 설치법

  - `Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))`
  - 관리자 권한의 파워셀에 복사 실행

- 패키지들
  - <https://community.chocolatey.org/packages>
  - python - `choco install python`
  - Windows Terminal 1.11.3471.0 - `choco install microsoft-windows-terminal`

## 1.3 Windows Terminal

- Windows Terminal 1.11.3471.0 - `choco install microsoft-windows-terminal`

## 1.4 WSL2

- WSL2 - `wsl --install`

- ubuntu - microsoft store에서 설치

- Windows Terminal의 디폴트 터미널을 ubuntu로 변경

## 2 TERMINAL CUSTOMIZATION

## 2.0 Installation

- Linux 쉘 변경

- zsh

  - Z쉘 - bash쉘 대신 사용 할 것.
  - `sudo apt install zsh`

- oh my zsh

  - zsh 테마 플러그인.
  - `sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"`

### 2.1 Powerlevel10K (12:26)

- terminal Splash

  - 윈도우 터미널 테마 사이트
  - <https://terminalsplash.com/>
  - Windows Termianl의 setting 좌 하단에 stting.json 편집
  - Scheme에 위의 사이트의 색상 값을 복사.
  - name 필드 생성 후 이름 설정
  - profiles의 defaults에 colorScheme 항목 추가 후 Scheme의 이름 설정.

- terminal font 변경, 크기 변경

  - profiles의 defaults에 font 항목 추가
  - "fontFace": "MesloLGS NF", "fontSize": 14 설정

- vscode 기본 terminal 변경
  <!-- - "terminal.integrated.defaultProfile.windows": "Ubuntu (WSL)" -->
  - "terminal.integrated.fontFamily": "MesloLGS NF"

```json
"profiles": {
    "defaults": {
      "colorScheme": "One Half Dark",
      "fontFace": "MesloLGS NF",
      "fontSize": 14
    },
// 이하 생략
```

- Powerlevel10K

  - oh my zsh 테마
  - `git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k`
  - Set `ZSH_THEME="powerlevel10k/powerlevel10k"` in `~/.zshrc`.
  - Restart Zsh with `exec zsh`.
  - `p10k configure` - Powerlevel10K 설정. 처음 켤 때 나오는 것.

- ls color
  - `LS_COLORS="ow=01;36;40" && export LS_COLORS`

## 3 INSTALLING EVERYTHING

### 3.0 Folders

- ~ - 리눅스 root
- /mnt/c/ - 윈도우의 c

- `sudo apt-get update` - apt-get을 업데이트해 패키지 목록을 갱신.
- `sudo apt-get upgrade` - apt-get으로 설치한 패키지를 최신버전으로 갱신.

### 3.1 Installing NodeJS

- <https://nodejs.org/ko/download/package-manager/>
- `curl -fsSL https://deb.nodesource.com/setup_16.x | sudo -E bash -`
- `sudo apt-get install -y nodejs`

### 3.2 Installing Python

- deadsnakes

  - <https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa>
  - 우분투를 위한 파이썬 제공 레포지터리

- apt에 PPA 데이터베이스 추가

  - `sudo add-apt-repository ppa:deadsnakes/ppa`
  - `sudo apt-get update`
  - `sudo apt-get install python3.9`

- 단축 명령어
  - python 명령으로 python3.9 실행 시키기
  - ~/.zshrc에 alias python="python3.9" 추가

### 3.3 Prettier and More Commands

> 윈도우에서 되는게 리눅스에서 안되기도 하고 그 반대도 있음.

eg. MongoDB는 윈도우에 설치해야함.

- prettier install wsl

### 3.4 Git and Github CLI (06:02)

- git - 기본으로 깔려있음.

  - `sudo apt-get git`

- github cli - 다운받아 설치하는 법
  - <https://github.com/cli/cli/releases/tag/v2.4.0>
  - gh_2.4.0_linux_amd64.deb 다운로드
  - `sudo apt install ./gh_2.4.0_linux_amd64.deb`
  - nodejs처럼 레포지토리 추가해서 다운받아 설치해도 됨.

```shell
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/etc/apt/trusted.gpg.d/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/trusted.gpg.d/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update
sudo apt install gh
```

### 3.5 nvm

- nvm - node.js 버전 관리하는 bash 스크립트

## 출처

- <https://nomadcoders.co/windows-setup-for-developers/>
