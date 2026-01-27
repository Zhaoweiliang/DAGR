# Diversified Attack Grouping Refinement (DAGR) Demo
We present a simple and effective approach that enhances the efficacy of jailbreak attacks by promoting diversity in adversarial prompt generation. By deviating prompts from the original unsuccessful attempts, our approach achieves a 36% higher success rate in jailbreaking OpenAI’s GPT-4 compared to previous methods, while using only one-third of the queries.
## Successful Examples

Successful jailbreak prompts for ```GPT-4```, ```GPT-3.5-Turbo```, ```Vicuna```, and ```Llama``` can be found [here](https://github.com/DAGR-2024/DAGR/blob/888bb8601cc51f413ec3f6a7f7848c015854e9b0/Sucess_Attack_Example.json).

## Setup Experiment (Demo):
* Setup a virtual environment  
```bash
sudo apt update
sudo apt install python3 python3-venv
python3 -m venv DAGR
source DAGR/bin/activate
```

* Install the required dependencies:
```bash
pip install -r requirements.txt
```
* Install open-source models (e.g. Vicuna):
  * The model is installed in ```../.cache/huggingface/hub/models--lmsys--vicuna-7b-v1.5```
```
  pip3 install "fschat[model_worker,webui]"
  python3 -m fastchat.serve.cli --model-path lmsys/vicuna-13b-v1.5
```

* Setup the API keys, model path, and dataset path in ```config.py``` file

* If using Gemini as a target specify ```project_id``` and ```location``` in ```language_models.py```
  
* Specify the home directory (```home```) in ```run_example.py```

* Configure [lines 36-38](https://github.com/DAGR-2024/DAGR/blob/f04b9bde5af66abfb6d2cff7f08da432a745e788/run_example.py#L36) in ```run_example.py``` to match the desired dataset (default: AdvBench Dataset)

* Run the demo with:
```
python run_example.py
```
# DAGR
