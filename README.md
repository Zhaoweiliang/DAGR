# DAGR: Diversity Helps Jailbreak Large Language Models

Research code for **Diversity Helps Jailbreak Large Language Models**, published
at **NAACL 2025**.

**Authors:** Weiliang Zhao, Daniel Ben-Levi, Wei Hao, Junfeng Yang, and Chengzhi Mao.

[Paper (ACL Anthology)](https://aclanthology.org/2025.naacl-long.238/) |
[Project website](https://daplab.cs.columbia.edu/projects/dagr/) |
[arXiv](https://arxiv.org/abs/2411.04223)

DAGR stands for **Diversified Attack Grouping Refinement** and studies
diversity-guided black-box red teaming of large language models.

## Overview

We present a simple and effective approach that enhances the efficacy of jailbreak attacks by promoting diversity in adversarial prompt generation. By deviating prompts from the original unsuccessful attempts, our approach achieves a 36% higher success rate in jailbreaking OpenAI’s GPT-4 compared to previous methods, while using only one-third of the queries.

See the [published paper](https://aclanthology.org/2025.naacl-long.238/) for the
full evaluation and examples.

## Repository contents and setup status

- [main.py](main.py): research entry point and command-line argument definitions.
- [config.py](config.py): model paths, endpoints, and API configuration.
- [language_models.py](language_models.py): model interfaces.
- [evaluators.py](evaluators.py): evaluation interfaces.

The earlier demo instructions referred to `run_example.py`, `requirements.txt`,
and `Sucess_Attack_Example.json` in the old `DAGR-2024/DAGR` repository. That
repository is no longer accessible, and these files are not included in this
checkout. Those instructions therefore do not describe a runnable demo of the
current release. A complete dependency specification and verified reproduction
instructions still need to be supplied by the maintainers; this documentation
update does not claim to restore them.

## Citation

If you use this work, please cite the published paper:

```bibtex
@inproceedings{zhao-etal-2025-diversity,
  title = {Diversity Helps Jailbreak Large Language Models},
  author = {Zhao, Weiliang and Ben-Levi, Daniel and Hao, Wei and Yang, Junfeng and Mao, Chengzhi},
  booktitle = {Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},
  year = {2025},
  month = apr,
  publisher = {Association for Computational Linguistics},
  pages = {4647--4680},
  doi = {10.18653/v1/2025.naacl-long.238},
  url = {https://aclanthology.org/2025.naacl-long.238/}
}
```

## License

This repository is distributed under the [MIT License](LICENSE).
