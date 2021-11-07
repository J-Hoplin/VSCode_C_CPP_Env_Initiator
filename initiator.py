"""
Written by Hoplin(https://github.com/J-hoplin1)
Version : v 1.0.0
Last Written 2021 / 11 /07
Python Version : 3.7.5
"""
import os,sys,yaml,platform,zipfile,shutil
import subprocess
from enum import Enum
from pathlib import Path

class textColor:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class GlobalUtilities(object):
    '''

    '''
    # Option dictionary : For class FeatureProcessors
    __optionMapper = {
        1: "ftpr.help()",
        2: "ftpr.installAndBuildENV()",
        3: "ftpr.openExistingProject()",
        4: "ftpr.deleteExistingProject()",
        5: "ftpr.initiateNewProject()",
        6: "ftpr.viewSettings()"
    }
    def __init__(self):
        pass

    @classmethod
    def optionInitiator(cls,num) -> None:
        eval(GlobalUtilities.__optionMapper[num])

    @classmethod
    def clearConsole(cls) -> None:
        os.system('cls')

    @classmethod
    def pressKeyToContinue(cls) -> None:
        input("Press any key to continue...")

    @classmethod
    def checkDirectoryExist(cls,directory) -> bool:
        return Path(directory).is_dir()

    @classmethod
    def endProcess(cls) -> None:
        sys.exit()

    def warningMessageHandler(self,message) -> None:
        print(f"{textColor.WARNING}{message}{textColor.ENDC}")

    def errorMessageHandler(self,message,additionalmsg="Additional Message Not Exist") -> None:
        #print(dir(message))
        #print(message.strerror)
        print(f"{textColor.FAIL}Error Occured : {message.strerror} / {additionalmsg}{textColor.ENDC}")
        self.pressKeyToContinue()
        self.clearConsole()
        self.endProcess()
