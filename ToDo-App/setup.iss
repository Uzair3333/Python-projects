; --------------------------------------------
; Inno Setup Script for To-Do App
; --------------------------------------------

[Setup]
; Application details
AppName=To-Do App
AppVersion=1.0
DefaultDirName={pf}\To-Do App
DefaultGroupName=To-Do App
OutputBaseFilename=ToDoAppInstaller
Compression=lzma
SolidCompression=yes
ArchitecturesInstallIn64BitMode=x64
WizardStyle=modern

; Application icon (optional)
SetupIconFile=assets\icon.ico

; Allow user to uninstall
UninstallDisplayIcon={app}\gui.exe
AllowNoIcons=yes
RestartIfNeededByRun=false
AlwaysRestart=no

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Files]
; Main executable
Source: "dist\gui.exe"; DestDir: "{app}"; Flags: ignoreversion

; Optional tasks.json if you want to ship a default empty file
Source: "tasks.json"; DestDir: "{app}"; Flags: ignoreversion

; Optional icon (if any additional assets)
; Source: "assets\*"; DestDir: "{app}\assets"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\To-Do App"; Filename: "{app}\gui.exe"
Name: "{userdesktop}\To-Do App"; Filename: "{app}\gui.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Create a &desktop icon"; GroupDescription: "Additional icons:"; Flags: unchecked

[Run]
Filename: "{app}\gui.exe"; Description: "Launch To-Do App"; Flags: nowait postinstall skipifsilent