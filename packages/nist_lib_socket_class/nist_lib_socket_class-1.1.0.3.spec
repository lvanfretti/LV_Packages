[Package]
Name="nist_lib_socket_class"
Version="1.1.0.3"
Release=""
ID=94d7bccb1a56f151b66c521d6c7e3646
File Format="vip"
Format Version="2014"
Display Name="Socket Class"


[Description]
Description="Socket class:  A low-level networking API.  Currently there are two child classes, Socket.TCP and Socket.UDP.  "
Summary="Low level networking API"
License="NIST Open Source"
Copyright="uncopyrighted"
Distribution=""
Vendor="NIST"
URL="https://github.com/usnistgov"
Packager="Allen Goldstein"
Demo="FALSE"
Release Notes="First Release"
System Package="FALSE"
Sub Package="FALSE"
License Agreement="TRUE"


[LabVIEW]
close labview before install="FALSE"
restart labview after install="FALSE"
skip mass compile after install="FALSE"


[Platform]
Exclusive_LabVIEW_Version="LabVIEW>=14.0"
Exclusive_LabVIEW_System="ALL"
Exclusive_OS="ALL"


[Script VIs]
PreInstall=""
PostInstall=""
PreUninstall=""
PostUninstall=""
Verify=""
PreBuild=""
PostBuild=""


[Dependencies]
AutoReqProv=FALSE
Requires=""
Conflicts=""


[Activation]
License File=""
Licensed Library=""


[Files]
Num File Groups="3"
Sub-Packages=""
Namespaces=""


