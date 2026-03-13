Microsoft Windows [Version 10.0.26200.7840]
(c) Microsoft Corporation. All rights reserved.

C:\Py_workspace\Demo_bedrock_bot>uv python install 3.12  
Python 3.12 is already installed

C:\Py_workspace\Demo_bedrock_bot>python --version
Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.

C:\Py_workspace\Demo_bedrock_bot>uv python --version
error: unexpected argument '--version' found

tip: a similar argument exists: '--verbose'

Usage: uv python --verbose... <COMMAND>

For more information, try '--help'.

C:\Py_workspace\Demo_bedrock_bot>uv venv chatbot
Using CPython 3.14.2
Creating virtual environment at: chatbot
Activate with: chatbot\Scripts\activate

C:\Py_workspace\Demo_bedrock_bot>chatbot\Scripts\activate

(chatbot) C:\Py_workspace\Demo_bedrock_bot>aws configure
'aws' is not recognized as an internal or external command,
operable program or batch file.

(chatbot) C:\Py_workspace\Demo_bedrock_bot>c:\Py_workspace\Demo_bedrock_bot\chatbot\Scripts\activate.bat

(chatbot) C:\Py_workspace\Demo_bedrock_bot>uv pip install -r requirements.txt
Using Python 3.14.2 environment at: chatbot
Resolved 13 packages in 946ms
Prepared 9 packages in 5.51s
Installed 13 packages in 3.50s

- awscli==1.44.54
- boto3==1.42.64
- botocore==1.42.64
- colorama==0.4.6
- docutils==0.19
- jmespath==1.1.0
- pyasn1==0.6.2
- python-dateutil==2.9.0.post0
- pyyaml==6.0.3
- rsa==4.7.2
- s3transfer==0.16.0
- six==1.17.0
- urllib3==2.6.3

(chatbot) C:\Py_workspace\Demo_bedrock_bot>aws configure
File association not found for extension .py

<!-- AWS Access Key ID [None]:
AWS Secret Access Key [None]:  -->

Default region name [None]:  
Default output format [None]: json

(chatbot) C:\Py_workspace\Demo_bedrock_bot>