#ENV initiator
class FeatureProcessors(GlobalUtilities):
    '''
    Class : It's a class that handles each option functionally.
    '''
    __CDirectory = 'C:\\'
    __GCCDirectory = 'C:\\mingw64\\bin'
    __minGWzipfile = os.getcwd() + "\\mingw\\mingw64.zip"
    __batchfilesDirectory = os.getcwd() + "\\batchfiles"
    __decompressDirectory = 'C:\\mingw64'
    __ProjectDirectory = None

    def __init__(self,bitselection="64bit") -> None:
        try:
            with open('config.yml') as f:
                self.yml = yaml.load(f,yaml.FullLoader)
                self.directoryInfo = self.yml['directories']
                self.__ProjectDirectory = self.directoryInfo['Project_Directory']
                #If user designated project directory exist save directory
                if self.checkDirectoryExist(self.__ProjectDirectory):
                    pass
                #If user designated project directory didn't exist make directory
                else:
                    try:
                        os.mkdir(self.__ProjectDirectory)
                        print(f"Project directory : {self.__ProjectDirectory} generated, due to non exist directory")
                    except OSError as e:
                        self.errorMessageHandler(e,"Can't generate directory. Check if directory written in config.yml has the proper directory form.")
        except FileNotFoundError as e:
            self.errorMessageHandler(e,"Config.yml not found! Please regenerate config.yml. Program close")

    @classmethod
    def returnStaticVariableGCCDir(cls) -> str:
        return cls.__gccdirectory

    def returnProjectDirectory(self):
        return os.listdir(self.__ProjectDirectory)

    def help(self) -> None:
        self.clearConsole()
        print(f"""
        <Document : About function per each Option>
        
        ※ Basic Command

        /exit : You can exit this program. You can use this command in main
        
        /back : You can go back to before state. You can use this command in option 3,4,5
        
        1. Help
        
        -> show this documentation
        
        2. Install MinGW 64bit and build basic ENV
        
        {textColor.WARNING}* Warning : This option require VS Code to be in PATH. If not installation may be in process abnormally.{textColor.ENDC}
        * Neccessary :  Check windows environment variable, VSCode Extension if successfully install, enroll
        -> Unzip MinGW GCC Compiler(Standard : 64bit / v 8.1.0) and enroll to environment variable. After this it enroll    GCC to environment variable, next it install Basic C/C++ VS Code Extension.
        
        3. Open Existing Project
        
        -> You can select project directory and open it with vscode
        
        4. Delete Existing Project
        
        {textColor.WARNING}* Warning : You can't recover delete file after remove.{textColor.ENDC}
        -> You can delete project which you generated before
        
        5. Initiate New Project
        
        -> You can initiate new C/C++ Project at VSCode

        6. View Settings

        -> You can see basic information about this software
        """)
        self.pressKeyToContinue()
        self.clearConsole()


    def installAndBuildENV(self):
        if self.checkDirectoryExist(self.__GCCDirectory):
            self.warningMessageHandler(f"Directory : {self.__GCCDirectory} already exist! Please check if MingW has already been installed")
        else:
            try:
                print("Decompressing minGW64. This might take some time. Please wait a moment.")
                print(f"Decompressing to : {self.__decompressDirectory}")
                self.clearConsole()
                with zipfile.ZipFile(self.__minGWzipfile, 'r') as z:
                    z.extractall(self.__decompressDirectory)
            except FileNotFoundError as e:
                self.errorMessageHandler(e, "mingw64/mingw64.zip not found. Program close")
                # Add minGW64 GCC/G++ to Windows PATH : run batch file
            batname_enrollvariable = self.__batchfilesDirectory + "\\enrollvariable.bat"
            subprocess.run([batname_enrollvariable])
            print(
                "Install C/C++ Extension to Visual Studio Code. Make sure extension installed completely after this process.")
            batname_installExtension = self.__batchfilesDirectory + "\\installCExtension.bat"
            subprocess.run([batname_installExtension])

    def openExistingProject(self):
        dir_list = self.returnProjectDirectory()
        if not dir_list:
            self.warningMessageHandler(f"Warning : Project Directory({self.__ProjectDirectory}) you designated is empty!")
            self.pressKeyToContinue()
            self.clearConsole()
        else:
            while True:
                print("Select project you want to open with Visual Studio Code.\nEnter '/back' to go back to main.")
                print(f"{'-' * 15}")
                for n, i in enumerate(dir_list, start=1):
                    print(f"{n}. {i}",end='\n')
                print(f"{'-' * 15}")
                try:
                    selection = input(">> ")
                    if selection.lower() == "/back":
                        self.clearConsole()
                        break
                    elif 1 <= int(selection) <= len(dir_list):
                        projectName = dir_list[int(selection) - 1]
                        projectdir = self.__ProjectDirectory + f"\\{projectName}"
                        batname_openproject = self.__batchfilesDirectory + "\\openproject.bat"
                        subprocess.run([batname_openproject,projectdir])
                        self.clearConsole()
                        break
                    else:
                        self.clearConsole()
                        self.warningMessageHandler("Warning : 잘못된 값이 입력되었습니다.")
                except ValueError:
                    self.clearConsole()
                    self.warningMessageHandler("Warning : 정확한 값을 입력해주세요.")
                    pass
                except KeyboardInterrupt:
                    self.clearConsole()
                    self.warningMessageHandler("Warning : 뒤로가기 위해서는 '/back'을 입력해주세요")

    def deleteExistingProject(self):
        dir_list = self.returnProjectDirectory()
        if not dir_list:
            self.warningMessageHandler(f"Warning : Project Directory({self.__ProjectDirectory}) you designated is empty!")
            self.pressKeyToContinue()
            self.clearConsole()
        else:
            while True:
                print("Select project you want to delete.")
                print(f"{'-' * 15}")
                for n, i in enumerate(dir_list, start=1):
                    print(f"{n}. {i}", end='\n')
                print(f"{'-' * 15}")
                try:
                    selection = input(">> ")
                    if selection.lower() == "/back":
                        self.clearConsole()
                        break
                    elif 1 <= int(selection) <= len(dir_list):
                        self.clearConsole()
                        projectName = dir_list[int(selection) - 1]
                        projectdir = self.__ProjectDirectory + f"\\{projectName}"
                        while True:
                            self.warningMessageHandler(f"Warning : 삭제된 디렉토리는 어떠한 방법으로도 복구할 수 없습니다. 진행하시겠습니까?(Yes / No)\n현재 선택한 프로젝트 이름 : {projectName} ")
                            try:
                                opt = input("yes 혹은 no를 입력하여 승인 혹은 보류하기 >> ")
                                if opt.lower() == "yes":
                                    shutil.rmtree(projectdir)
                                    self.clearConsole()
                                    break
                                elif opt.lower() == "no":
                                    self.clearConsole()
                                    break
                                else:
                                    self.clearConsole()
                                    self.warningMessageHandler("Warning : yes 혹은 no만 입력가능합니다.")
                            except ValueError as e:
                                self.clearConsole()
                                self.warningMessageHandler("Warning : 잘못된 값이 입력되었습니다.")
                            except PermissionError as e:
                                self.clearConsole()
                                self.warningMessageHandler("Warning : 윈도우 권한오류. 해당 디렉토리의 모든 프로세스가 종료되었는지 확인해주세요.")
                        break
                    else:
                        self.clearConsole()
                        self.warningMessageHandler("Warning : 잘못된 값이 입력되었습니다.")
                except ValueError:
                    self.clearConsole()
                    self.warningMessageHandler("Warning : 정확한 값을 입력해주세요.")
                    pass
                except KeyboardInterrupt:
                    self.clearConsole()
                    self.warningMessageHandler("Warning : 뒤로가기 위해서는 '/back'을 입력해주세요")

    def initiateNewProject(self):
        while True:
            try:
                print("Please enter the name of the project to be initialized.")
                print(f"* Project directory will be generated at {self.__ProjectDirectory}")
                projectName = input(">> ")
                if projectName.lower() == "/back":
                    self.clearConsole()
                    break
                try:
                    newProjectDirectory = self.__ProjectDirectory + f"\\{projectName}"
                    batname_initiateProject = self.__batchfilesDirectory + "\\initiateProject.bat"
                    batname_openproject = self.__batchfilesDirectory + "\\openproject.bat"
                    print(f"{textColor.OKBLUE}Generating Project Directory : {newProjectDirectory} {textColor.ENDC}")
                    os.mkdir(newProjectDirectory)
                    print(f"{textColor.OKBLUE}Generating VSCode Configuration File : {newProjectDirectory}{textColor.ENDC}")
                    subprocess.run([batname_initiateProject, newProjectDirectory])
                    print(f"Open initiated project at Visual Studio Code...")
                    subprocess.run([batname_openproject, newProjectDirectory])
                    self.pressKeyToContinue()
                    self.clearConsole()
                    break
                except OSError as e:
                    self.clearConsole()
                    self.warningMessageHandler("Warning : 이 오류에는 몇가지 가능성이 있습니다. \n 1. Winodws 폴더 이름 생성 규정 위반 \n 2. 이미 존재하는 디렉토리 이름 \n 3. '/back'이라는 단어는 소프트웨어 커맨드로 사용되고 있습니다. 다른이름을 사용해주세요")
            except ValueError:
                self.clearConsole()
                self.warningMessageHandler("Warning : 정확한 값을 입력해주세요.")
                pass
            except KeyboardInterrupt:
                self.clearConsole()
                self.warningMessageHandler("Warning : 뒤로가기 위해서는 '/back'을 입력해주세요")

    def viewSettings(self) -> None:
        print(f"""
        <Settings>
        
        ac : Able to change in config.yml
        nc : Not able to change this value
        
        1. nc - Basic GCC Directory( + to Path) : {self.__GCCDirectory}

        2. ac - Where did my project saved in this session? : {self.__ProjectDirectory}

        3. nc - Support Language / Compiler Info : C_C++ / MinGW64 GCC Compiler 8.1.0 64bit(x86_64-posix-seh) 
        
        4. nc - Support Tool : Visual Studio Code

        * MinGW URL : https://sourceforge.net/projects/mingw-w64/files/mingw-w64/
        * You can change your project directory from config.yml : Project_Directory
        * This software source code is open source : https://github.com/J-hoplin1/VSCode_C_CPP_Env_Initiator
        * License : MIT License
        """)
        self.pressKeyToContinue()
        self.clearConsole()

