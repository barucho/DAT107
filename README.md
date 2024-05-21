# Using vectors with graphs for gen AI apps in Amazon NeptuneAnalytics (Session ID DAT107) 2024

## workshop Instruction

1. This repo contain:

```
.
├── LICENSE
├── README.md
├── lab
│   ├── DAT107_streamlit_chatbot.py
│   ├── DAT107_workshshop_notebook.ipynb
│   └── LOGO.jpg
└── templates
    └── notebook.yaml
```

2. Create the notebook from the templates directory by using AWS CLI or by using the CloudFormation [console](https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks?filteringText=&filteringStatus=active&viewNested=true)
or by using this AWS CLI command
```bash
aws cloudformation create-stack --stack-name neptuneDAT107 --template-body file://notebook.yaml
```

3. Connect to the notebook and clone this repo 
    * in the notebook menu select git --> Clone a repo 
    * enter the name of this repo.

    ```
    https://github.com/barucho/DAT107.git
    ```

    * select Clone.
    * start working from the notebook named *DAT107_workshshop_notebook.ipynb*
