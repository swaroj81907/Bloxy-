your_project/
│
├── bot_server.py                     ← Main Python server (you run this)
│
├── configs/                          ← Folder for logic/configs
│   ├── __init__.py                   ← (Can be empty)
│   ├── response_handler.py           ← Handles bot logic
│   ├── search_module.py              ← Uses Google CSE
│   └── Api_search_configator.py      ← Stores your API key + CX ID
│
├── feedback/                         ← Folder to store user feedback
│   └── (created automatically)
│
├── server/                           ← Contains your frontend (UI files)
│   ├── index.html                    ← Main chatbot interface
│   ├── style.css                     ← CSS for styling
│   ├── script.js                     ← JavaScript logic
│   ├── Ulogo.png                     ← User avatar
│   ├── Blogo.png                     ← Bot avatar
│   └── (any other assets like fonts/images)