# CLI UI class
class CliUI(GlobalUtilities):
    '''
    Class : It's a class that processes the CLI UI environment-related parts.
    '''
    def __init__(self) -> None:
        self.__options = Enum('option', ['Help', 'Install_MinGW_64bit_and_build_basic_ENV', 'Open_existing_project_VSCode','Delete_existing_project','Initiate_new_C_C++_Project','View settings'])

    def option_selector(self) -> Enum:
        opt = [f'{i.value}. {i.name}' for i in self.__options]

        while True:
            print("\nStandard : MinGW GCC / G++ 8.1.0")
            print(f"System Info : {platform.system()} {platform.architecture()[0]}")
            print("Enter '/exit' to end program.")
            print(f"{'-' * 15}")
            for l in opt:
                print(l,end='\n')
            print(f"{'-' * 15}")
            try:
                select = input(">> ")
                if select.lower() == '/exit':
                    self.clearConsole()
                    self.endProcess()
                elif 1 <= int(select) <= len(opt):
                    self.clearConsole()
                    return self.__options(int(select))
                else:
                    self.clearConsole()
                    self.warningMessageHandler("Warning : 잘못된 값이 입력되었습니다.")
            except ValueError:
                self.clearConsole()
                self.warningMessageHandler("Warning : 정확한 값을 입력해주세요.")
            except KeyboardInterrupt:
                self.clearConsole()
                self.warningMessageHandler("Warning : 종료를 하기 위해 /exit를 입력해주시기 바랍니다")

    def returnUserOption(self):
        selectedOption = self.option_selector()
        #return value of options
        return selectedOption.value


if __name__=="__main__":
    GlobalUtilities.clearConsole()
    ftpr = FeatureProcessors()
    cli = CliUI()
    while True:
        # Option : User selection
        optionSelect = cli.returnUserOption()
        GlobalUtilities.optionInitiator(optionSelect)