[File Group 0]
Target Dir="<application>"
Replace Mode="Always"
Num Files=67
File 0="user.lib/NIST/Socket Class/MetaData/Socket.xml"
File 1="user.lib/NIST/Socket Class/documentation/DISCLAIMER.txt"
File 2="user.lib/NIST/Socket Class/documentation/LICENSE.txt"
File 3="user.lib/NIST/Socket Class/documentation/Socket.pdf"
File 4="user.lib/NIST/Socket Class/documentation/Socket_Calss_reveiw"
File 5="user.lib/NIST/Socket Class/Classes/Socket.lvlib"
File 6="user.lib/NIST/Socket Class/Classes/Socket.UDP/Close.vi"
File 7="user.lib/NIST/Socket Class/Classes/Socket.UDP/Connect.vi"
File 8="user.lib/NIST/Socket Class/Classes/Socket.UDP/New.vi"
File 9="user.lib/NIST/Socket Class/Classes/Socket.UDP/Receive.vi"
File 10="user.lib/NIST/Socket Class/Classes/Socket.UDP/Socket.UDP.lvclass"
File 11="user.lib/NIST/Socket Class/Classes/Socket.UDP/Transmit.vi"
File 12="user.lib/NIST/Socket Class/Classes/Socket.UDP/UDP.ctl"
File 13="user.lib/NIST/Socket Class/Classes/Socket.UDP/Accessors/Read host_address.vi"
File 14="user.lib/NIST/Socket Class/Classes/Socket.UDP/Accessors/Read host_port.vi"
File 15="user.lib/NIST/Socket Class/Classes/Socket.UDP/Accessors/Read remote_address .vi"
File 16="user.lib/NIST/Socket Class/Classes/Socket.UDP/Accessors/Read remote_port .vi"
File 17="user.lib/NIST/Socket Class/Classes/Socket.UDP/Accessors/Read time-to-live.vi"
File 18="user.lib/NIST/Socket Class/Classes/Socket.UDP/Accessors/Read transfer_mode.vi"
File 19="user.lib/NIST/Socket Class/Classes/Socket.UDP/Accessors/Read udp_refnum.vi"
File 20="user.lib/NIST/Socket Class/Classes/Socket.UDP/Accessors/Write host_address.vi"
File 21="user.lib/NIST/Socket Class/Classes/Socket.UDP/Accessors/Write host_port.vi"
File 22="user.lib/NIST/Socket Class/Classes/Socket.UDP/Accessors/Write remote_address .vi"
File 23="user.lib/NIST/Socket Class/Classes/Socket.UDP/Accessors/Write remote_port .vi"
File 24="user.lib/NIST/Socket Class/Classes/Socket.UDP/Accessors/Write time-to-live.vi"
File 25="user.lib/NIST/Socket Class/Classes/Socket.UDP/Accessors/Write transfer_mode.vi"
File 26="user.lib/NIST/Socket Class/Classes/Socket.UDP/Accessors/Write udp_refnum.vi"
File 27="user.lib/NIST/Socket Class/Classes/Socket.TCP/Close.vi"
File 28="user.lib/NIST/Socket Class/Classes/Socket.TCP/Connect.vi"
File 29="user.lib/NIST/Socket Class/Classes/Socket.TCP/Enquire.vi"
File 30="user.lib/NIST/Socket Class/Classes/Socket.TCP/Listen.vi"
File 31="user.lib/NIST/Socket Class/Classes/Socket.TCP/Listen_close.vi"
File 32="user.lib/NIST/Socket Class/Classes/Socket.TCP/Listen_wait.vi"
File 33="user.lib/NIST/Socket Class/Classes/Socket.TCP/New.vi"
File 34="user.lib/NIST/Socket Class/Classes/Socket.TCP/Receive.vi"
File 35="user.lib/NIST/Socket Class/Classes/Socket.TCP/Socket.TCP.lvclass"
File 36="user.lib/NIST/Socket Class/Classes/Socket.TCP/TCP.ctl"
File 37="user.lib/NIST/Socket Class/Classes/Socket.TCP/Transmit.vi"
File 38="user.lib/NIST/Socket Class/Classes/Socket.TCP/Accessors/Read host_address.vi"
File 39="user.lib/NIST/Socket Class/Classes/Socket.TCP/Accessors/Read host_port.vi"
File 40="user.lib/NIST/Socket Class/Classes/Socket.TCP/Accessors/Read listener_refnum.vi"
File 41="user.lib/NIST/Socket Class/Classes/Socket.TCP/Accessors/Read remote_address .vi"
File 42="user.lib/NIST/Socket Class/Classes/Socket.TCP/Accessors/Read remote_port .vi"
File 43="user.lib/NIST/Socket Class/Classes/Socket.TCP/Accessors/Read tcp _refnum.vi"
File 44="user.lib/NIST/Socket Class/Classes/Socket.TCP/Accessors/Write host_address.vi"
File 45="user.lib/NIST/Socket Class/Classes/Socket.TCP/Accessors/Write host_port.vi"
File 46="user.lib/NIST/Socket Class/Classes/Socket.TCP/Accessors/Write listener_refnum.vi"
File 47="user.lib/NIST/Socket Class/Classes/Socket.TCP/Accessors/Write remote_address .vi"
File 48="user.lib/NIST/Socket Class/Classes/Socket.TCP/Accessors/Write remote_port .vi"
File 49="user.lib/NIST/Socket Class/Classes/Socket.TCP/Accessors/Write tcp _refnum.vi"
File 50="user.lib/NIST/Socket Class/Classes/Socket.Base/Close.vi"
File 51="user.lib/NIST/Socket Class/Classes/Socket.Base/Connect.vi"
File 52="user.lib/NIST/Socket Class/Classes/Socket.Base/New.vi"
File 53="user.lib/NIST/Socket Class/Classes/Socket.Base/Receive.vi"
File 54="user.lib/NIST/Socket Class/Classes/Socket.Base/Socket.Base.lvclass"
File 55="user.lib/NIST/Socket Class/Classes/Socket.Base/Transmit.vi"
File 56="user.lib/NIST/Socket Class/Classes/Socket.Base/Accessors/Read connected.vi"
File 57="user.lib/NIST/Socket Class/Classes/Socket.Base/Accessors/Read initialized.vi"
File 58="user.lib/NIST/Socket Class/Classes/Socket.Base/Accessors/Read timeout.vi"
File 59="user.lib/NIST/Socket Class/Classes/Socket.Base/Accessors/Write connected.vi"
File 60="user.lib/NIST/Socket Class/Classes/Socket.Base/Accessors/Write initialized.vi"
File 61="user.lib/NIST/Socket Class/Classes/Socket.Base/Accessors/Write timeout.vi"
File 62="examples/exbins/Socket.bin3"
File 63="examples/Data Communication/Socket Class/Examples/UDP/Socket.UDP Multicast Client.vi"
File 64="examples/Data Communication/Socket Class/Examples/UDP/Socket.UDP Multicast Server.vi"
File 65="examples/Data Communication/Socket Class/Examples/TCP/Socket.TCP Echo Client.vi"
File 66="examples/Data Communication/Socket Class/Examples/TCP/Socket.TCP Echo Server.vi"


[File Group 1]
Target Dir="<menus>/Categories/Data Communication"
Replace Mode="Always"
Num Files=2
File 0="_functions_nist_lib_socket_class_1.mnu"
File 1="functions_NIST_lib_Socket_Class.mnu"


[File Group 2]
Target Dir="<menus>/Controls"
Replace Mode="Always"
Num Files=1
File 0="controls_NIST_lib_Socket_Class.mnu"
